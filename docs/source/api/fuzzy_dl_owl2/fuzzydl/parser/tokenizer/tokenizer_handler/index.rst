fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler
========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler

.. autoapi-nested-parse::

   Tokenizer backends and registry for the fuzzy-DL parser.

   All tokenizers produce the same ``(kind, value, lower/raw, offset)`` 4-tuple
   format with a trailing ``T_EOF`` sentinel, so the recursive-descent parser is
   agnostic to which backend ran.

   Usage::

       from tokenizer_handler import TokenizerHandler
       handler = TokenizerHandler()
       tokens = handler.tokenize(source_string)




.. ── LLM-GENERATED DESCRIPTION START ──

Manages a registry of tokenizer backends for the fuzzy-DL parser, providing a unified interface that abstracts over pure-Python and compiled C implementations.


Description
-----------


The software provides a flexible tokenization system designed to feed a recursive-descent parser with a consistent stream of 4-tuples containing token kind, value, normalized text, and offset. It implements a strategy pattern where a central handler inspects the runtime environment to select the most efficient backend, prioritizing compiled C extensions for speed while falling back to a pure Python regex implementation if necessary. To support the specific syntax of fuzzy-DL, the logic includes specialized handling for splitting compound identifiers on arithmetic operators and converts numeric literals into appropriate Python types. For large inputs, the architecture supports streaming by breaking source files into chunks based on top-level form boundaries, ensuring that memory usage remains bounded even when processing multi-gigabyte files.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler.Token
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler._FDL_CODE_TO_TK
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler._HANDLER
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler._PROTECTED_KW
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler._SPLIT_CHARS
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler._SPLIT_NUM_RE
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler._STREAM_THRESHOLD
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler._TOKEN_RE
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler._fdl_ok


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler.BaseTokenizer
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler.FdlFileTokenizer
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler.FdlStringTokenizer
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler.PythonRegexTokenizer
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler.TokenizerHandler


Functions
---------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler._emit_split_ident
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler._iter_form_chunks
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler._tokenize_best


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokenizer_handler_BaseTokenizer.png
       :alt: UML Class Diagram for BaseTokenizer
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **BaseTokenizer**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokenizer_handler_BaseTokenizer.pdf
       :alt: UML Class Diagram for BaseTokenizer
       :align: center
       :width: 8.3cm
       :class: uml-diagram

       UML Class Diagram for **BaseTokenizer**

.. py:class:: BaseTokenizer

   Abstract base for all fuzzy-DL tokenizers.


   .. py:method:: available() -> bool

      Returns whether this tokenizer backend can be used in the current
      process (e.g. its compiled extension is importable).

      :return: ``True`` if the backend is usable, ``False`` otherwise.

      :rtype: bool



   .. py:method:: tokenize(source: str) -> List[Token]
      :abstractmethod:


      Tokenizes the source string into the parser's 4-tuple stream. Each
      concrete backend must implement this method.

      :param source: The fuzzy-DL source text to tokenize.
      :type source: str

      :raises NotImplementedError: always, because this is an abstract base method.

      :return: The parser's 4-tuple token stream, terminated by an EOF token.

      :rtype: typing.List[Token]



   .. py:property:: name
      :type: str


      Returns a human-readable name for this tokenizer backend. The base implementation falls back to the concrete class name; subclasses override it with a stable short identifier used in logging and backend selection.

      :return: The backend's display name.

      :rtype: str


.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokenizer_handler_FdlFileTokenizer.png
       :alt: UML Class Diagram for FdlFileTokenizer
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FdlFileTokenizer**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokenizer_handler_FdlFileTokenizer.pdf
       :alt: UML Class Diagram for FdlFileTokenizer
       :align: center
       :width: 11.4cm
       :class: uml-diagram

       UML Class Diagram for **FdlFileTokenizer**

.. py:class:: FdlFileTokenizer

   Bases: :py:obj:`BaseTokenizer`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler.FdlFileTokenizer
      :parts: 1
      :private-bases:


   re2c/flex backend for files (uses mmap + streaming).


   .. py:method:: _form_batches(toks: fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.Tokens, batch_min: int = _STREAM_THRESHOLD)
      :staticmethod:


      Yields ``(lo, hi)`` index ranges covering whole top-level forms within
      the token array. Parenthesis depth is tracked so each batch ends at a
      form boundary; batches are yielded only once they reach at least
      *batch_min* tokens.

      :param toks: The token array to partition into form batches.
      :type toks: Tokens
      :param batch_min: Minimum token count before a batch is yielded.
      :type batch_min: int



   .. py:method:: available() -> bool

      Returns whether this backend can be used, i.e. whether at least one of its compiled entry points (the Cython streaming scanner or the CFFI mmap tokenizer) was successfully imported at construction.

      :return: ``True`` if a compiled file tokenizer is available, ``False`` otherwise.

      :rtype: bool



   .. py:method:: tokenize_file(path: str) -> Iterator[List[Token]]

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



   .. py:attribute:: _FdlScan
      :type:  Optional[Any]
      :value: None



   .. py:attribute:: _get_tokens
      :type:  Optional[Callable]
      :value: None



   .. py:property:: name
      :type: str


      Returns the stable identifier ``"fdl-file"`` for this file-based re2c/flex backend.

      :return: The backend's display name.

      :rtype: str


.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokenizer_handler_FdlStringTokenizer.png
       :alt: UML Class Diagram for FdlStringTokenizer
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FdlStringTokenizer**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokenizer_handler_FdlStringTokenizer.pdf
       :alt: UML Class Diagram for FdlStringTokenizer
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FdlStringTokenizer**

.. py:class:: FdlStringTokenizer

   Bases: :py:obj:`BaseTokenizer`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler.FdlStringTokenizer
      :parts: 1
      :private-bases:


   re2c/flex backend for in-memory strings.  Fastest when built.


   .. py:method:: _tokens_to_parser(toks: fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.Tokens, src_len: int) -> List[Token]
      :staticmethod:


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



   .. py:method:: available() -> bool

      Returns whether this backend can be used, i.e. whether at least one of its compiled entry points (the Cython tuple builder or the CFFI byte tokenizer) was successfully imported at construction.

      :return: ``True`` if a compiled string tokenizer is available, ``False`` otherwise.

      :rtype: bool



   .. py:method:: tokenize(source: str) -> List[Token]

      Tokenizes the source string into the parser's 4-tuple stream using the fastest available compiled backend. The text is UTF-8 encoded and, when present, handed to the Cython ``tokenize_tuples`` (which builds the tuples in C and the timing is logged); otherwise the CFFI byte tokenizer is used and its raw token arrays are converted with ``_tokens_to_parser`` before the underlying buffer is released. A ``RuntimeError`` is raised if neither entry point was built.

      :param source: The fuzzy-DL source text to tokenize.
      :type source: str

      :raises RuntimeError: if no compiled string tokenizer backend is available.

      :return: The parser's 4-tuple token stream.

      :rtype: typing.List[Token]



   .. py:attribute:: _get_tokens_from_bytes
      :type:  Optional[Callable[[bytes], Any]]
      :value: None



   .. py:attribute:: _tokenize_tuples
      :type:  Optional[Callable[[bytes], List[Token]]]
      :value: None



   .. py:property:: name
      :type: str


      Returns the stable identifier ``"fdl-string"`` for this in-memory re2c/flex backend.

      :return: The backend's display name.

      :rtype: str


.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokenizer_handler_PythonRegexTokenizer.png
       :alt: UML Class Diagram for PythonRegexTokenizer
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **PythonRegexTokenizer**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokenizer_handler_PythonRegexTokenizer.pdf
       :alt: UML Class Diagram for PythonRegexTokenizer
       :align: center
       :width: 8.3cm
       :class: uml-diagram

       UML Class Diagram for **PythonRegexTokenizer**

.. py:class:: PythonRegexTokenizer

   Bases: :py:obj:`BaseTokenizer`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler.PythonRegexTokenizer
      :parts: 1
      :private-bases:


   Pure-Python regex tokenizer — always available, the ultimate fallback.


   .. py:method:: tokenize(source: str) -> List[Token]

      Tokenizes the source string into the parser's 4-tuple stream using the pure-Python master regex. Each match is classified into identifiers, numbers, brackets/braces, and quoted strings; identifiers that contain split characters and are not protected keywords are further broken up via ``_emit_split_ident``, while numbers are converted to ``int`` or ``float``. A terminating EOF token is appended. This backend is always available and serves as the ultimate fallback when the compiled scanners are absent.

      :param source: The fuzzy-DL source text to tokenize.
      :type source: str

      :return: The parser's 4-tuple token stream, terminated by an EOF token.

      :rtype: typing.List[Token]



   .. py:property:: name
      :type: str


      Returns the stable identifier ``"python-regex"`` for this pure-Python fallback backend.

      :return: The backend's display name.

      :rtype: str


.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokenizer_handler_TokenizerHandler.png
       :alt: UML Class Diagram for TokenizerHandler
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **TokenizerHandler**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokenizer_handler_TokenizerHandler.pdf
       :alt: UML Class Diagram for TokenizerHandler
       :align: center
       :width: 13.6cm
       :class: uml-diagram

       UML Class Diagram for **TokenizerHandler**

.. py:class:: TokenizerHandler

   Selects and dispatches to the fastest available tokenizer backend.

   Preference order (fastest first):
     1. ``FdlStringTokenizer``  – re2c/flex C backend
     2. ``CRegexTokenizer``     – hand-written C tokenizer
     3. ``PythonRegexTokenizer`` – pure-Python fallback (always works)


   .. py:method:: tokenize(source: str) -> List[Token]

      Tokenizes an in-memory source string by delegating to the active backend's ``tokenize`` method, returning the parser's 4-tuple token stream.

      :param source: The fuzzy-DL source text to tokenize.
      :type source: str

      :return: The parser's 4-tuple token stream.

      :rtype: typing.List[Token]



   .. py:method:: tokenize_file(path: str) -> Iterator[List[Token]]

      File path entry point. Uses :class:`FdlFileTokenizer` when its compiled
      backend is available (streaming for large files); otherwise reads the
      whole file into a string and delegates to the active in-memory backend.

      :param path: Path to the fuzzy-DL source file.
      :type path: str

      :return: An iterator yielding batches of parser 4-tuples.

      :rtype: typing.Iterator[typing.List[Token]]



   .. py:attribute:: _backends
      :type:  List[BaseTokenizer]


   .. py:attribute:: _best
      :type:  BaseTokenizer


   .. py:property:: best
      :type: BaseTokenizer


      Returns the active tokenizer backend chosen at construction, i.e. the fastest one that reported itself available.

      :return: The selected tokenizer backend.

      :rtype: BaseTokenizer


   .. py:property:: best_name
      :type: str


      Returns the display name of the active tokenizer backend, useful for logging which scanner the parser actually selected.

      :return: The name of the selected backend.

      :rtype: str


.. py:function:: _emit_split_ident(raw: str, offset: int, out: List[Token]) -> None

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


.. py:function:: _iter_form_chunks(src: str, chunk_bytes: int = 4 * 1024 * 1024) -> Iterator[str]

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


.. py:function:: _tokenize_best(source: str) -> List[Token]

   Returns the parser's 4-tuple token stream using the fastest available
   backend, via the module-level :class:`TokenizerHandler` singleton.

   :param source: The fuzzy-DL source text to tokenize.
   :type source: str

   :return: The parser's 4-tuple token stream.

   :rtype: typing.List[Token]


.. py:data:: Token

.. py:data:: _FDL_CODE_TO_TK
   :type:  Dict[int, Optional[int]]

.. py:data:: _HANDLER

.. py:data:: _PROTECTED_KW
   :type:  FrozenSet[str]

.. py:data:: _SPLIT_CHARS
   :type:  str
   :value: '*+'


.. py:data:: _SPLIT_NUM_RE

.. py:data:: _STREAM_THRESHOLD
   :type:  int
   :value: 1048576


.. py:data:: _TOKEN_RE

.. py:data:: _fdl_ok
   :type:  bool
