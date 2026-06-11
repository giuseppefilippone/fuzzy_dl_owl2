"""Lightweight directed graph backed by a plain adjacency list.

Drop-in replacement for the subset of ``networkx.DiGraph`` used by
``KnowledgeBase.is_tbox_acyclic`` and related helpers.  Building edges
via ``add_edge`` and checking for cycles via ``has_cycle`` is 10-50x
faster than networkx because it avoids per-edge dict/set bookkeeping,
decorator overhead, and the generic ``find_cycle`` edge-DFS iterator.
"""

from __future__ import annotations

import typing


class DiGraph:
    """Minimal directed graph using ``dict[int, list[int]]``."""

    # Color constants for cycle detection.
    WHITE: int = 0
    GRAY: int = 1
    BLACK: int = 2

    # Using __slots__ to reduce memory usage and improve performance, since we only need one attribute.
    __slots__ = ("_adj",)

    def __init__(self) -> None:
        """
        Initializes an empty directed graph. The adjacency mapping ``_adj`` is created as an empty ``dict`` that lazily associates each source node with the list of its out-neighbours as edges are added.
        """

        self._adj: dict[int, typing.Optional[list[int]]] = {}

    @property
    def adj(self) -> dict[int, typing.Optional[list[int]]]:
        """
        Returns the adjacency list mapping each source node to its list of
        out-neighbours. Nodes with no outgoing edges may be absent from the dict.

        :return: The adjacency mapping.

        :rtype: dict[int, typing.Optional[list[int]]]
        """

        return self._adj

    def add_edge(self, u: int, v: int) -> None:
        """
        Appends a directed edge ``u -> v`` to the graph. If ``u`` already has
        outgoing edges, ``v`` is appended to the existing list; otherwise a new
        list is created.

        :param u: The source node.
        :type u: int
        :param v: The target node.
        :type v: int
        """

        neighbors: typing.Optional[list[int]] = self._adj.get(u)
        if neighbors is not None:
            neighbors.append(v)
        else:
            self.adj[u] = [v]

    def has_cycle(self) -> bool:
        """
        Detects whether the graph contains at least one directed cycle using an
        iterative three-colour depth-first search (white = unvisited, grey = on
        recursion stack, black = fully processed).

        :return: ``True`` if a directed cycle exists, ``False`` otherwise.

        :rtype: bool
        """

        color: dict[int, int] = {}
        for node in self.adj:
            if color.get(node, DiGraph.WHITE) != DiGraph.WHITE:
                continue
            stack: list[tuple[int, int]] = [(node, 0)]
            color[node] = DiGraph.GRAY
            while stack:
                v, idx = stack[len(stack) - 1]
                neighbors: typing.Optional[list[int]] = self.adj.get(v)
                if neighbors is not None and idx < len(neighbors):
                    stack[len(stack) - 1] = (v, idx + 1)
                    w = neighbors[idx]
                    c = color.get(w, DiGraph.WHITE)
                    if c == DiGraph.GRAY:
                        return True
                    if c == DiGraph.WHITE:
                        color[w] = DiGraph.GRAY
                        stack.append((w, 0))
                else:
                    stack.pop()
                    color[v] = DiGraph.BLACK
        return False

    def number_of_nodes(self) -> int:
        """
        Returns the number of source nodes recorded in the adjacency list. Only nodes that appear as the source ``u`` of at least one ``add_edge`` call are counted; nodes seen exclusively as edge targets are not tracked as keys and therefore not included.

        :return: The number of source nodes in the graph.

        :rtype: int
        """

        return len(self._adj)

    def number_of_edges(self) -> int:
        """
        Returns the total number of directed edges in the graph, computed by summing the lengths of every adjacency list. Because edges are appended without de-duplication, parallel edges between the same pair of nodes are counted individually.

        :return: The total number of directed edges in the graph.

        :rtype: int
        """

        return sum(len(v) for v in self._adj.values() if v is not None)
