fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface
===========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract interface is provided for managing concepts that require both a specific role and an associated generic value.


Description
-----------


Building upon the foundation of role management, this abstract class introduces the capability to associate an arbitrary value with a specific role. It encapsulates this data through a private attribute that is accessible and modifiable via public properties, ensuring that subclasses can represent or manipulate specific data within a defined context. The initialization process delegates role handling to the parent class while simultaneously storing the provided value, thereby combining role and value attributes into a cohesive interface. Although the documentation suggests isolation of state, the current implementation of the value setter assigns the object by reference rather than creating a deep copy, meaning that modifications to mutable objects will affect the internal state directly.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface.HasValueInterface


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_interface_has_value_interface_HasValueInterface.png
       :alt: UML Class Diagram for HasValueInterface
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **HasValueInterface**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_interface_has_value_interface_HasValueInterface.pdf
       :alt: UML Class Diagram for HasValueInterface
       :align: center
       :width: 8.9cm
       :class: uml-diagram

       UML Class Diagram for **HasValueInterface**

.. py:class:: HasValueInterface(role: str, value: Any)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface.HasRoleInterface`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface.HasValueInterface
      :parts: 1
      :private-bases:


   This abstract base class extends role management capabilities by introducing a mechanism to handle a generic value alongside a role. It provides concrete implementations for initializing and accessing the value, with the setter specifically utilizing a deep copy operation to ensure that the internal state remains isolated from external modifications. By combining role and value attributes, it offers a consistent interface for objects that need to represent or manipulate specific data within a defined context.

   :param _value: Internal storage for the value represented by the class, managed via the public property and stored as a deep copy to prevent external mutation.
   :type _value: typing.Any


   .. py:attribute:: _value
      :type:  Any


   .. py:property:: value
      :type: Any


      Retrieves the current value stored in the instance. This getter provides access to the internal `_value` attribute without creating a copy, meaning that modifications to the returned object will affect the internal state if the object is mutable.

      :return: The value currently stored in the instance.
      :rtype: typing.Any

