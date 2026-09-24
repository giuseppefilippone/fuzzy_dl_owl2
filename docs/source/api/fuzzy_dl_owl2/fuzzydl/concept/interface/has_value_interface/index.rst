fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface
===========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface







.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class that augments role-based fuzzy description-logic concepts with the ability to carry and expose an arbitrary filler value.


Description
-----------


HasValueInterface builds on HasRoleInterface, delegating all role handling to the superclass constructor and layering a single additional piece of state on top: a value of any type, held in a private attribute and exposed through a read/write property. Because the value is typed as ``typing.Any``, the abstraction stays deliberately agnostic about whether the filler is an individual, a data value, or something else entirely, which makes it reusable across the different kinds of value-carrying concepts in the fuzzy DL framework, such as value restrictions and datatype fillers. Since it is an ``abc.ABC``, it cannot be instantiated directly and instead acts as a mixin-style contract that concrete concept classes inherit from. One notable design point is that the setter stores the value **by reference** — the deep-copy safeguard that would isolate the internal state from external mutation survives only as a commented-out line — so mutable values assigned through the property remain shared with the caller, and the getter likewise returns the stored object without copying, meaning outside modifications to a mutable value will be visible through the interface.

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