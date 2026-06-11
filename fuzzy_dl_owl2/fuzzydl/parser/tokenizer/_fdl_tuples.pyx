# cython: language_level=3, boundscheck=False, wraparound=False
"""C tuple-builder over the re2c/flex fuzzy DL scanner.

The pure-C scanner (compiled from ``lexer_re2c.re`` / ``lexer_flex.l``) exposes
``fdl_count_tokens`` / ``fdl_tokenize``, which fill three int32 spans per token
and build no Python objects. That is fast, but leaves the per-token tuple
construction to Python — the hot loop in ``dl_parser_fast._fdl_slice_to_parser``.

``tokenize_tuples`` moves that conversion into Cython-generated C: it runs both
scanner passes and emits exactly the ``(kind, value, lower, offset)`` 4-tuples
the recursive-descent parser consumes, so it is a drop-in faster replacement
for that Python loop. COMMA is dropped; a trailing TK_EOF sentinel is appended.
"""

from libc.stdint cimport int32_t
from libc.stdlib cimport malloc, free
from cpython.unicode cimport PyUnicode_DecodeUTF8

# Scanner entry points, linked from the generated lexer .c (re2c or flex).
cdef extern from *:
    """
    #include <stddef.h>
    #include <stdint.h>
    size_t fdl_count_tokens(const char *buf, size_t len);
    size_t fdl_tokenize(const char *buf, size_t len,
                        int32_t *types, int32_t *starts, int32_t *lens);
    """
    size_t fdl_count_tokens(const char *buf, size_t length) nogil
    size_t fdl_tokenize(const char *buf, size_t length,
                        int32_t *types, int32_t *starts, int32_t *lens) nogil

# Parser-side + scanner-side token kinds live in tokens.h — one-line import
# so every code stays in sync with the generated header automatically.
cdef extern from "tokens.h":
    int T_LPAREN, T_RPAREN, T_LBRACK, T_RBRACK, T_LBRACE, T_RBRACE, T_COMMA, T_NUMBER, T_IDENT, T_ERROR, T_EOF


cdef inline int _code_to_tk(int code) nogil:
    """Map a scanner code to a parser kind; 0 means drop (COMMA).
    Structural and NUMBER map to themselves (identity).  IDENT and ERROR
    both fold to T_IDENT; the parser dispatches on the lowercased spelling."""
    if code == T_LPAREN:
        return T_LPAREN
    if code == T_RPAREN:
        return T_RPAREN
    if code == T_LBRACK:
        return T_LBRACK
    if code == T_RBRACK:
        return T_RBRACK
    if code == T_LBRACE:
        return T_LBRACE
    if code == T_RBRACE:
        return T_RBRACE
    if code == T_COMMA:
        return 0
    if code == T_NUMBER:
        return T_NUMBER
    # Operators, IDENT, ERROR and every keyword fold to IDENT.
    return T_IDENT


cdef inline unicode _decode(const char *buf, int start, int length):
    return PyUnicode_DecodeUTF8(buf + start, length, NULL)


cdef inline object _make_number(unicode raw):
    """int / float matching the Python loop: float if '.', 'e' or 'E' present."""
    if ("." in raw) or ("e" in raw) or ("E" in raw):
        return float(raw)
    return int(raw)


cdef list _build_slice(const char *buf,
                       int32_t *types, int32_t *starts, int32_t *lens,
                       size_t lo, size_t hi, int eof_off):
    """Build the parser's 4-tuple list for token range ``[lo, hi)``.

    Appends a TK_EOF sentinel at byte offset *eof_off*. Pure C apart from the
    Python object construction Cython generates.
    """
    cdef list out = []
    cdef size_t i
    cdef int code, kind, start, tlen
    cdef unicode raw
    for i in range(lo, hi):
        code = types[i]
        kind = _code_to_tk(code)
        if kind == 0:
            continue  # COMMA dropped
        start = starts[i]
        tlen = lens[i]
        raw = _decode(buf, start, tlen)
        if kind == T_NUMBER:
            out.append((T_NUMBER, _make_number(raw), raw, start))
        else:
            out.append((kind, raw, raw.lower(), start))
    # Sentinel so every _peek / _advance call is safe even at EOF.
    out.append((T_EOF, u"", u"", eof_off))
    return out


def tokenize_tuples(bytes data):
    """Tokenize UTF-8 source *data* and return the parser's 4-tuple list."""
    cdef const char *buf = data
    cdef size_t length = len(data)
    cdef size_t ntok = fdl_count_tokens(buf, length)

    cdef int32_t *types = NULL
    cdef int32_t *starts = NULL
    cdef int32_t *lens = NULL
    if ntok > 0:
        types = <int32_t *> malloc(ntok * sizeof(int32_t))
        starts = <int32_t *> malloc(ntok * sizeof(int32_t))
        lens = <int32_t *> malloc(ntok * sizeof(int32_t))
        if types == NULL or starts == NULL or lens == NULL:
            free(types); free(starts); free(lens)
            raise MemoryError()
        with nogil:
            fdl_tokenize(buf, length, types, starts, lens)

    try:
        return _build_slice(buf, types, starts, lens, 0, ntok, <int> length)
    finally:
        free(types)
        free(starts)
        free(lens)


cdef class FdlScan:
    """Scan *data* once, hold the token arrays, and build per-form-batch
    4-tuple lists in C on demand.

    Used by the streaming parse path for large files: the whole source is
    scanned a single time (cheap, no Python objects), then ``batch(lo, hi)``
    converts one bounded range of tokens at a time so peak tuple memory stays
    proportional to a batch rather than the whole file. ``form_batches``
    computes paren-balanced batch ranges of at least ``batch_min`` tokens.
    """

    cdef bytes _data            # keeps buf alive for the object's lifetime
    cdef const char *_buf
    cdef size_t _length
    cdef size_t _ntok
    cdef int32_t *_types
    cdef int32_t *_starts
    cdef int32_t *_lens

    def __cinit__(self, bytes data):
        self._data = data
        self._buf = data
        self._length = len(data)
        self._types = NULL
        self._starts = NULL
        self._lens = NULL
        self._ntok = fdl_count_tokens(self._buf, self._length)
        if self._ntok > 0:
            self._types = <int32_t *> malloc(self._ntok * sizeof(int32_t))
            self._starts = <int32_t *> malloc(self._ntok * sizeof(int32_t))
            self._lens = <int32_t *> malloc(self._ntok * sizeof(int32_t))
            if self._types == NULL or self._starts == NULL or self._lens == NULL:
                raise MemoryError()
            with nogil:
                fdl_tokenize(self._buf, self._length,
                             self._types, self._starts, self._lens)

    def __dealloc__(self):
        free(self._types)
        free(self._starts)
        free(self._lens)

    @property
    def ntok(self):
        return self._ntok

    def batch(self, size_t lo, size_t hi):
        """Return the 4-tuple list for token range ``[lo, hi)`` (C-built)."""
        return _build_slice(self._buf, self._types, self._starts, self._lens,
                            lo, hi, <int> self._length)

    def form_batches(self, size_t batch_min):
        """Yield ``(lo, hi)`` ranges covering whole top-level forms, each at
        least *batch_min* tokens. A form spans a depth-0 ``(`` to its matching
        ``)`` (scanner codes T_LPAREN / T_RPAREN)."""
        cdef size_t n = self._ntok
        cdef int depth = 0
        cdef size_t lo = 0
        cdef size_t i = 0
        cdef int code
        while i < n:
            code = self._types[i]
            if code == T_LPAREN:
                depth += 1
            elif code == T_RPAREN:
                if depth > 0:
                    depth -= 1
                    if depth == 0 and (i + 1 - lo) >= batch_min:
                        yield (lo, i + 1)
                        lo = i + 1
            i += 1
        if lo < n:
            yield (lo, n)