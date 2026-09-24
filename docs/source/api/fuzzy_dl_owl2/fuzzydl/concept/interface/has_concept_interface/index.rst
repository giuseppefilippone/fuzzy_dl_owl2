fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface
=============================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface







.. ── LLM-GENERATED DESCRIPTION START ──

An abstract interface that lets implementing classes wrap, inspect, and replace a single fuzzy ``Concept`` object through a managed property.


Description
-----------


``HasConceptInterface`` defines a small mixin contract for any entity in the fuzzy description-logic framework that operates on exactly one concept, such as unary concept constructors or modifiers. Subclasses initialise the wrapper by passing a ``Concept`` to the constructor, which stores it by reference in a private attribute; because no validation or deep copying is performed, later mutations of the original ``Concept`` remain visible through the wrapper. All access is funnelled through the ``curr_concept`` property, whose getter exposes the currently wrapped operand and whose setter allows that operand to be swapped for a different concept at runtime. Centralising the storage-and-update logic behind a property gives every concrete concept-wrapping type a uniform, encapsulated way to track the operand it is currently manipulating, while deriving from ``abc.ABC`` marks the class as intended for inheritance rather than direct instantiation.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface.HasConceptInterface


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_interface_has_concept_interface_HasConceptInterface.png
       :alt: UML Class Diagram for HasConceptInterface
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **HasConceptInterface**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_interface_has_concept_interface_HasConceptInterface.pdf
       :alt: UML Class Diagram for HasConceptInterface
       :align: center
       :width: 7.4cm
       :class: uml-diagram

       UML Class Diagram for **HasConceptInterface**

.. py:class:: HasConceptInterface(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)

   Bases: :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface.HasConceptInterface
      :parts: 1
      :private-bases:


   This class serves as an abstract base class that provides a standard interface for managing a mutable conceptual entity, ensuring that implementing objects can track and modify a specific concept. It encapsulates the logic for storing and updating the current concept through the `curr_concept` property, which allows for dynamic changes to the underlying representation at runtime. Subclasses can leverage this functionality to maintain a consistent state regarding the concept they are operating on, initializing with a specific concept instance and replacing it as needed through the provided property setter.

   :param _curr_concept: Internal storage for the active concept that the instance is currently representing or manipulating.
   :type _curr_concept: Concept


   .. py:attribute:: _curr_concept
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:property:: curr_concept
      :type: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


      Returns the single concept currently held by this object, i.e. the operand that the implementing concept wraps. The value is read from the private ``_curr_concept`` attribute without modifying the instance.

      :return: The wrapped concept.

      :rtype: Concept