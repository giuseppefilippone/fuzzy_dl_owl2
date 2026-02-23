import typing


class ClassificationNode:
    """
    This entity models a specific concept within a classification hierarchy, serving as a fundamental building block for the reasoner's logic. It maintains a collection of equivalent names (synonyms) and manages weighted directed connections to other nodes, representing relationships such as inheritance or association. Users can instantiate this object to define a concept, add alternative labels, and establish weighted links to other concepts to build a graph structure. The class also includes logic to identify universal concepts (top) and empty concepts (bottom) based on specific naming conventions. It is important to note that the underlying data structures for names and edges are shared across all instances, meaning modifications affect the global classification state rather than being isolated to a single object instance.

    :param EQUIVALENT_NAMES: A collection of alternative names or labels that identify the node.
    :type EQUIVALENT_NAMES: set[str]
    :param INPUT_EDGES: A dictionary mapping source nodes to the weights of input edges.
    :type INPUT_EDGES: dict[typing.Self, float]
    :param OUTPUT_EDGES: Maps destination nodes to the weights of the edges originating from this node.
    :type OUTPUT_EDGES: dict[typing.Self, float]
    """


    EQUIVALENT_NAMES: set[str] = set()
    INPUT_EDGES: dict[typing.Self, float] = dict()
    OUTPUT_EDGES: dict[typing.Self, float] = dict()

    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the ClassificationNode class with the specified name. As a side effect of instantiation, the provided name is added to the class-level collection `EQUIVALENT_NAMES`, ensuring it is tracked globally across the classification system. If the name already exists within the collection, it will be ignored without raising an error.

        :param name: The name of the node to be registered as an equivalent name.
        :type name: str
        """

        ClassificationNode.EQUIVALENT_NAMES.add(name)

    def is_thing(self) -> bool:
        """
        Determines whether the current classification node represents the root entity or the universal 'thing' node. This method returns `True` if the node's name is exactly the string '*top*', which typically signifies the top of the hierarchy, and `False` for any other node. The operation relies on the `has_name` method to perform the name comparison.

        :return: True if the object has the name '*top*', otherwise False.

        :rtype: bool
        """

        return self.has_name("*top*")

    def is_nothing(self) -> bool:
        """
        Checks if the current node represents the special "nothing" concept within the classification hierarchy. This is determined by verifying whether the node's internal name corresponds to the sentinel value "*bottom*". The method returns True if the name matches this specific string, and False otherwise. This operation does not modify the node's state.

        :return: True if the object represents the 'nothing' value, False otherwise.

        :rtype: bool
        """

        return self.has_name("*bottom*")

    def add_input_edge(self, node: typing.Self, n: float) -> None:
        """
        Updates the class-level registry of input edges by associating a specific node instance with a floating-point weight. This method assigns the provided value to the shared `INPUT_EDGES` dictionary using the node as the key, effectively creating or updating the edge's weight. Because this modifies a class attribute, the change affects the global state of the `ClassificationNode` class rather than being isolated to the instance calling the method. If the node is already present in the registry, its existing value will be replaced.

        :param node: The source node for the input edge, required to be an instance of the same class.
        :type node: typing.Self
        :param n: The weight of the input edge.
        :type n: float
        """

        ClassificationNode.INPUT_EDGES[node] = n

    def add_ouput_edge(self, node: typing.Self, n: float) -> None:
        """
        Registers a weighted output edge to a specific target node within the class-level registry. This method accepts a target node instance and a floating-point weight, mapping the target to the weight in the shared `OUTPUT_EDGES` dictionary. Because this dictionary is a class attribute, the modification affects the global state of the `ClassificationNode` class rather than being isolated to the current instance. If the target node already exists as a key in the registry, its associated weight will be overwritten by the new value.

        :param node: The destination node instance to which the output edge connects.
        :type node: typing.Self
        :param n: The weight or value associated with the output edge to the specified node.
        :type n: float
        """

        ClassificationNode.OUTPUT_EDGES[node] = n

    def remove_input_edge(self, node: typing.Self, n: float) -> None:
        """
        Conditionally removes an input edge from the class-level collection of edges based on a threshold value. This method checks the `INPUT_EDGES` dictionary for an entry corresponding to the specified `node`. If the entry exists and its associated value is less than or equal to the provided float `n`, the edge is deleted from the dictionary. The operation has no effect if the node is not present or if its value exceeds the threshold, and it modifies the shared class state directly.

        :param node: The node representing the source of the input edge to be removed if its associated value is less than or equal to the specified threshold.
        :type node: typing.Self
        :param n: Threshold value used to determine if the input edge should be removed. The edge is deleted if its current value is less than or equal to this number.
        :type n: float
        """

        value: typing.Optional[float] = ClassificationNode.INPUT_EDGES.get(node)
        if value is not None and value <= n:
            del ClassificationNode.INPUT_EDGES[node]

    def remove_ouput_edge(self, node: typing.Self, n: float) -> None:
        """
        Removes an output edge connection to the specified `ClassificationNode` instance from the shared class registry if the associated weight meets a specific threshold. It checks the class-level `OUTPUT_EDGES` dictionary for the target node and deletes the entry only if the node exists and its corresponding value is less than or equal to the provided float `n`. This method modifies the shared class state, but it has no effect if the node is not currently connected or if its weight exceeds the threshold.

        :param node: The target node to remove from the output edges.
        :type node: typing.Self
        :param n: Threshold value used to determine if the edge should be removed; the edge is deleted if its associated value is less than or equal to this number.
        :type n: float
        """

        value: typing.Optional[float] = ClassificationNode.OUTPUT_EDGES.get(node)
        if value is not None and value <= n:
            del ClassificationNode.OUTPUT_EDGES[node]

    def has_name(self, name: str) -> bool:
        """
        Determines whether the provided string matches any of the equivalent names defined for this classification node. The method performs a case-sensitive check against the class-level `EQUIVALENT_NAMES` collection, returning `True` if an exact match is found and `False` otherwise. This operation is read-only and does not alter the state of the node.

        :param name: The name to verify against the list of equivalent names.
        :type name: str

        :return: True if the provided name is an equivalent name for this node, False otherwise.

        :rtype: bool
        """

        for s in ClassificationNode.EQUIVALENT_NAMES:
            if s == name:
                return True
        return False

    def add_label(self, c: str) -> None:
        """
        Adds the specified string to the class-level collection of equivalent names associated with this classification node. This method modifies the shared `EQUIVALENT_NAMES` attribute, meaning the addition affects all instances of the class rather than just the specific instance calling the method. If the provided string is already present in the collection, the set remains unchanged.

        :param c: The label or alias to add to the set of equivalent names.
        :type c: str
        """

        ClassificationNode.EQUIVALENT_NAMES.add(c)

    def get_output_edges() -> dict[typing.Self, float]:
        """
        Retrieves the mapping of outgoing edges associated with this node, where the keys are target `ClassificationNode` instances and the values are floating-point weights representing the strength or probability of the connection. This method returns a direct reference to the class-level `OUTPUT_EDGES` attribute, meaning that any modifications made to the returned dictionary will affect the shared state of the class. If the node has no outgoing connections, an empty dictionary is returned.

        :return: A dictionary mapping target nodes to their associated edge weights.

        :rtype: dict[typing.Self, float]
        """

        return ClassificationNode.OUTPUT_EDGES

    def get_immediate_successors() -> set[typing.Self]:
        """
        Returns a set containing the immediate successor nodes of the current classification node. This method retrieves the keys from the class-level `INPUT_EDGES` mapping, representing the nodes directly connected to the current one. The operation does not modify the graph structure and returns an empty set if no successors exist.

        :return: A set containing the nodes that are immediate successors of the current node.

        :rtype: set[typing.Self]
        """

        return set(ClassificationNode.INPUT_EDGES.keys())

    def get_immediate_predecessors() -> set[typing.Self]:
        """
        Returns a set containing all nodes that are keys in the class-level `OUTPUT_EDGES` dictionary, representing the immediate predecessors within the classification graph structure. This method accesses the shared class attribute to identify source nodes and returns a new set object, ensuring that modifications to the result do not impact the underlying graph data. If the `OUTPUT_EDGES` mapping is empty, the method returns an empty set.

        :return: A set of the immediate predecessor nodes.

        :rtype: set[typing.Self]
        """

        return set(ClassificationNode.OUTPUT_EDGES.keys())

    def get_full_name(self) -> str:
        """
        Generates a comprehensive string representation of the classification node's identity by inspecting the class-level collection of equivalent names. If the collection contains exactly one entry, the method returns the standard string representation of the node instance. Conversely, if multiple equivalent names exist, it concatenates them with spaces and wraps the result in curly braces to denote a group of synonymous terms. This approach ensures that the output reflects the complexity of the classification's nomenclature without modifying the instance's state.

        :return: A string representing the full name of the classification node. If multiple equivalent names exist, they are returned as a space-separated list enclosed in braces; otherwise, the standard string representation is returned.

        :rtype: str
        """

        if len(ClassificationNode.EQUIVALENT_NAMES) == 1:
            return str(self)
        return f"{{{ ' '.join(name for name in ClassificationNode.EQUIVALENT_NAMES) }}}"

    def __hash__(self) -> int:
        """
        Returns the hash value of the node, allowing instances of `ClassificationNode` to be used as dictionary keys or stored in sets. The hash is calculated based on the string representation of the object, meaning that two nodes with identical string representations will produce the same hash value. This implementation relies on the `__str__` method to define the identity used for hashing.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))

    def __repr__(self) -> str:
        """
        Returns the official string representation of the classification node by delegating to the `__str__` method. This ensures that the output used for debugging and logging matches the user-friendly string representation. The method does not modify the object's state and simply returns a formatted string describing the node's content.

        :return: A string representation of the object.

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Returns the canonical string representation of the classification node by extracting the first element from the class-level collection of equivalent names. This method serves as the primary human-readable identifier for the node, effectively selecting the preferred name from a set of synonyms. It relies on the existence of at least one entry in the `EQUIVALENT_NAMES` collection; otherwise, an `IndexError` will be raised.

        :return: Returns the primary name of the classification node, derived from the first element of the equivalent names collection.

        :rtype: str
        """

        return list(ClassificationNode.EQUIVALENT_NAMES)[0]
