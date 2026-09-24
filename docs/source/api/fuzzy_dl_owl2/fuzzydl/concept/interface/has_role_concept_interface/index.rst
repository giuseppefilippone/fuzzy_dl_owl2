fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_concept_interface
==================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_concept_interface







.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class that combines role and concept ownership into a single contract, requiring concrete subclasses to manage both a string-based role and an associated ``Concept`` object.


Description
-----------


``HasRoleConceptInterface`` merges two smaller abstractions — ``HasRoleInterface`` and ``HasConceptInterface`` — into one mixin-style contract, so any concrete subclass is guaranteed to expose the role and concept properties that those interfaces prescribe. The composition mirrors the structure of fuzzy description logic expressions such as qualified existential restrictions (∃R.C), where a role and a concept must travel together as an inseparable pair. Rather than relying on cooperative multiple inheritance through ``super()``, the constructor explicitly invokes each parent's initializer in a fixed order, which sidesteps method-resolution-order subtleties and makes the two independent initialisation steps explicit and predictable. Because the class remains abstract, it contributes no behaviour of its own beyond wiring the two concerns together; storage, validation, and property access are delegated entirely to the parent interfaces and, ultimately, to concrete implementations. This keeps the design modular, allowing role handling and concept handling to evolve independently while still giving downstream code a single, uniform type to program against.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_concept_interface.HasRoleConceptInterface


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_interface_has_role_concept_interface_HasRoleConceptInterface.png
       :alt: UML Class Diagram for HasRoleConceptInterface
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **HasRoleConceptInterface**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_interface_has_role_concept_interface_HasRoleConceptInterface.pdf
       :alt: UML Class Diagram for HasRoleConceptInterface
       :align: center
       :width: 9.0cm
       :class: uml-diagram

       UML Class Diagram for **HasRoleConceptInterface**

.. py:class:: HasRoleConceptInterface(role: str, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface.HasRoleInterface`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface.HasConceptInterface`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_concept_interface.HasRoleConceptInterface
      :parts: 1
      :private-bases:


   This abstract base class defines a contract for objects that must manage both a functional role and a specific concept. It combines the behaviors of role and concept handling, requiring implementations to provide properties for getting and setting a string-based role and a `Concept` object. This design allows for dynamic modification of the operational context and the associated domain entity, ensuring that the class can flexibly adapt to changes in the role it performs or the concept it represents.