fuzzy_dl_owl2.fuzzydl.role_parent_with_degree
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.role_parent_with_degree



.. ── LLM-GENERATED DESCRIPTION START ──

Models a weighted hierarchical relationship between a role and its parent by storing a parent identifier and an associated degree of inclusion.


Description
-----------


Designed to support complex role inheritance logic, this structure captures the extent to which a parent role is included within a child role. It associates a string identifier representing the parent with a floating-point value that quantifies the strength or probability of the relationship, typically ranging from zero to one. The implementation acts as a simple data container, storing these values directly upon initialization without applying validation logic. Accessor methods are provided to retrieve the stored parent name and degree, allowing other components of the system to inspect the specific weights assigned to hierarchical connections.

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

