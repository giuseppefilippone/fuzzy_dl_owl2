fuzzy_dl_owl2.fuzzydl.graph
===========================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_graph.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.graph
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.graph**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_graph.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.graph
       :align: center
       :width: 11.4cm
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.graph**

.. py:module:: fuzzy_dl_owl2.fuzzydl.graph



.. ── LLM-GENERATED DESCRIPTION START ──

A minimal directed-graph component that provides the fuzzy description-logic engine with fast cycle detection for TBox acyclicity checks, serving as a **drop-in replacement** for the small slice of networkx the reasoner previously relied on.


Description
-----------


Checking whether a TBox is acyclic is a hot path in the reasoner, and networkx's generality — per-edge dictionary and set bookkeeping, decorator overhead, and the generic edge-DFS iterator behind its cycle finder — made it 10-50x slower than necessary for this use case. The replacement therefore exposes only the operations the reasoner actually consumes: appending edges, deciding whether a directed cycle exists, and reporting basic node and edge counts, while deliberately mirroring the networkx method names so callers can swap implementations without changing their code. Internally, the graph is nothing more than a mapping from each source node to the list of its out-neighbours, with a node's list created lazily the first time an edge leaves it and the memory footprint pinned down to that single attribute; edges are appended without de-duplication and only source nodes become dictionary keys, a deliberate trade-off that keeps insertion cheap because the sole consumer cares about reachability rather than exact statistics. Cycle detection runs as an iterative three-colour depth-first search — white for unvisited, grey for on the current path, black for fully processed — driven by an explicit stack of node/index pairs instead of recursion, which both sidesteps Python's recursion limit on deep concept hierarchies and eliminates per-call function overhead; encountering a grey node during the traversal proves a back edge exists, so the search returns immediately, whereas a traversal in which every node finishes black certifies the graph acyclic.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.graph.digraph``] — A minimal directed graph, **DiGraph**, that stores its edges in a plain adjacency dictionary and answers cycle queries with an iterative depth-first search, acting as a fast drop-in replacement for the small slice of ``networkx.DiGraph`` that the fuzzy description-logic engine needs when checking whether a TBox is acyclic.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/graph/digraph/index

