fuzzy_dl_owl2.fuzzydl.milp.milp_helper
======================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.milp.milp_helper



.. ── LLM-GENERATED DESCRIPTION START ──

A comprehensive manager for Mixed-Integer Linear Programming problems that translates fuzzy logic constructs into mathematical optimization models and interfaces with various solver backends.


Description
-----------


The software functions as a bridge between high-level fuzzy logic definitions—such as concepts, roles, and individuals—and the concrete mathematical formulations required by MILP solvers. It manages the entire lifecycle of decision variables, ensuring they are created with appropriate types and bounds based on the logical context, while simultaneously collecting linear constraints that define the feasible region of the problem. By abstracting the specifics of underlying solver libraries, the system allows users to construct optimization problems generically and then dispatch them to various backends, including Gurobi, Python-MIP, and PuLP, depending on the configuration. Advanced capabilities include specialized handling for crisp concepts and roles, nominal variables, and string features, as well as a partitioning strategy that decomposes the constraint graph into smaller sub-problems to improve solver performance on complex models.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_milp_milp_helper_MILPHelper.png
       :alt: UML Class Diagram for MILPHelper
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **MILPHelper**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_milp_milp_helper_MILPHelper.pdf
       :alt: UML Class Diagram for MILPHelper
       :align: center
       :width: 10.5cm
       :class: uml-diagram

       UML Class Diagram for **MILPHelper**

.. py:class:: MILPHelper

   This class serves as a comprehensive manager for Mixed-Integer Linear Programming (MILP) problems, functioning as an interface that translates high-level logical constructs—such as fuzzy concepts, roles, and individuals—into mathematical optimization models. It allows users to construct problems by retrieving or creating variables associated with specific domain entities, adding linear constraints or inequalities, and defining objective functions. The `optimize` method orchestrates the solving process by delegating to various external solver backends, including Gurobi, MIP, and PuLP, while also offering an optional partitioning strategy to handle complex problem structures. Beyond standard MILP operations, it provides specialized handling for "crisp" concepts and roles (enforcing binary variables), nominal variables, and string features, along with utilities to clone the problem state or output variable values and linguistic label memberships for analysis.

   :param PARTITION: Flag to enable a partitioning strategy that decomposes the MILP problem into smaller sub-problems based on variable connectivity.
   :type PARTITION: bool
   :param PRINT_LABELS: Determines whether to display the membership degrees of variables to linguistic labels.
   :type PRINT_LABELS: bool
   :param PRINT_VARIABLES: Controls whether the values of the variables are printed to the debug output.
   :type PRINT_VARIABLES: bool
   :param nominal_variables: Controls whether variables representing nominal concepts (e.g., `a:{a}`) are retained in the MILP problem. If False, these variables and their associated constraints are removed prior to optimization.
   :type nominal_variables: bool
   :param cardinalities: SigmaCount objects representing the cardinality constraints in the MILP problem.
   :type cardinalities: list[SigmaCount]
   :param constraints: A list of `Inequation` objects representing the linear constraints defining the feasible region of the MILP problem.
   :type constraints: list[Inequation]
   :param crisp_concepts: A set of concept names that are restricted to binary values (0 or 1), ensuring that any variables representing these concepts in the MILP problem are defined as binary variables.
   :type crisp_concepts: set[str]
   :param crisp_roles: A set of role names that are restricted to binary values (0 or 1), ensuring their corresponding variables in the MILP problem are binary.
   :type crisp_roles: set[str]
   :param number_of_variables: Maps variable names to their integer indices, ensuring uniqueness and enabling efficient variable lookup.
   :type number_of_variables: dict[str, int]
   :param show_vars: Helper instance that tracks variables designated for output and manages their association with linguistic labels for displaying membership degrees.
   :type show_vars: ShowVariablesHelper
   :param string_features: Stores the names of features that take string values, identifying variables in the MILP problem that require special handling distinct from numeric variables.
   :type string_features: set[str]
   :param string_values: Maps integer encodings to their corresponding string values, used to handle string features within the MILP problem.
   :type string_values: dict[int, str]
   :param variables: Stores the decision variables for the MILP problem in creation order, serving as the primary source for model construction and result mapping.
   :type variables: list[Variable]

   :raises ValueError: Raised if the configured MILP provider is unsupported or if methods are called with invalid arguments.


   .. py:method:: __add_new_constraint_1(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, constraint_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> None

      Constructs and appends a new inequality constraint to the internal collection of constraints, assuming the right-hand side is zero. The method accepts a mathematical expression and an inequality type (such as equality, greater than, or less than) to define the relationship between the expression and zero. This operation directly modifies the state of the MILP helper by adding the resulting `Inequation` object to the `constraints` list.

      :param expr: The left-hand side expression of the inequality.
      :type expr: Expression
      :param constraint_type: Specifies the relational operator for the inequality, such as equality, greater than, or less than.
      :type constraint_type: InequalityType



   .. py:method:: __add_new_constraint_2(x: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, n: float) -> None

      Adds a linear inequality constraint to the model that enforces the variable `x` to be greater than or equal to the numeric value `n`. This method constructs a linear expression representing the variable and delegates to the main constraint addition routine using a greater-than inequality type. As a side effect, the internal state of the optimization model is modified to include this new restriction, which may alter the feasible region of the problem.

      :param x: The variable to be constrained in the inequality.
      :type x: Variable
      :param n: The numeric value representing the lower bound.
      :type n: float



   .. py:method:: __add_new_constraint_3(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, n: float) -> None

      This method enforces a lower bound on the decision variable associated with a given fuzzy assertion by adding a new inequality constraint to the model. It retrieves the variable corresponding to the assertion and ensures that its value is greater than or equal to the specified numeric threshold. As a side effect, this modifies the internal state of the optimization problem by introducing a new constraint, but it does not return any value.

      :param ass: A fuzzy assertion representing the condition a:C >= L.
      :type ass: Assertion
      :param n: The lower bound value for the inequality constraint.
      :type n: float



   .. py:method:: __add_new_constraint_4(x: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, d: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> None

      Adds a linear inequality constraint to the optimization model requiring the specified variable to be greater than or equal to the given degree. This helper method constructs a linear expression representing the variable and delegates to the core constraint addition logic, effectively enforcing a lower bound on the variable within the problem formulation. The operation modifies the internal state of the model by appending this new constraint to the set of defined conditions, assuming that the provided variable and degree are valid types compatible with the underlying solver.

      :param x: The variable on the left-hand side of the inequality.
      :type x: Variable
      :param d: The lower bound for the variable in the inequality.
      :type d: Degree



   .. py:method:: __add_new_constraint_5(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None

      Adds a new inequality constraint to the model based on a provided fuzzy assertion. The method extracts the variable associated with the assertion and its lower limit degree. It specifically handles the edge case where the degree is a variable; if the assertion variable and the degree variable are identical, the method returns without adding a constraint to avoid redundancy. If the variables are distinct or the degree is a constant, the method delegates to the standard constraint addition routine to enforce the inequality.

      :param ass: The fuzzy assertion representing the inequality to be added, from which the variable and lower limit are extracted.
      :type ass: Assertion



   .. py:method:: __add_new_constraint_6(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, constraint_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> None

      Constructs and appends a new inequality constraint to the internal list of constraints maintained by the helper. The constraint is defined by a relationship between a provided expression and a degree value, where the specific inequality type (equality, greater than, or less than) is determined by the `constraint_type` argument. The actual construction of the inequality object is delegated to the `degree` argument via its `create_inequality_with_degree_rhs` method, resulting in a direct modification of the object's state.

      :param expr: The expression representing the left-hand side of the inequality.
      :type expr: Expression
      :param constraint_type: Specifies the relational operator for the inequality (e.g., EQ, GR, or LE).
      :type constraint_type: InequalityType
      :param degree: The degree object representing the right-hand side of the inequality.
      :type degree: Degree



   .. py:method:: __add_new_constraint_7(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, constraint_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType, n: float) -> None

      This private method constructs and registers a new inequality constraint where the right-hand side is a scalar value. It accepts a linear expression, a constraint type (such as equality, greater than, or less than), and a floating-point number, converting the number into a `DegreeNumeric` object to match the solver's internal representation. The method then delegates the actual addition of the constraint to the main `add_new_constraint` routine, effectively updating the model's constraints to enforce the specified relationship.

      :param expr: The expression on the left-hand side of the inequality.
      :type expr: Expression
      :param constraint_type: Specifies the relational operator for the inequality, such as equality, greater than, or less than.
      :type constraint_type: InequalityType
      :param n: A real number representing the right-hand side of the inequality.
      :type n: float



   .. py:method:: __bfs(graph: networkx.Graph, solution: dict[int, int]) -> int

      Identifies connected components within the graph using a Breadth-First Search (BFS) approach and assigns partition identifiers to nodes. The method initializes the provided solution dictionary, mapping all nodes to a default partition of 0, and then iterates through the nodes to find unvisited starting points. For each unvisited node, it invokes the `__compute_partition` helper method to traverse the graph and assign the current partition ID to all reachable nodes. The `solution` dictionary is modified in place to reflect these assignments, and the method returns the total count of partitions found.

      :param graph: The graph structure to be traversed and partitioned.
      :type graph: nx.Graph
      :param solution: Dictionary mapping node indices to their assigned partition IDs, modified in place to store the result.
      :type solution: dict[int, int]

      :return: The total number of partitions identified in the graph.

      :rtype: int



   .. py:method:: __common_partition_part(objective: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> tuple[list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable], dict[int, int], int, list[int], int, int]

      Performs a graph-based partitioning of the variables involved in the provided objective expression to analyze their distribution across the problem structure. It utilizes a breadth-first search (BFS) algorithm on the internal graph to group variables into partitions, then maps the specific variables from the objective to these partitions. The method returns a tuple containing the list of objective variables, the mapping of variable indices to partition IDs, the total number of partitions, a breakdown of variable counts per partition, and statistics identifying partitions that contain multiple objective variables. This operation relies on the internal graph and variable list, logs the execution time for debugging, and assumes that all variables found in the objective are present within the graph structure.

      :param objective: The objective function expression used to extract variables for partition analysis.
      :type objective: Expression

      :return: A tuple containing the list of objective variables, a mapping of variable indices to partition IDs, the total number of partitions, a list of variable counts per partition, the number of partitions containing multiple variables, and the total count of variables within those partitions.

      :rtype: tuple[list[Variable], dict[int, int], int, list[int], int, int]



   .. py:method:: __compute_partition(queue: list[int], solution: dict[int, int], p: int, graph: networkx.Graph) -> None

      Propagates a partition identifier through a graph starting from the nodes provided in the queue. The method iteratively processes nodes, assigning the specified partition ID `p` to all adjacent neighbors that have not yet been assigned a value in the solution dictionary. This traversal continues until the queue is exhausted, effectively marking a connected region of the graph. The `solution` dictionary is modified in-place to reflect these assignments, and the input `queue` is consumed during the operation.

      :param queue: List of node identifiers to be processed, used to traverse the graph and assign the partition ID to connected neighbors.
      :type queue: list[int]
      :param solution: Dictionary mapping node IDs to partition assignments, where a value of 0 indicates an unassigned node. Updated in place to assign the partition ID `p` to reachable nodes.
      :type solution: dict[int, int]
      :param p: The partition identifier or label to assign to nodes.
      :type p: int
      :param graph: The graph structure defining the connectivity between nodes, used to identify neighbors during the partition traversal.
      :type graph: nx.Graph



   .. py:method:: __get_graph() -> networkx.Graph

      Constructs a NetworkX graph representing the relationships between variables based on the defined constraints. Nodes are added for each variable in the internal list, indexed by their order. Edges are created by iterating through the constraints; for each constraint containing multiple terms, the method connects the first variable to every subsequent variable in that constraint, effectively creating a star topology for each constraint. Each edge is labeled with a unique sequential number. The method returns the newly created graph without modifying the state of the MILP helper instance, and it skips constraints that contain no terms.

      :return: A NetworkX graph where nodes represent variables and edges connect variables that appear together in a constraint. Each edge is assigned a unique sequential number.

      :rtype: nx.Graph



   .. py:method:: __get_nominal_variable_1(i1: str) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves the decision variable representing the assertion that a specific individual belongs to its corresponding nominal concept. This method serves as a convenience wrapper that calls the general `get_nominal_variable` method, passing the same identifier for both the individual and the concept parameters. The resulting variable is used within the MILP formulation to encode the membership of the individual in the singleton set defined by itself.

      :param i1: The identifier of the individual representing the nominal concept.
      :type i1: str

      :return: A variable representing the assertion that the individual `i1` belongs to the nominal concept `{i1}`.

      :rtype: Variable



   .. py:method:: __get_nominal_variable_2(i1: str, i2: str) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves or creates a binary decision variable representing the assertion that a specific individual belongs to a nominal concept. The method generates a unique variable name by combining the individual identifier and the nominal concept identifier, formatted as 'i1:{ i2 }'. It ensures the returned variable is configured as a binary type, delegating the actual variable lookup or instantiation to the underlying `get_variable` helper method.

      :param i1: The individual acting as the subject of the assertion.
      :type i1: str
      :param i2: An individual representing the nominal concept that the subject individual is asserted to belong to.
      :type i2: str

      :return: A binary Variable representing the assertion that individual i1 belongs to the nominal concept i2.

      :rtype: Variable



   .. py:method:: __get_ordered_permutation_1(x: list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]) -> list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]

      Constructs an ordered permutation of the input variables by introducing an $n   imes n$ matrix of auxiliary binary decision variables to model the sorting constraints. This method generates the necessary binary variables to represent the permutation mapping and delegates the actual constraint formulation and variable ordering to the `get_ordered_permutation` method. As a side effect of this operation, new binary variables are added to the underlying model.

      :param x: The list of variables to be permuted.
      :type x: list[Variable]

      :return: A list of variables representing the ordered permutation of the input list.

      :rtype: list[Variable]



   .. py:method:: __get_ordered_permutation_2(x: list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable], z: list[list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]]) -> list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]

      Constructs a set of new variables representing the input variables sorted in non-increasing order. The method creates `n` semi-continuous variables `y` and adds constraints to enforce the sequence `y[0] >= y[1] >= ... >= y[n-1]`. It utilizes the provided matrix `z` to establish a system of linear constraints that ensures `y` is a permutation of the input list `x`, specifically by linking the values of `x` and `y` through `z` and enforcing that the sum of each row and column in `z` equals `n-1`. This process modifies the underlying model by adding these constraints and introducing the new variables.

      :param x: The list of variables to be sorted into a non-increasing order.
      :type x: list[Variable]
      :param z: A matrix of auxiliary variables used to formulate the constraints linking the input variables to the sorted output.
      :type z: list[list[Variable]]

      :return: A list of new variables representing the input variables sorted in non-increasing order.

      :rtype: list[Variable]



   .. py:method:: __get_variable_1(var_name: str) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves a variable instance corresponding to the specified name, creating it if necessary. If a variable with the provided name already exists in the internal registry, the existing object is returned. Otherwise, a new variable of type `SEMI_CONTINUOUS` is instantiated, appended to the internal list of variables, and registered in the variable count dictionary. This method modifies the internal state of the helper whenever a new variable is generated.

      :param var_name: Name of the variable to retrieve or create.
      :type var_name: str

      :return: The variable instance associated with the given name. If the variable does not exist, a new semi-continuous variable bounded in [0, 1] is created and returned.

      :rtype: Variable



   .. py:method:: __get_variable_10(a: str, b: str, role: str, v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves or creates a decision variable representing a specific relationship between two entities, identified by the strings `a` and `b`, and characterized by the provided `role`. The method constructs a unique identifier for the variable by combining these inputs and fetches the corresponding object from an internal registry. If the role is designated as "crisp," the variable is constrained to be binary; otherwise, its mathematical type is set according to the `v_type` argument. Additionally, the method checks visibility conditions based on abstract or concrete fillers for the role and entity `a`, registering the variable with a display manager if these conditions are met. The fully configured variable object is then returned.

      :param a: The first component of the variable's identifier, used to construct the variable name and check visibility conditions.
      :type a: str
      :param b: The second component of the pair used to construct the variable's unique identifier.
      :type b: str
      :param role: The role or relationship defining the variable, used to construct its name, determine if it is binary, and check visibility settings for fillers.
      :type role: str
      :param v_type: The type classification to assign to the variable.
      :type v_type: VariableType

      :return: The `Variable` object corresponding to the specified role and arguments, configured with the provided type and binary status.

      :rtype: Variable



   .. py:method:: __get_variable_11(ind: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves or creates a continuous optimization variable associated with the provided concrete individual. This method acts as a specialized wrapper around the general variable retrieval logic, explicitly enforcing that the resulting variable is of the continuous type to accommodate real-valued constraints. It ensures that the MILP model correctly represents the individual's assertion using a non-discrete variable, potentially modifying the solver's internal state if the variable does not yet exist.

      :param ind: The concrete individual instance whose value is to be assigned to the variable.
      :type ind: CreatedIndividual

      :return: A continuous variable representing the value of the provided concrete individual.

      :rtype: Variable



   .. py:method:: __get_variable_12(ind: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual, v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType) -> None

      Retrieves or creates a MILP variable associated with a specific concrete individual, deriving a unique identifier from the individual's role and parent context. The method constructs the variable name by combining the role name and parent string, substituting default placeholders or the individual's string representation if these attributes are missing. If the variable does not already exist in the internal registry, it is initialized, assigned the specified variable type, and conditionally added to the display tracking system based on visibility settings for concrete fillers.

      :param ind: The concrete individual instance used to generate the variable's name based on its role and parent.
      :type ind: CreatedIndividual
      :param v_type: The type classification to assign to the variable representing the individual's value.
      :type v_type: VariableType



   .. py:method:: __get_variable_2(var_name: str, v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves a variable instance identified by the given name and explicitly sets its type to the specified value. This method first fetches the variable using the standard retrieval mechanism, mutates the variable's type attribute, and then returns the modified object. It is primarily utilized by the DatatypeReasoner to ensure variables are configured with the correct constraints during the reasoning process.

      :param var_name: The identifier for the variable to be retrieved.
      :type var_name: str
      :param v_type: The type or bound to assign to the variable.
      :type v_type: VariableType

      :return: The Variable object corresponding to `var_name`, configured with the specified type `v_type`.

      :rtype: Variable



   .. py:method:: __get_variable_3(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves the decision variable associated with a specific concept assertion, ensuring that the variable exists within the model. If the variable has not been previously defined, this method instantiates a new semi-continuous variable constrained to the interval [0, 1]. The returned variable represents the degree of truth or membership for the specified individual and concept pair.

      :param ass: The fuzzy concept assertion whose value is to be represented by a variable.
      :type ass: Assertion

      :return: The variable representing the truth value of the assertion.

      :rtype: Variable



   .. py:method:: __get_variable_4(rel: fuzzy_dl_owl2.fuzzydl.relation.Relation) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves a variable representing the truth value of a specific fuzzy role assertion, creating it if necessary. The method extracts the subject individual, object individual, and role name from the provided `Relation` object and delegates to the underlying variable management system. If a variable for this specific assertion does not already exist, a new semi-continuous variable bounded between 0 and 1 is instantiated and added to the model. The function returns the variable associated with the assertion.

      :param rel: The fuzzy role assertion for which to retrieve or create the corresponding variable.
      :type rel: Relation

      :return: The variable representing the truth value of the role assertion, created as a semi-continuous variable in the range [0, 1] if it does not already exist.

      :rtype: Variable



   .. py:method:: __get_variable_5(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, restrict: fuzzy_dl_owl2.fuzzydl.restriction.restriction.Restriction) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves a decision variable representing a universal restriction applied to a specific individual, generating a unique key by combining the individual's identifier with the restriction's name. The method relies on the `get_variable` helper to fetch or instantiate the variable, ensuring it is available for the Mixed-Integer Linear Programming model. As a side effect, if the display configuration flags the individual for visibility, the variable is added to the display manager for tracking or logging.

      :param ind: The subject individual of the restriction, used to identify and retrieve the associated variable.
      :type ind: Individual
      :param restrict: A fuzzy role assertion representing the restriction associated with the individual.
      :type restrict: Restriction

      :return: The variable representing the value of the universal restriction for the given individual. If the variable does not already exist, a new semi-continuous variable bounded between 0 and 1 is created and returned.

      :rtype: Variable



   .. py:method:: __get_variable_6(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves or creates a variable representing the truth value of a concept assertion for a specific individual. If the concept is a `HAS_VALUE` restriction, the method extracts the role and value to define a semi-continuous variable bounded between 0 and 1. For other concept types, it generates the variable based on the individual and the string representation of the concept. The actual variable instantiation or lookup is delegated to the `get_variable` method, which handles the creation if the variable does not already exist.

      :param ind: The individual entity for which the concept assertion variable is being retrieved or created.
      :type ind: Individual
      :param c: The fuzzy concept representing the assertion. Used to identify the variable, extracting role and value details if the concept is of type HAS_VALUE.
      :type c: Concept

      :return: The variable representing the truth value of the assertion that the individual belongs to the concept. If the concept is a 'has-value' restriction, the variable is semi-continuous.

      :rtype: Variable



   .. py:method:: __get_variable_7(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, concept_name: str) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves a variable representing the truth value of a concept assertion for a specific individual, identified by the combination of the individual and concept name. If the concept is defined as a crisp concept, the method ensures the variable is configured as a binary variable. Additionally, if the display settings are configured to show either the specific individual or the concept, the variable is added to the display tracker. The method returns the resulting variable object.

      :param ind: The individual entity for which the concept assertion variable is defined.
      :type ind: Individual
      :param concept_name: The name of the fuzzy concept associated with the individual.
      :type concept_name: str

      :return: The decision variable representing the truth value of the concept assertion for the given individual.

      :rtype: Variable



   .. py:method:: __get_variable_8(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, b: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role: str) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves the decision variable representing the assertion of a specific role between a subject individual and an object individual. If a variable for this specific relationship does not already exist, the method creates a new one defined as a semi-continuous variable within the bounds of 0 and 1. This ensures that the Mixed-Integer Linear Programming model has a corresponding variable to track the state or validity of the role assertion.

      :param a: The object individual involved in the role assertion.
      :type a: Individual
      :param b: The subject individual of the role assertion.
      :type b: Individual
      :param role: The name of the role or relationship connecting the subject and object individuals.
      :type role: str

      :return: The variable representing the role assertion between the two individuals, configured as a semi-continuous variable in the range [0, 1].

      :rtype: Variable



   .. py:method:: __get_variable_9(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, b: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role: str, v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves or creates a variable representing a role assertion between two individuals within the mixed-integer linear programming model. This method serves as a wrapper that converts the subject and object individuals to their string representations before delegating to the underlying `get_variable` method, passing the role name and the specified variable type. If a variable for this specific role assertion does not already exist, the delegated call handles its instantiation, ensuring consistent access to variables modeling relationships between entities.

      :param a: The individual representing the object of the role assertion.
      :type a: Individual
      :param b: The individual acting as the subject in the role assertion.
      :type b: Individual
      :param role: The name of the role connecting the two individuals.
      :type role: str
      :param v_type: Specifies the classification or domain type of the variable representing the role assertion.
      :type v_type: VariableType

      :return: The variable representing the role assertion between the object individual and the subject individual, creating a new one if it does not already exist.

      :rtype: Variable



   .. py:method:: __has_variable_1(name: str) -> bool

      Determines whether a variable with the specified name exists within the internal collection of variables managed by the helper. This method performs a membership check against the keys present in the `number_of_variables` attribute. It returns `True` if the variable name is found and `False` otherwise. The operation does not modify the state of the object or any of its attributes.

      :param name: The identifier of the variable to check for existence.
      :type name: str

      :return: True if a variable with the given name exists, False otherwise.

      :rtype: bool



   .. py:method:: __has_variable_2(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> bool

      Checks for the existence of a variable associated with a specific concept assertion by normalizing the assertion's identifier. The method strips degree information from the assertion's name before querying the internal variable registry. It returns a boolean indicating whether a variable corresponding to the normalized name is currently defined.

      :param ass: The concept assertion to check for an associated variable.
      :type ass: Assertion

      :return: True if a variable exists for the given assertion's name, otherwise False.

      :rtype: bool



   .. py:method:: __print_instance_of_labels_1(f_name: str, ind_name: str, value: float) -> None

      This method retrieves the linguistic labels associated with a specific feature and individual combination, identified by the constructed string `f_name(ind_name)`. It iterates through the retrieved labels, calculates the membership degree of the provided numerical value for each label, and prints the results to the console. If no labels are found for the given identifier, the method produces no output. The operation relies on the `show_vars` attribute to access the label definitions and uses a utility function to display the formatted information.

      :param f_name: Name of the feature for which membership degrees are displayed.
      :type f_name: str
      :param ind_name: Name of the individual entity to which the feature value belongs.
      :type ind_name: str
      :param value: Numerical value of the feature for the individual, used to compute and display membership degrees.
      :type value: float



   .. py:method:: __print_instance_of_labels_2(name: str, value: float) -> None

      Retrieves the linguistic labels associated with the specified feature name and calculates the membership degree of the provided value for each label. For every label found, it formats and outputs a message containing the feature name, the label's computed name, and the calculated membership degree. This method acts as a diagnostic utility to visualize how a specific numerical value fits into the defined fuzzy categories, producing side effects in the form of log output without modifying the object's state.

      :param name: Name of the feature or individual used to retrieve the associated linguistic labels.
      :type name: str
      :param value: The numerical value of the feature for which membership degrees are calculated.
      :type value: float



   .. py:method:: __remove_nominal_variables() -> None

      This method purges nominal variables and any constraints that depend on them from the object's internal state. It iterates through the existing constraints to identify those containing nominal terms and scans the variables to determine which are nominal. Once the indices of these elements are collected, the method reconstructs the `constraints` and `variables` lists, excluding the identified items. This process mutates the object's state by reassigning these attributes, effectively removing data that is incompatible with the solver's requirements. If no nominal variables or dependent constraints are present, the lists remain unchanged.



   .. py:method:: __solve_gurobi_using_partitions(objective: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Optional[fuzzy_dl_owl2.fuzzydl.milp.solution.Solution]

      This method solves a Mixed-Integer Linear Programming (MILP) problem by decomposing it into smaller sub-problems based on variable partitions, utilizing the Gurobi optimizer. It begins by determining the partition structure of the variables relative to the objective; if no partition contains more than one variable, it disables the partitioning strategy and delegates to the standard solver. The algorithm proceeds in two phases: first, it solves a model containing only variables from partitions with zero or one variable to check for immediate infeasibility. Second, for each variable in the objective that belongs to a partition with multiple variables, it constructs and optimizes a separate Gurobi model restricted to that partition, effectively optimizing for that specific variable within its local constraints. The results are aggregated into a Solution object, which is returned unless a sub-problem is infeasible (resulting in an inconsistent knowledge base indicator) or a Gurobi error occurs (resulting in None).

      :param objective: The mathematical expression representing the objective function to be optimized. It is analyzed to determine variable partitions and defines the optimization target for the sub-problems.
      :type objective: Expression

      :return: A Solution object representing the optimization result, or None if a Gurobi error occurs. If the model is infeasible, the Solution indicates an inconsistent knowledge base.

      :rtype: typing.Optional[Solution]



   .. py:method:: add_cardinality_list(sc: fuzzy_dl_owl2.fuzzydl.concept.sigma_count.SigmaCount) -> None

      Appends a `SigmaCount` object to the internal collection of cardinality constraints maintained by the helper. This method registers a specific cardinality calculation, defined by a role, a concept, and a set of candidate individuals, for subsequent processing in the Mixed-Integer Linear Programming (MILP) model. The operation modifies the state of the instance by adding the element to the `cardinalities` list and returns `None`. It does not perform validation on the input object or check for duplicates within the list.

      :param sc: The cardinality constraint object to be appended to the list.
      :type sc: SigmaCount



   .. py:method:: add_contradiction() -> None

      Forces the fuzzy Knowledge Base (KB) into an unsatisfiable state by introducing a logical contradiction. This method first clears all existing constraints stored in the helper, effectively discarding any prior model state. It then adds a new constraint requiring a constant expression of 1.0 to equal zero, which is mathematically impossible, thereby ensuring that the MILP model becomes infeasible.



   .. py:method:: add_crisp_concept(concept_name: str) -> None

      Marks a specified concept as crisp by adding its identifier to the internal collection of crisp concepts. This method updates the state of the MILPHelper instance to indicate that the given concept should be treated with crisp logic during subsequent operations. Since the underlying storage is a set, adding a concept that has already been marked as crisp will have no additional effect.

      :param concept_name: The name of the concept to be defined as crisp.
      :type concept_name: str



   .. py:method:: add_crisp_role(role_name: str) -> None

      Registers the specified role name as a crisp role by adding it to the internal collection of crisp roles. This action modifies the object's state to indicate that the role should be treated as non-fuzzy or binary in subsequent operations. The operation is idempotent; if the role name is already present in the collection, the method has no effect.

      :param role_name: Name of the role to be defined as crisp.
      :type role_name: str



   .. py:method:: add_equality(var1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, var2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> None

      Adds a linear constraint to the optimization model that enforces the equivalence of two specified variables. By creating an expression representing the difference between the first and second variable and setting it to zero, this method ensures that the solver assigns the same value to both variables. This action updates the internal model state, potentially affecting the feasibility or optimality of the solution depending on other existing constraints.

      :param var1: The first variable in the equality constraint.
      :type var1: Variable
      :param var2: The variable to equate to var1.
      :type var2: Variable



   .. py:method:: add_new_constraint(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, constraint_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> None
                  add_new_constraint(x: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, n: float) -> None
                  add_new_constraint(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion, n: float) -> None
                  add_new_constraint(x: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, d: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> None
                  add_new_constraint(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None
                  add_new_constraint(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, constraint_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> None
                  add_new_constraint(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, constraint_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType, n: float) -> None

      Adds a new constraint to the MILP model, supporting multiple overloads based on the provided arguments to accommodate various ways of defining linear constraints. Depending on the number and types of arguments, the method dispatches to specific internal handlers for cases such as a single `Assertion`; a pair consisting of an `Expression` and `InequalityType`, a `Variable` and a numeric value, an `Assertion` and a numeric value, or a `Variable` and a `Degree`; or a triplet consisting of an `Expression`, an `InequalityType`, and either a `Degree` or a numeric value. If the number of arguments is not between 1 and 3, or if the specific type combination does not match a supported signature, a `ValueError` is raised. This operation modifies the internal state of the helper object by incorporating the new constraint into the underlying model.

      :param args: Variable-length arguments defining the constraint, accepting an Assertion or combinations of Expressions, Variables, InequalityTypes, Degrees, or numeric constants.
      :type args: typing.Any

      :raises ValueError: Raised when the provided arguments do not match any of the supported signatures or type combinations.



   .. py:method:: add_string_feature(role: str) -> None

      Appends a specified string role to the internal collection of string features maintained by the helper. This operation modifies the object's state by adding the input to the `string_features` set. If the provided role is already present in the collection, the set ensures that no duplicate entry is created, making the operation idempotent.

      :param role:
      :type role: str



   .. py:method:: add_string_value(value: str, int_value: int) -> None

      Associates a human-readable string with a specific integer identifier, creating a mapping used to translate between solver indices and feature names. This method updates the internal dictionary responsible for storing these relationships, using the integer as the key and the string as the value. If the provided integer key already exists in the mapping, the previous string value will be overwritten with the new one.

      :param value: The string value to be associated with the integer identifier.
      :type value: str
      :param int_value: The integer key to associate with the string feature value.
      :type int_value: int



   .. py:method:: change_variable_names(old_name: str, new_name: str, old_is_created_individual: bool) -> None

      Updates the MILP model by renaming variables that include a specific individual identifier, replacing the old name with the new one within variable definitions. It iterates through existing variables to identify matches and establishes constraints linking the original variables to their renamed counterparts. The specific constraint logic depends on whether the old individual is a created individual: if true, an equality constraint is enforced to ensure the variables remain equivalent; otherwise, an inequality constraint is added involving a nominal variable to enforce that the value of the variable associated with the new name is greater than or equal to the value associated with the old name when the nominal condition is met.

      :param old_name: The existing individual name to be replaced within the variable definitions.
      :type old_name: str
      :param new_name: The target individual name used to replace the old name in variable definitions and construct new variable identifiers.
      :type new_name: str
      :param old_is_created_individual: Flag indicating if the old individual is a created individual; if True, an equality constraint is added between the old and new variables, otherwise an inequality constraint is added.
      :type old_is_created_individual: bool



   .. py:method:: check_if_replacement_is_needed(v1: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, s1: str, v2: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, s2: str) -> bool

      Determines whether the string representations of two variables are structurally identical except for specific substrings located at the same position. The method compares the names of the variables by checking if the substrings `s1` and `s2` appear at the same starting index and if the characters preceding and following these substrings are exactly the same. This effectively verifies if the names follow a pattern of `prefix + s1 + suffix` and `prefix + s2 + suffix`. Note that the method will raise a `ValueError` if either `s1` is not found in the name of `v1` or `s2` is not found in the name of `v2`.

      :param v1: The first variable in the comparison, converted to a string to locate the substring s1 and compare its surrounding context with that of v2.
      :type v1: Variable
      :param s1: The substring to find within the first variable's name, acting as the anchor for comparing the surrounding context.
      :type s1: str
      :param v2: The variable to compare against `v1`, checking if its name matches `v1`'s name with `s2` replacing `s1`.
      :type v2: Variable
      :param s2: The substring within the second variable's name used to verify structural alignment with the first variable.
      :type s2: str

      :return: True if the string representations of v1 and v2 are identical except for the substrings s1 and s2, provided they occur at the same index.

      :rtype: bool



   .. py:method:: clone() -> Self

      Creates and returns a deep copy of the current `MILPHelper` instance. The method constructs a new object and populates it by recursively cloning lists of complex objects such as `cardinalities`, `constraints`, and `variables`, while using `copy.deepcopy` for other mutable structures like `crisp_concepts` and `string_features`. This ensures that the returned instance is independent of the original for most attributes, though it is important to note that `nominal_variables` is assigned by reference rather than copied, meaning modifications to this specific attribute in the clone will affect the original object.

      :return: A deep copy of the current instance.

      :rtype: typing.Self



   .. py:method:: exists_nominal_variable(i: str) -> bool

      Determines whether a variable representing the nominal concept for a specific individual `i` is currently defined within the model. The method constructs the expected variable name based on the individual's identifier and checks for its presence in the internal collection of variables. This is a read-only operation that returns a boolean indicating whether the specific nominal variable has been instantiated.

      :param i: The identifier of the individual to check for the existence of a corresponding nominal variable.
      :type i: str

      :return: True if a variable representing the nominal concept for the individual `i` exists, False otherwise.

      :rtype: bool



   .. py:method:: exists_variable(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, b: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role: str) -> bool

      Determines whether a MILP variable representing a specific role assertion between two individuals has been registered within the helper. The method constructs a unique variable identifier by formatting the subject individual, object individual, and role name into a specific string pattern. It then checks for the existence of this key in the internal variable registry and returns a boolean result without modifying the state of the object.

      :param a: The object individual involved in the role assertion.
      :type a: Individual
      :param b: The individual acting as the subject in the role assertion.
      :type b: Individual
      :param role: The name of the role assertion defining the relationship between the subject and object individuals.
      :type role: str

      :return: True if a variable representing the role assertion between the object individual `a` and the subject individual `b` exists, False otherwise.

      :rtype: bool



   .. py:method:: get_name_for_integer(i: int) -> Optional[str]

      Retrieves the symbolic name associated with a specific integer index by performing a reverse lookup on the internal mapping of variable names to their integer identifiers. If the provided integer corresponds to a known variable index, the method returns the associated name string; otherwise, it returns None to indicate that no variable is currently mapped to that value. This is a read-only operation that does not modify the state of the object.

      :param i: The integer identifier of the variable to look up.
      :type i: int

      :return: The name of the variable associated with the given integer, or None if the integer is not found.

      :rtype: typing.Optional[str]



   .. py:method:: get_negated_nominal_variable(i1: str, i2: str) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves or creates a binary decision variable representing the assertion that a specific individual does not belong to the nominal concept defined by another individual. The variable is identified by the string pattern "{i1}: not { {i2} }". If this variable is being created for the first time, the method sets its type to binary and adds a linear constraint to the model enforcing the relationship that the sum of this negated variable and its corresponding positive nominal variable equals one, ensuring they are mutually exclusive. If the variable already exists within the helper's variable set, it is returned directly without adding new constraints.

      :param i1: The individual representing the entity that is the subject of the negated assertion.
      :type i1: str
      :param i2: The individual representing the nominal concept that `i1` is asserted not to belong to.
      :type i2: str

      :return: A binary variable representing the assertion that individual `i1` does not belong to the nominal concept `{i2}`. If the variable is created for the first time, it is constrained to be the logical complement of the corresponding nominal variable.

      :rtype: Variable



   .. py:method:: get_new_variable(v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Creates a new variable of the specified type and registers it within the MILP helper instance. The method guarantees a unique variable name by checking against the internal registry of existing variables; if a name collision is detected, it regenerates the variable until a unique identifier is found. As a side effect, the new variable is appended to the internal list of variables, and its name is recorded in the tracking dictionary with its corresponding index.

      :param v_type: The type of the variable to create.
      :type v_type: VariableType

      :return: A newly created Variable of the specified type, guaranteed to have a unique name and added to the internal variable list.

      :rtype: Variable



   .. py:method:: get_nominal_variable(i1: str) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable
                  get_nominal_variable(i1: str, i2: str) -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves a nominal variable instance associated with the provided string identifiers, supporting two distinct calling conventions based on the number of arguments. The method validates that the input consists of either one or two strings, raising an assertion error otherwise, and delegates the actual retrieval logic to private helper methods. It returns the corresponding Variable object, which serves as a fundamental component within the Mixed-Integer Linear Programming model managed by the helper.

      :param args: One or two string arguments used to identify the nominal variable.
      :type args: typing.Any

      :return: The nominal variable matching the specified identifier(s).

      :rtype: Variable



   .. py:method:: get_number_for_assertion(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> int

      Retrieves the integer codification associated with a given assertion by first resolving the assertion to its variable representation and then looking up the corresponding integer value in the internal variable mapping. This method serves as a bridge between logical assertions and their numerical identifiers used in the MILP formulation, performing a read-only operation without modifying the underlying data structures. If the assertion has not been previously registered in the mapping, the method returns None.

      :param ass: The assertion to be converted into an integer codification.
      :type ass: Assertion

      :return: The integer identifier associated with the variable of the assertion.

      :rtype: int



   .. py:method:: get_ordered_permutation(x: list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]) -> list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]
                  get_ordered_permutation(x: list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable], z: list[list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]]) -> list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]

      Generates and returns a list of decision variables used to model an ordered permutation within a Mixed-Integer Linear Programming (MILP) context. The method acts as a dispatcher based on the number of arguments provided: it accepts either a single list of variables or a list of variables paired with a two-dimensional list of variables. Input validation is performed to ensure the first argument is a list of `Variable` objects and, if present, the second argument is a list of lists containing `Variable` objects. Depending on the argument count, the logic delegates to internal helper methods to construct the specific variable set required for the permutation constraints.

      :param args: A variable-length argument list accepting either a single list of Variables, or a list of Variables followed by a list of lists of Variables.
      :type args: typing.Any

      :raises ValueError: Raised if the number of provided arguments is not 1 or 2.

      :return: A list of Variable objects representing the ordered permutation derived from the input arguments.

      :rtype: list[Variable]



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

      Retrieves a `Variable` instance by acting as a polymorphic dispatcher that delegates to specific internal handlers based on the number and types of arguments provided. The method supports a wide variety of signatures involving strings, domain entities such as `Individual`, `Concept`, `Restriction`, and `CreatedIndividual`, as well as logical constructs like `Assertion` and `Relation`. Depending on the specific combination of inputs, the method may infer the variable type or accept an explicit `VariableType` argument. If the argument count is not between one and four, or if the provided types do not correspond to any defined overload, a `ValueError` is raised.

      :param args: Variable-length arguments specifying the criteria for retrieving the variable. The specific combination of argument types and count determines the lookup strategy, supporting inputs ranging from a simple name string to complex combinations of Individuals, Relations, and VariableTypes.
      :type args: typing.Any

      :raises ValueError: Raised if the provided arguments do not match any of the supported type signatures or argument counts.

      :return: The Variable object corresponding to the provided arguments.

      :rtype: Variable



   .. py:method:: has_nominal_variable(terms: list[fuzzy_dl_owl2.fuzzydl.milp.term.Term]) -> bool

      Determines whether the provided list of terms contains at least one variable that is classified as nominal. The method iterates through the collection, extracting the variable identifier from each term and verifying its status using the `is_nominal_variable` helper. It returns `True` immediately upon finding the first nominal variable and `False` if the list is empty or no such variable is found. This function performs a read-only check and does not modify the input terms.

      :param terms: A list of Term objects to inspect for nominal variables.
      :type terms: list[Term]

      :return: True if the provided list of terms contains at least one nominal variable, False otherwise.

      :rtype: bool



   .. py:method:: has_variable(name: str) -> bool
                  has_variable(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> bool

      Checks for the existence of a variable based on the type of the provided argument. The method accepts a single argument, which must be either a string representing a variable name or an `Assertion` object. If the argument is a string, the method verifies if a variable with that name exists; if it is an `Assertion`, it checks the assertion's association with variables. The function returns a boolean value indicating the presence of the variable. Passing an argument of any other type raises a `ValueError`.

      :param args: The object to check, which must be either a string or an Assertion instance.
      :type args: typing.Any

      :raises ValueError: Raised if the provided argument is not a string or an Assertion instance.

      :return: True if the variable identified by the provided string or Assertion exists, False otherwise.

      :rtype: bool



   .. py:method:: is_crisp_concept(concept_name: str) -> bool

      Determines whether the specified concept is classified as a crisp concept by checking its membership in the internal collection of crisp concepts. The method returns True if the concept name is present in the collection, indicating a crisp definition, and False otherwise. This operation is read-only and does not modify the state of the helper object.

      :param concept_name: The identifier of the concept to verify.
      :type concept_name: str

      :return: True if the specified concept name is present in the set of crisp concepts, otherwise False.

      :rtype: bool



   .. py:method:: is_crisp_role(role_name: str) -> bool

      Determines if the specified role is classified as a crisp role by checking for its presence in the internal collection of crisp roles. This method returns a boolean value indicating whether the role name is a member of that collection. It performs a read-only operation and does not modify the state of the object.

      :param role_name: The name of the role to check for crispness.
      :type role_name: str

      :return: True if the specified role is a crisp role, False otherwise.

      :rtype: bool



   .. py:method:: is_nominal_variable(i: str) -> bool

      Determines whether the provided string `i` represents a nominal variable by checking if it conforms to the specific naming convention `name:{name}`. The method employs a regular expression to identify substrings where the text preceding a colon matches exactly the text enclosed within curly braces. It returns `True` if at least one such pattern is found within the input string, and `False` otherwise. This function performs a read-only operation and does not produce any side effects on the object's state or the input argument.

      :param i: The string representation of the variable to check.
      :type i: str

      :return: True if the input string matches the pattern 'name:{name}', indicating it is a nominal variable; otherwise, False.

      :rtype: bool



   .. py:method:: optimize(objective: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Optional[fuzzy_dl_owl2.fuzzydl.milp.solution.Solution]

      Optimizes the provided objective expression by dispatching the problem to a specific Mixed-Integer Linear Programming (MILP) solver defined in the global configuration. The method inspects the `MILP_PROVIDER` setting to select the appropriate backend, supporting options such as Gurobi, Python-MIP, and various PuLP interfaces. It delegates the actual solving process to the corresponding internal method and returns the resulting solution object. If the configured provider is not recognized or supported, a `ValueError` is raised.

      :param objective: The mathematical expression or model to be optimized using the configured MILP solver.
      :type objective: Expression

      :raises ValueError: Raised when the configured MILP provider is unsupported or unrecognized.

      :return: The optimal solution for the given objective expression, or None if no solution is found.

      :rtype: typing.Optional[Solution]



   .. py:method:: print_instance_of_labels(f_name: str, ind_name: str, value: float) -> None
                  print_instance_of_labels(name: str, value: float) -> None

      Outputs the membership degrees of a numerical value with respect to specific linguistic labels. This method acts as a dispatcher that supports two distinct calling signatures based on the number of arguments provided. If two arguments are supplied, it expects a string identifier and a numerical value; if three arguments are supplied, it expects two string identifiers followed by a numerical value. The method validates the input types and delegates the actual printing logic to private helper methods.

      :param args: The linguistic label and numeric value to evaluate, optionally preceded by a variable name.
      :type args: typing.Any



   .. py:method:: set_binary_variables() -> None

      Iterates over the collection of variables managed by the helper and converts them into binary variables, restricting their domain to the discrete set {0, 1}. This transformation specifically excludes variables that are already defined as continuous or integer, as well as those designated as datatype fillers. The method modifies the state of the variable objects in place, effectively preparing the model for a Mixed-Integer Linear Programming context by enforcing boolean constraints on the applicable variables.



   .. py:method:: set_nominal_variables(value: bool) -> None

      Updates the configuration of the MILP helper instance by setting the flag that determines whether nominal variables are used. This method accepts a boolean value, which is assigned to the instance's internal state, thereby influencing the formulation of the optimization problem in subsequent operations. The operation modifies the object in-place and does not return a value.

      :param value: Flag indicating whether nominal variables are enabled.
      :type value: bool



   .. py:method:: solve_gurobi(objective: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Optional[fuzzy_dl_owl2.fuzzydl.milp.solution.Solution]

      Constructs and optimizes a Mixed-Integer Linear Programming (MILP) model using the Gurobi solver based on the variables and constraints defined in the current instance. It translates the provided objective expression into Gurobi coefficients and handles various variable types, including binary, integer, continuous, and semi-continuous, while respecting their bounds. The method filters out duplicate or zero constraints before optimization and delegates to a partition-based solver if the `PARTITION` flag is enabled. Upon completion, it writes the model and solution files to the results directory and prints statistics or debug information if configured. If the model is infeasible, it returns a Solution object indicating inconsistency; if a Gurobi error occurs, it logs the exception and returns None.

      :param objective: The linear expression representing the objective function to be optimized.
      :type objective: Expression

      :return: A Solution object containing the optimal objective value and relevant variable assignments if the model is feasible, a Solution indicating inconsistency if the model is infeasible, or None if a Gurobi error occurs during solving.

      :rtype: typing.Optional[Solution]



   .. py:method:: solve_mip(objective: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Optional[fuzzy_dl_owl2.fuzzydl.milp.solution.Solution]

      Constructs and solves a Mixed-Integer Linear Programming (MIP) model using the CBC solver to minimize the provided objective expression. The method translates internal variable definitions and constraints into a `mip.Model`, handling binary, integer, continuous, and semi-continuous variable types while respecting their bounds. It returns a `Solution` object containing the optimal objective value and variable values, or a specific solution indicating an inconsistent knowledge base if the problem is infeasible. If an exception occurs during the process, the method returns `None`. Side effects include writing the generated model and solution files to the results directory and logging debug information regarding the model's structure and optimization statistics.

      :param objective: The linear expression defining the objective function to be minimized by the MIP solver.
      :type objective: Expression

      :return: A Solution object containing the optimization result, including the objective value and variable assignments if feasible, or a status indicating inconsistency if the model is infeasible. Returns None if an error occurs during the solving process.

      :rtype: typing.Optional[Solution]



   .. py:method:: solve_pulp(objective: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Optional[fuzzy_dl_owl2.fuzzydl.milp.solution.Solution]

      Solves the defined Mixed-Integer Linear Programming (MILP) problem using the PuLP library to minimize the provided objective expression. The method constructs a PuLP model by mapping internal variables to PuLP variables, supporting binary, integer, continuous, and semi-continuous types. Specifically, for semi-continuous variables when using GLPK or CPLEX, it introduces auxiliary binary variables and linear constraints to enforce the semi-continuous domain. It iterates through the helper's constraints to populate the model, skipping zero or duplicate entries. The solver is selected and configured dynamically based on the `MILP_PROVIDER` setting, with specific tolerances and logging options applied for CBC, GLPK, HiGHS, and CPLEX. Upon completion, it returns a `Solution` object containing the optimal objective value and variable assignments, or a specific solution indicating inconsistency if the problem is infeasible. If an exception occurs during the process, the method returns `None`. Side effects include generating debug logs, writing temporary log and model files to disk, and cleaning up specific temporary files created by CPLEX.

      :param objective: The linear expression defining the objective function to be minimized.
      :type objective: Expression

      :return: A Solution object containing the optimal objective value and variable assignments if the MILP problem is solved successfully. If the problem is infeasible or unbounded, returns a Solution indicating an inconsistent knowledge base. Returns None if an exception occurs during execution.

      :rtype: typing.Optional[Solution]



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


