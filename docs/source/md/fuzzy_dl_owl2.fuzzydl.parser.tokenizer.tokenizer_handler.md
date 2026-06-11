# Summary

Manages a registry of tokenizer backends for the fuzzy-DL parser, providing a unified interface that abstracts over pure-Python and compiled C implementations.

## Description

The software provides a flexible tokenization system designed to feed a recursive-descent parser with a consistent stream of 4-tuples containing token kind, value, normalized text, and offset. It implements a strategy pattern where a central handler inspects the runtime environment to select the most efficient backend, prioritizing compiled C extensions for speed while falling back to a pure Python regex implementation if necessary. To support the specific syntax of fuzzy-DL, the logic includes specialized handling for splitting compound identifiers on arithmetic operators and converts numeric literals into appropriate Python types. For large inputs, the architecture supports streaming by breaking source files into chunks based on top-level form boundaries, ensuring that memory usage remains bounded even when processing multi-gigabyte files.
