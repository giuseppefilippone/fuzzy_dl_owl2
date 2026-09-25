fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface
=======================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract interface that augments basic concept management with an optional collection of numerical weights, enabling objects to represent weighted aggregations of concepts in a fuzzy description-logic setting.


Description
-----------


``HasWeightedConceptsInterface`` builds on the simpler concept-holding contract because several fuzzy-DL constructs — such as weighted sums or other weighted aggregations — need not only a set of concepts but also a magnitude expressing each concept's relative significance. The constructor delegates the concepts themselves to the parent class and then materialises whatever weight iterable it receives into a plain list, a deliberate choice that protects against one-shot iterators such as generators being consumed prematurely; passing ``None`` leaves the object in an explicitly unweighted state rather than defaulting to an empty list, so callers can distinguish "no weighting applied" from "all weights are zero". A property pair exposes the weights: the getter returns the stored list (or ``None`` when unset), while the setter replaces any existing values wholesale, again accepting either an iterable or ``None`` to clear them. Because the class is declared abstract and introduces no new abstract methods of its own, it functions purely as a reusable contract: concrete subclasses — typically fuzzy concept aggregations — inherit both concept storage and weight handling, guaranteeing a uniform API across everything that carries weighted concepts.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface.HasWeightedConceptsInterface


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_interface_has_weighted_concepts_interface_HasWeightedConceptsInterface.png
       :alt: UML Class Diagram for HasWeightedConceptsInterface
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **HasWeightedConceptsInterface**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_interface_has_weighted_concepts_interface_HasWeightedConceptsInterface.pdf
       :alt: UML Class Diagram for HasWeightedConceptsInterface
       :align: center
       :width: 19.0cm
       :class: uml-diagram

       UML Class Diagram for **HasWeightedConceptsInterface**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:class:: HasWeightedConceptsInterface(weights: Optional[Iterable[float]], concepts: Iterable[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface.HasConceptsInterface`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface.HasWeightedConceptsInterface
      :parts: 1
      :private-bases:


   This abstract base class defines a contract for objects that manage a collection of concepts alongside associated numerical weights, extending the functionality of the basic concept interface. It provides properties to retrieve and update the list of weights, ensuring that these values are stored as mutable lists of floats or explicitly set to null to indicate the absence of weighting. By handling the initialization and modification of these weights, the class enables dynamic representation of concepts where each element carries a specific magnitude or significance.

   :param _weights: Internal list of weights associated with the current concepts, or None if no weights are assigned.
   :type _weights: typing.Optional[list[float]]


   .. py:attribute:: _weights
      :type:  Optional[list[float]]


   .. py:property:: weights
      :type: Optional[list[float]]


      Returns the per-concept weights applied in the weighted aggregation, or ``None`` when no weights are set. The value is read from the private ``_weights`` attribute without modifying the instance.

      :return: The list of weights, or ``None`` if unset.

      :rtype: typing.Optional[list[float]]

