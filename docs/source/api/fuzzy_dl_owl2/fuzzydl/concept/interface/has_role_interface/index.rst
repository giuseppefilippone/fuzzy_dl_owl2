fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface
==========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface







.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class equips description-logic concepts with a uniform way to store, read, and update the role (binary relation) they are associated with.


Description
-----------


In the fuzzydl framework, concepts such as existential or universal restrictions quantify over a role, so many concept implementations need a shared, reusable mechanism for holding that role name. **HasRoleInterface** supplies exactly that: its constructor accepts a role string and stores it in a private attribute, while a property pair exposes read and write access so the role can be inspected or replaced at any point during the object's lifetime. The design is intentionally minimal — no runtime type checking or validation is performed, and the constructor's type hint is advisory only — which keeps the mixin lightweight and imposes no behavioural constraints on the classes that inherit it beyond the storage contract itself. By centralising this small piece of state management, the interface eliminates duplicated boilerplate across every role-bearing concept and guarantees that all such concepts interact with their role through one consistent API.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface.HasRoleInterface


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_interface_has_role_interface_HasRoleInterface.png
       :alt: UML Class Diagram for HasRoleInterface
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **HasRoleInterface**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_interface_has_role_interface_HasRoleInterface.pdf
       :alt: UML Class Diagram for HasRoleInterface
       :align: center
       :width: 5.5cm
       :class: uml-diagram

       UML Class Diagram for **HasRoleInterface**

.. py:class:: HasRoleInterface(role: str)

   Bases: :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface.HasRoleInterface
      :parts: 1
      :private-bases:


   This abstract base class provides a standard implementation for managing a role attribute, designed to be inherited by classes that need to track a specific context or function. It initializes with a string representing the role and exposes this value through getter and setter properties, enabling the role to be accessed or dynamically modified throughout the object's lifecycle. By integrating this component, classes gain a consistent mechanism for handling role-based state without needing to implement the logic themselves.

   :param _role: Internal storage for the current role that the class is working with or representing.
   :type _role: str


   .. py:attribute:: _role
      :type:  str


   .. py:property:: role
      :type: str


      Returns the name of the role (binary relation) associated with this concept, such as the role quantified over by an existential or universal restriction. The value is read from the private ``_role`` attribute without modifying the instance.

      :return: The associated role name.

      :rtype: str