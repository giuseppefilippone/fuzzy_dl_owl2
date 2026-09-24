fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface
==============================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface







.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class that provides its subclasses with shared, mutable storage for a collection of fuzzy concepts, along with a property for reading and replacing them.


Description
-----------


**HasConceptsInterface** acts as a small reusable building block for objects in the fuzzy description-logic toolkit that wrap several **Concept** operands at once, such as compound concept expressions. Its constructor accepts any iterable of concepts and immediately materialises it into a plain Python list, which both exhausts one-shot generators and creates a shallow copy that decouples the object's internal state from the caller's original collection. The stored list is exposed through a property whose getter returns it unchanged and whose setter replaces it wholesale — again converting the incoming iterable to a list — so callers can swap the entire set of operands but never append to it piecemeal. Because the class is abstract and contributes no behaviour beyond this storage contract, concrete subclasses remain free to decide how the concepts they hold are interpreted or combined, while relying on the interface for consistent access to their operands.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface.HasConceptsInterface


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_interface_has_concepts_interface_HasConceptsInterface.png
       :alt: UML Class Diagram for HasConceptsInterface
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **HasConceptsInterface**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_interface_has_concepts_interface_HasConceptsInterface.pdf
       :alt: UML Class Diagram for HasConceptsInterface
       :align: center
       :width: 10.4cm
       :class: uml-diagram

       UML Class Diagram for **HasConceptsInterface**

.. py:class:: HasConceptsInterface(concepts: Iterable[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface.HasConceptsInterface
      :parts: 1
      :private-bases:


   This abstract base class serves as a foundational component for objects that manage a collection of concepts, providing a concrete implementation for storage and access. It initializes with an iterable of concepts and exposes a property that allows for both retrieval and dynamic modification of the underlying list. By handling the conversion of input iterables to a list, it ensures a consistent internal state for subclasses that need to track or represent multiple conceptual entities.

   :param _concepts: Internal storage for the concepts currently represented or manipulated by the class.
   :type _concepts: list[Concept]


   .. py:attribute:: _concepts
      :type:  list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:property:: concepts
      :type: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


      Returns the list of concepts held by this object, i.e. the operands that the implementing concept combines. The value is read from the private ``_concepts`` attribute without modifying the instance.

      :return: The wrapped operand concepts.

      :rtype: list[Concept]