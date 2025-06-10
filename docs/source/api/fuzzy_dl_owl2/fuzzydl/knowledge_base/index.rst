fuzzy_dl_owl2.fuzzydl.knowledge_base
====================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.knowledge_base


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.knowledge_base.ClassicalSolver
   fuzzy_dl_owl2.fuzzydl.knowledge_base.CreatedIndividualHandler
   fuzzy_dl_owl2.fuzzydl.knowledge_base.DatatypeReasoner
   fuzzy_dl_owl2.fuzzydl.knowledge_base.IndividualHandler
   fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase
   fuzzy_dl_owl2.fuzzydl.knowledge_base.LukasiewiczSolver
   fuzzy_dl_owl2.fuzzydl.knowledge_base.ZadehSolver


Module Contents
---------------

.. py:class:: ClassicalSolver

   Solver for classical logic semantics.


   .. py:method:: solve_all(rel: fuzzy_dl_owl2.fuzzydl.relation.Relation, restrict: fuzzy_dl_owl2.fuzzydl.restriction.restriction.Restriction, kb: KnowledgeBase) -> None
      :staticmethod:


      Solves a universal restriction fuzzy assertion with respect to a reference fuzzy KB.



   .. py:method:: solve_and(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:


      Solves a conjunction fuzzy assertion with respect to a reference fuzzy KB.



   .. py:method:: solve_or(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:


      Solves a disjunction fuzzy assertion with respect to a reference fuzzy KB.



   .. py:method:: solve_some(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:


      Solves a existential restriction fuzzy assertion with respect to a reference fuzzy KB.



.. py:class:: CreatedIndividualHandler

   .. py:method:: get_representative(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType, f_name: str, f: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber, kb: KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual
      :staticmethod:


      Gets b individual p with b representative of b set of individuals.
      Given b fuzzy number F, b representative individual is the set of individuals that are greater or equal (or less or equal) than F.
      The representative individual is related to p via b concrete feature f.

      :param current_individual: The individual we want the representative
      :type current_individual: CreatedIndividual
      :param type: Type of the representative individual (GREATER_EQUAL, LESS_EQUAL)
      :type type: InequalityType
      :param f_name: Name of the feature for which the individual is b filler
      :type f_name: str
      :param f: Fuzzy number
      :type f: TriangularFuzzyNumber
      :param kb: KnowledgeBase
      :type kb: KnowledgeBase

      :returns: A new individual with b representative individual
      :rtype: CreatedIndividual



   .. py:method:: is_blocked(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> bool
      :staticmethod:


      Gets if the individual is blocked with respect to a fuzzy KB.



   .. py:method:: is_directly_anywhere_pairwise_blocked(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> bool
      :staticmethod:


      Test if the individual is anywhere pair-wise directly blocked with respect to a fuzzy KB



   .. py:method:: is_directly_anywhere_simple_blocked(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> bool
      :staticmethod:


      Gets if the individual is directly anywhere simple blocked with respect to a fuzzy KB.
          Case SUBSET or SET blocking.
          It is assumed that the individual and all ancestors are not blocked.



   .. py:method:: is_directly_blocked(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> bool
      :staticmethod:


      Gets if the individual is directly blocked with respect to a fuzzy KB.
      A node v is directly blocked iff none of its ancestors are blocked and there exists an ancestor w such that L(v) = L(w), where L(*) is the set of Concept's labels for a node.
      In this case we say that w directly blocks v.



   .. py:method:: is_directly_pairwise_blocked(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> bool
      :staticmethod:


      Test if the individual is pair-wise directly blocked with respect to a fuzzy KB.



   .. py:method:: is_directly_simple_blocked(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> bool
      :staticmethod:


      Gets if the individual is directly blocked with respect to a fuzzy KB.
          Case SUBSET or SET blocking
          It is assumed that the individual and all ancestors are not blocked



   .. py:method:: is_indirectly_anywhere_pairwise_blocked(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> bool
      :staticmethod:


      Gets if the individual is indirectly anywhere pairwise blocked with respect to a fuzzy KB.



   .. py:method:: is_indirectly_anywhere_simple_blocked(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> bool
      :staticmethod:


      Gets if the individual is indirectly anywhere blocked with respect to a fuzzy KB. Case SUBSET or SET blocking.



   .. py:method:: is_indirectly_blocked(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> bool
      :staticmethod:


      Gets if the individual is indirectly blocked with respect to a fuzzy KB.
      A node v is indirectly blocked iff one of its ancestors are blocked.



   .. py:method:: is_indirectly_pairwise_blocked(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> bool
      :staticmethod:


      Gets if the individual is indirectly blocked with respect to a fuzzy KB.



   .. py:method:: is_indirectly_simple_blocked(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> bool
      :staticmethod:


      Gets if the individual is indirectly blocked with respect to a fuzzy KB.
      Case SUBSET or SET blocking.
      A node v is indirectly blocked iff one of its ancestors are blocked.



   .. py:method:: mark_indirectly_simple_unchecked(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> None
      :staticmethod:


      Marks the subtree of a node as indirectly unblocked



   .. py:method:: match_concept_labels(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, b: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> bool
      :staticmethod:


      Checks if two individuals match concept labels



   .. py:method:: match_set_concept_labels(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, b: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual) -> bool
      :staticmethod:


      Check that two concept labels are equal



   .. py:method:: match_subset_concept_labels(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, b: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual) -> bool
      :staticmethod:


      Check that every concept in the labels of this is also in b



   .. py:method:: matching_individual(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> set[fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual]
      :staticmethod:


      Checks if there is a matching individual to this one



   .. py:method:: unblock(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> None
      :staticmethod:



   .. py:method:: unblock_directly_blocked(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> None
      :staticmethod:


      Unblocks an directly blocked individual.



   .. py:method:: unblock_indirectly_blocked(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> None
      :staticmethod:


      Unblocks an indirectly blocked individual.



   .. py:method:: unblock_pairwise(current_individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase) -> None
      :staticmethod:


      Unblock the individual



   .. py:method:: update_role_successors(name: str, role_name: str, kb: KnowledgeBase) -> None
      :staticmethod:



.. py:class:: DatatypeReasoner

   .. py:method:: apply_at_least_value_rule(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:



   .. py:method:: apply_at_most_value_rule(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:



   .. py:method:: apply_exact_value_rule(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:



   .. py:method:: apply_not_at_least_value_rule(b: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:



   .. py:method:: apply_not_at_most_value_rule(b: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:



   .. py:method:: apply_not_exact_value_rule(b: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:



   .. py:method:: apply_not_rule(b: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase, type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> None
      :staticmethod:



   .. py:method:: apply_rule(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase, type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> None
      :staticmethod:



   .. py:method:: geq_equation(y: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:



   .. py:method:: get_bounds(t: fuzzy_dl_owl2.fuzzydl.concrete_feature.ConcreteFeature) -> Optional[list[float]]
      :staticmethod:



   .. py:method:: get_created_individual_and_variables(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role: str, t: fuzzy_dl_owl2.fuzzydl.concrete_feature.ConcreteFeature, k: list[float], kb: KnowledgeBase) -> list[Any]
      :staticmethod:



   .. py:method:: get_feature(f_name: str, kb: KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.concrete_feature.ConcreteFeature
      :staticmethod:



   .. py:method:: get_xb(b: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, t: fuzzy_dl_owl2.fuzzydl.concrete_feature.ConcreteFeature, kb: KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable
      :staticmethod:



   .. py:method:: rule_feature_function(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, t: fuzzy_dl_owl2.fuzzydl.concrete_feature.ConcreteFeature, fun: fuzzy_dl_owl2.fuzzydl.feature_function.FeatureFunction, kb: KnowledgeBase, x_b: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_is_c: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_f: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, k: list[float], type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> None
      :staticmethod:



   .. py:method:: rule_not_simple_restriction(n: Any, kb: KnowledgeBase, x_b: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_f: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_is_c: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, k: list[float], type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> None
      :staticmethod:



   .. py:method:: rule_not_triangular_fuzzy_number(b: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase, f_name: str, x_b: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_f: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_is_c: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, n: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber, k: list[float], type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> None
      :staticmethod:



   .. py:method:: rule_simple_restriction(n: Any, kb: KnowledgeBase, x_b: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_is_c: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_f: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, k: list[float], type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> None
      :staticmethod:



   .. py:method:: rule_triangular_fuzzy_number(b: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, kb: KnowledgeBase, f_name: str, x_b: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_f: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_is_c: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, n: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber, type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> None
      :staticmethod:



   .. py:method:: write_feature_equation(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, fun: fuzzy_dl_owl2.fuzzydl.feature_function.FeatureFunction, x_b: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_is_c: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_f: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, k: list[float], type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType, kb: KnowledgeBase)
      :staticmethod:



   .. py:method:: write_fuzzy_number_equation(x_f: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_b: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_b_prime: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType, kb: KnowledgeBase)
      :staticmethod:



   .. py:method:: write_not_feature_equation(deg: fuzzy_dl_owl2.fuzzydl.degree.degree_expression.DegreeExpression, x_b: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_f: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_is_c: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, k: list[float], type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType, kb: KnowledgeBase) -> None
      :staticmethod:



   .. py:method:: write_not_fuzzy_number_equation(x_b: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_b_prime: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_b_prime_is_f: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_f: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_is_c: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_is_f: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, k: list[float], type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType, kb: KnowledgeBase) -> None
      :staticmethod:



.. py:class:: IndividualHandler

   .. py:method:: add_not_self_restriction(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role: str, kb: KnowledgeBase) -> None
      :staticmethod:



   .. py:method:: add_relation(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role_name: str, b: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree, kb: KnowledgeBase) -> Optional[fuzzy_dl_owl2.fuzzydl.relation.Relation]
      :staticmethod:


      Adds b relation to the individual.



   .. py:method:: add_restriction(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role_name: str, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree, kb: KnowledgeBase) -> None
                  add_restriction(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role_name: str, ind_name: str, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree, kb: KnowledgeBase) -> None
      :staticmethod:



   .. py:method:: common_part_add_restriction(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role_name: str, restrict: fuzzy_dl_owl2.fuzzydl.restriction.restriction.Restriction, kb: KnowledgeBase) -> None
      :staticmethod:



   .. py:method:: solve_not_self_rule(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role_name: str, kb: KnowledgeBase) -> None
      :staticmethod:


      Apply not self rule.



   .. py:method:: solve_relation_restriction(rel: fuzzy_dl_owl2.fuzzydl.relation.Relation, restrict: fuzzy_dl_owl2.fuzzydl.restriction.restriction.Restriction, kb: KnowledgeBase) -> None
      :staticmethod:


      Apply b universal restriction to b relation of the individual.



   .. py:method:: unblock_simple(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, kb: KnowledgeBase) -> None
      :staticmethod:


      Unblock the individual.
          Case subset/set blocking



.. py:class:: KnowledgeBase

   .. py:method:: add_assertion(new_ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None
                  add_assertion(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, n: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> None
                  add_assertion(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, restrict: fuzzy_dl_owl2.fuzzydl.restriction.restriction.Restriction) -> None

      Adds a fuzzy assertion.



   .. py:method:: add_assertions(list_of_assertions: list[fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion]) -> None

      Adds a list of fuzzy assertions.



   .. py:method:: add_atomic_concepts_disjoint(disjoint_concepts: list[str]) -> None

      Adds some disjoint concept axioms.

      :param disjoint_concepts: A vector of concept names.
      :type disjoint_concepts: list[str]



   .. py:method:: add_axiom_to_A_equiv_C(a: str, conc: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None


   .. py:method:: add_axiom_to_A_is_a_C(a: str, pcd: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition, pcd_dict: dict[str, set[fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition]]) -> None


   .. py:method:: add_axiom_to_C_is_a_A(conc1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, conc2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree, logic_type: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType) -> None

      Adds a GCI (conc2, conc1, degree, type) to add_axiom_to_C_is_a_A.

      :param conc1: Subsumer concept.
      :type conc1: Concept
      :param conc2: Subsumed concept.
      :type conc2: Concept
      :param degree: Lower bound for the degree.
      :type degree: Degree
      :param logic_type: Type of the GCI (semantics according to the implication).
      :type logic_type: LogicOperatorType



   .. py:method:: add_axiom_to_C_is_a_D(conc1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, conc2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree, logic_type: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType) -> None

      Adds a GCI (conc2, conc1, degree, type) to axioms_C_is_a_D.

      :param conc1: Subsumer concept.
      :type conc1: Concept
      :param conc2: Subsumed concept.
      :type conc2: Concept
      :param degree: Lower bound for the degree.
      :type degree: Degree
      :param logic_type: Type of the GCI (semantics according to the implication).
      :type logic_type: LogicOperatorType



   .. py:method:: add_axiom_to_C_is_a_X(conc1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, conc2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree, logic_type: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType, atomic: bool) -> None

      Adds a GCI (conc2, conc1, degree, type) to axioms_C_is_a_A or axioms_C_is_a_D.

      :param conc1: Subsumer concept.
      :type conc1: Concept
      :param conc2: Subsumed concept.
      :type conc2: Concept
      :param degree: Lower bound for the degree.
      :type degree: Degree
      :param logic_type: Type of the GCI (semantics according to the implication).
      :type logic_type: LogicOperatorType
      :param atomic: true for C isA A; false for C isA D
      :type atomic: bool



   .. py:method:: add_axiom_to_do_A_is_a_X(a: str, pcd: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition) -> None


   .. py:method:: add_axiom_to_inc(a: str, pcd: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition) -> None


   .. py:method:: add_axioms_to_tg() -> None


   .. py:method:: add_concept(concept_name: str, conc: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept) -> None

      Adds a fuzzy concept to the array of concepts in the fuzzy KB.



   .. py:method:: add_concepts_disjoint(disjoint_concepts: list[str]) -> None
                  add_concepts_disjoint(c1: str, c2: str) -> None
                  add_concepts_disjoint(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, d: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None

      Adds some disjoint concept axioms.



   .. py:method:: add_created_individual(ind_name: str, ind: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual) -> None

      Adds a created individual to the KB.



   .. py:method:: add_datatype_restriction(restriction_type: fuzzy_dl_owl2.fuzzydl.util.constants.RestrictionType, o: Any, f_name: str) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Adds a datatype restriction of the form (restriction_type, f_name, o).

      :param restriction_type: Type of the datatype restriction.
      :type restriction_type: RestrictionType
      :param o: Value of the datatype restriction.
      :type o: typing.Any
      :param f_name: Concrete feature.
      :type f_name: str

      :returns: A datatype restriction.
      :rtype: Concept



   .. py:method:: add_disjoint_union_concept(disjoint_union_concepts: list[str]) -> None

      Adds a disjoint union concept axiom.

      :param disjoint_union_concepts: A vector of concepts names.
      :type disjoint_union_concepts: list[str]



   .. py:method:: add_equivalence_relation(role: str) -> None

      Adds a fuzzy equivalence relation.



   .. py:method:: add_equivalent_concepts(equiv_concepts: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]) -> None

      Adds some equivalent concept axioms.

      :param equiv_concepts: An array list of vector of equivalent fuzzy concepts.
      :type equiv_concepts: list[Concept]



   .. py:method:: add_equivalent_roles(equiv_roles: list[str]) -> None

      Adds some equivalent funcRole axioms.

      :param equiv_roles: An array list of equivalent fuzzy funcRole names.
      :type equiv_roles: list[str]



   .. py:method:: add_fuzzy_number(f_name: str, f: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber) -> None

      Adds a fuzzy number to the fuzzy KB.



   .. py:method:: add_gci(conc1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, conc2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree, logic_type: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType) -> None

      Adds a General Concept Inclusion (conc2, conc1, degree, type).

      :param conc1: Subsumer concept.
      :type conc1: Concept
      :param conc2: Subsumed concept.
      :type conc2: Concept
      :param degree: Lower bound for the degree.
      :type degree: Degree
      :param logic_type: Type of the GCI (semantics according to the implication).
      :type logic_type: LogicOperatorType



   .. py:method:: add_individual(ind_name: str, ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual) -> None

      Adds a individual to the KB.



   .. py:method:: add_individual_to_concept(concept_id: int, ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual) -> None

      Add the individual a to the individual list of the concept.



   .. py:method:: add_inverse_roles(role: str, inv_role: str) -> None

      Adds an inverse funcRole axiom.



   .. py:method:: add_labels_with_nodes(node: str, ind_name: str) -> None


   .. py:method:: add_modifier(mod_name: str, mod: fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier) -> None

      Adds a fuzzy modifier to the fuzzy KB.



   .. py:method:: add_mutually_disjoint(c1: str, c2: str) -> None


   .. py:method:: add_negated_datatype_restriction(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: add_negated_equations(i: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None

      For some and all concepts, add x_{v:C} = 1 - x_{v:not C}.



   .. py:method:: add_parent_recursively(role_c: str, all_parents: dict[str, float], current_role: str, n1: float) -> None

      Used in the computation of the transitive closure of the Role Inclusion Axioms.



   .. py:method:: add_relation(ind_A: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role: str, ind_B: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> fuzzy_dl_owl2.fuzzydl.relation.Relation

      Adds a fuzzy relation of the form (ind_A, ind_B, role, degree)

      :param ind_A: A subbject individual.
      :type ind_A: Individual
      :param role: An abstract role.
      :type role: str
      :param ind_B: An object individual.
      :type ind_B: Individual
      :param degree: Lower bound for the degree.
      :type degree: Degree

      :returns: Added relation.
      :rtype: Relation



   .. py:method:: add_relation_with_role_parent(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role_c: str, role_p: str, n: float) -> None


   .. py:method:: add_relation_with_role_parent_in_lukasiewicz(r: fuzzy_dl_owl2.fuzzydl.relation.Relation, role_p: str, n: float) -> None


   .. py:method:: add_similarity_relation(role: str) -> None

      Adds a fuzzy similarity relation.



   .. py:method:: add_simple_inverse_roles(role: str, inv_role: str) -> None

      States that two roles are inverse without recursion.



   .. py:method:: add_subsumption(conc2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, conc1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree, logic_type: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType) -> None

      Adds a General Concept Inclusion (conc2, conc1, degree, type) even if the left side is atomic.

      :param conc1: Subsumed concept.
      :type conc1: Concept
      :param conc2: Subsumer concept.
      :type conc2: Concept
      :param degree: Lower bound for the degree.
      :type degree: Degree
      :param logic_type: Type of the GCI (semantics according to the implication).
      :type logic_type: LogicOperatorType



   .. py:method:: add_tdef_links(g: networkx.DiGraph, A_t_C: dict[str, int], use_tdr: bool) -> bool

      We return true if we know that htere are cycles because of t_synonyms.
      False does not mean that there are no cycles!



   .. py:method:: add_tdr_links(g: networkx.DiGraph, A_t_C: dict[str, int], used_roles: set[str], v: int) -> bool

      We return true if we know that there are cycles because of t_synonyms.
      False does not mean that there are no cycles!



   .. py:method:: add_tinc_links(g: networkx.DiGraph, A_t_C: dict[str, int], use_tdr: bool) -> bool

      We return true if we know that there are cycles because of t_synonyms.
      False does not mean that there are no cycles!



   .. py:method:: add_tmp_feature(feature: str) -> None

      Add a feature from the DL parser.



   .. py:method:: check_fuzzy_number_concept_exists(conc_name: str) -> bool

      Checks if there exists a fuzzy number with the indicated name.



   .. py:method:: check_individual_exists(ind_name: str) -> bool

      Checks if there exists an individual with the given name.



   .. py:method:: check_role(role_name: str, conc: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None

      Checks the disjointness between abstract and concrete roles.

      :param role_name: A role name.
      :type role_name: str
      :param conc: A concept appearing in a restrictions involving the role.
      :type conc: Concept



   .. py:method:: check_trans_role_applied(rel: fuzzy_dl_owl2.fuzzydl.relation.Relation, restrict: fuzzy_dl_owl2.fuzzydl.restriction.restriction.Restriction) -> bool

      Checks if transitivity has been applied to a universal restriction.

      :param rel: A relation.
      :type rel: Relation
      :param restrict: A restriction.
      :type restrict: Restriction

      :returns: true if the transitivity rule has been applied; false otherwise.
      :rtype: bool



   .. py:method:: classify() -> None


   .. py:method:: clone() -> Self

      Gets a copy of a knowledge base.



   .. py:method:: clone_without_abox() -> Self

      Gets a copy of a knowledge base except the ABox.



   .. py:method:: compute_blocking_type() -> None

      Computes the type of the blocking in {NO_BLOCKING, SUBSET_BLOCKING, SET_BLOCKING, (ANYWHERE) DOUBLE_BLOCKING}.
      If the type is in {SUBSET_BLOCKING, SET_BLOCKING, (ANYWHERE) DOUBLE_BLOCKING}, it also computes whether it is dynamic or not.



   .. py:method:: compute_language() -> None

      Computes the language of the fuzzy KB, from ALC to SHIF(D).



   .. py:method:: compute_variables_old_calculus(fcc: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept) -> None


   .. py:method:: concept_absorption(pcd: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition, atomic: bool) -> bool
                  concept_absorption(tau: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion, atomic: bool) -> bool


   .. py:method:: concept_exists(name: str) -> bool

      Checks if there exists a concept with the given name.



   .. py:method:: convert_strings_into_integers() -> None

      Transforms string datatype restrictions into integer datatype restrictions.



   .. py:method:: create_roles_with_all_parents() -> None

      Computes transitive closure of the Role Inclusion Axioms.



   .. py:method:: create_roles_with_trans_children() -> None

      Used in the computation of the transitive closure of the Role Inclusion Axioms.



   .. py:method:: define_atomic_concept(concept_name: str, conc: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, implication: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType, n: float) -> None

      Adds an atomic fuzzy concept definition.



   .. py:method:: define_boolean_concrete_feature(fun_role: str) -> None

      Define a concrete feature with range boolean.

      :param fun_role: Name of the concrete feature.
      :type fun_role: str



   .. py:method:: define_concept(concept_name: str, conc: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None

      Adds a fuzzy concept definition.



   .. py:method:: define_concreate_feature(role: str) -> None


   .. py:method:: define_equivalent_concepts(c1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None

      Adds a concept equivalence axiom.



   .. py:method:: define_integer_concrete_feature(fun_role: str, d1: int, d2: int) -> None

      Define a concrete feature with range integers in [d1, d2].

      :param fun_role: Name of the concrete feature.
      :type fun_role: str
      :param d1: Lower bound of the range.
      :type d1: int
      :param d2: Upper bound of the range.
      :type d2: int



   .. py:method:: define_real_concrete_feature(fun_role: str, d1: float, d2: float) -> None

      Define a concrete feature with range real numbers in [d1, d2].

      :param fun_role: Name of the concrete feature.
      :type fun_role: str
      :param d1: Lower bound of the range.
      :type d1: int
      :param d2: Upper bound of the range.
      :type d2: int



   .. py:method:: define_string_concrete_feature(fun_role: str) -> None

      Define a concrete feature with range string.

      :param fun_role: Name of the concrete feature.
      :type fun_role: str



   .. py:method:: define_synonym(concept_name_1: str, concept_name_2: str) -> None

      Adds a fuzzy synonym definition.



   .. py:method:: define_synonyms(concept_name_1: str, concept_name_2: str) -> None

      Adds a fuzzy synonym definition.



   .. py:method:: definition_absorption(gci: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion) -> bool

      :param gci: A GCI.
      :type gci: GeneralConceptInclusion

      :returns: true if there are changes; false otherwise.
      :rtype: bool



   .. py:method:: definition_absorption_to_do(pcd: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition) -> bool

      :param pcd: A primitive concept definition.
      :type pcd: PrimitiveConceptDefinition

      :returns: true if there are changes; false otherwise.
      :rtype: bool



   .. py:method:: degree_if_not_one(deg: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> str
                  degree_if_not_one(d: float) -> str

      Return a string representation of the degree if it is different to 1.0.



   .. py:method:: disjoint_with_defined_concept(a: str) -> bool

      Computes if there is some disjoint(a, b) in tDis with b being a head of an axiom in Tdef



   .. py:method:: exists_primite_concept_definition(pcds: set[fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition], pcd: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition) -> bool


   .. py:method:: exit_condition() -> None

      Add every GCI to tG using the form *top* isA (C -> D).



   .. py:method:: exit_condition_A_is_a_X(pcd: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition) -> None


   .. py:method:: exit_condition_C_is_a_X(gci: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion) -> None


   .. py:method:: form_inv_role_inc_axioms() -> None

      Computes relations for the inverse roles and Role Inclusion Axioms (R => P, n) implies (inv(R) => inv(P), n)



   .. py:method:: form_inv_role_relations() -> None

      Computes relations for the inverse roles



   .. py:method:: form_inv_trans_roles() -> None

      Computes relations for the inverse roles and transitive roles.



   .. py:method:: gci_transform_define_atomic_concept(concept_name: str, conc: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, implication: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType, n: float)


   .. py:method:: gci_transformation(tau: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion, atomic: bool) -> bool
                  gci_transformation(pcd: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition) -> bool


   .. py:method:: gci_transformation_add_axiom_to_C_is_a_X(conc1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, conc2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree, logic_type: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType) -> None


   .. py:method:: gci_transformations_A_is_a_C() -> None


   .. py:method:: gci_transformations_C_is_a_A() -> None


   .. py:method:: gci_transformations_C_is_a_D() -> None


   .. py:method:: get_A_t_C() -> dict[str, int]


   .. py:method:: get_classification_node() -> Optional[fuzzy_dl_owl2.fuzzydl.classification_node.ClassificationNode]


   .. py:method:: get_concept(name: str) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Gets a concept with indicated name.



   .. py:method:: get_concept_from_number(n: int) -> Optional[str]

      Gets the concept name encoded by a number.



   .. py:method:: get_correct_version_of_individual(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None
                  get_correct_version_of_individual(rel: fuzzy_dl_owl2.fuzzydl.relation.Relation) -> None

      Use right version of the individual (needed when we clone the KB or merge individuals)



   .. py:method:: get_inclusion_degree(subsumed: str, subsumer: str) -> float

      Computes the inclusion degree between two roles.

      :param subsumed: Subsumed funcRole.
      :type subsumed: str
      :param subsumer: Subsumer funcRole.
      :type subsumer: str

      :returns: Inclusion degree of subsumed in subsumer.
      :rtype: float



   .. py:method:: get_individual(ind_name: str) -> Union[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual]

      Gets an individual with the indicated name (creating it if necessary).



   .. py:method:: get_individuals() -> dict[str, fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]

      Gets all individuals of the KB.



   .. py:method:: get_inverses_of_inverse_role(role: str) -> Optional[set[str]]

      Gets the set of inverse roles of some inverse of a given role.



   .. py:method:: get_language() -> str

      Gets the language of the fuzzy KB, from ALC to SHIF(D).



   .. py:method:: get_logic() -> fuzzy_dl_owl2.fuzzydl.util.constants.FuzzyLogic

      Gets the fuzzy logic of the fuzzy knowledge base.



   .. py:method:: get_named_individuals() -> list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]


   .. py:method:: get_new_atomic_concept() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: get_new_concrete_individual(parent: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, f_name: str) -> fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual


   .. py:method:: get_new_individual() -> fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual
                  get_new_individual(parent: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, f_name: str) -> fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual


   .. py:method:: get_new_individual_common_code(parent: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, f_name: str) -> fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual


   .. py:method:: get_number_from_concept(concept_name: str) -> int

      Gets a number to encode a concept name.



   .. py:method:: get_number_of_domain_restrictions() -> int


   .. py:method:: get_number_of_range_restrictions() -> int


   .. py:method:: get_subsumption_flags(b: fuzzy_dl_owl2.fuzzydl.classification_node.ClassificationNode) -> float

      Retrieves the value subFlags(a, b)



   .. py:method:: get_tmp_feature(feature: str) -> str

      Gets a feature from the DL parser.



   .. py:method:: get_truth_constants(s: str) -> Optional[float]

      Gets a truth constant from the DL parser.



   .. py:method:: goedel_implies(conc1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, conc2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> None

      Adds a Goedel General Concept Inclusion.

      :param conc1: Subsumed concept.
      :type conc1: Concept
      :param conc2: Subsumer concept.
      :type conc2: Concept
      :param degree: Lower bound for the degree.
      :type degree: Degree



   .. py:method:: has_functional_abstract_roles() -> bool


   .. py:method:: has_nominals_in_abox() -> bool

      Checks if the ABox contains the b-some constructor.

      :returns: true if the ABox contains the b-some constructor; false otherwise.
      :rtype: bool



   .. py:method:: has_nominals_in_tbox() -> bool

      Checks if the TBox contains the b-some constructor.

      :returns: true if the TBox contains the b-some constructor; false otherwise.
      :rtype: bool



   .. py:method:: has_only_crisp_sub_concepts(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool

      Checks if a concept c is only composed of crisp concepts or not.



   .. py:method:: implies(conc1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, conc2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> None

      Adds a General Concept Inclusion (conc1, conc2, degree).

      :param conc1: Subsumed concept.
      :type conc1: Concept
      :param conc2: Subsumer concept.
      :type conc2: Concept
      :param degree: Lower bound for the degree.
      :type degree: Degree



   .. py:method:: is_assertion_processed(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None

      Checks if an assertion has already been processed.



   .. py:method:: is_atomic_crisp_concept(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool

      Checks if a concept is atomic and crisp.



   .. py:method:: is_classified() -> bool

      Checks if the knowledge base has already been classified.



   .. py:method:: is_concrete_type(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool

      Computes if the type is one of the concretes (concrete, fuzzy number, or their complements)



   .. py:method:: is_crisp_concept(concept_name: str) -> bool

      Checks if a concept is crisp.

      :param concept_name: Name of the concept.
      :type concept_name: str

      :returns: true if the semantics is classical logic or if the concept is crisp, false otherwise.
      :rtype: bool



   .. py:method:: is_crisp_role(role_name: str) -> bool

      Checks if a role is crisp.

      :param role_name: Name of the role.
      :type role_name: str

      :returns: true if the semantics is classical logic or if the role is crisp, false otherwise.
      :rtype: bool



   .. py:method:: is_lazy_unfoldable() -> bool

      Checks if the fuzzy KB is already lazy unfoldable.



   .. py:method:: is_loaded() -> bool

      Checks if the fuzzy KB is loaded.



   .. py:method:: is_redundant_A_is_a_C(concept_name: str, conc: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, implication: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType, n: float) -> bool


   .. py:method:: is_redundant_gci(C: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, D: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, implication: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType, n: float) -> bool

      Checks if C => D redundant.

      :param C: Subsumed concept.
      :type C: Concept
      :param D: Subsumer concept.
      :type D: Concept
      :param implication: A fuzzy implication.
      :type implication: LogicOperatorType
      :param n: Degree of truth.
      :type n: float

      :raises InconsistentOntologyException: If C is *top* concept and D is *bottom* concept.



   .. py:method:: is_tbox_acyclic() -> bool

      Check if t_inclusions \cup t_definitions is acyclic



   .. py:method:: kleene_dienes_implies(conc1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, conc2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> None

      Adds a Kleene-Dienes General Concept Inclusion.

      :param conc1: Subsumed concept.
      :type conc1: Concept
      :param conc2: Subsumer concept.
      :type conc2: Concept
      :param degree: Lower bound for the degree.
      :type degree: Degree



   .. py:method:: lukasiewicz_implies(conc1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, conc2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> None

      Adds a Lukasiewicz General Concept Inclusion.

      :param conc1: Subsumed concept.
      :type conc1: Concept
      :param conc2: Subsumer concept.
      :type conc2: Concept
      :param degree: Lower bound for the degree.
      :type degree: Degree



   .. py:method:: mark_process_assertion(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None

      Marks assertion as processed.



   .. py:method:: merge(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, b: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual) -> None

      Merges two individuals.

      :param a: An individual. As an effect, it will contain a merged individual.
      :type a: Individual
      :param b: Another individual.
      :type b: Individual



   .. py:method:: merge_fillers(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, func_role: str) -> None

      If individual ind has two or more fillers via the functional role funcRole, they are merged into just one filler concept.

      :param ind: Subject individual.
      :type ind: Individual
      :param func_role: A functional role.
      :type func_role: str



   .. py:method:: nominal_absorption(conc1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, conc2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> bool


   .. py:method:: optimize(e: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      It optimizes an expression.

      :param e: Expression to be optimized.
      :type e: Expression

      :returns: An optimal solution of the expression.
      :rtype: Solution



   .. py:method:: partition_loop_A_is_a_B() -> None


   .. py:method:: partition_loop_A_is_a_C() -> None


   .. py:method:: partition_loop_C_is_a_A() -> None


   .. py:method:: partition_loop_C_is_a_D() -> None


   .. py:method:: partition_loop_to_do_A_is_a_B() -> None


   .. py:method:: partition_loop_to_do_A_is_a_C() -> None


   .. py:method:: preprocess_tbox() -> None

      Computes if the fuzzy KB has an acyclic TBox.
      If not, add primitive and concept definitions as GCIs.



   .. py:method:: print_tbox() -> None


   .. py:method:: read_object_from_file(file_path: str) -> KnowledgeBase


   .. py:method:: remove_A_is_a_B(key: str, pcd: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition) -> None


   .. py:method:: remove_A_is_a_C(key: str, pcd: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition) -> None


   .. py:method:: remove_A_is_a_X(key: str, pcd: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition, pcd_dict: dict[str, set[fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition]]) -> None
                  remove_A_is_a_X(key: str, pcd: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition, atomic: bool) -> None


   .. py:method:: remove_C_is_a_A(key: str, gci: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion) -> None


   .. py:method:: remove_C_is_a_D(key: str, gci: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion) -> None


   .. py:method:: remove_C_is_a_X(key: str, gci: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion, atomic: bool) -> None


   .. py:method:: represent_tbox_with_gcis() -> None


   .. py:method:: restrict_range(x_b: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, k1: float, k2: float) -> None
                  restrict_range(x_b: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_f: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, k1: float, k2: float) -> None

      Restricts the range of a variable to [k1, k2].



   .. py:method:: role_absorption(tau: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition) -> bool
                  role_absorption(tau: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion, atomic: bool) -> bool


   .. py:method:: role_domain(role: str, conc: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None

      Adds a domain funcRole axiom.



   .. py:method:: role_implies(subsumed: str, subsumer: str) -> None
                  role_implies(subsumed: str, subsumer: str, n: float) -> None

      Adds a Role Inclusion Axiom (subsumed, subsumer, degree).



   .. py:method:: role_is_functional(role: str) -> None

      Adds a functional funcRole axiom.



   .. py:method:: role_is_inverse_functional(role: str) -> None

      Adds an inverse functional funcRole axiom.



   .. py:method:: role_is_reflexive(role: str) -> None

      Adds a reflexive funcRole axiom.



   .. py:method:: role_is_symmetric(role: str) -> None

      Adds a symmetric funcRole axiom.



   .. py:method:: role_is_transitive(role: str) -> None

      Adds a transitive funcRole axiom.



   .. py:method:: role_range(role: str, conc: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None

      Adds a funcRole range axiom.



   .. py:method:: role_subsumes(subsumer: str, subsumed: str, n: float) -> None

      Adds a Role Inclusion Axiom (subsumer, subsumed, degree).

      :param subsumer: Subsumer funcRole.
      :type subsumer: str
      :param subsumed: Subsumed funcRole.
      :type subsumed: str
      :param n: Lower bound for the degree.
      :type n: float



   .. py:method:: role_subsumes_bool(subsumer: str, subsumed: str, n: float) -> bool
                  role_subsumes_bool(subsumer: str, subsumed: str, n: float, p_list: dict[str, dict[str, float]]) -> bool

      Adds a Role Inclusion Axiom (subsumer, subsumed, degree).



   .. py:method:: rule_all(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_and(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_ass_nom(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, v: str) -> None

      Applies the rule AssNom to a node v and an assertion <a : C>.

      :param a: Individual of an assertion.
      :type a: Individual
      :param c: Concept of an assertion.
      :type c: Concept
      :param v: Node that is an a-node.
      :type v: str



   .. py:method:: rule_atomic(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_bottom(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_choquet(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented(i: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None


   .. py:method:: rule_complemented_at_least_datatype_restriction(b: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_at_most_datatype_restriction(b: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_atomic(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_choquet(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_complex_assertion(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_concrete(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_exact_datatype_restriction(b: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_extended_negative_threshold(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_extended_positive_threshold(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_fuzzy_number(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_goedel_implication(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_has_value(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_lazy_unfolding(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_modified(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_negative_threshold(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_owa(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_positive_threshold(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_quantified_owa(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_quasi_sugeno(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_self(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_sigma_concept(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_sugeno(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_weighted_concept(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_weighted_max(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_weighted_min(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_weighted_sum(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_weighted_sum_zero(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_complemented_zadeh_implication(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_concrete(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_domain_lazy_unfolding(domain_role: str, rel: fuzzy_dl_owl2.fuzzydl.relation.Relation) -> None


   .. py:method:: rule_extended_negative_threshold(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_extended_positive_threshold(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_fuzzy_number(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_goedel_and(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_goedel_implication(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_goedel_or(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_has_value(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_lazy_unfolding(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_loose_lower_approximation(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_loose_upper_approximation(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_lower_approximation(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_lukasiewicz_and(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_lukasiewicz_or(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_modified(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_n2() -> None


   .. py:method:: rule_n3() -> None


   .. py:method:: rule_negative_threshold(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_or(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_owa(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_positive_threshold(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_quantified_owa(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_quasi_sugeno(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_range_lazy_unfolding(range_role: str, rel: fuzzy_dl_owl2.fuzzydl.relation.Relation) -> None


   .. py:method:: rule_self(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_sigma_concept(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_some(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_sugeno(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_threshold_common(x_a_in_c: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x_a_in_tc: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, y: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> None


   .. py:method:: rule_tight_lower_approximation(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_tight_upper_approximation(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_top(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_upper_approximation(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_weighted_concept(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_weighted_max(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_weighted_min(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_weighted_sum(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_weighted_sum_zero(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: rule_zadeh_implication(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None


   .. py:method:: save_absorbed_tbox_to_file(output: Callable) -> None


   .. py:method:: save_tbox_common_part_to_file(output: Callable) -> None


   .. py:method:: save_tbox_to_file(output: Callable) -> None


   .. py:method:: save_to_file(file_name: str) -> None

      Saves a fuzzy KB into a text file.



   .. py:method:: set_crisp_concept(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None

      Defines a concept to be crisp.



   .. py:method:: set_crisp_role(role_name: str) -> None

      Defines a role to be crisp.



   .. py:method:: set_dynamic_blocking() -> None

      Sets dynamic blocking unless the current blocking is pairwise blocking.



   .. py:method:: set_logic(logic: fuzzy_dl_owl2.fuzzydl.util.constants.FuzzyLogic) -> None

      Sets the fuzzy logic of the fuzzy knowledge base.



   .. py:method:: set_truth_constants(s: str, w: float) -> None

      Sets a truth constant from the DL parser.



   .. py:method:: set_unsatisfiable_KB() -> None


   .. py:method:: show_statistics() -> None


   .. py:method:: solve_abox() -> None

      Solves all the fuzzy assertions.



   .. py:method:: solve_assertions() -> None

      Solves all the fuzzy assertions.



   .. py:method:: solve_cardinality_list() -> None

      Solve the list of sigma-count pending tasks



   .. py:method:: solve_choquet_integral_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, c: fuzzy_dl_owl2.fuzzydl.concept.choquet_integral.ChoquetIntegral) -> None

      Solves an assertion of the form (individual, concept) with respect to a fuzzy KB.



   .. py:method:: solve_choquet_integral_complemented_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, c: fuzzy_dl_owl2.fuzzydl.concept.operator_concept.OperatorConcept) -> None

      Solves an assertion of the form (individual, not concept) with respect to a fuzzy KB.



   .. py:method:: solve_concept_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None


   .. py:method:: solve_concept_complemented_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, lower_limit: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None


   .. py:method:: solve_concrete_value_assertions() -> None

      Solves the datatypes restrictions.



   .. py:method:: solve_crisp_concrete_concept_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, concept: fuzzy_dl_owl2.fuzzydl.concept.concrete.crisp_concrete_concept.CrispConcreteConcept) -> None

      This function define the equations for the individual belonging to the crisp set.

      :param ind: current individual
      :type ind: Individual
      :param Variables:
                        - x     => variable associated with the individual
                        - x'    => generic variable associated with an individual belonging to this crisp concept
      :param Draw the four lines:
                                  - (b, 1) -- (k_2, 0) -> y_2 <= (x - k_2) / (k_2 - b)
                                  - (a, 1) -- (k_2, 0) -> y_1 <= (x - k_2) / (k_2 - a)
                                  - (b, 1) -- (k_1, 0) -> y_3 >= (x - k_1) / (k_1 - b)
                                  - (a, 1) -- (k_1, 0) -> y_2 >= (x - k_1) / (k_1 - a)
      :param Along with the following constraints:
                                                   - y_1 + y_2 + y_3 = 1
                                                   - x' + y_1 + y_3 <= 1
                                                   - x' - y_2 >= 0



   .. py:method:: solve_domain_and_range_axioms() -> None

      Solves all the domain and range restrictions.



   .. py:method:: solve_functional_roles() -> None

      Solves the functional role axioms.



   .. py:method:: solve_fuzzy_concrete_concept_complement_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, lower_limit: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree, curr_concept: fuzzy_dl_owl2.fuzzydl.concept.operator_concept.OperatorConcept) -> None

      Solves an assertion of the form (individual, complement of the concept, degree) with respect to a fuzzy KB.



   .. py:method:: solve_gci(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, gci: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion) -> None
                  solve_gci(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual) -> None

      Solves a GCI for a given individual.



   .. py:method:: solve_goedel_gci(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, gci: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion) -> None


   .. py:method:: solve_inverse_roles() -> None

      Solves the inverse funcRole axioms.



   .. py:method:: solve_kb() -> None

      Prepares the fuzzy knowledge base to reason with it.



   .. py:method:: solve_kleene_dienes_gci(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, gci: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion) -> None


   .. py:method:: solve_left_concrete_concept_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, concept: fuzzy_dl_owl2.fuzzydl.concept.concrete.left_concrete_concept.LeftConcreteConcept) -> None


   .. py:method:: solve_linear_concrete_concept_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, concept: fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept.LinearConcreteConcept) -> None


   .. py:method:: solve_linear_modifier_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, con: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, modifier: fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier.LinearModifier) -> None


   .. py:method:: solve_lukasiewicz_gci(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, gci: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion) -> None


   .. py:method:: solve_modifier_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, modifier: fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier) -> None

      Solves an assertion of the form (individual, concept, lower degree) with respect to a fuzzy KB.



   .. py:method:: solve_modifier_complemented_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, concept: fuzzy_dl_owl2.fuzzydl.concept.operator_concept.OperatorConcept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> None

      Solves an assertion of the form (individual, negated concept, lower degree) with respect to a fuzzy KB.



   .. py:method:: solve_one_exist_assertion() -> None

      Solves one existential assertion.



   .. py:method:: solve_owa_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, c: Union[fuzzy_dl_owl2.fuzzydl.concept.owa_concept.OwaConcept, fuzzy_dl_owl2.fuzzydl.concept.qowa_concept.QowaConcept]) -> None

      Solves an assertion of the form (individual, concept) with respect to a fuzzy KB.



   .. py:method:: solve_owa_complemented_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, curr_concept: fuzzy_dl_owl2.fuzzydl.concept.operator_concept.OperatorConcept) -> None

      Solves an assertion of the form (individual, not concept) with respect to a fuzzy KB.



   .. py:method:: solve_reflexive_role(role: str) -> None

      Solves a reflexive funcRole axiom.



   .. py:method:: solve_reflexive_roles(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual) -> None
                  solve_reflexive_roles() -> None

      Solves a reflexive funcRole axiom.



   .. py:method:: solve_right_concrete_concept_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, concept: fuzzy_dl_owl2.fuzzydl.concept.concrete.right_concrete_concept.RightConcreteConcept) -> None


   .. py:method:: solve_role_inclusion_axioms() -> None
                  solve_role_inclusion_axioms(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, r: fuzzy_dl_owl2.fuzzydl.relation.Relation) -> None

      Solves the fuzzy funcRole inclusion axioms.



   .. py:method:: solve_sugeno_integral_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, concept: Union[fuzzy_dl_owl2.fuzzydl.concept.sugeno_integral.SugenoIntegral, fuzzy_dl_owl2.fuzzydl.concept.quasi_sugeno_integral.QsugenoIntegral]) -> None

      Solves an assertion of the form (individual, concept) with respect to a fuzzy KB.



   .. py:method:: solve_sugeno_integral_complemented_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, curr_concept: fuzzy_dl_owl2.fuzzydl.concept.operator_concept.OperatorConcept) -> None

      Solves an assertion of the form (individual, not concept) with respect to a fuzzy KB.



   .. py:method:: solve_trapezoidal_concrete_concept_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, concept: fuzzy_dl_owl2.fuzzydl.concept.concrete.trapezoidal_concrete_concept.TrapezoidalConcreteConcept) -> None


   .. py:method:: solve_triangular_concrete_concept_assertion(individual: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, concept: fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept.TriangularConcreteConcept) -> None


   .. py:method:: solve_triangular_modifier_assertion(individual: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, modifier: fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier.TriangularModifier) -> None


   .. py:method:: solve_w_max_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, concept: fuzzy_dl_owl2.fuzzydl.concept.weighted_max_concept.WeightedMaxConcept) -> None

      Solves an assertion of the form (individual, concept) with respect to a fuzzy KB.



   .. py:method:: solve_w_max_complemented_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, curr_concept: fuzzy_dl_owl2.fuzzydl.concept.operator_concept.OperatorConcept) -> None

      Solves an assertion of the form (individual, not concept) with respect to a fuzzy KB.



   .. py:method:: solve_w_min_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, concept: fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept.WeightedMinConcept) -> None

      Solves an assertion of the form (individual, concept) with respect to a fuzzy KB.



   .. py:method:: solve_w_min_complemented_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, curr_concept: fuzzy_dl_owl2.fuzzydl.concept.operator_concept.OperatorConcept) -> None

      Solves an assertion of the form (individual, not concept) with respect to a fuzzy KB.



   .. py:method:: solve_w_sum_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, concept: fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_concept.WeightedSumConcept) -> None

      Solves an assertion of the form (individual, concept) with respect to a fuzzy KB.



   .. py:method:: solve_w_sum_complemented_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, curr_concept: fuzzy_dl_owl2.fuzzydl.concept.operator_concept.OperatorConcept) -> None

      Solves an assertion of the form (individual, not concept) with respect to a fuzzy KB.



   .. py:method:: solve_w_sum_zero_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, concept: fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_zero_concept.WeightedSumZeroConcept) -> None

      Solves an assertion of the form (individual, concept) with respect to a fuzzy KB.



   .. py:method:: solve_w_sum_zero_complemented_assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, curr_concept: fuzzy_dl_owl2.fuzzydl.concept.operator_concept.OperatorConcept) -> None

      Solves an assertion of the form (individual, not concept) with respect to a fuzzy KB.



   .. py:method:: solve_zadeh_gci(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, gci: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion) -> None


   .. py:method:: synonym_absorption_A_is_a_B(pcd1: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition) -> bool

      Absorbs synonyms in axioms_A_is_a_B.

      :returns: true if there are changes; false otherwise.
      :rtype: bool



   .. py:method:: synonym_absorption_to_do_A_is_a_B(pcd1: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition) -> bool

      Absorbs synonyms in axioms_to_do_A_is_a_B. note that A => B is in t_inclusions.

      :returns: true if there are changes; false otherwise.
      :rtype: bool



   .. py:method:: unblock_children(ancestor: str) -> None

      Unblocks the children of the individual with the given name.

      :param ancestor: Name of the ancestor individual.
      :type ancestor: str



   .. py:method:: unblock_individual(node_name: str) -> None

      Unblocks the individual and descendants of the individual with the given name.
      :param node_name: Name of the ancestor individual.
      :type node_name: str



   .. py:method:: write_object_to_file(file_path: str) -> None


   .. py:method:: zadeh_implies(conc1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, conc2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None

      Adds a Zadeh General Concept Inclusion.

      :param conc1: Subsumed concept.
      :type conc1: Concept
      :param conc2: Subsumer concept.
      :type conc2: Concept



   .. py:attribute:: ABOX_EXPANDED
      :type:  bool
      :value: False



   .. py:attribute:: CLASSIFIED
      :type:  bool
      :value: False



   .. py:attribute:: KB_LOADED
      :type:  bool
      :value: False



   .. py:attribute:: KB_UNSAT
      :type:  bool
      :value: False



   .. py:attribute:: abstract_roles
      :type:  set[str]


   .. py:attribute:: acyclic_tbox
      :type:  bool
      :value: False



   .. py:attribute:: applied_trans_role_rules
      :type:  list[str]
      :value: []



   .. py:attribute:: assertions
      :type:  list[fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion]
      :value: []



   .. py:attribute:: atomic_concepts
      :type:  dict[str, fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:attribute:: axioms_A_equiv_C
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]]


   .. py:attribute:: axioms_A_is_a_B
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition]]


   .. py:attribute:: axioms_A_is_a_C
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition]]


   .. py:attribute:: axioms_C_equiv_D
      :type:  list[fuzzy_dl_owl2.fuzzydl.concept_equivalence.ConceptEquivalence]
      :value: []



   .. py:attribute:: axioms_C_is_a_A
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion]]


   .. py:attribute:: axioms_C_is_a_D
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion]]


   .. py:attribute:: axioms_to_do_A_is_a_B
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition]]


   .. py:attribute:: axioms_to_do_A_is_a_C
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition]]


   .. py:attribute:: axioms_to_do_C_is_a_A
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion]]


   .. py:attribute:: axioms_to_do_C_is_a_D
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion]]


   .. py:attribute:: axioms_to_do_tmp_A_is_a_C
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition]]


   .. py:attribute:: axioms_to_do_tmp_C_is_a_A
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion]]


   .. py:attribute:: axioms_to_do_tmp_C_is_a_D
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion]]


   .. py:attribute:: blocked_assertions
      :type:  dict[str, list[fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion]]


   .. py:attribute:: blocked_exist_assertions
      :type:  dict[str, list[fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion]]


   .. py:attribute:: blocking_dynamic
      :type:  bool
      :value: False



   .. py:attribute:: blocking_type
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.BlockingDynamicType


   .. py:attribute:: concept_individual_list
      :type:  dict[int, sortedcontainers.SortedSet[fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual]]


   .. py:attribute:: concrete_concepts
      :type:  dict[str, fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept]


   .. py:attribute:: concrete_features
      :type:  dict[str, fuzzy_dl_owl2.fuzzydl.concrete_feature.ConcreteFeature]


   .. py:attribute:: concrete_fuzzy_concepts
      :type:  bool
      :value: False



   .. py:attribute:: concrete_roles
      :type:  set[str]


   .. py:attribute:: directly_blocked_children
      :type:  dict[str, list[str]]


   .. py:attribute:: disjoint_variables
      :type:  dict[str, set[str]]


   .. py:attribute:: domain_restrictions
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]]


   .. py:attribute:: exist_assertions
      :type:  list[fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion]
      :value: []



   .. py:attribute:: functional_roles
      :type:  set[str]


   .. py:attribute:: fuzzy_numbers
      :type:  dict[str, fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber]


   .. py:attribute:: individuals
      :type:  dict[str, fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]


   .. py:attribute:: inverse_functional_roles
      :type:  set[str]


   .. py:attribute:: inverse_roles
      :type:  dict[str, set[str]]


   .. py:attribute:: labels_with_nodes
      :type:  dict[str, set[str]]


   .. py:attribute:: language
      :type:  str
      :value: ''



   .. py:attribute:: lazy_unfondable
      :type:  bool
      :value: False



   .. py:attribute:: max_depth
      :type:  int
      :value: 1



   .. py:attribute:: milp
      :type:  fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper


   .. py:attribute:: modifiers
      :type:  dict[str, fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier]


   .. py:attribute:: nodes_classification
      :type:  list[fuzzy_dl_owl2.fuzzydl.classification_node.ClassificationNode]
      :value: []



   .. py:attribute:: num_assertions
      :type:  int
      :value: 0



   .. py:attribute:: num_defined_concepts
      :type:  int
      :value: 0



   .. py:attribute:: num_defined_individuals
      :type:  int
      :value: 0



   .. py:attribute:: num_relations
      :type:  int
      :value: 0



   .. py:attribute:: number_of_concepts
      :type:  dict[str, int]


   .. py:attribute:: number_of_roles
      :type:  dict[str, int]


   .. py:attribute:: old_01_variables
      :type:  int
      :value: 0



   .. py:attribute:: old_binary_variables
      :type:  int
      :value: 0



   .. py:attribute:: order
      :type:  dict[str, int]


   .. py:attribute:: positive_concrete_value_assertions
      :type:  list[fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion]
      :value: []



   .. py:attribute:: processed_assertions
      :type:  set[int]


   .. py:attribute:: r_successors
      :type:  dict[str, list[str]]


   .. py:attribute:: range_restrictions
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]]


   .. py:attribute:: reflexive_roles
      :type:  set[str]


   .. py:attribute:: roles_with_all_parents
      :type:  dict[str, dict[str, float]]


   .. py:attribute:: roles_with_parents
      :type:  dict[str, dict[str, float]]


   .. py:attribute:: roles_with_trans_children
      :type:  dict[str, list[str]]


   .. py:attribute:: rule_acyclic_tbox
      :type:  bool
      :value: False



   .. py:attribute:: rules_applied
      :type:  dict[fuzzy_dl_owl2.fuzzydl.util.constants.KnowledgeBaseRules, int]


   .. py:attribute:: show_language
      :type:  bool
      :value: False



   .. py:attribute:: similarity_relations
      :type:  set[str]


   .. py:attribute:: subsumption_flags
      :type:  dict[str, dict[str, float]]


   .. py:attribute:: symmetric_roles
      :type:  set[str]


   .. py:attribute:: t_G
      :type:  list[fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion]
      :value: []



   .. py:attribute:: t_definitions
      :type:  dict[str, fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:attribute:: t_disjoints
      :type:  dict[str, set[str]]


   .. py:attribute:: t_inclusions
      :type:  dict[str, set[fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition]]


   .. py:attribute:: t_synonyms
      :type:  dict[str, set[str]]


   .. py:attribute:: temp_relations_list
      :type:  dict[str, list[fuzzy_dl_owl2.fuzzydl.relation.Relation]]


   .. py:attribute:: temp_string_concept_list
      :type:  list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]
      :value: []



   .. py:attribute:: temp_string_list
      :type:  list[str]
      :value: []



   .. py:attribute:: tmp_features
      :type:  list[str]
      :value: []



   .. py:attribute:: transitive_roles
      :type:  set[str]


   .. py:attribute:: truth_constants
      :type:  dict[str, float]


   .. py:attribute:: x_prime_individuals
      :type:  dict[str, list[str]]


   .. py:attribute:: y_prime_individuals
      :type:  dict[str, list[str]]


.. py:class:: LukasiewiczSolver

   .. py:method:: and_(n1: float, n2: float) -> float
      :staticmethod:


      Gets the value n1 and n2, according to Lukasiewicz t-norm



   .. py:method:: and_equation(x: list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable], z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
                  and_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: float, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
                  and_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:



   .. py:method:: and_geq_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
                  and_geq_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: float, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:



   .. py:method:: and_leq_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:


      Compute z <= x1 AND x2



   .. py:method:: or_equation(x: list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable], z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:


      Compute z = x1 OR x2 OR ... OR xN



   .. py:method:: solve_all(rel: fuzzy_dl_owl2.fuzzydl.relation.Relation, restrict: fuzzy_dl_owl2.fuzzydl.restriction.restriction.Restriction, kb: KnowledgeBase) -> None
      :staticmethod:


      Solves a universal restriction fuzzy assertion with respect to a reference fuzzy KB.



   .. py:method:: solve_and(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:


      Solves a conjunction fuzzy assertion with respect to a reference fuzzy KB.



   .. py:method:: solve_or(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:


      Solves a disjunction fuzzy assertion with respect to a reference fuzzy KB.



   .. py:method:: solve_some(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:


      Solves a existential restriction fuzzy assertion with respect to a reference fuzzy KB.



.. py:class:: ZadehSolver

   Solver for Zadeh fuzzy logic semantics.


   .. py:method:: and_(n1: float, n2: float) -> float
      :staticmethod:


      Gets the value n1 and n2, according to Goedel t-norm



   .. py:method:: and_equation(x: list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable], z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
                  and_equation(x: list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable], t: fuzzy_dl_owl2.fuzzydl.milp.term.Term, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
                  and_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: float, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
                  and_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
                  and_equation(x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:



   .. py:method:: and_geq_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
                  and_geq_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: float, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:



   .. py:method:: and_leq_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:


      Compute z <= x1 AND x2



   .. py:method:: and_negated_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: float, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:


      Compute z = (1 - x1) AND x2



   .. py:method:: goedel_implies_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:


      Compute z = x1 G-implies x2



   .. py:method:: goedel_not_equation(y: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:


      Compute y = NOT z



   .. py:method:: kleene_dienes_implies_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:


      Compute z <= x1 KD-implies x2



   .. py:method:: or_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
                  or_equation(x: list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable], z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:



   .. py:method:: or_negated_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: float, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:


      Compute z = (1 - x1) OR x2



   .. py:method:: solve_all(rel: fuzzy_dl_owl2.fuzzydl.relation.Relation, restrict: fuzzy_dl_owl2.fuzzydl.restriction.restriction.Restriction, kb: KnowledgeBase) -> None
      :staticmethod:


      Solves a universal restriction fuzzy assertion with respect to a reference fuzzy KB.



   .. py:method:: solve_and(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:


      Solves a conjunction fuzzy assertion with respect to a reference fuzzy KB.



   .. py:method:: solve_or(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:


      Solves a disjunction fuzzy assertion with respect to a reference fuzzy KB.



   .. py:method:: solve_some(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, kb: KnowledgeBase) -> None
      :staticmethod:


      Solves a existential restriction fuzzy assertion with respect to a reference fuzzy KB.



   .. py:method:: zadeh_implies_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
                  zadeh_implies_equation(z: float, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:



   .. py:method:: zadeh_implies_leq_equation(z: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, x2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> None
      :staticmethod:


      Compute z <= x1 Z-implies x2, where x1 is binary



