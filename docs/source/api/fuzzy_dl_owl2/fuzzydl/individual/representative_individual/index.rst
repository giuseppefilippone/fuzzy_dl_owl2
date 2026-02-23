fuzzy_dl_owl2.fuzzydl.individual.representative_individual
==========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.individual.representative_individual



.. ── LLM-GENERATED DESCRIPTION START ──

A proxy class representing a collection of individuals satisfying a fuzzy condition based on a specific feature and threshold.


Description
-----------


The software models a concrete proxy for a collection of entities that satisfy a specific fuzzy condition relative to a defined threshold. By encapsulating a ``TriangularFuzzyNumber`` applied to a particular feature, it determines membership through a comparison type, thereby modeling the relationship between a specific individual and the abstract group it represents. This structure enables the handling of uncertainty and partial truths within a fuzzy logic framework by associating a concrete ``CreatedIndividual`` with a fuzzy constraint. Accessor methods are provided to retrieve the classification type, the feature name, the fuzzy value, and the referenced individual, allowing the system to evaluate degrees of satisfaction during feature evaluation.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.individual.representative_individual.RepresentativeIndividual


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_individual_representative_individual_RepresentativeIndividual.png
       :alt: UML Class Diagram for RepresentativeIndividual
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **RepresentativeIndividual**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_individual_representative_individual_RepresentativeIndividual.pdf
       :alt: UML Class Diagram for RepresentativeIndividual
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **RepresentativeIndividual**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:class:: RepresentativeIndividual(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.RepresentativeIndividualType, f_name: str, f: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber, ind: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual)

   This class serves as a concrete proxy for a collection of individuals that satisfy a specific fuzzy condition relative to a threshold. It encapsulates the logic required to define a set of entities based on a `TriangularFuzzyNumber` applied to a specific feature, determining membership through a comparison type (such as greater than or less than). By associating a specific `CreatedIndividual` with this fuzzy constraint, the object models the relationship between an individual and the abstract group it represents or belongs to. This structure is primarily used to represent degrees of satisfaction within a fuzzy logic framework, enabling the system to handle uncertainty and partial truths in feature evaluation.

   :param f_name: The name of the feature for which this individual acts as a filler.
   :type f_name: str
   :param type: The classification of the representative individual, defining the specific criteria or nature of the set it represents.
   :type type: RepresentativeIndividualType
   :param f: Fuzzy number representing the degree of satisfaction of the concept by the individual.
   :type f: TriangularFuzzyNumber
   :param ind: The concrete individual entity referenced by this representative instance.
   :type ind: CreatedIndividual


   .. py:method:: get_feature_name() -> str

      Retrieves the name of the feature represented by this instance. This method serves as a simple getter for the internal `f_name` attribute, returning its current value. It performs no computation or modification of the object's state.

      :return: The name of the feature.

      :rtype: str



   .. py:method:: get_fuzzy_number() -> fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber

      Retrieves the triangular fuzzy number associated with this representative individual. This method serves as a direct accessor for the internal attribute representing the individual's value, returning the specific `TriangularFuzzyNumber` instance stored within the object. Because it returns a reference to the internal object rather than a copy, any modifications made to the returned fuzzy number will directly alter the state of this individual. If the internal attribute has not been initialized prior to calling this method, an `AttributeError` will be raised.

      :return: The TriangularFuzzyNumber instance stored in the object.

      :rtype: TriangularFuzzyNumber



   .. py:method:: get_individual() -> fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual

      Retrieves the `CreatedIndividual` instance currently associated with this `RepresentativeIndividual`. This method serves as an accessor for the internal `ind` attribute, returning the stored object directly. Since it returns a reference to the internal state, any modifications made to the returned object will be reflected in the `RepresentativeIndividual` instance.

      :return: The CreatedIndividual instance associated with this object.

      :rtype: CreatedIndividual



   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzydl.util.constants.RepresentativeIndividualType

      Returns the classification type associated with this representative individual instance. This method serves as a getter for the internal `type` attribute, providing access to the specific `RepresentativeIndividualType` that defines the individual's category. The operation is read-only and does not modify the state of the object.

      :return: The type of the representative individual.

      :rtype: RepresentativeIndividualType



   .. py:attribute:: f
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber


   .. py:attribute:: f_name
      :type:  str


   .. py:attribute:: ind
      :type:  fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual


   .. py:attribute:: type
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.RepresentativeIndividualType

