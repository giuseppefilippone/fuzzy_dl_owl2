"""Tokenizer subpackage: token tables, the re2c/flex lexer and tokenizer backends.

Holds the generated token codes (``tokens``), the C-lexer CFFI/Cython
extensions (``_fdl_lexer`` / ``_fdl_tuples``), the tokenizer registry
(``tokenizer_handler``) and the generator that produces them all
(``generate_tokens``).

Kept import-light on purpose: importing this package must not pull in the
compiled lexer, so ``generate_tokens`` can run at build time before the
extensions exist.
"""