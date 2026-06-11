fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface
=======================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract interface extending the basic concept management contract to include support for numerical weights associated with each concept.


Description
-----------


Building upon the foundation of managing generic concepts, this abstract class introduces the capability to associate specific numerical values or magnitudes with those concepts. It enforces a structural pattern where objects must handle a mutable list of floating-point weights, allowing for dynamic updates or the complete removal of weighting information. The design utilizes property decorators to encapsulate the internal storage of these weights, ensuring that any provided iterable is converted into a list or explicitly set to null to represent an unweighted state. By integrating this functionality directly into the inheritance hierarchy, the class facilitates the creation of complex fuzzy logic constructs where concepts contribute to a result with varying degrees of importance.

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

