# Summary

A minimal directed graph, **DiGraph**, that stores its edges in a plain adjacency dictionary and answers cycle queries with an iterative depth-first search, acting as a fast drop-in replacement for the small slice of `networkx.DiGraph` that the fuzzy description-logic engine needs when checking whether a TBox is acyclic.

## Description

Checking TBox acyclicity is a hot path in the reasoner, and networkx's generality — per-edge dictionary and set bookkeeping, decorator overhead, and the generic edge-DFS iterator behind `find_cycle` — makes it 10-50x slower than necessary for this use case. The replacement therefore provides only the operations actually consumed by `KnowledgeBase.is_tbox_acyclic` and related helpers: appending edges, deciding whether a directed cycle exists, and reporting basic node and edge counts, while mirroring the networkx method names so callers can swap implementations without changing their code.

Internally the graph is nothing more than a mapping from each source node to the list of its out-neighbours, with a node's list created lazily the first time an edge leaves it, and `__slots__` pins the memory footprint down to that single attribute. Edges are appended without de-duplication and only source nodes become dictionary keys, so parallel edges are counted individually and nodes seen purely as targets are invisible to the node count — a deliberate trade-off that keeps insertion cheap, since the only consumer cares about reachability rather than exact statistics.

Cycle detection uses an iterative three-colour depth-first search (white for unvisited, grey for on the current path, black for fully processed) driven by an explicit stack of node/index pairs instead of recursion, which both sidesteps Python's recursion limit on deep concept hierarchies and eliminates per-call function overhead. Encountering a grey node during the traversal proves a back edge exists, so the search returns immediately; if every node finishes black, the graph is declared acyclic.
