fuzzy_dl_owl2.fuzzydl.role_parent_with_degree
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.role_parent_with_degree



.. ── LLM-GENERATED DESCRIPTION START ──

Models a weighted hierarchical relationship between a role and its parent by associating a specific inclusion degree with the parent identifier.


Description
-----------


Designed to support fuzzy logic reasoning, the software captures the extent to which a parent role is included within a specific hierarchy, moving beyond simple binary relationships. It encapsulates a string identifier for the parent entity alongside a floating-point value that quantifies the strength or probability of the inheritance link, typically constrained between zero and one. By providing direct access to these stored values, the logic allows external systems to evaluate complex role inheritance rules where relationships are graded rather than absolute. The absence of strict validation logic ensures flexibility for various input scenarios, relying on the calling context to enforce specific constraints on the degree or naming conventions.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.role_parent_with_degree.RoleParentWithDegree


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_role_parent_with_degree_RoleParentWithDegree.png
       :alt: UML Class Diagram for RoleParentWithDegree
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **RoleParentWithDegree**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_role_parent_with_degree_RoleParentWithDegree.pdf
       :alt: UML Class Diagram for RoleParentWithDegree
       :align: center
       :width: 8.5cm
       :class: uml-diagram

       UML Class Diagram for **RoleParentWithDegree**

.. py:class:: RoleParentWithDegree(parent: str, degree: float)

   This class models a weighted hierarchical relationship between a role and its parent, capturing the extent to which the parent role is included. It stores a string identifier for the parent role alongside a floating-point degree value, which usually represents a probability or strength of inclusion within the range of 0 to 1. Users can instantiate this object with the parent name and degree, and subsequently retrieve these values via the getter methods to support complex role inheritance logic.

   :param parent: The name of the parent role.
   :type parent: str
   :param degree: Inclusion degree of the parent role, ranging from 0 to 1.
   :type degree: float


   .. py:method:: get_degree() -> float

      Retrieves the current degree value associated with the instance. This method serves as an accessor for the `degree` attribute, returning the stored numeric value without modifying the object's internal state. It is typically used to inspect the specific weight or metric assigned to this role.

      :return: The degree value associated with the object.

      :rtype: float



   .. py:method:: get_parent() -> str

      Retrieves the parent identifier associated with the current role instance. This method returns the string value stored in the `parent` attribute, representing the hierarchical relationship or predecessor of the current role. It is a read-only operation that does not alter the object's state.

      :return: The string representing the parent of the object.

      :rtype: str



   .. py:attribute:: degree
      :type:  float


   .. py:attribute:: parent
      :type:  str

