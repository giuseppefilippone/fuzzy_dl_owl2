fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2
=================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2.FuzzyOwl2


Module Contents
---------------

.. py:class:: FuzzyOwl2(input_file: str, output_file: str, base_iri: str = 'http://www.semanticweb.org/ontologies/fuzzydl_ontology#')

   Bases: :py:obj:`object`


   .. py:method:: get_atomic_concept_name(c: pyowl2.base.owl_class.OWLClass) -> str


   .. py:method:: get_atomic_data_property_name(p: pyowl2.expressions.data_property.OWLDataProperty) -> str


   .. py:method:: get_atomic_object_property_name(p: pyowl2.expressions.object_property.OWLObjectProperty) -> str


   .. py:method:: get_bottom_concept_name() -> str


   .. py:method:: get_bottom_data_property_name() -> str


   .. py:method:: get_bottom_object_property_name() -> str


   .. py:method:: get_class_name(c: pyowl2.abstracts.class_expression.OWLClassExpression) -> str


   .. py:method:: get_data_all_values_from_name(p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, range: pyowl2.abstracts.data_range.OWLDataRange) -> str


   .. py:method:: get_data_exact_cardinality_restriction(cardinality: int, p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, range: pyowl2.abstracts.data_range.OWLDataRange = None) -> str


   .. py:method:: get_data_has_value_name(p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, literal: pyowl2.literal.literal.OWLLiteral) -> str


   .. py:method:: get_data_max_cardinality_restriction(cardinality: int, p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, range: pyowl2.abstracts.data_range.OWLDataRange = None) -> str


   .. py:method:: get_data_min_cardinality_restriction(cardinality: int, p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, range: pyowl2.abstracts.data_range.OWLDataRange = None) -> str


   .. py:method:: get_data_property_name(p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression) -> str


   .. py:method:: get_data_some_values_from_name(p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, range: pyowl2.abstracts.data_range.OWLDataRange) -> str


   .. py:method:: get_individual_name(i: pyowl2.abstracts.individual.OWLIndividual) -> Optional[str]


   .. py:method:: get_object_all_values_from_name(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression) -> str


   .. py:method:: get_object_complement_of_name(c: pyowl2.abstracts.class_expression.OWLClassExpression) -> str


   .. py:method:: get_object_exact_cardinality_restriction(cardinality: int, p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression = None) -> str


   .. py:method:: get_object_has_self_name(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> str


   .. py:method:: get_object_has_value_name(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, i: pyowl2.abstracts.individual.OWLIndividual) -> str


   .. py:method:: get_object_intersection_of_name(operands: set[pyowl2.abstracts.class_expression.OWLClassExpression]) -> str


   .. py:method:: get_object_max_cardinality_restriction(cardinality: int, p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression = None) -> str


   .. py:method:: get_object_min_cardinality_restriction(cardinality: int, p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression = None) -> str


   .. py:method:: get_object_one_of_name(ind_set: set[pyowl2.abstracts.individual.OWLIndividual]) -> str


   .. py:method:: get_object_property_name(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> str


   .. py:method:: get_object_some_values_from_name(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression) -> str


   .. py:method:: get_object_union_of_name(operands: set[pyowl2.abstracts.class_expression.OWLClassExpression]) -> str


   .. py:method:: get_short_name(e: pyowl2.abstracts.entity.OWLEntity) -> str


   .. py:method:: get_top_concept_name() -> str


   .. py:method:: get_top_data_property_name() -> str


   .. py:method:: get_top_object_property_name() -> str


   .. py:method:: process_concept_annotations() -> None


   .. py:method:: process_datatype_annotations() -> None


   .. py:method:: process_ontology_annotations() -> None


   .. py:method:: process_ontology_axioms() -> None


   .. py:method:: process_property_annotations() -> None


   .. py:method:: translate_owl2ontology() -> None


   .. py:method:: write_asymmetric_object_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: write_choquet_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept.ChoquetConcept) -> None


   .. py:method:: write_concept_assertion_axiom(i: pyowl2.abstracts.individual.OWLIndividual, c: pyowl2.abstracts.class_expression.OWLClassExpression, d: float) -> None


   .. py:method:: write_concept_declaration(c: pyowl2.abstracts.class_expression.OWLClassExpression) -> None


   .. py:method:: write_data_property_assertion_axiom(i: pyowl2.abstracts.individual.OWLIndividual, lit: pyowl2.literal.literal.OWLLiteral, p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, d: float) -> None


   .. py:method:: write_data_property_declaration(dp: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression) -> None


   .. py:method:: write_data_property_domain_axiom(p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression) -> None


   .. py:method:: write_data_property_range_axiom(p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, range: pyowl2.abstracts.data_range.OWLDataRange) -> None


   .. py:method:: write_different_individuals_axiom(ind_set: set[pyowl2.abstracts.individual.OWLIndividual]) -> None


   .. py:method:: write_disjoint_classes_axiom(class_set: set[pyowl2.abstracts.class_expression.OWLClassExpression]) -> None


   .. py:method:: write_disjoint_data_properties_axiom(class_set: set[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]) -> None


   .. py:method:: write_disjoint_object_properties_axiom(class_set: set[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]) -> None


   .. py:method:: write_disjoint_union_axiom(class_set: set[pyowl2.abstracts.class_expression.OWLClassExpression]) -> None


   .. py:method:: write_equivalent_classes_axiom(class_set: set[pyowl2.abstracts.class_expression.OWLClassExpression]) -> None


   .. py:method:: write_equivalent_data_properties_axiom(class_set: set[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]) -> None


   .. py:method:: write_equivalent_object_properties_axiom(class_set: set[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]) -> None


   .. py:method:: write_functional_data_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: write_functional_object_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: write_fuzzy_logic(logic: str) -> None


   .. py:method:: write_fuzzy_nominal_concept_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_nominal_concept.FuzzyNominalConcept) -> None


   .. py:method:: write_inverse_functional_object_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: write_inverse_object_property_axiom(p1: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, p2: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: write_irreflexive_object_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: write_left_shoulder_function_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.left_shoulder_function.LeftShoulderFunction) -> None


   .. py:method:: write_linear_function_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function.LinearFunction) -> None


   .. py:method:: write_linear_modifier_definition(name: str, mod: fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier.LinearModifier) -> None


   .. py:method:: write_modified_concept_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_concept.ModifiedConcept) -> None


   .. py:method:: write_modified_function_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_function.ModifiedFunction) -> None


   .. py:method:: write_modified_property_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property.ModifiedProperty) -> None


   .. py:method:: write_negative_data_property_assertion_axiom(i: pyowl2.abstracts.individual.OWLIndividual, lit: pyowl2.literal.literal.OWLLiteral, p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, d: float) -> None


   .. py:method:: write_negative_object_property_assertion_axiom(i1: pyowl2.abstracts.individual.OWLIndividual, i2: pyowl2.abstracts.individual.OWLIndividual, p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, d: float) -> None


   .. py:method:: write_object_property_assertion_axiom(i1: pyowl2.abstracts.individual.OWLIndividual, i2: pyowl2.abstracts.individual.OWLIndividual, p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, d: float) -> None


   .. py:method:: write_object_property_declaration(op: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: write_object_property_domain_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression) -> None


   .. py:method:: write_object_property_range_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression) -> None


   .. py:method:: write_owa_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept.OwaConcept) -> None


   .. py:method:: write_qowa_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.qowa_concept.QowaConcept) -> None


   .. py:method:: write_quasi_sugeno_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept.QsugenoConcept) -> None


   .. py:method:: write_reflexive_object_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: write_right_shoulder_function_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.right_shoulder_function.RightShoulderFunction) -> None


   .. py:method:: write_same_individual_axiom(ind_set: set[pyowl2.abstracts.individual.OWLIndividual]) -> None


   .. py:method:: write_sub_data_property_of_axiom(subproperty: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, superproperty: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, d: float) -> None


   .. py:method:: write_sub_object_property_of_axiom(subproperty: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, superproperty: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, d: float) -> None


   .. py:method:: write_sub_property_chain_of_axiom(chain: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], superproperty: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, d: float) -> None


   .. py:method:: write_subclass_of_axiom(subclass: pyowl2.abstracts.class_expression.OWLClassExpression, superclass: pyowl2.abstracts.class_expression.OWLClassExpression, d: float) -> None


   .. py:method:: write_sugeno_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept.SugenoConcept) -> None


   .. py:method:: write_symmetric_object_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: write_transitive_object_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None


   .. py:method:: write_trapezoidal_function_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.trapezoidal_function.TrapezoidalFunction) -> None


   .. py:method:: write_triangular_function_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_function.TriangularFunction) -> None


   .. py:method:: write_triangular_modifier_definition(name: str, mod: fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_modifer.TriangularModifier) -> None


   .. py:method:: write_weighted_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_concept.WeightedConcept) -> None


   .. py:method:: write_weighted_max_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_max_concept.WeightedMaxConcept) -> None


   .. py:method:: write_weighted_min_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_min_concept.WeightedMinConcept) -> None


   .. py:method:: write_weighted_sum_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_concept.WeightedSumConcept) -> None


   .. py:method:: write_weighted_sum_zero_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_zero_concept.WeightedSumZeroConcept) -> None


   .. py:attribute:: NEG_INFINITY
      :type:  float
      :value: -10000.0



   .. py:attribute:: POS_INFINITY
      :type:  float
      :value: 10000.0



   .. py:attribute:: defined_concepts
      :type:  dict[str, fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition]


   .. py:attribute:: defined_properties
      :type:  dict[str, fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition]


   .. py:attribute:: fuzzy_datatypes
      :type:  dict[str, fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition]


   .. py:attribute:: fuzzy_label
      :type:  pyowl2.base.annotation_property.OWLAnnotationProperty


   .. py:attribute:: fuzzy_modifiers
      :type:  dict[str, fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition]


   .. py:attribute:: ontologies
      :type:  set[pyowl2.ontology.OWLOntology]


   .. py:attribute:: ontology
      :type:  pyowl2.ontology.OWLOntology


   .. py:attribute:: ontology_iri


   .. py:attribute:: ontology_path


   .. py:attribute:: output_dl
      :type:  str


   .. py:attribute:: processed_axioms
      :type:  set[str]


