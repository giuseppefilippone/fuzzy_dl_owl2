fuzzy_dl_owl2.fuzzydl.parser.dl_parser_clean
============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.parser.dl_parser_clean



.. ── LLM-GENERATED DESCRIPTION START ──

A semantic action handler that transforms parsed tokens into a Fuzzy Description Logic knowledge base and associated query objects.


Description
-----------


The software serves as a collection of semantic callbacks designed to construct a domain model from raw input tokens, effectively bridging the gap between syntactic parsing and the internal representation of a Fuzzy Description Logic knowledge base. By converting strings and numeric values into specialized objects such as concepts, individuals, degrees, and mathematical expressions, the logic ensures that the resulting structure adheres to the specific semantics of the chosen fuzzy logic, whether it be Zadeh, Lukasiewicz, or classical. Beyond simple object creation, the implementation enforces strict validation rules, such as distinguishing between abstract and concrete roles or verifying that fuzzy-specific operators are not used in incompatible reasoning contexts. Furthermore, the system manages the accumulation of query objects and Mixed-Integer Linear Programming constraints, preparing the entire model for subsequent reasoning and execution tasks.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_clean.DLParser


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_dl_parser_clean_DLParser.png
       :alt: UML Class Diagram for DLParser
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **DLParser**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_dl_parser_clean_DLParser.pdf
       :alt: UML Class Diagram for DLParser
       :align: center
       :width: 10.8cm
       :class: uml-diagram

       UML Class Diagram for **DLParser**

.. py:class:: DLParser

   Bases: :py:obj:`object`


   This class holds the semantic callbacks for the Fuzzy Description Logic parser, transforming raw string tokens into domain-specific objects such as `Concept`, `Individual`, and `Degree` instances. It is pyparsing-free: each static `_parse_*` method consumes a token list and either returns a constructed object (`Concept`, `Term`, `Degree`, `Expression`, `Inequation`, ...) or mutates the shared `KnowledgeBase` in place (side-effect callbacks return `None`). The hand-written recursive-descent driver in `dl_parser_fast.py` invokes these callbacks while walking the input. The class handles semantic validation and logic-specific constraints (e.g., distinguishing between Zadeh and Lukasiewicz logic), ensuring that the constructed knowledge base adheres to the specified fuzzy logic semantics. Parsed queries are accumulated in `queries_list`.

   :param kb: The KnowledgeBase instance constructed and populated by the parser with the parsed domain model.
   :type kb: KnowledgeBase
   :param queries_list: Accumulates Query objects extracted from the input during parsing, which are subsequently returned for execution against the knowledge base.
   :type queries_list: list[Query]


   .. py:method:: _check_abstract(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None
      :staticmethod:


      Validates that the provided `Concept` instance is abstract, ensuring it is not marked as concrete. If the concept is determined to be concrete, this method triggers an error reporting routine to signal a violation of the expected schema. This static method serves as a guard clause within the parsing logic to enforce structural constraints.

      :param c: The concept to validate as abstract.
      :type c: Concept



   .. py:method:: _create_fuzzy_number(tokens: list) -> fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber
      :staticmethod:


      This static method processes parse tokens to construct a `TriangularFuzzyNumber` instance, supporting multiple input formats. If a single numeric value is provided, it generates a crisp fuzzy number where the lower, middle, and upper bounds are equal. When a string identifier is encountered, the method retrieves the corresponding fuzzy number from the knowledge base; if the identifier is undefined, an error is triggered. If three numeric values are present, they are interpreted as the lower, middle, and upper bounds of the triangular distribution. The method also outputs debug information if the global debug flag is enabled.

      :param tokens: The parsed elements representing a fuzzy number, which can be a single numeric value, a string identifier referencing a predefined number, or a list of three numeric values.
      :type tokens: list

      :return: A TriangularFuzzyNumber instance derived from the input tokens.

      :rtype: TriangularFuzzyNumber



   .. py:method:: _fuzzy_logic_parser(tokens: list) -> None
      :staticmethod:


      This static method acts as a semantic callback to process and apply a specified fuzzy logic type to the system. It extracts the first token, converts it to a lowercase string, and instantiates a corresponding FuzzyLogic object. The method then updates the Knowledge Base associated with the parser by setting this logic, effectively configuring the reasoning engine for the session. It assumes the input grammar guarantees the presence of at least one token to define the logic.

      :param tokens: The tokens containing the identifier for the fuzzy logic type to be applied to the knowledge base.
      :type tokens: list



   .. py:method:: _get_modifier(m: str) -> fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier
      :staticmethod:


      Retrieves a `Modifier` object from the shared knowledge base corresponding to the given string name. This method verifies that the modifier is defined; if the knowledge base is uninitialized or the name is not found, it invokes an error handling routine to signal the issue. Furthermore, it outputs debug logging details if the debug print configuration is active.

      :param m: The name of the modifier to retrieve from the knowledge base.
      :type m: str

      :return: The `Modifier` object associated with the specified name.

      :rtype: Modifier



   .. py:method:: _is_non_decreasing(v: list[Any]) -> bool
      :staticmethod:


      Utility method to check if a list is sorted in non-decreasing order. It iterates through the list and compares each element with the next one, returning `False` if it finds any pair of elements that are out of order. If the entire list is traversed without finding any such pair, it returns `True`, indicating that the list is sorted.

      :param v: The list to be checked for sorted order.
      :type v: list[typing.Any]

      :return: A boolean value indicating whether the list is sorted in non-decreasing order.
      :rtype: bool



   .. py:method:: _parse_axioms(tokens: list) -> None
      :staticmethod:


      Processes a list of parsed tokens representing Description Logic axioms and updates the global knowledge base accordingly. The method inspects the leading keyword to dispatch specific logic for various axiom types, including individual assertions, role relations, concept implications (supporting multiple fuzzy logic semantics such as Goedel, Lukasiewicz, and Zadeh), concept definitions, and disjointness constraints. Additionally, it manages role characteristics like domain, range, transitivity, symmetry, and inverse relationships, performing validation to ensure concrete roles are not used in invalid contexts. Fuzzy degrees are applied to assertions and implications where provided, defaulting to 1.0 otherwise.

      :param tokens: The parsed result containing the axiom keyword and its associated arguments (e.g., concepts, individuals, roles) to be processed and added to the knowledge base.
      :type tokens: list



   .. py:method:: _parse_binary_concept(tokens: list) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      Parses a binary or n-ary concept expression from the provided parse results, identifying the specific operation based on the first token. The method handles a variety of logical constructs, including conjunctions, disjunctions, implications, quantifiers, value restrictions, and approximation operators, dynamically selecting the appropriate implementation (e.g., Lukasiewicz, Goedel, or Zadeh) based on the current fuzzy logic setting in the knowledge base. It validates that operands are abstract concepts, ensures referenced roles and individuals exist, and enforces logic-specific constraints by raising errors if fuzzy-specific operators are used within a classical logic context. If the operator token is already a Concept object, the method returns the input tokens unchanged.

      :param tokens: The parsed structure containing the operator and operands for the binary concept.
      :type tokens: list

      :return: The specific Concept instance (e.g., OperatorConcept, ImpliesConcept) constructed from the input tokens.

      :rtype: Concept



   .. py:method:: _parse_constraints(tokens: list) -> None
      :staticmethod:


      This static method processes parsed tokens to apply variable constraints to the Mixed-Integer Linear Programming (MILP) model associated with the parser's knowledge base. It examines the first token to identify the constraint type; if the token indicates a binary or free variable, the method retrieves the corresponding variable object by name and updates its type definition. It modifies the global model state rather than transforming the data stream.

      :param tokens: Tokens containing the constraint definition, used to extract the variable type and identifier for updating the MILP model.
      :type tokens: list



   .. py:method:: _parse_crisp_declarations(tokens: list) -> None
      :staticmethod:


      This static method processes parsed tokens to identify and handle crisp declarations for either concepts or roles. Based on the leading keyword in the token list, it iterates through the remaining identifiers to update the global knowledge base. If the declaration targets concepts, it converts the identifiers to Concept objects and registers them as crisp; if it targets roles, it registers the role identifiers directly. The operation modifies the state of the knowledge base.

      :param tokens: The tokens containing the declaration type keyword followed by the identifiers of the concepts or roles to be marked as crisp.
      :type tokens: list



   .. py:method:: _parse_datatype_restriction(tokens: list) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      This static method processes a datatype restriction from the provided tokens, determining the restriction type (such as exact, at most, or at least) based on the operator token and identifying the associated concrete feature role. It validates that the role has been previously defined in the knowledge base and ensures that any triangular fuzzy numbers used have a defined range before proceeding. Depending on the value token's type, the method resolves strings to either existing fuzzy number concepts or new continuous variables, and handles triangular fuzzy numbers by extracting their crisp or fuzzy representations. The constructed restriction is then added to the global knowledge base.

      :param tokens: The parsed components of the datatype restriction, containing the operator, the feature role, and the value or concept.
      :type tokens: list

      :return: The datatype restriction Concept that was added to the knowledge base.

      :rtype: Concept



   .. py:method:: _parse_degree(tokens: list) -> fuzzy_dl_owl2.fuzzydl.degree.degree.Degree
      :staticmethod:


      Converts raw parsing tokens into specific semantic Degree objects based on the type of the first token found in the input. If the token is a numeric value, the method returns a `DegreeNumeric` object; if it is an `Expression` instance, it returns a `DegreeExpression` object. For string tokens, the method consults the knowledge base to check for a defined truth constant, returning a `DegreeNumeric` if a match is found, or otherwise treating the string as a variable name to retrieve and return a `DegreeVariable`. Debug information may be logged if enabled.

      :param tokens: The parsed output containing the raw degree data, expected to be a numeric value, an expression, or a variable name.
      :type tokens: list

      :return: The specific Degree instance (DegreeNumeric, DegreeExpression, or DegreeVariable) derived from the input tokens.

      :rtype: Degree



   .. py:method:: _parse_expression(tokens: list) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression
      :staticmethod:


      Converts raw parsing tokens into a structured Expression object, specifically handling the construction of additive expressions. The method first normalizes the input by unwrapping nested list structures. If the resulting list contains a single Term, it wraps that term in an Expression; if it contains a sequence of Terms separated by addition operators, it aggregates them into a single Expression.

      :param tokens: The raw parsing result containing the terms and operators that constitute the expression.
      :type tokens: list

      :return: The constructed Expression representing a single term or sum of terms.

      :rtype: Expression



   .. py:method:: _parse_feature(tokens: list) -> None
      :staticmethod:


      Processes a parsed feature definition to register a concrete feature within the global knowledge base. It inspects the provided token list to identify the feature's role and data type, dispatching to the appropriate definition method—such as defining integer or real ranges, or boolean and string types. This method mutates the knowledge base state by adding the new feature definition.

      :param tokens: The parsed components of a feature definition, including the role name, data type, and optional numeric bounds.
      :type tokens: list



   .. py:method:: _parse_fuzzy_concept(tokens: list) -> None
      :staticmethod:


      Parses a fuzzy concept definition from the provided tokens and registers the corresponding concrete concept object in the global knowledge base. The method validates that the concept name is not already defined and ensures that non-crisp concept types are not used with a classical reasoner. Depending on the keyword found in the tokens, it instantiates a specific concept class—such as `CrispConcreteConcept`, `TriangularConcreteConcept`, or `ModifiedConcreteConcept`—using the extracted parameters. For modified concepts, it verifies that the base concept exists prior to creation. As a side effect, adding a non-crisp concept sets a flag in the knowledge base indicating the presence of concrete fuzzy concepts.

      :param tokens: Tokens containing the fuzzy concept definition, including the concept name, type keyword, and associated parameters or references.
      :type tokens: list



   .. py:method:: _parse_fuzzy_equivalence(tokens: list) -> None
      :staticmethod:


      Processes the parsed tokens corresponding to a fuzzy equivalence relation and updates the global knowledge base accordingly. This static method extracts the primary identifier from the token list and invokes the knowledge base's `add_equivalence_relation` method to register the relation. Its primary effect is the mutation of the shared `DLParser.kb` state.

      :param tokens: The tokens containing the fuzzy equivalence relation to be added to the knowledge base.
      :type tokens: list



   .. py:method:: _parse_fuzzy_number_range(tokens: list) -> None
      :staticmethod:


      Extracts the lower and upper bounds from the provided tokens to configure the range for triangular fuzzy numbers. This static method invokes the `TriangularFuzzyNumber.set_range` method with the first two elements, resulting in a side effect that updates the class-level state. It assumes the input contains at least two elements to define the range boundaries.

      :param tokens: The tokens containing the values that define the fuzzy number range.
      :type tokens: list



   .. py:method:: _parse_fuzzy_similarity(tokens: list) -> None
      :staticmethod:


      This static method processes a fuzzy similarity relation identified during the parsing phase. It extracts the primary identifier from the provided tokens and adds it to the parser's knowledge base as a similarity relation. It serves as a side-effect trigger that updates the internal state of the knowledge base.

      :param tokens: The tokens containing the fuzzy similarity relation data extracted from the input string.
      :type tokens: list



   .. py:method:: _parse_inequation(tokens: list) -> fuzzy_dl_owl2.fuzzydl.milp.inequation.Inequation
      :staticmethod:


      Processes a set of parsing tokens representing an inequation to construct a formal constraint and update the underlying mathematical model. If the tokens contain a valid expression followed by an operator and a constant, the method normalizes the expression by subtracting the constant and determines the specific inequality type based on the operator string. It then registers this constraint within the MILP model associated with the current knowledge base.

      :param tokens: The parsed components of the inequation, consisting of an expression, a comparison operator, and a constant value.
      :type tokens: list

      :return: The parsed Inequation instance.

      :rtype: Inequation



   .. py:method:: _parse_modifier(tokens: list) -> None
      :staticmethod:


      This static method processes a parsed modifier definition by extracting the modifier type and parameters from the provided tokens. It distinguishes between linear and triangular modifiers based on the specific keyword present, instantiating the corresponding `LinearModifier` or `TriangularModifier` object with the extracted arguments. The constructed modifier is then registered with the global knowledge base (`DLParser.kb`), effectively updating the application's state. The method assumes the input list contains sufficient elements for the specific modifier type, potentially raising an error if the token structure is invalid.

      :param tokens: The parsed components of a modifier definition, including the name, type keyword, and associated parameters.
      :type tokens: list



   .. py:method:: _parse_modifier_concept(tokens: list) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      This static method processes a sequence of tokens representing a modifier applied to a concept, expecting the input list to contain exactly two elements. It extracts the modifier from the first token and the base concept from the second, resolving them into their respective object instances. The method then applies the modification logic to the concept and returns the resulting modified concept.

      :param tokens: The parsed tokens containing the modifier and concept components to be combined.
      :type tokens: list

      :return: The Concept resulting from applying the parsed Modifier to the parsed Concept.

      :rtype: Concept



   .. py:method:: _parse_owa_integral_concept(tokens: list) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      Parses a fuzzy logic integral concept—specifically OWA, Choquet, Sugeno, or Q-Sugeno—from the provided tokens. The method extracts the operator from the first token and divides the remaining tokens into two equal lists representing weights and concepts, converting the latter into `Concept` objects. It performs validation on the weights, ensuring they sum to 1.0 for OWA operators and that the maximum weight is 1.0 for Choquet, Sugeno, and Q-Sugeno operators, reporting an error if these conditions are not met. The result is the appropriate specialized concept instance.

      :param tokens: The tokens containing the integral operator, associated weights, and the list of concepts to be aggregated.
      :type tokens: list

      :return: The specific integral concept instance (OwaConcept, ChoquetIntegral, SugenoIntegral, or QsugenoIntegral) parsed from the input tokens.

      :rtype: Concept



   .. py:method:: _parse_q_owa_concept(tokens: list) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      This static method processes a sequence of tokens to construct a Quantified OWA (Ordered Weighted Averaging) concept. It interprets the first token as the name of a fuzzy concrete concept, retrieving it from the knowledge base to serve as the aggregation function. The method enforces strict type checking, ensuring the retrieved function is either a `RightConcreteConcept` or `LeftConcreteConcept`, and triggers an error if the concept is undefined or of an incorrect type. Subsequent tokens are recursively parsed into standard `Concept` objects to serve as arguments. Finally, it returns the fully initialized `QowaConcept`.

      :param tokens: Tokens representing the components of a Q-OWA concept, comprising a fuzzy aggregation function identifier and a list of concepts to aggregate.
      :type tokens: list

      :return: The constructed QowaConcept instance.

      :rtype: Concept



   .. py:method:: _parse_queries(tokens: list) -> None
      :staticmethod:


      Parses a list of tokens representing a query definition and constructs the appropriate query object to be added to the parser's query list. The method identifies the specific query type—such as satisfiability, subsumption, instance checking, or defuzzification—by examining the first token. It then instantiates the corresponding query class (e.g., `KbSatisfiableQuery`, `MaxSubsumesQuery`) using subsequent tokens as arguments, converting strings to concepts or individuals as needed. During this process, it performs validation checks, such as ensuring roles are not concrete for related queries and that features are defined for defuzzification operations, raising errors if these conditions are not met. Additionally, it may update the knowledge base's abstract roles set. The constructed query is appended to `DLParser.queries_list`.

      :param tokens: Parsed result containing the query keyword and its associated arguments (e.g., concepts, individuals, roles) used to construct a specific query object.
      :type tokens: list



   .. py:method:: _parse_restrictions() -> fuzzy_dl_owl2.fuzzydl.feature_function.FeatureFunction

      This method processes a list of tokens generated by the parser to construct `FeatureFunction` objects representing various restriction types. It first normalizes the input by flattening nested lists and then inspects the token count and content to determine the specific structure to build. For single tokens, it wraps the value directly; for pairs starting with a number, it creates a weighted feature function. For longer sequences, it identifies specific keywords—such as multiplication, subtraction, or summation—to construct composite feature functions involving the surrounding operands.

      :param tokens: The parsed tokens representing the components of a restriction expression, including operands and operators, used to construct FeatureFunction objects.
      :type tokens: list

      :return: A FeatureFunction instance constructed from the tokens based on detected operators or structure.

      :rtype: FeatureFunction



   .. py:method:: _parse_sigma_count_concept(tokens: list) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      Parses a sequence of tokens to construct a SigmaConcept, which represents a sigma count operation involving a specific role, concept, and set of individuals. The method extracts the role, the base concept, and a list of individuals from the input tokens, while the final token identifies a fuzzy concept used for the sigma count calculation. It performs validation to ensure the specified fuzzy concept exists in the knowledge base and is a concrete function type (specifically Left, Right, or Triangular), raising an error if these conditions are not met.

      :param tokens: The parsed output containing the role, concept, individuals, and fuzzy concept name required to construct a SigmaConcept.
      :type tokens: list

      :return: The `SigmaConcept` instance constructed from the parsed tokens.

      :rtype: Concept



   .. py:method:: _parse_term(tokens: list) -> fuzzy_dl_owl2.fuzzydl.milp.term.Term
      :staticmethod:


      This static method processes a parsed token sequence representing a single term within a mathematical expression and constructs a corresponding Term object. It handles two specific structures: a standalone variable name, which is interpreted as having an implicit coefficient of 1.0, and a triple consisting of a coefficient, an operator, and a variable name. In both cases, the variable string is resolved to a specific variable object via the MILP knowledge base associated with the parser.

      :param tokens: The parsed result containing the components of a mathematical term, representing either a single variable or a coefficient and variable pair.
      :type tokens: list

      :return: A Term instance representing the parsed coefficient and variable.

      :rtype: Term



   .. py:method:: _parse_threshold_concept(tokens: list) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      Parses a threshold concept definition from the provided tokens and constructs the corresponding concept object. The method expects a token list containing a comparison operator, a threshold value (which can be a numeric literal or a string representing a MILP variable), and a concept identifier. It converts the identifier to a Concept instance, validates that the concept is not abstract, and then instantiates either a standard ThresholdConcept or an ExtThresholdConcept based on the operator type and value type. If debug printing is enabled, the input tokens are logged to the console.

      :param tokens: The parsed elements of a threshold expression, structured as an operator, a threshold value (numeric or variable), and a concept.
      :type tokens: list

      :return: The ThresholdConcept or ExtThresholdConcept built from the threshold expression.

      :rtype: Concept



   .. py:method:: _parse_truth_constants(tokens: list) -> None
      :staticmethod:


      This static method serves as a semantic callback that processes tokens matched by a grammar rule for truth constants. It extracts the first two elements from the tokens and updates the class-level knowledge base by invoking `set_truth_constants` with these values. It assumes the input list contains at least two elements.

      :param tokens: The tokens containing the truth constant values to be set in the knowledge base.
      :type tokens: list



   .. py:method:: _parse_unary_concept(tokens: list) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      This static method processes a parsed unary concept expression, transforming raw tokens into a specific Concept object based on the operator provided. If the operator is a negation (NOT), it retrieves the operand concept, converts it to a Concept object, and returns its negation. If the operator is a self-reference (SELF), it validates that the associated role is not concrete, registers the role as abstract within the global knowledge base, and constructs a SelfConcept instance. The method modifies the global knowledge base by adding roles to the set of abstract roles when processing self-concepts, and it raises an error if a self-concept is applied to a concrete role.

      :param tokens: The parsed input containing the unary operator and the concept or role it modifies.
      :type tokens: list

      :return: The constructed unary concept, such as a negated concept or a self-concept.

      :rtype: Concept



   .. py:method:: _parse_weighted_concept(tokens: list) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      Parses a weighted concept expression from the provided tokens, expecting the first token to be an operator and subsequent tokens to be WeightedConcept instances. It extracts the weights and underlying concepts, then validates them based on the specific operator type: sum-based operators require the total weight to be less than or equal to 1.0, while min/max operators require the maximum weight to be exactly 1.0. If validation fails, an error is triggered via the utility function. Upon success, it returns the appropriate specialized concept object, such as WeightedSumConcept or WeightedMaxConcept.

      :param tokens: Tokens containing an operator keyword and a list of WeightedConcept objects to be combined.
      :type tokens: list

      :return: The constructed weighted concept (WeightedSumConcept, WeightedMaxConcept, WeightedMinConcept, or WeightedSumZeroConcept) based on the parsed operator.

      :rtype: Concept



   .. py:method:: _parse_weighted_concept_simple(tokens: list) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      This static method processes a sequence of parsed tokens to construct a WeightedConcept object, typically serving as a semantic callback. It extracts the first token as a floating-point weight and converts the second token into a Concept object using the `_to_concept` helper method. The method assumes the input tokens contain at least two elements and may output debug information if the debug flag is enabled.

      :param tokens: The parsed elements containing the weight and concept string, where the first element is the weight and the second is the concept.
      :type tokens: list

      :return: The constructed WeightedConcept instance.

      :rtype: Concept



   .. py:method:: _set_fuzzy_number(tokens: list) -> fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber
      :staticmethod:


      Processes a parsed fuzzy number definition to construct a TriangularFuzzyNumber instance and register it within the global knowledge base. The method supports direct assignment and arithmetic operations—specifically addition, subtraction, multiplication, and division—by resolving string identifiers in the input tokens to existing fuzzy number objects. It validates that the target name is unique, reporting an error if a fuzzy number with that name already exists. As a side effect, the method updates the knowledge base with the new definition and sets a flag indicating the presence of concrete fuzzy concepts.

      :param tokens: Parsed components of a fuzzy number definition, including the identifier, the defining expression (value or operator), and associated operands.
      :type tokens: list

      :return: The TriangularFuzzyNumber instance that was defined or calculated and added to the knowledge base.

      :rtype: TriangularFuzzyNumber



   .. py:method:: _show_abstract_fillers(tokens: list) -> None
      :staticmethod:


      Parses the tokens associated with a 'show-abstract-fillers' statement to update the MILP model's display configuration. The method iterates over the roles specified in the input, ensuring they are abstract; if a concrete role is detected, an error is raised and that specific role is ignored. Successfully validated abstract roles are registered within the knowledge base's MILP structure to be included in the variable output.

      :param tokens: Tokens containing the list of role identifiers extracted from the show-abstract-fillers statement.
      :type tokens: list



   .. py:method:: _show_abstract_fillers_for(tokens: list) -> None
      :staticmethod:


      Processes a parsed 'show-abstract-fillers-for' statement to configure the MILP model output. It validates that all specified roles are abstract; if a concrete role is found, an error is raised. Upon successful validation, it registers the variables representing the fillers of these roles for the given individual within the knowledge base's MILP display configuration.

      :param tokens: Tokens containing the abstract roles and individual name specified in the show-abstract-fillers-for statement.
      :type tokens: list



   .. py:method:: _show_concepts(tokens: list) -> None
      :staticmethod:


      This static method processes the tokens resulting from a "show-concepts" statement, extracting a list of individual names. It iterates through these names and updates the MILP model's configuration by adding each individual to the set of variables designated for display. The method includes debug logging if enabled.

      :param tokens: Tokens containing the list of individual identifiers to be displayed in the MILP model.
      :type tokens: list



   .. py:method:: _show_concrete_fillers(tokens: list) -> None
      :staticmethod:


      Processes the parsed tokens of a 'show-concrete-fillers' statement to update the MILP model's display configuration. It iterates through the provided tokens, treating each as a role identifier, and validates that the role exists in the knowledge base's set of concrete roles. If the role is valid, it is added to the list of variables to be shown in the MILP model; otherwise, an error is triggered indicating that only concrete roles are supported.

      :param tokens: The parsed tokens containing the concrete roles to be displayed in the MILP model.
      :type tokens: list



   .. py:method:: _show_concrete_fillers_for(tokens: list) -> None
      :staticmethod:


      Processes a parsed command to identify specific concrete role fillers associated with a given individual for display in the MILP model. The method extracts the individual name from the first token and iterates over the remaining tokens, treating them as role names. For each role, it verifies its existence within the knowledge base's set of concrete roles; if valid, it updates the MILP model's configuration to include the corresponding filler variable in the output. If a role is not concrete, an error is raised.

      :param tokens: The tokens containing the individual name followed by the list of concrete roles to display fillers for.
      :type tokens: list



   .. py:method:: _show_concrete_instance_for(tokens: list) -> None
      :staticmethod:


      This static method processes a parsed "show-concrete-instance-for" statement to update the MILP model's variable tracking configuration. It extracts the individual name, role, and a list of concept names from the input tokens, performing strict validation to ensure the role is defined as a concrete role and that the concepts are defined as concrete fuzzy concepts or fuzzy numbers within the knowledge base. If any validation fails, an error is raised. Upon success, it modifies the global knowledge base state by adding the specified concrete fillers to the list of variables to be displayed in the MILP model.

      :param tokens: Tokens containing the individual name, role, and concrete concepts specified in the statement.
      :type tokens: list



   .. py:method:: _show_instances(tokens: list) -> None
      :staticmethod:


      This static method processes a 'show-instances' statement by extracting the specified concepts from the tokens and registering them for display within the MILP model. It iterates through the provided tokens, converting each item into a Concept object and adding it to the model's configuration of variables to show. This operation has a side effect of modifying the internal state of the knowledge base's MILP solver to ensure the instances of these concepts are tracked.

      :param tokens: Tokens from a show-instances statement, containing the concepts to be added to the MILP display list.
      :type tokens: list



   .. py:method:: _show_languages(tokens: list) -> None
      :staticmethod:


      This static method serves as a semantic callback for a "show-languages" statement, modifying the state of the global knowledge base to indicate that language information should be displayed. It sets the `show_language` attribute of the `DLParser` knowledge base to `True`. Additionally, if debug mode is active, it logs the input tokens for troubleshooting purposes.

      :param tokens: The tokens representing the show-languages statement.
      :type tokens: list



   .. py:method:: _show_variables(tokens: list) -> None
      :staticmethod:


      Processes the parsed tokens of a show-variables statement to identify and register specific variables for display. It iterates through the list of variable names contained in the input tokens, retrieves the corresponding `Variable` objects from the MILP model, and adds them to the model's collection of variables to show. This method modifies the state of the MILP model's `show_vars` attribute and assumes that all provided variable names exist within the current model context.

      :param tokens: The tokens containing the list of variable names extracted from the show-variables statement.
      :type tokens: list



   .. py:method:: _to_concept(c: Union[str, fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      This static method ensures that the provided argument is returned as a Concept object, handling both string identifiers and existing Concept instances. If the input is already a Concept, it is returned unchanged; otherwise, the method treats the input as a string and attempts to retrieve the corresponding Concept from the parser's knowledge base. The operation includes a side effect of printing debug information if debug mode is enabled.

      :param c: A string identifier or Concept object to be resolved into a Concept instance.
      :type c: typing.Union[str, Concept]

      :return: The Concept object corresponding to the input string, or the input object itself if it is already a Concept.

      :rtype: Concept



   .. py:method:: _to_number(tokens: list) -> float | int
      :staticmethod:


      Converts the first element of the provided parse results into a numeric type, prioritizing integers when appropriate. The method extracts the initial token, ensures it is a string, and attempts to parse it as a floating-point number. If the parsed value is mathematically an integer, it is returned as an `int`; otherwise, it is returned as a `float`. This function assumes the input token represents a valid numeric string and will raise a `ValueError` if the conversion fails.

      :param tokens: The parsed results containing the string representation of the number to be converted.
      :type tokens: list

      :return: The numeric representation of the input token, returned as an int if the value is a whole number, or as a float otherwise.

      :rtype: float | int



   .. py:method:: _to_top_bottom_concept(tokens: list) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      Transforms the provided parse results into a specific concept object based on the content of the first token. If the token corresponds to the 'TOP' keyword, the method returns the universal truth concept; if it corresponds to 'BOTTOM', it returns the empty truth concept. For any other token, the method delegates the conversion to the internal `_to_concept` method to generate a standard Description Logic concept. The method may output debug information depending on the global configuration settings.

      :param tokens: Parsed results containing a keyword or identifier representing a top, bottom, or regular concept.
      :type tokens: list

      :return: A Concept object representing the Top concept, Bottom concept, or a regular concept derived from the input tokens.

      :rtype: Concept



   .. py:method:: load_config(**kwargs) -> None
      :staticmethod:


      This static method acts as a wrapper to load specific configuration parameters from a predefined INI file located in the current working directory. It constructs the file path for 'CONFIG.ini' and delegates the actual parsing and parameter extraction to the `ConfigReader` class, passing along the provided arguments to determine which specific settings to retrieve. The function relies on the presence of the configuration file in the file system and triggers side effects within the `ConfigReader` rather than returning a value directly. By accepting a variable length argument list, it allows for selective loading of configuration data based on the caller's needs.

      :param kwargs: Keys specifying which configuration parameters to load from the file.
      :type kwargs: typing.Any



   .. py:attribute:: kb
      :type:  fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase
      :value: None



   .. py:attribute:: queries_list
      :type:  list[fuzzy_dl_owl2.fuzzydl.query.query.Query]
      :value: []


