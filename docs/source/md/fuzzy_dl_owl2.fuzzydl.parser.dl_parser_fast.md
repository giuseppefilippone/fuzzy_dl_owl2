# Summary

A high-performance recursive-descent parser that acts as a drop-in replacement for the legacy FuzzyDL parser by reusing semantic actions while eliminating backtracking and caching overhead.

## Description

Designed as a high-speed alternative to the original implementation, this software employs a hand-rolled tokenizer combined with a deterministic recursive-descent strategy to process FuzzyDL syntax. Instead of reimplementing the logic for building the knowledge base, it imports the legacy `DLParser` class and invokes its semantic action callbacks with pre-processed token lists, ensuring identical behavior while drastically reducing computational overhead. The architecture eliminates the need for backtracking, packrat caching, and complex recursion limits found in the older version, resulting in a significant performance increase even when run as standard Python code. To handle large inputs efficiently, the implementation supports streaming the source text in bounded chunks, which keeps memory usage proportional to the chunk size rather than the total file size. Additionally, the code is structured to allow compilation with Cython for native-code execution, further accelerating the parsing of complex fuzzy description logic ontologies.
