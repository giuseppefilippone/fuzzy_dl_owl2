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

A high-performance directed graph structure designed specifically for efficient cycle detection and edge construction.


Description
-----------


The implementation serves as a highly optimized drop-in replacement for the subset of ``networkx.DiGraph`` functionality required by knowledge base acyclicity checks. By utilizing a plain adjacency list backed by a dictionary of lists, the structure avoids the significant overhead associated with generic graph libraries, such as per-edge bookkeeping and decorator calls. This design choice results in a ten to fifty-fold performance improvement when building edges and detecting cycles compared to standard networkx operations. Cycle detection is performed using an iterative three-color depth-first search algorithm, which efficiently identifies back edges without recursion. Memory usage is further minimized through the use of ``__slots__``, and the graph allows for parallel edges while only tracking nodes that serve as edge sources.

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

