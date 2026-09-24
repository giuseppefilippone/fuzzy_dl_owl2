fuzzy_dl_owl2.fuzzydl.graph.digraph
===================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.graph.digraph

.. autoapi-nested-parse::

   Lightweight directed graph backed by a plain adjacency list.

   Drop-in replacement for the subset of ``networkx.DiGraph`` used by
   ``KnowledgeBase.is_tbox_acyclic`` and related helpers.  Building edges
   via ``add_edge`` and checking for cycles via ``has_cycle`` is 10-50x
   faster than networkx because it avoids per-edge dict/set bookkeeping,
   decorator overhead, and the generic ``find_cycle`` edge-DFS iterator.






.. ── LLM-GENERATED DESCRIPTION START ──

A minimal directed graph, **DiGraph**, that stores its edges in a plain adjacency dictionary and answers cycle queries with an iterative depth-first search, acting as a fast drop-in replacement for the small slice of ``networkx.DiGraph`` that the fuzzy description-logic engine needs when checking whether a TBox is acyclic.


Description
-----------


Checking TBox acyclicity is a hot path in the reasoner, and networkx's generality — per-edge dictionary and set bookkeeping, decorator overhead, and the generic edge-DFS iterator behind ``find_cycle`` — makes it 10-50x slower than necessary for this use case. The replacement therefore provides only the operations actually consumed by ``KnowledgeBase.is_tbox_acyclic`` and related helpers: appending edges, deciding whether a directed cycle exists, and reporting basic node and edge counts, while mirroring the networkx method names so callers can swap implementations without changing their code.

Internally the graph is nothing more than a mapping from each source node to the list of its out-neighbours, with a node's list created lazily the first time an edge leaves it, and ``__slots__`` pins the memory footprint down to that single attribute. Edges are appended without de-duplication and only source nodes become dictionary keys, so parallel edges are counted individually and nodes seen purely as targets are invisible to the node count — a deliberate trade-off that keeps insertion cheap, since the only consumer cares about reachability rather than exact statistics.

Cycle detection uses an iterative three-colour depth-first search (white for unvisited, grey for on the current path, black for fully processed) driven by an explicit stack of node/index pairs instead of recursion, which both sidesteps Python's recursion limit on deep concept hierarchies and eliminates per-call function overhead. Encountering a grey node during the traversal proves a back edge exists, so the search returns immediately; if every node finishes black, the graph is declared acyclic.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.graph.digraph.DiGraph


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_graph_digraph_DiGraph.png
       :alt: UML Class Diagram for DiGraph
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **DiGraph**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_graph_digraph_DiGraph.pdf
       :alt: UML Class Diagram for DiGraph
       :align: center
       :width: 8.0cm
       :class: uml-diagram

       UML Class Diagram for **DiGraph**

.. py:class:: DiGraph

   Minimal directed graph using ``dict[int, list[int]]``.


   .. py:method:: add_edge(u: int, v: int) -> None

      Appends a directed edge ``u -> v`` to the graph. If ``u`` already has
      outgoing edges, ``v`` is appended to the existing list; otherwise a new
      list is created.

      :param u: The source node.
      :type u: int
      :param v: The target node.
      :type v: int



   .. py:method:: has_cycle() -> bool

      Detects whether the graph contains at least one directed cycle using an
      iterative three-colour depth-first search (white = unvisited, grey = on
      recursion stack, black = fully processed).

      :return: ``True`` if a directed cycle exists, ``False`` otherwise.

      :rtype: bool



   .. py:method:: number_of_edges() -> int

      Returns the total number of directed edges in the graph, computed by summing the lengths of every adjacency list. Because edges are appended without de-duplication, parallel edges between the same pair of nodes are counted individually.

      :return: The total number of directed edges in the graph.

      :rtype: int



   .. py:method:: number_of_nodes() -> int

      Returns the number of source nodes recorded in the adjacency list. Only nodes that appear as the source ``u`` of at least one ``add_edge`` call are counted; nodes seen exclusively as edge targets are not tracked as keys and therefore not included.

      :return: The number of source nodes in the graph.

      :rtype: int



   .. py:attribute:: BLACK
      :type:  int
      :value: 2



   .. py:attribute:: GRAY
      :type:  int
      :value: 1



   .. py:attribute:: WHITE
      :type:  int
      :value: 0



   .. py:attribute:: __slots__
      :value: ('_adj',)



   .. py:attribute:: _adj
      :type:  dict[int, Optional[list[int]]]


   .. py:property:: adj
      :type: dict[int, Optional[list[int]]]


      Returns the adjacency list mapping each source node to its list of
      out-neighbours. Nodes with no outgoing edges may be absent from the dict.

      :return: The adjacency mapping.

      :rtype: dict[int, typing.Optional[list[int]]]
