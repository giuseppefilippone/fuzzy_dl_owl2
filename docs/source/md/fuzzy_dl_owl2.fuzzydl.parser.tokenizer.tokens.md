# Summary

A high-performance tokenizer for the FuzzyDL language that bridges Python and a C-based lexer using CFFI and memory mapping.

## Description

The software implements a bridge between Python and a low-level C lexer, specifically designed to parse FuzzyDL syntax efficiently. By utilizing C Foreign Function Interface (CFFI), it delegates the heavy lifting of lexical analysis to C functions while managing memory and data structures within Python. A two-pass tokenization strategy is employed where the first pass counts the tokens to allocate exact-sized NumPy arrays, and the second pass populates these arrays with token types, start offsets, and lengths. This design supports both memory-mapped file inputs for large ontologies and in-memory byte strings, ensuring that the underlying C backend receives NUL-terminated buffers regardless of the source. The resulting token stream is encapsulated in a class that allows lazy decoding of source text and provides context management to safely release system resources.
