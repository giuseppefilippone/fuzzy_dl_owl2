fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface
===========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class that extends role management capabilities by incorporating a generic value attribute protected by deep copy operations to ensure state isolation.


Description
-----------


Building upon the foundation of role management, this abstract class introduces a mechanism to associate an arbitrary value with a specific role. The design prioritizes data integrity by utilizing a deep copy operation whenever the value is modified, ensuring that the internal state remains isolated from any subsequent changes to the original input object. By combining role and value attributes into a single interface, it provides a consistent structure for representing complex data relationships within the broader system. This approach allows subclasses to leverage robust encapsulation, where the stored value is effectively shielded from external side effects, which is particularly important for maintaining consistency in fuzzy logic or description logic operations.

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


      Updates the internal state of the instance by assigning a deep copy of the provided argument to the `_value` attribute. This setter accepts any Python object and ensures that subsequent modifications to the original input object do not affect the stored value. Because it relies on `copy.deepcopy`, the operation may be computationally expensive for complex objects and will raise an error if the input cannot be deep-copied.

      :param value: The value to set. A deep copy of this object is stored internally to prevent external mutations from affecting the internal state.
      :type value: typing.Any

