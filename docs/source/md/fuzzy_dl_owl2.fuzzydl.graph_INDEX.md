# Summary

A high-performance directed graph implementation optimized for rapid cycle detection and edge construction during knowledge base acyclicity checks.

## Description

Designed as a lightweight alternative to generic graph libraries, the software utilizes a plain adjacency list backed by a dictionary of lists to eliminate the overhead associated with per-edge bookkeeping and decorator calls. Cycle detection relies on an iterative three-color depth-first search algorithm that identifies back edges without recursion, ensuring efficient acyclicity verification for knowledge bases. Memory footprint is minimized through the use of `__slots__`, while the architecture specifically tracks only nodes acting as edge sources and supports parallel edges to maximize utility. These optimizations collectively deliver a ten to fifty-fold performance improvement over standard networkx operations for edge building and cycle analysis.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.graph.digraph`] — A high-performance directed graph structure designed specifically for efficient cycle detection and edge construction.
