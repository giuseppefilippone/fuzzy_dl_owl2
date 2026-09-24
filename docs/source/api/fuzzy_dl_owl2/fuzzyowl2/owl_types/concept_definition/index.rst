fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition
====================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition







.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class that anchors the hierarchy of fuzzy concept definitions in the FuzzyOWL2 framework by tagging each definition with a ``ConceptType`` and exposing that tag through a common interface.


Description
-----------


``ConceptDefinition`` is the root abstraction for all fuzzy concept definitions, and it is declared abstract so that it can never be instantiated on its own — every usable definition must come from a concrete subclass modelling a particular kind of fuzzy concept. Its design rests on a simple type-tag pattern: at construction time each definition receives a ``ConceptType`` value recording its category, that value is stored privately and never changed afterwards, and a single accessor exposes it to the rest of the system. This lets other components, such as the ontology serialiser or the fuzzy reasoner, handle arbitrary concept definitions uniformly, querying what kind of concept they are looking at without needing to know its concrete class and dispatching accordingly. The only additional behaviour is a deliberate convenience in which the formal, debugging-oriented string representation simply delegates to the informal one, guaranteeing that both forms of output always agree. The minimalism is intentional — the abstraction exists to impose a shared contract on the hierarchy while leaving every aspect of concept-specific semantics to the subclasses.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_concept_definition_ConceptDefinition.png
       :alt: UML Class Diagram for ConceptDefinition
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ConceptDefinition**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_concept_definition_ConceptDefinition.pdf
       :alt: UML Class Diagram for ConceptDefinition
       :align: center
       :width: 7.6cm
       :class: uml-diagram

       UML Class Diagram for **ConceptDefinition**

.. py:class:: ConceptDefinition(type: fuzzy_dl_owl2.fuzzyowl2.util.constants.ConceptType)

   Bases: :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition
      :parts: 1
      :private-bases:


   This abstract base class serves as the foundational representation for concept definitions within the FuzzyOWL2 framework. It is designed to be subclassed rather than instantiated directly, providing a common interface for various types of fuzzy concept definitions. Upon initialization, a specific `ConceptType` must be provided to categorize the nature of the definition, which can subsequently be retrieved using the `get_type` method.

   :param _type: The specific classification or category of the fuzzy concept definition.
   :type _type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType


   .. py:method:: __repr__() -> str

      Returns the official string representation of the `ConceptDefinition` instance. This method delegates directly to the `__str__` method, ensuring that the output used for debugging and logging is identical to the informal string representation provided by the object.

      :return: The string representation of the object.

      :rtype: str



   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzyowl2.util.constants.ConceptType

      Returns the type classification associated with this concept definition. This method acts as an accessor for the internal `_type` attribute, providing the specific `ConceptType` that categorizes the concept. It does not modify the state of the object.

      :return: The type of the concept.

      :rtype: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType



   .. py:attribute:: _type
      :type:  fuzzy_dl_owl2.fuzzyowl2.util.constants.ConceptType