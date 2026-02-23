fuzzy_dl_owl2.fuzzydl.individual.created_individual
===================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.individual.created_individual



.. ── LLM-GENERATED DESCRIPTION START ──

A class representing dynamically generated nodes within a completion forest for tableau-based reasoning, supporting hierarchical tracking, blocking mechanisms, and state cloning.


Description
-----------


Extending the base individual structure allows this component to function as a node in a tableau algorithm's completion forest, managing the creation of abstract entities derived during inference. It establishes a lineage by tracking parent nodes and the specific role relations that led to the node's generation, which enables the reasoning engine to calculate the depth of the individual and navigate the tree structure effectively. A critical aspect of the design involves optimization through blocking, which prevents infinite expansion of the reasoning process by tracking both direct and indirect blocking states and referencing specific ancestors that satisfy blocking conditions.

To handle the non-deterministic nature of tableau reasoning, the entity supports deep cloning of its internal state, including concept labels, representatives, and role relations, allowing the system to preserve snapshots for backtracking or branching scenarios. The logic utilizes a breadth-first traversal to propagate indirect blocking status to descendant nodes, ensuring that redundant branches are not explored while explicitly avoiding backtracking via inverse roles. Furthermore, the implementation distinguishes between abstract nodes and concrete instances, providing flags to manage this distinction while implementing rich comparison operators based on integer identifiers for sorting and storage within ordered collections.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_individual_created_individual_CreatedIndividual.png
       :alt: UML Class Diagram for CreatedIndividual
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **CreatedIndividual**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_individual_created_individual_CreatedIndividual.pdf
       :alt: UML Class Diagram for CreatedIndividual
       :align: center
       :width: 14.4cm
       :class: uml-diagram

       UML Class Diagram for **CreatedIndividual**

.. py:class:: CreatedIndividual(name: str, parent: Optional[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual] = None, role_name: Optional[str] = None)
              CreatedIndividual(name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.individual.individual.Individual`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual
      :parts: 1
      :private-bases:


   This class models a dynamically generated node within a completion forest, typically utilized in tableau-based reasoning algorithms to represent abstract entities derived during the inference process. It extends the base individual structure by incorporating hierarchical context, tracking the parent node and the specific role relation that led to its creation, as well as calculating its depth within the tree. The entity is designed to manage optimization states known as blocking, which prevents infinite expansion by tracking direct and indirect block statuses alongside references to blocking ancestors. Furthermore, it maintains collections of concept labels and representative individuals for handling complex constraints, supports deep cloning for state preservation, and distinguishes between abstract nodes and concrete instances.

   :raises NotImplementedError: Raised when the constructor is invoked with an unsupported number of arguments; the class only supports initialization with a single name or with a name, parent, and role name.


   .. py:method:: __created_ind_init_1(name: str, parent: Optional[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual] = None, role_name: Optional[str] = None) -> None

      Initializes a new instance of a created individual within a completion forest structure, setting up attributes necessary for tableau reasoning or blocking algorithms. It accepts a name, an optional parent individual, and an optional role name that defines the relationship to the parent. The method initializes internal collections for representatives, concept labels, and roles, and sets blocking status flags to an unchecked state. The depth of the individual is calculated based on the parent's depth if the parent is blockable; otherwise, it defaults to a depth of 2. Additionally, it marks the individual as abstract (non-concrete) by default and logs debug information if a parent is provided.

      :param name: The unique identifier or label for the individual.
      :type name: str
      :param parent: The parent individual in the completion forest structure, used to determine the depth and lineage of the new individual.
      :type parent: typing.Optional[Individual]
      :param role_name: The name of the role for which the individual is a filler.
      :type role_name: typing.Optional[str]



   .. py:method:: __created_ind_init_2(name: str) -> None

      Initializes the individual instance by delegating to the primary initialization logic with a specific set of default arguments. Specifically, it invokes `__created_ind_init_1` with the provided name and `None` for the remaining two parameters, effectively creating an individual without those specific attributes. As a side effect, it outputs a debug log message confirming the creation of the individual, displaying its name and the assigned integer ID.

      :param name: The name or identifier assigned to the individual being created.
      :type name: str



   .. py:method:: __eq__(value: Self) -> bool

      Determines equality between the current instance and another `CreatedIndividual` object by comparing their `name` attributes. The method returns `True` if the names are identical and `False` otherwise. It is important to note that passing an argument that lacks a `name` attribute will raise an `AttributeError`.

      :param value: The object to compare against, where equality is determined by comparing the 'name' attribute.
      :type value: typing.Self

      :return: True if the `name` attribute of the current instance is equal to the `name` attribute of the provided instance, otherwise False.

      :rtype: bool



   .. py:method:: __ge__(value: Self) -> bool

      Implements the greater-than-or-equal-to comparison operator for instances of the class. The method returns True if the current instance is not less than the provided value, effectively delegating the logic to the `__lt__` (less-than) implementation. This approach ensures consistency with the defined ordering but means that any side effects or exceptions raised by the less-than comparison will also occur here.

      :param value: The object to compare against the current instance.
      :type value: typing.Self

      :return: True if the object is greater than or equal to the specified value, otherwise False.

      :rtype: bool



   .. py:method:: __gt__(value: Self) -> bool

      Determines whether the current instance is strictly greater than the provided value. The operation is implemented by returning the logical negation of the less-than-or-equal-to comparison (`<=`). This method ensures that the greater-than relationship is consistent with the defined ordering for the class and expects the argument to be an instance of the same type.

      :param value: The object to compare against.
      :type value: typing.Self

      :return: True if the current instance is strictly greater than the specified value, False otherwise.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Returns an integer hash value for the instance, derived from the string representation of the object. This method enables `CreatedIndividual` instances to be used as keys in dictionaries or members of sets. Because the hash is calculated based on the output of `__str__`, any changes to the object's state that affect its string representation will alter its hash value, potentially causing issues if the object is already stored in a hash-based collection. Consequently, instances should be treated as immutable regarding their string representation if used in such contexts.

      :return: An integer hash value computed from the string representation of the object.

      :rtype: int



   .. py:method:: __le__(value: Self) -> bool

      Determines whether the current instance is less than or equal to another instance of the same class by comparing their integer identifiers. The method retrieves the integer ID of both the current object and the provided value, returning True if the current object's ID is less than or equal to the other's ID, and False otherwise. This comparison relies on the availability and comparability of the integer identifiers returned by the `get_integer_id` method.

      :param value: The object to compare against, evaluated based on its integer ID.
      :type value: typing.Self

      :return: True if the integer ID of the current instance is less than or equal to the integer ID of the specified value, otherwise False.

      :rtype: bool



   .. py:method:: __lt__(value: Self) -> bool

      Determines whether the current instance is considered less than another instance of the same class by comparing their underlying integer identifiers. The method retrieves the integer ID for both the current object and the provided value, returning `True` only if the current object's ID is numerically smaller. This comparison does not modify the state of either object and assumes that both instances provide valid integer identifiers via the `get_integer_id` method.

      :param value: Another instance of the class to compare against based on its integer ID.
      :type value: typing.Self

      :return: True if the integer ID of the current instance is less than the integer ID of the specified value.

      :rtype: bool



   .. py:method:: __ne__(value: Self) -> bool

      Determines whether the current instance is not equal to the provided value. This method is invoked by the inequality operator (`!=`) and returns the logical negation of the equality comparison (`self == value`). Consequently, its behavior is entirely dependent on the implementation of the `__eq__` method, and it does not perform any direct attribute comparison itself. If the equality check raises an exception, this method will also fail.

      :param value: The object to compare against.
      :type value: typing.Self

      :return: True if the current instance is not equal to the specified value, otherwise False.

      :rtype: bool



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the instance, which consists solely of the value stored in the `name` attribute. This method is invoked implicitly by the built-in `str()` function and the `print()` statement whenever the object needs to be displayed as a string. It performs no modification to the object's state, though it will raise an `AttributeError` if the `name` attribute has not been defined.

      :return: The string representation of the object, which is the value of the `name` attribute.

      :rtype: str



   .. py:method:: clone() -> Self

      Creates and returns a new instance that is a copy of the current object. The clone is initialized using the string representation of the original instance, a `None` value for the parent reference, and the original role name. Additionally, the method invokes `clone_special_attributes` to transfer any specific internal properties from the source to the new instance, ensuring the duplicate maintains the relevant state of the original.

      :return: A new instance of the same class that is a clone of the current object.

      :rtype: typing.Self



   .. py:method:: clone_special_attributes(ind: Self) -> None

      Copies specialized attributes from the current instance to the target instance `ind`, effectively populating `ind` with a snapshot of the source's state. The method initiates by calling the general `clone_attributes` method and then proceeds to handle fields requiring specific logic, such as deep copying mutable collections like `representatives`, `concept_list`, and `indirectly_blocked` to prevent shared references. It also handles the cloning of the `parent` node recursively if it exists, ensuring the target maintains an independent structural link. Finally, it transfers scalar values and flags, including `depth`, `directly_blocked`, `_is_concrete`, and `role_name`, directly to the target.

      :param ind: The target instance of the same class to receive the cloned special attributes.
      :type ind: typing.Self



   .. py:method:: get_depth() -> int

      Retrieves the depth value associated with the current `CreatedIndividual` instance. This method serves as a straightforward accessor for the internal `depth` attribute, returning the integer that typically represents the entity's hierarchical level or generation within a tree-like structure. As a read-only operation, it has no side effects on the object's state or the wider system.

      :return: The depth of the object.

      :rtype: int



   .. py:method:: get_integer_id() -> int

      Extracts the unique numeric identifier from the individual's name by stripping the standard default name prefix and converting the remaining characters into an integer. The method relies on the name being formatted with the default prefix followed by a valid numeric suffix; consequently, it will raise a ValueError if the name is shorter than the prefix or if the trailing characters cannot be parsed as an integer.

      :return: The integer suffix of the object's name, obtained by stripping the default prefix.

      :rtype: int



   .. py:method:: get_parent() -> Optional[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]

      Retrieves the parent entity associated with this instance. The method returns the object referenced by the internal `parent` attribute, which represents the progenitor or source of the current individual. If no parent relationship has been established, the method returns `None`. This operation is a read-only accessor and does not modify the state of the object or its parent.

      :return: The parent Individual associated with this instance, or None if no parent is set.

      :rtype: typing.Optional[Individual]



   .. py:method:: get_parent_name() -> str

      Retrieves the name of the parent entity associated with this individual. The method performs a safe check to determine if a parent object exists before attempting to access its attributes. If a parent is present, the value of the parent's `name` attribute is returned; otherwise, an empty string is returned to signify that no parent is currently assigned.

      :return: The name of the parent object, or an empty string if no parent is set.

      :rtype: str



   .. py:method:: get_representative_if_exists(type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType, f_name: str, f: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber) -> Optional[Self]

      Searches the collection of representatives associated with this instance for an entry matching the specified inequality type, feature name, and triangular fuzzy number. If a matching representative is found, the method returns the underlying individual linked to that representative; otherwise, it returns None.

      :param type: Specifies the inequality condition (e.g., GREATER_EQUAL or LESS_EQUAL) that defines the representative individual relative to the fuzzy number.
      :type type: InequalityType
      :param f_name: The name of the feature associated with the representative individual.
      :type f_name: str
      :param f: The fuzzy number defining the representative individual to retrieve.
      :type f: TriangularFuzzyNumber

      :return: The individual associated with the representative matching the specified inequality type, feature name, and fuzzy number, or None if no such representative exists.

      :rtype: typing.Optional[typing.Self]



   .. py:method:: get_role_name() -> str

      Retrieves the string identifier representing the specific function or designation assigned to this individual. This method acts as a simple accessor for the internal `role_name` attribute, providing read-only access to the entity's classification without modifying the underlying state. The returned value corresponds directly to the attribute set during the object's initialization or subsequent modification.

      :return: The name of the role.

      :rtype: str



   .. py:method:: individual_set_intersection_of(set1: sortedcontainers.SortedSet[Self], set2: sortedcontainers.SortedSet[Self]) -> sortedcontainers.SortedSet[Self]

      Computes the intersection of two sorted sets containing instances of the class, returning a new set that includes only the elements present in both input collections. This operation does not modify the original sets, ensuring that the input data remains unchanged. If the input sets share no common elements, the method returns an empty set.

      :param set1: The first sorted set of concept labels to intersect.
      :type set1: SortedSet[typing.Self]
      :param set2: The second sorted set of concept labels to intersect with the first set.
      :type set2: SortedSet[typing.Self]

      :return: A SortedSet containing the elements common to both `set1` and `set2`.

      :rtype: SortedSet[typing.Self]



   .. py:method:: is_blockable() -> bool

      Determines whether the individual is eligible for blocking by checking if it is associated with any nominals. The method returns True if the internal list of nominals is empty, signifying that the individual can be blocked, and False if the list contains one or more elements. This predicate is a read-only operation that does not alter the state of the object or its attributes.

      :return: True if the nominal list is empty, indicating that the object is blockable; False otherwise.

      :rtype: bool



   .. py:method:: is_concrete() -> bool

      Returns a boolean indicating whether the individual is concrete. This method provides access to the internal `_is_concrete` state, distinguishing between fully realized entities and abstract definitions. It performs no side effects and simply reflects the current status of the instance.

      :return: True if the object is concrete, False otherwise.

      :rtype: bool



   .. py:method:: mark_indirectly_blocked() -> None

      Performs a breadth-first traversal of the subtree rooted at the current individual, marking all reachable descendants as indirectly blocked. During traversal, the method follows role relations but explicitly skips the parent node to prevent backtracking via inverse roles. Only individuals that satisfy the `is_blockable` condition are modified; their `indirectly_blocked` attribute is updated to reflect the blocked state.



   .. py:method:: set_concrete_individual() -> None

      Marks the individual as concrete, indicating that it represents a specific, fully realized entity rather than an abstract or placeholder concept. This method updates the internal `_is_concrete` flag to `True`, effectively changing the state of the object. The operation is idempotent; calling it multiple times has the same effect as calling it once, and it does not return any value.


