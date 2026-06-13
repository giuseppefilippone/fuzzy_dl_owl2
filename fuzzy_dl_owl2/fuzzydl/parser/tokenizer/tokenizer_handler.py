"""Tokenizer backends and registry for the fuzzy-DL parser.

All tokenizers produce the same ``(kind, value, lower/raw, offset)`` 4-tuple
format with a trailing ``T_EOF`` sentinel, so the recursive-descent parser is
agnostic to which backend ran.

Usage::

    from tokenizer_handler import TokenizerHandler
    handler = TokenizerHandler()
    tokens = handler.tokenize(source_string)
"""

from __future__ import annotations

import re
import time
import traceback
import typing

from fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens import (
    FIRST_KEYWORD,
    LBRACE,
    LBRACK,
    LPAREN,
    NUMBER,
    RBRACE,
    RBRACK,
    RPAREN,
    T_EOF,
    T_IDENT,
    Tokens,
)
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.constants import FuzzyDLKeyword
from fuzzy_dl_owl2.fuzzydl.util.util import Util

# ---------------------------------------------------------------------------
# Shared types & constants
# ---------------------------------------------------------------------------

Token = typing.Tuple[int, typing.Any, str, int]

_PROTECTED_KW: typing.FrozenSet[str] = frozenset(k.get_name() for k in FuzzyDLKeyword)
_SPLIT_CHARS: str = "*+"
_SPLIT_NUM_RE = re.compile(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?")

# Streaming thresholds (single-sourced here so dl_parser_fast.py can import).
# Above this source-byte size, parse_string switches to chunked streaming.
_STREAM_THRESHOLD: int = (
    1 * 1024 * 1024
)  # ~1 MiB of tokens; tuned for <1GB files to avoid too many batches


# Whether the re2c/flex backend is importable (used by dl_parser_fast.py).
try:
    from fuzzy_dl_owl2.fuzzydl.parser.tokenizer._fdl_tuples import FdlScan as _fs
    from fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens import (
        get_tokens_from_bytes as _gtfb,
    )

    _fdl_ok: bool = _gtfb is not None or _fs is not None
except Exception:
    _fdl_ok: bool = False

# Master tokenizer regex (same as the original dl_parser_fast.py)
_TOKEN_RE = re.compile(
    r"[\ \t\r\n,]+|[\#%][^\n]*|(?P<lp>\()|(?P<rp>\))|(?P<lb>\{)|(?P<rb>\})|(?P<lbr>\[)|(?P<rbr>\])|\"(?P<dq>[^\"]*)\"|'(?P<sq>[^']*)'|(?P<num>[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)(?![a-zA-Z_'\-/.0-9])|(?P<ident>[^\s(){}\[\]\"'\#%,][^\s(){}\[\]\"\#%,]*)"
)

# Map _fdl_lexer structural codes (1..21) onto parser kinds (unified with scanner names).
_FDL_CODE_TO_TK: typing.Dict[int, typing.Optional[int]] = {
    1: LPAREN,  # LPAREN
    2: RPAREN,  # RPAREN
    3: LBRACK,  # LBRACK  -> [
    4: RBRACK,  # RBRACK  -> ]
    5: LBRACE,  # LBRACE  -> {
    6: RBRACE,  # RBRACE  -> }
    7: None,  # COMMA   -> dropped
    8: T_IDENT,  # GE      -> ">="
    9: T_IDENT,  # LE      -> "<="
    10: T_IDENT,  # EQ     -> "="
    11: T_IDENT,  # PLUS   -> "+"
    12: T_IDENT,  # MINUS  -> "-"
    13: T_IDENT,  # STAR   -> "*"
    14: T_IDENT,  # SLASH  -> "/"
    15: T_IDENT,  # FADD   -> "f+"
    16: T_IDENT,  # FSUB   -> "f-"
    17: T_IDENT,  # FMUL   -> "f*"
    18: T_IDENT,  # FDIV   -> "f/"
    19: NUMBER,  # NUMBER
    20: T_IDENT,  # IDENT
    21: T_IDENT,  # ERROR  -> surface as identifier; parser reports context
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _emit_split_ident(raw: str, offset: int, out: typing.List[Token]) -> None:
    """
    Splits a compound identifier on ``*`` and ``+`` operators and appends the
    resulting tokens to the output list. Numeric substrings are converted to
    ``int`` or ``float``; alphabetic substrings become identifier tokens; the
    operators themselves are emitted as separate ``T_IDENT`` tokens.

    :param raw: The compound identifier string to split.
    :type raw: str
    :param offset: The byte offset of the original identifier in the source.
    :type offset: int
    :param out: The token list to append split results to.
    :type out: typing.List[Token]
    """

    current = ""
    for ch in raw:
        if ch in _SPLIT_CHARS:
            if current:
                if _SPLIT_NUM_RE.fullmatch(current):
                    v: typing.Union[int, float] = (
                        float(current)
                        if "." in current or "e" in current or "E" in current
                        else int(current)
                    )
                    out.append((NUMBER, v, current, offset))
                else:
                    out.append((T_IDENT, current, current.lower(), offset))
                current = ""
            out.append((T_IDENT, ch, ch, offset))
        else:
            current += ch
    if current:
        if _SPLIT_NUM_RE.fullmatch(current):
            v = (
                float(current)
                if "." in current or "e" in current or "E" in current
                else int(current)
            )
            out.append((NUMBER, v, current, offset))
        else:
            out.append((T_IDENT, current, current.lower(), offset))


def _iter_form_chunks(
    src: str, chunk_bytes: int = 4 * 1024 * 1024
) -> typing.Iterator[str]:
    """
    Yields substrings of *src*, each a run of whole top-level forms bounded by
    matching parentheses. Strings and line comments are skipped during
    parenthesis counting. Chunks are yielded once they reach at least
    *chunk_bytes* in size so the parser can stream large files without
    materialising the entire source at once.

    :param src: The fuzzy-DL source text to chunk.
    :type src: str
    :param chunk_bytes: Minimum byte size of a chunk before it is yielded.
    :type chunk_bytes: int

    :return: An iterator over whole-form source chunks.

    :rtype: typing.Iterator[str]
    """

    n: int = len(src)
    depth: int = 0
    chunk_start: int = 0
    i: int = 0
    in_str: typing.Optional[str] = None
    while i < n:
        c: str = src[i]
        if in_str is not None:
            if c == in_str:
                in_str = None
            i += 1
            continue
        if c == "#" or c == "%":
            j: int = src.find("\n", i)
            i = n if j < 0 else j
            continue
        if c == '"' or c == "'":
            in_str = c
            i += 1
            continue
        if c == "(":
            depth += 1
        elif c == ")":
            if depth > 0:
                depth -= 1
                if depth == 0 and (i + 1 - chunk_start) >= chunk_bytes:
                    yield src[chunk_start : i + 1]
                    chunk_start = i + 1
        i += 1
    if chunk_start < n:
        yield src[chunk_start:n]


# ---------------------------------------------------------------------------
# Base class
# ---------------------------------------------------------------------------


class BaseTokenizer:
    """Abstract base for all fuzzy-DL tokenizers."""

    @property
    def name(self) -> str:
        """
        Returns a human-readable name for this tokenizer backend. The base implementation falls back to the concrete class name; subclasses override it with a stable short identifier used in logging and backend selection.

        :return: The backend's display name.

        :rtype: str
        """

        return self.__class__.__name__

    def available(self) -> bool:
        """
        Returns whether this tokenizer backend can be used in the current
        process (e.g. its compiled extension is importable).

        :return: ``True`` if the backend is usable, ``False`` otherwise.

        :rtype: bool
        """

        return True

    def tokenize(self, source: str) -> typing.List[Token]:
        """
        Tokenizes the source string into the parser's 4-tuple stream. Each
        concrete backend must implement this method.

        :param source: The fuzzy-DL source text to tokenize.
        :type source: str

        :raises NotImplementedError: always, because this is an abstract base method.

        :return: The parser's 4-tuple token stream, terminated by an EOF token.

        :rtype: typing.List[Token]
        """

        raise NotImplementedError


# ---------------------------------------------------------------------------
# Concrete backends
# ---------------------------------------------------------------------------


class PythonRegexTokenizer(BaseTokenizer):
    """Pure-Python regex tokenizer — always available, the ultimate fallback."""

    @property
    def name(self) -> str:
        """
        Returns the stable identifier ``"python-regex"`` for this pure-Python fallback backend.

        :return: The backend's display name.

        :rtype: str
        """

        return "python-regex"

    def tokenize(self, source: str) -> typing.List[Token]:
        """
        Tokenizes the source string into the parser's 4-tuple stream using the pure-Python master regex. Each match is classified into identifiers, numbers, brackets/braces, and quoted strings; identifiers that contain split characters and are not protected keywords are further broken up via ``_emit_split_ident``, while numbers are converted to ``int`` or ``float``. A terminating EOF token is appended. This backend is always available and serves as the ultimate fallback when the compiled scanners are absent.

        :param source: The fuzzy-DL source text to tokenize.
        :type source: str

        :return: The parser's 4-tuple token stream, terminated by an EOF token.

        :rtype: typing.List[Token]
        """

        out: typing.List[Token] = []
        protected = _PROTECTED_KW
        split_chars = _SPLIT_CHARS
        for m in _TOKEN_RE.finditer(source):
            kind = m.lastgroup
            if kind is None:
                continue
            start = m.start()
            if kind == "ident":
                s = m.group("ident")
                low = s.lower()
                if low in protected or (
                    split_chars[0] not in s and split_chars[1] not in s
                ):
                    out.append((T_IDENT, s, low, start))
                else:
                    _emit_split_ident(s, start, out)
            elif kind == "num":
                s = m.group("num")
                v: typing.Union[int, float] = (
                    float(s) if "." in s or "e" in s or "E" in s else int(s)
                )
                out.append((NUMBER, v, s, start))
            elif kind == "lp":
                out.append((LPAREN, "(", "(", start))
            elif kind == "rp":
                out.append((RPAREN, ")", ")", start))
            elif kind == "lb":
                out.append((LBRACE, "{", "{", start))
            elif kind == "rb":
                out.append((RBRACE, "}", "}", start))
            elif kind == "lbr":
                out.append((LBRACK, "[", "[", start))
            elif kind == "rbr":
                out.append((RBRACK, "]", "]", start))
            elif kind == "dq" or kind == "sq":
                s = m.group(kind)
                out.append((T_IDENT, s, s.lower(), start))
        out.append((T_EOF, "", "", len(source)))
        return out


class FdlStringTokenizer(BaseTokenizer):
    """re2c/flex backend for in-memory strings.  Fastest when built."""

    def __init__(self) -> None:
        """
        Initializes the in-memory re2c/flex string backend by attempting to import its two compiled entry points. The Cython ``tokenize_tuples`` (fastest) and the CFFI ``get_tokens_from_bytes`` (fallback) are imported independently; each import is wrapped so that a missing or unbuilt extension leaves the corresponding callable as ``None`` rather than raising, with the failure optionally logged when debugging is enabled. The backend reports itself unavailable only if both imports fail.
        """

        self._tokenize_tuples: typing.Optional[
            typing.Callable[[bytes], typing.List[Token]]
        ] = None
        self._get_tokens_from_bytes: typing.Optional[
            typing.Callable[[bytes], typing.Any]
        ] = None
        try:
            from fuzzy_dl_owl2.fuzzydl.parser.tokenizer._fdl_tuples import (
                tokenize_tuples as _tt,
            )

            self._tokenize_tuples = _tt
        except Exception as e:
            if ConfigReader.DEBUG_PRINT:
                Util.warning(
                    f"Failed to import _fdl_tuples: {e}\n{traceback.format_exc()}"
                )
        try:
            from fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens import (
                get_tokens_from_bytes as _gtfb,
            )

            self._get_tokens_from_bytes = _gtfb
        except Exception as e:
            if ConfigReader.DEBUG_PRINT:
                Util.warning(f"Failed to import tokens: {e}\n{traceback.format_exc()}")

        from fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens import AVAILABLE_LEXER

        self._available: bool = AVAILABLE_LEXER

    @property
    def name(self) -> str:
        """
        Returns the stable identifier ``"fdl-string"`` for this in-memory re2c/flex backend.

        :return: The backend's display name.

        :rtype: str
        """

        return "fdl-string"

    def available(self) -> bool:
        """
        Returns whether this backend can be used, i.e. whether at least one of its compiled entry points (the Cython tuple builder or the CFFI byte tokenizer) was successfully imported at construction.

        :return: ``True`` if a compiled string tokenizer is available, ``False`` otherwise.

        :rtype: bool
        """

        return self._available and (
            self._tokenize_tuples is not None or self._get_tokens_from_bytes is not None
        )

    def tokenize(self, source: str) -> typing.List[Token]:
        """
        Tokenizes the source string into the parser's 4-tuple stream using the fastest available compiled backend. The text is UTF-8 encoded and, when present, handed to the Cython ``tokenize_tuples`` (which builds the tuples in C and the timing is logged); otherwise the CFFI byte tokenizer is used and its raw token arrays are converted with ``_tokens_to_parser`` before the underlying buffer is released. A ``RuntimeError`` is raised if neither entry point was built.

        :param source: The fuzzy-DL source text to tokenize.
        :type source: str

        :raises RuntimeError: if no compiled string tokenizer backend is available.

        :return: The parser's 4-tuple token stream.

        :rtype: typing.List[Token]
        """

        data: bytes = source.encode("utf-8")
        if self._tokenize_tuples is not None:
            t0 = time.perf_counter_ns()
            result = self._tokenize_tuples(data)
            t1 = time.perf_counter_ns()
            Util.info(f"Tokenization took {(t1 - t0) * 1e-9}s")
            return result
        if self._get_tokens_from_bytes is not None:
            toks = self._get_tokens_from_bytes(data)
            try:
                return self._tokens_to_parser(toks, len(data))
            finally:
                toks.close()
        raise RuntimeError("FDL string tokenizer not available")

    @staticmethod
    def _tokens_to_parser(toks: Tokens, src_len: int) -> typing.List[Token]:
        """
        Converts a :class:`Tokens` object (the CFFI int32-array output) into the
        parser's 4-tuple stream. Each token's raw source text is lazily decoded
        from the backing buffer via the span offsets stored in the token arrays.
        Keyword codes are remapped to ``T_IDENT`` with their lowercase spelling;
        structural codes are remapped via :data:`_FDL_CODE_TO_TK`; numbers are
        parsed into ``int`` or ``float``. A trailing EOF token is appended.

        :param toks: The CFFI token array produced by the re2c/flex backend.
        :type toks: Tokens
        :param src_len: The total byte length of the original source, used as the
            EOF token's offset.
        :type src_len: int

        :return: The parser's 4-tuple token stream, terminated by an EOF token.

        :rtype: typing.List[Token]
        """

        view = toks._buf.view
        ty_list = toks.types.tolist()
        st_list = toks.starts.tolist()
        ln_list = toks.lens.tolist()
        out: typing.List[Token] = []
        for i in range(len(toks)):
            code: int = ty_list[i]
            start: int = st_list[i]
            raw: str = bytes(view[start : start + ln_list[i]]).decode("utf-8")
            if code >= FIRST_KEYWORD:
                out.append((T_IDENT, raw, raw.lower(), start))
                continue
            kind = _FDL_CODE_TO_TK.get(code, T_IDENT)
            if kind is None:
                continue
            if kind == NUMBER:
                v: typing.Union[int, float] = (
                    float(raw) if "." in raw or "e" in raw or "E" in raw else int(raw)
                )
                out.append((NUMBER, v, raw, start))
            else:
                out.append((kind, raw, raw.lower(), start))
        out.append((T_EOF, "", "", src_len))
        return out


class FdlFileTokenizer(BaseTokenizer):
    """re2c/flex backend for files (uses mmap + streaming)."""

    def __init__(self) -> None:
        """
        Initializes the file-based re2c/flex backend by attempting to import its two compiled entry points. The Cython ``FdlScan`` streaming scanner (preferred) and the CFFI ``get_tokens`` mmap-based tokenizer (fallback) are imported independently; each import failure silently leaves the corresponding attribute as ``None``. The backend reports itself unavailable only if both imports fail.
        """

        self._FdlScan: typing.Optional[typing.Any] = None
        self._get_tokens: typing.Optional[typing.Callable] = None
        try:
            from fuzzy_dl_owl2.fuzzydl.parser.tokenizer._fdl_tuples import (
                FdlScan as _fs,
            )

            self._FdlScan = _fs
        except Exception:
            pass
        try:
            from fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens import get_tokens as _gt

            self._get_tokens = _gt
        except Exception:
            pass
        
        from fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens import AVAILABLE_LEXER

        self._available: bool = AVAILABLE_LEXER

    @property
    def name(self) -> str:
        """
        Returns the stable identifier ``"fdl-file"`` for this file-based re2c/flex backend.

        :return: The backend's display name.

        :rtype: str
        """

        return "fdl-file"

    def available(self) -> bool:
        """
        Returns whether this backend can be used, i.e. whether at least one of its compiled entry points (the Cython streaming scanner or the CFFI mmap tokenizer) was successfully imported at construction.

        :return: ``True`` if a compiled file tokenizer is available, ``False`` otherwise.

        :rtype: bool
        """

        return self._available and (self._FdlScan is not None or self._get_tokens is not None)

    def tokenize_file(self, path: str) -> typing.Iterator[typing.List[Token]]:
        """
        Tokenizes a file into batched 4-tuple token streams, streaming for large
        files so peak memory stays bounded. When the Cython ``FdlScan`` is
        available it reads the whole file and yields scan batches; otherwise the
        CFFI mmap-backed tokenizer is used and its raw token arrays are converted
        form-by-form via :meth:`_form_batches`.

        :param path: Path to the fuzzy-DL source file to tokenize.
        :type path: str

        :raises RuntimeError: if no compiled file tokenizer backend is available.

        :return: An iterator yielding batches of parser 4-tuples.

        :rtype: typing.Iterator[typing.List[Token]]
        """

        if self._FdlScan is not None:
            t0 = time.perf_counter_ns()
            with open(path, "rb") as fh:
                scan = self._FdlScan(fh.read())
            t1 = time.perf_counter_ns()
            if ConfigReader.DEBUG_PRINT:
                Util.debug(f"Scanning {path} took {(t1 - t0) * 1e-9}s")
            if scan.ntok <= _STREAM_THRESHOLD:
                yield scan.batch(0, scan.ntok)
                return
            for lo, hi in scan.form_batches(_STREAM_THRESHOLD):
                yield scan.batch(lo, hi)
            return

        # Fallback: CFFI int32-array API + Python conversion, mmap-backed.
        if self._get_tokens is not None:
            toks = self._get_tokens(path)
            ntok = len(toks)
            eof_off = toks._buf.size
            try:
                if ntok > _STREAM_THRESHOLD:
                    for lo, hi in self._form_batches(toks):
                        yield FdlFileTokenizer._tokens_to_parser_slice(
                            toks, lo, hi, eof_off
                        )
                else:
                    yield FdlFileTokenizer._tokens_to_parser_slice(
                        toks, 0, ntok, eof_off
                    )
            finally:
                toks.close()
            return
        raise RuntimeError("FDL file tokenizer not available")

    @staticmethod
    def _form_batches(toks: Tokens, batch_min: int = _STREAM_THRESHOLD):
        """
        Yields ``(lo, hi)`` index ranges covering whole top-level forms within
        the token array. Parenthesis depth is tracked so each batch ends at a
        form boundary; batches are yielded only once they reach at least
        *batch_min* tokens.

        :param toks: The token array to partition into form batches.
        :type toks: Tokens
        :param batch_min: Minimum token count before a batch is yielded.
        :type batch_min: int
        """

        ty_list = toks.types.tolist()
        n = len(ty_list)
        depth = 0
        lo = 0
        i = 0
        while i < n:
            code = ty_list[i]
            if code == LPAREN:
                depth += 1
            elif code == RPAREN:
                if depth > 0:
                    depth -= 1
                    if depth == 0 and (i + 1 - lo) >= batch_min:
                        yield (lo, i + 1)
                        lo = i + 1
            i += 1
        if lo < n:
            yield (lo, n)


# ---------------------------------------------------------------------------
# Registry / handler
# ---------------------------------------------------------------------------


class TokenizerHandler:
    """Selects and dispatches to the fastest available tokenizer backend.

    Preference order (fastest first):
      1. ``FdlStringTokenizer``  – re2c/flex C backend
      2. ``CRegexTokenizer``     – hand-written C tokenizer
      3. ``PythonRegexTokenizer`` – pure-Python fallback (always works)
    """

    def __init__(self) -> None:
        """
        Initializes the handler by instantiating the candidate backends in preference order (the compiled ``FdlStringTokenizer`` first, then the always-available ``PythonRegexTokenizer``) and selecting the first one that reports itself available as the active backend. The pure-Python fallback is used as the default so that a backend is always chosen even when no compiled extension is built.
        """

        self._backends: typing.List[BaseTokenizer] = [
            FdlStringTokenizer(),
            PythonRegexTokenizer(),
        ]
        self._best: BaseTokenizer = self._backends[len(self._backends) - 1]
        for b in self._backends:
            if b.available():
                self._best = b
                break

    @property
    def best(self) -> BaseTokenizer:
        """
        Returns the active tokenizer backend chosen at construction, i.e. the fastest one that reported itself available.

        :return: The selected tokenizer backend.

        :rtype: BaseTokenizer
        """

        return self._best

    def tokenize(self, source: str) -> typing.List[Token]:
        """
        Tokenizes an in-memory source string by delegating to the active backend's ``tokenize`` method, returning the parser's 4-tuple token stream.

        :param source: The fuzzy-DL source text to tokenize.
        :type source: str

        :return: The parser's 4-tuple token stream.

        :rtype: typing.List[Token]
        """

        return self._best.tokenize(source)

    def tokenize_file(self, path: str) -> typing.Iterator[typing.List[Token]]:
        """
        File path entry point. Uses :class:`FdlFileTokenizer` when its compiled
        backend is available (streaming for large files); otherwise reads the
        whole file into a string and delegates to the active in-memory backend.

        :param path: Path to the fuzzy-DL source file.
        :type path: str

        :return: An iterator yielding batches of parser 4-tuples.

        :rtype: typing.Iterator[typing.List[Token]]
        """

        fdl_file = FdlFileTokenizer()
        if fdl_file.available():
            return fdl_file.tokenize_file(path)
        # Fallback: read whole file as string, then use best string tokenizer.
        with open(path, "r", encoding="utf-8") as fh:
            src = fh.read()
        return iter([self.tokenize(src)])

    @property
    def best_name(self) -> str:
        """
        Returns the display name of the active tokenizer backend, useful for logging which scanner the parser actually selected.

        :return: The name of the selected backend.

        :rtype: str
        """

        return self._best.name


# Module-level singleton — imported by dl_parser_fast.py as ``_tokenize_best``.
_HANDLER = TokenizerHandler()


def _tokenize_best(source: str) -> typing.List[Token]:
    """
    Returns the parser's 4-tuple token stream using the fastest available
    backend, via the module-level :class:`TokenizerHandler` singleton.

    :param source: The fuzzy-DL source text to tokenize.
    :type source: str

    :return: The parser's 4-tuple token stream.

    :rtype: typing.List[Token]
    """

    return _HANDLER.tokenize(source)
