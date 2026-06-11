# Summary

A high-performance directed graph structure designed specifically for efficient cycle detection and edge construction.

## Description

The implementation serves as a highly optimized drop-in replacement for the subset of `networkx.DiGraph` functionality required by knowledge base acyclicity checks. By utilizing a plain adjacency list backed by a dictionary of lists, the structure avoids the significant overhead associated with generic graph libraries, such as per-edge bookkeeping and decorator calls. This design choice results in a ten to fifty-fold performance improvement when building edges and detecting cycles compared to standard networkx operations. Cycle detection is performed using an iterative three-color depth-first search algorithm, which efficiently identifies back edges without recursion. Memory usage is further minimized through the use of `__slots__`, and the graph allows for parallel edges while only tracking nodes that serve as edge sources.
