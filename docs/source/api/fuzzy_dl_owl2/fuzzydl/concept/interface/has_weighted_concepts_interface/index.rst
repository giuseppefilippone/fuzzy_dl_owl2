fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface
=======================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract interface that extends concept management to include associated numerical weights.


Description
-----------


Building upon the foundation of managing collections of concepts, this abstract base class introduces the capability to associate numerical weights with those concepts. It enforces a contract where implementing classes must handle a list of floating-point values that correspond to the managed concepts, allowing for dynamic representation of magnitude or significance. The design ensures that weights are stored internally as mutable lists or explicitly set to null, providing flexibility for scenarios where weighting is optional or conditional. By offering properties to retrieve and modify these values, the interface facilitates the seamless integration of weighted logic into complex fuzzy description logic structures.

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


      Sets the weights for the instance, replacing any existing values. The method accepts an optional iterable of floats; if a value is provided, it is converted to a list and assigned to the internal storage. Passing None explicitly sets the internal weights to None, effectively clearing them.

      :param value: An iterable of floating-point values representing the weights. If None, the weights are reset.
      :type value: typing.Optional[typing.Iterable[float]]

