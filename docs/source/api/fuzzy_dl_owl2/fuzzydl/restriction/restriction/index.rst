fuzzy_dl_owl2.fuzzydl.restriction.restriction
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.restriction.restriction



.. ── LLM-GENERATED DESCRIPTION START ──

A class representing a universal restriction that combines a role, a concept, and a degree threshold within a fuzzy logic framework.


Description
-----------


The software models a universal restriction within a logical framework by combining a specific role, a target concept, and a lower bound degree to define a constraint. It represents the condition that for all entities connected via the given role, they must belong to the specified concept with a certainty or membership level that meets or exceeds the provided degree. The structure supports cloning to create independent copies of the restriction and provides accessors for the role name, concept, and degree. String representations are generated to reflect the logical syntax, including a format that explicitly includes the degree threshold as an inequality.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.restriction.restriction.Restriction


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_restriction_restriction_Restriction.png
       :alt: UML Class Diagram for Restriction
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **Restriction**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_restriction_restriction_Restriction.pdf
       :alt: UML Class Diagram for Restriction
       :align: center
       :width: 13.4cm
       :class: uml-diagram

       UML Class Diagram for **Restriction**

.. py:class:: Restriction(role_name: str, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree)

   This class models a universal restriction within a logical framework, combining a specific role, a target concept, and a lower bound degree to define a constraint. It represents the condition that for all entities connected via the given role, they must belong to the specified concept with a certainty or membership level that meets or exceeds the provided degree. The structure supports cloning and provides string representations that reflect the logical syntax, including a format that explicitly includes the degree threshold.

   :param role_name: The name of the role for which the restriction is defined.
   :type role_name: str
   :param concept: The concept defining the target of the universal restriction.
   :type concept: Concept
   :param degree: The lower bound degree defining the threshold for the restriction.
   :type degree: Degree


   .. py:method:: __repr__() -> str

      Returns the string representation of the restriction object by delegating to the `__str__` method. This implementation ensures that the official representation used by the interpreter is identical to the informal string representation, prioritizing human readability over a machine-parseable format. The method does not modify the object's state, though it will propagate any exceptions raised during the string conversion process.

      :return: Returns the string representation of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the restriction, formatted to display the constraint condition as "name >= degree". This method is primarily used for logging or displaying the object to a user, providing a clear indication of the minimum threshold enforced by the restriction. It relies on the `get_name_without_degree` method to retrieve the identifier and accesses the `degree` attribute directly, ensuring that the output reflects the current state of the object without causing any side effects.

      :return: A string representation of the object in the format 'name >= degree'.

      :rtype: str



   .. py:method:: clone() -> Self

      Creates and returns a new instance of the `Restriction` class that duplicates the state of the current object. The new object is initialized with the same `role_name`, `concept`, and `degree` values as the original. This method does not modify the existing instance, providing a way to obtain an independent copy of the restriction for further use or modification.

      :return: A new instance of the class initialized with the same role name, concept, and degree as the current object.

      :rtype: typing.Self



   .. py:method:: get_concept() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the `Concept` entity to which this restriction applies. This accessor method provides direct read-only access to the underlying concept attribute without modifying the state of the `Restriction` instance. The returned object represents the specific subject or entity being constrained by the current restriction logic.

      :return: The Concept object associated with this instance.

      :rtype: Concept



   .. py:method:: get_degree() -> fuzzy_dl_owl2.fuzzydl.degree.degree.Degree

      Returns the `Degree` object associated with this `Restriction` instance. This method provides access to the internal `degree` attribute, allowing the caller to inspect the specific degree defined by the restriction. As a getter, it performs a read-only operation and does not alter the state of the object.

      :return: The degree associated with the object.

      :rtype: Degree



   .. py:method:: get_name_without_degree() -> str

      Constructs and returns a string representation of the restriction that excludes any specific degree or quantifier, defaulting to a universal scope. The output is formatted as a parenthetical statement combining the role name and concept with the prefix 'all', effectively describing the restriction as applying to all instances of the concept for that role.

      :return: A string representing the restriction name without the degree, formatted as '(all {role_name} {concept})'.

      :rtype: str



   .. py:method:: get_role_name() -> str

      Retrieves the name of the role associated with this restriction instance. This method acts as a getter for the internal `role_name` attribute, returning its current value without modifying the object's state. The returned value is expected to be a string representing the specific role identifier.

      :return: The name of the role.

      :rtype: str



   .. py:attribute:: concept
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: degree
      :type:  fuzzy_dl_owl2.fuzzydl.degree.degree.Degree


   .. py:attribute:: role_name
      :type:  str

