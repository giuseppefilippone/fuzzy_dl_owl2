fuzzy_dl_owl2.fuzzydl.milp.milp_helper
======================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.milp.milp_helper


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper


Module Contents
---------------

.. py:class:: MILPHelper

   MILP problem manager, storing the problem and calling an external solver.


   .. py:method:: add_cardinality_list(sc: fuzzy_dl_owl2.fuzzydl.concept.sigma_count.SigmaCount) -> None

      SigmaCount(r,C,O,d)^I(w) = d^I(xSigma)

      :param sc: xSigma: Free variable taking the value  \sigma_{i2 \in O} r(i1, i2) \otimes C(i2)
                 i1: Name of an individual, subject of the relation.
                 O: Set of individuals candidates to be the object of the relation.
                 r: Role.
                 C: Concept.
      :type sc: SigmaCount



   .. py:method:: add_contradiction() -> None

      Add a contradiction to make the fuzzy KB unsatisfiable



   .. py:method:: add_crisp_concept(concept_name: str) -> None

      Defines a concept to be crisp.



   .. py:method:: add_crisp_role(role_name: str) -> None

      Defines a role to be crisp.



   .. py:method:: add_equality(var1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, var2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> None

      Add an equality of the form: var1 = var2.



   .. py:method:: add_new_constraint(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, constraint_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> None
                  add_new_constraint(x: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, n: float) -> None
                  add_new_constraint(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, n: float) -> None
                  add_new_constraint(x: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, d: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> None
                  add_new_constraint(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None
                  add_new_constraint(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, constraint_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> None
                  add_new_constraint(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, constraint_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType, n: float) -> None


   .. py:method:: add_string_feature(role: str) -> None

      Adds a string feature.



   .. py:method:: add_string_value(value: str, int_value: int) -> None

      Relates the value of a string feature with an integer value.

      :param value: Value of a string feature.
      :type value: str
      :param int_value: Corresponding integer value.
      :type int_value: int



   .. py:method:: change_variable_names(old_name: str, new_name: str, old_is_created_individual: bool) -> None

      Replaces the name of the variables including an individual name with the name of another individual name.

      :param old_name: Old individual name.
      :type old_name: str
      :param new_name: New individual name.
      :type new_name: str
      :param old_is_created_individual: Indicates whether the old individual is a created individual or not.
      :type old_is_created_individual: bool



   .. py:method:: check_if_replacement_is_needed(v1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, s1: str, v2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, s2: str) -> bool


   .. py:method:: clone() -> Self


   .. py:method:: exists_nominal_variable(i: str) -> bool

      Checks if there exists a variable taking the value of an individual i belonging to the nominal concept {i}.



   .. py:method:: exists_variable(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, b: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role: str) -> bool

      Checks if a variable taking the value of a role assertion exists.

      :param a: Object individual.
      :type a: Individual
      :param b: Subject individual.
      :type b: Individual
      :param role: A role name.
      :type role: str



   .. py:method:: get_name_for_integer(i: int) -> Optional[str]

      Gets the name of the i-th variable.



   .. py:method:: get_negated_nominal_variable(i1: str, i2: str) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Gets a variable taking the value of an individual i1 not belonging to the nominal concept {i2}.

      :param i1: An individual that is subject of the assertion.
      :type i1: str
      :param i2: An individual representing the nominal concept.
      :type i2: str

      :returns: A variable taking the value of the assertion i1: not {i2}.
      :rtype: Variable



   .. py:method:: get_new_variable(v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Gets a new variable with the indicated type.



   .. py:method:: get_nominal_variable(i1: str) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable
                  get_nominal_variable(i1: str, i2: str) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable


   .. py:method:: get_number_for_assertion(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> int

      Gets an integer codification of an assertion.



   .. py:method:: get_ordered_permutation(x: list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]) -> list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]
                  get_ordered_permutation(x: list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable], z: list[list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]]) -> list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]


   .. py:method:: get_variable(var_name: str) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable
                  get_variable(var_name: str, v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable
                  get_variable(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable
                  get_variable(rel: fuzzy_dl_owl2.fuzzydl.relation.Relation) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable
                  get_variable(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, restrict: fuzzy_dl_owl2.fuzzydl.restriction.restriction.Restriction) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable
                  get_variable(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable
                  get_variable(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, concept_name: str) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable
                  get_variable(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, b: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role: str) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable
                  get_variable(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, b: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role: str, v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable
                  get_variable(a: str, b: str, role: str, v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable
                  get_variable(ind: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable
                  get_variable(ind: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType) -> None


   .. py:method:: has_nominal_variable(terms: list[fuzzy_dl_owl2.fuzzydl.milp.term.Term]) -> bool

      Checks if a collection of terms has a nominal variable.



   .. py:method:: has_variable(name: str) -> bool
                  has_variable(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> bool


   .. py:method:: is_crisp_concept(concept_name: str) -> bool

      Checks if a concept is crisp or not.



   .. py:method:: is_crisp_role(role_name: str) -> bool

      Checks if a role is crisp or not.



   .. py:method:: is_nominal_variable(i: str) -> bool

      Checks if a variable 'i' is a nominal variable.



   .. py:method:: optimize(objective: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Optional[fuzzy_dl_owl2.fuzzydl.milp.solution.Solution]

      It optimizes an expression using a solvers from MILPProvider.

      :param objective: Expression to be optimized.
      :type objective: Expression

      :raises ValueError: If MILPProvider is not known.

      :returns: An optimal solution of the expression
      :rtype: typing.Optional[Solution]



   .. py:method:: print_instance_of_labels(f_name: str, ind_name: str, value: float) -> None
                  print_instance_of_labels(name: str, value: float) -> None

      Shows the membership degrees to some linguistic labels.



   .. py:method:: set_binary_variables() -> None

      Transforms every [0,1]-variable into a {0,1} variable.



   .. py:method:: set_nominal_variables(value: bool) -> None


   .. py:method:: solve_gurobi(objective: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Optional[fuzzy_dl_owl2.fuzzydl.milp.solution.Solution]

      Solves a MILP problem using Gurobi.



   .. py:method:: solve_mip(objective: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Optional[fuzzy_dl_owl2.fuzzydl.milp.solution.Solution]


   .. py:method:: solve_pulp(objective: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Optional[fuzzy_dl_owl2.fuzzydl.milp.solution.Solution]


   .. py:attribute:: PARTITION
      :type:  bool
      :value: False



   .. py:attribute:: PRINT_LABELS
      :type:  bool
      :value: True



   .. py:attribute:: PRINT_VARIABLES
      :type:  bool
      :value: True



   .. py:attribute:: cardinalities
      :type:  list[fuzzy_dl_owl2.fuzzydl.concept.sigma_count.SigmaCount]
      :value: []



   .. py:attribute:: constraints
      :type:  list[fuzzy_dl_owl2.fuzzydl.milp.inequation.Inequation]
      :value: []



   .. py:attribute:: crisp_concepts
      :type:  set[str]


   .. py:attribute:: crisp_roles
      :type:  set[str]


   .. py:attribute:: nominal_variables
      :type:  bool
      :value: False



   .. py:attribute:: number_of_variables
      :type:  dict[str, int]


   .. py:attribute:: show_vars
      :type:  fuzzy_dl_owl2.fuzzydl.milp.show_variables_helper.ShowVariablesHelper


   .. py:attribute:: string_features
      :type:  set[str]


   .. py:attribute:: string_values
      :type:  dict[int, str]


   .. py:attribute:: variables
      :type:  list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]
      :value: []



