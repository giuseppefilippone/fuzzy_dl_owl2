fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens



.. ── LLM-GENERATED DESCRIPTION START ──

A high-performance tokenizer for the FuzzyDL language that bridges Python and a C-based lexer using CFFI and memory mapping.


Description
-----------


The software implements a bridge between Python and a low-level C lexer, specifically designed to parse FuzzyDL syntax efficiently. By utilizing C Foreign Function Interface (CFFI), it delegates the heavy lifting of lexical analysis to C functions while managing memory and data structures within Python. A two-pass tokenization strategy is employed where the first pass counts the tokens to allocate exact-sized NumPy arrays, and the second pass populates these arrays with token types, start offsets, and lengths. This design supports both memory-mapped file inputs for large ontologies and in-memory byte strings, ensuring that the underlying C backend receives NUL-terminated buffers regardless of the source. The resulting token stream is encapsulated in a class that allows lazy decoding of source text and provides context management to safely release system resources.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.COMMA
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.EQ
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.ERROR
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.FADD
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.FDIV
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.FIRST_KEYWORD
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.FMUL
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.FSUB
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.GE
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.IDENT
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.LBRACE
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.LBRACK
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.LE
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.LPAREN
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.MINUS
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.NUMBER
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.PLUS
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.RBRACE
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.RBRACK
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.RPAREN
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.STAR
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.TOK_NAMES
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.T_EOF
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.T_IDENT
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens._PAGE


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.Tokens
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens._Buffer
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens._BytesBuffer


Functions
---------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens._tokenize_buffer
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.get_tokens
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens.get_tokens_from_bytes


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokens_Tokens.png
       :alt: UML Class Diagram for Tokens
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **Tokens**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokens_Tokens.pdf
       :alt: UML Class Diagram for Tokens
       :align: center
       :width: 6.9cm
       :class: uml-diagram

       UML Class Diagram for **Tokens**

.. py:class:: Tokens(types, starts, lens, buf)

   Flat token stream. Holds the buffer so span offsets stay valid.


   .. py:method:: __enter__()

      Enters a context manager over the token stream and returns it, so the stream can be used in a ``with`` block that guarantees the backing buffer is released on exit.

      :return: This token stream instance.

      :rtype: Tokens



   .. py:method:: __exit__(*exc)

      Exits the context manager, releasing the backing buffer via :meth:`close` regardless of whether the ``with`` block exited normally or because of an exception. Any exception is allowed to propagate.

      :param exc: The exception type, value, and traceback (unused), present to satisfy the context-manager protocol.
      :type exc: typing.Any



   .. py:method:: __len__()

      Returns the number of tokens in the stream, i.e. the length of the underlying ``types`` array.

      :return: The token count.

      :rtype: int



   .. py:method:: close()

      Releases the source buffer backing this token stream by delegating to its ``close`` method. After this call the lazy ``text`` lookups are no longer valid, since the byte storage the span offsets point into has been released.



   .. py:method:: is_keyword(i)

      Returns whether token *i* is a keyword. This is a pure integer code
      comparison, so no string work is performed.

      :param i: Index of the token in the stream.
      :type i: int

      :return: ``True`` if the token is a keyword, ``False`` otherwise.

      :rtype: bool



   .. py:method:: is_name(i)

      Returns whether token *i* is a user-defined bare identifier (as opposed
      to a keyword or structural token).

      :param i: Index of the token in the stream.
      :type i: int

      :return: ``True`` if the token is a bare identifier, ``False`` otherwise.

      :rtype: bool



   .. py:method:: name(i)

      Returns the display name of token *i*: the structural token name for
      punctuation, or the keyword spelling itself for keyword tokens.

      :param i: Index of the token in the stream.
      :type i: int

      :return: The display name of the token.

      :rtype: str



   .. py:method:: text(i)

      Returns the raw source text of token *i*, lazily decoded from the backing
      buffer via the span offset and length. Only the requested token is
      decoded, so repeated lookups are cheap.

      :param i: Index of the token in the stream.
      :type i: int

      :return: The UTF-8 decoded source text of the token.

      :rtype: str



   .. py:attribute:: __slots__
      :value: ('types', 'starts', 'lens', '_buf')



   .. py:attribute:: _buf


   .. py:attribute:: lens


   .. py:attribute:: starts


   .. py:attribute:: types


.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokens__Buffer.png
       :alt: UML Class Diagram for _Buffer
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **_Buffer**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokens__Buffer.pdf
       :alt: UML Class Diagram for _Buffer
       :align: center
       :width: 6.5cm
       :class: uml-diagram

       UML Class Diagram for **_Buffer**

.. py:class:: _Buffer(path)

   Read-only file view with a guaranteed NUL at index `size` (needed by the
   re2c backend; harmless for flex). mmap zero-fills the final partial page for
   free; only a page-multiple file size needs a one-off copy with a NUL.


   .. py:method:: close()

      Releases the resources held by this buffer. The exported ``memoryview`` is released and the CFFI pointer is dropped before the underlying ``mmap`` (if any) is closed, ensuring no live pointer references the memory map when it is unmapped. Safe to call once after tokenization is complete.



   .. py:attribute:: __slots__
      :value: ('size', 'obj', 'cdata', 'view', '_mm')



   .. py:attribute:: cdata


   .. py:attribute:: view


.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokens__BytesBuffer.png
       :alt: UML Class Diagram for _BytesBuffer
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **_BytesBuffer**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_tokenizer_tokens__BytesBuffer.pdf
       :alt: UML Class Diagram for _BytesBuffer
       :align: center
       :width: 4.9cm
       :class: uml-diagram

       UML Class Diagram for **_BytesBuffer**

.. py:class:: _BytesBuffer(data: bytes)

   In-memory counterpart of ``_Buffer`` for tokenizing a source string
   that is already resident (a parser chunk). Appends the NUL sentinel the
   re2c backend needs; exposes the same ``cdata`` / ``view`` / ``size`` /
   ``close`` surface as ``_Buffer`` so ``Tokens`` is agnostic to the source.


   .. py:method:: close()

      Releases the resources held by this in-memory buffer. The exported ``memoryview`` is released and the CFFI pointer is dropped so no live pointer references the byte string afterwards. Safe to call once after tokenization is complete.



   .. py:attribute:: __slots__
      :value: ('size', 'obj', 'cdata', 'view')



   .. py:attribute:: cdata


   .. py:attribute:: obj


   .. py:attribute:: size


   .. py:attribute:: view


.. py:function:: _tokenize_buffer(buf) -> Tokens

   Two-pass tokenization over any buffer exposing ``cdata`` / ``size``.
   Pass 1 counts tokens in C so the parallel int32 arrays can be sized
   exactly; Pass 2 fills them. Shared by :func:`get_tokens` (mmap) and
   :func:`get_tokens_from_bytes` (in-memory) so the count/fill logic lives
   in one place.

   :param buf: A buffer object (``_Buffer`` or ``_BytesBuffer``) exposing
       ``cdata`` and ``size`` for the C scanner.
   :type buf: typing.Any

   :return: A :class:`Tokens` object holding the parallel token arrays.

   :rtype: Tokens


.. py:function:: get_tokens(path: str) -> Tokens

   Tokenizes the file at *path* via mmap. No whole-file Python ``str`` is
   built, so this is the fast / low-memory entry point for large ontologies.
   The returned :class:`Tokens` owns the mapping; call ``.close()`` (or use
   it as a context manager) to release it.

   :param path: Filesystem path of the file to tokenize.
   :type path: str

   :return: The token stream backed by a memory-mapped buffer.

   :rtype: Tokens


.. py:function:: get_tokens_from_bytes(data: bytes) -> Tokens

   Tokenizes an in-memory source already decoded to UTF-8 *bytes* (e.g. a
   parser chunk). Same :class:`Tokens` output as :func:`get_tokens`, without
   a file or mmap.

   :param data: The UTF-8 encoded source bytes to tokenize.
   :type data: bytes

   :return: The token stream backed by an in-memory buffer.

   :rtype: Tokens


.. py:data:: COMMA
   :value: 7


.. py:data:: EQ
   :value: 126


.. py:data:: ERROR
   :value: 10


.. py:data:: FADD
   :value: 93


.. py:data:: FDIV
   :value: 96


.. py:data:: FIRST_KEYWORD
   :value: 57


.. py:data:: FMUL
   :value: 95


.. py:data:: FSUB
   :value: 94


.. py:data:: GE
   :value: 125


.. py:data:: IDENT
   :value: 9


.. py:data:: LBRACE
   :value: 5


.. py:data:: LBRACK
   :value: 3


.. py:data:: LE
   :value: 124


.. py:data:: LPAREN
   :value: 1


.. py:data:: MINUS
   :value: 122


.. py:data:: NUMBER
   :value: 8


.. py:data:: PLUS
   :value: 121


.. py:data:: RBRACE
   :value: 6


.. py:data:: RBRACK
   :value: 4


.. py:data:: RPAREN
   :value: 2


.. py:data:: STAR
   :value: 123


.. py:data:: TOK_NAMES

.. py:data:: T_EOF
   :value: 131


.. py:data:: T_IDENT
   :value: 9


.. py:data:: _PAGE
   :value: 16384

