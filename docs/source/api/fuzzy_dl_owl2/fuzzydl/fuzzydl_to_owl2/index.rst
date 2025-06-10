fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2
=====================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2.FuzzydlToOwl2


Functions
---------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2.main


Module Contents
---------------

.. py:class:: FuzzydlToOwl2(input_file: str, output_file: str, base_iri: str = 'http://www.semanticweb.org/ontologies/fuzzydl_ontology#')

   Convert FuzzyDL to OWL2


   .. py:method:: add_entity_annotation(annotation: str, entity: pyowl2.abstracts.entity.OWLEntity) -> None

      Add annotation to an entity



   .. py:method:: add_ontology_annotation(annotation: str) -> None

      Add annotation to the ontology



   .. py:method:: annotate_gci(gci: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion) -> None

      Annotate a General Concept Inclusion (GCI)



   .. py:method:: annotate_pcd(c1: pyowl2.abstracts.class_expression.OWLClassExpression, pcd: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition) -> None

      Annotate a Primitive Concept Definition (PCD)



   .. py:method:: exist_data_property(role: str) -> bool

      Check if a data property exists



   .. py:method:: exist_object_property(role: str) -> bool

      Check if an object property exists



   .. py:method:: get_annotations_for_axiom(value: Union[float, fuzzy_dl_owl2.fuzzydl.degree.degree_numeric.DegreeNumeric]) -> set[pyowl2.base.annotation.OWLAnnotation]

      Get annotations for an axiom with degree



   .. py:method:: get_base(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> pyowl2.abstracts.class_expression.OWLClassExpression

      Get the base class for a concept



   .. py:method:: get_class(name: str) -> pyowl2.abstracts.class_expression.OWLClassExpression
                  get_class(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> pyowl2.abstracts.class_expression.OWLClassExpression

      Get or create an OWL class



   .. py:method:: get_data_property(role: str) -> Union[pyowl2.expressions.data_property.OWLDataProperty, pyowl2.expressions.object_property.OWLObjectProperty]

      Get or create a data property



   .. py:method:: get_individual(name: str) -> pyowl2.individual.named_individual.OWLNamedIndividual

      Get or create a named individual



   .. py:method:: get_new_atomic_class(name: str) -> pyowl2.abstracts.class_expression.OWLClassExpression

      Get or create a new atomic class



   .. py:method:: get_object_property(role: str) -> Union[pyowl2.expressions.data_property.OWLDataProperty, pyowl2.expressions.object_property.OWLObjectProperty]

      Get or create an object property



   .. py:method:: iri(o: object) -> pyowl2.base.iri.IRI

      Convert object to IRI string



   .. py:method:: run() -> None

      Execute the conversion process



   .. py:method:: to_owl_annotation(annotation: str) -> pyowl2.base.annotation.OWLAnnotation

      Convert a string to an OWL annotation



   .. py:attribute:: concepts
      :type:  dict[str, pyowl2.abstracts.class_expression.OWLClassExpression]


   .. py:attribute:: datatypes
      :type:  dict[str, pyowl2.base.datatype.OWLDatatype]


   .. py:attribute:: fuzzyLabel
      :type:  pyowl2.base.annotation_property.OWLAnnotationProperty


   .. py:attribute:: input_FDL
      :type:  str


   .. py:attribute:: modifiers
      :type:  dict[str, pyowl2.base.datatype.OWLDatatype]


   .. py:attribute:: num_classes
      :type:  int
      :value: 0



   .. py:attribute:: ontology
      :type:  pyowl2.ontology.OWLOntology


   .. py:attribute:: ontology_iri
      :type:  pyowl2.base.iri.IRI


   .. py:attribute:: ontology_path
      :type:  str
      :value: 'http://www.semanticweb.org/ontologies/fuzzydl_ontology#'



   .. py:attribute:: output_FOWL
      :type:  str


.. py:function:: main()

