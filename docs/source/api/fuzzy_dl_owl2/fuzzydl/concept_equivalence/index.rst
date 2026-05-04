fuzzy_dl_owl2.fuzzydl.concept_equivalence
=========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept_equivalence



.. ── LLM-GENERATED DESCRIPTION START ──

Encapsulates the logical axiom asserting that two distinct concepts are equivalent within a fuzzy description logic system.


Description
-----------


The implementation serves as a container for a pair of ``Concept`` objects, allowing the definition of relationships where two entities are treated as interchangeable. By storing references to both sides of the equivalence, the structure supports operations that require reasoning about or manipulating the equality of distinct logical entities. The design includes functionality to generate independent copies of the equivalence statement, ensuring that modifications to a cloned instance do not affect the original relationship. Accessor methods are provided to retrieve the specific concepts involved, facilitating the integration of this equivalence axiom into broader logical processing workflows without exposing the internal state directly.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept_equivalence.ConceptEquivalence


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_equivalence_ConceptEquivalence.png
       :alt: UML Class Diagram for ConceptEquivalence
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ConceptEquivalence**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_equivalence_ConceptEquivalence.pdf
       :alt: UML Class Diagram for ConceptEquivalence
       :align: center
       :width: 8.8cm
       :class: uml-diagram

       UML Class Diagram for **ConceptEquivalence**

.. py:class:: ConceptEquivalence(c1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)

   This class encapsulates the axiom of equivalence between two distinct concepts, serving as a structural representation that asserts their equality within a specific context. It functions as a container for a pair of `Concept` objects, allowing users to define and manipulate relationships where two entities are treated as interchangeable. To utilize this class, instantiate it with the two concepts you wish to equate; you can then access these concepts directly or via getter methods, and generate independent copies of the equivalence statement using the clone functionality.

   :param c1: The first concept participating in the equivalence relationship.
   :type c1: Concept
   :param c2: The second concept participating in the equivalence relation.
   :type c2: Concept


   .. py:method:: clone() -> Self

      Creates and returns a new instance of `ConceptEquivalence` that replicates the state of the current object. The new object is constructed using the same `c1` and `c2` attributes found in the original instance. This method performs a shallow copy of the attributes, meaning that if `c1` or `c2` are mutable objects, the clone will reference the same underlying objects as the source. The original instance remains unmodified by this operation.

      :return: A new instance of the class initialized with the same concepts as the current object.

      :rtype: typing.Self



   .. py:method:: get_c1() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the first concept associated with this equivalence instance. This accessor method retrieves the value of the internal attribute `c1`, representing one of the two concepts involved in the equivalence relationship. The operation is read-only and does not modify the state of the object or the returned concept.

      :return: The Concept instance stored in the c1 attribute.

      :rtype: Concept



   .. py:method:: get_c2() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the second concept associated with this equivalence instance. This method acts as an accessor for the `c2` attribute, retrieving the `Concept` object that forms one side of the equivalence relationship. It performs no modifications to the object state and simply returns the stored value.

      :return: The `Concept` object stored in the `c2` attribute.

      :rtype: Concept



   .. py:attribute:: c1
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: c2
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

