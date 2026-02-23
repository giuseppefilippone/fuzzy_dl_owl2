fuzzy_dl_owl2.fuzzydl.parser.dl_parser
======================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.parser.dl_parser



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized parser for Fuzzy Description Logic that interprets textual input to construct a knowledge base and a set of executable queries using the pyparsing library.


Description
-----------


The software defines a comprehensive grammar for a Fuzzy Description Logic language, enabling the interpretation of complex constructs such as fuzzy concepts, modifiers, roles, and axioms. It utilizes the pyparsing library to define syntax rules and parse actions that transform raw string tokens into domain-specific objects, including concepts, individuals, and various query types. During the parsing process, the system validates semantic constraints, such as ensuring abstract concepts are not used where concrete ones are required and enforcing logic-specific rules for operators like conjunction and implication. The parser populates a central ``KnowledgeBase`` instance with the interpreted data and accumulates a list of queries, which can subsequently be solved to perform reasoning tasks like subsumption checking, instance retrieval, and satisfiability analysis. By supporting multiple fuzzy logic semantics, including Zadeh and Lukasiewicz, the implementation provides a flexible framework for defining and reasoning about fuzzy ontologies.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.dl_parser.FILENAME
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser.LOG_DIR
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser.TODAY


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.dl_parser.DLParser


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_dl_parser_DLParser.png
       :alt: UML Class Diagram for DLParser
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **DLParser**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_dl_parser_DLParser.pdf
       :alt: UML Class Diagram for DLParser
       :align: center
       :width: 12.7cm
       :class: uml-diagram

       UML Class Diagram for **DLParser**

.. py:class:: DLParser

   Bases: :py:obj:`object`


   This class serves as a specialized parser for Fuzzy Description Logic, designed to interpret textual input and construct a corresponding knowledge base and set of queries. It utilizes the `pyparsing` library to define a comprehensive grammar that covers various fuzzy logic constructs, including concepts, roles, modifiers, axioms, and complex query types. The parser operates primarily through static methods that act as callbacks during the parsing process, transforming raw string tokens into domain-specific objects such as `Concept`, `Individual`, and `Degree` instances. Users typically interact with this class by calling the `get_kb` method, which accepts a file path, initializes the internal state, parses the file content, and returns the populated `KnowledgeBase` and a list of `Query` objects. The class handles semantic validation and logic-specific constraints (e.g., distinguishing between Zadeh and Lukasiewicz logic) during parsing, ensuring that the constructed knowledge base adheres to the specified fuzzy logic semantics. Additionally, it provides a `main` entry point to execute the parsing, solve the knowledge base, and process the resulting queries sequentially.

   :param kb: The KnowledgeBase instance constructed and populated by the parser with the parsed domain model.
   :type kb: KnowledgeBase
   :param queries_list: Accumulates Query objects extracted from the input during parsing, which are subsequently returned for execution against the knowledge base.
   :type queries_list: list[Query]


   .. py:method:: _check_abstract(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None
      :staticmethod:


      Validates that the provided `Concept` instance is abstract, ensuring it is not marked as concrete. If the concept is determined to be concrete, this method triggers an error reporting routine to signal a violation of the expected schema. This static method serves as a guard clause within the parsing logic to enforce structural constraints.

      :param c: The concept to validate as abstract.
      :type c: Concept



   .. py:method:: _create_fuzzy_number(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method processes parse tokens to construct a `TriangularFuzzyNumber` instance, supporting multiple input formats. If a single numeric value is provided, it generates a crisp fuzzy number where the lower, middle, and upper bounds are equal. When a string identifier is encountered, the method retrieves the corresponding fuzzy number from the knowledge base; if the identifier is undefined, an error is triggered. If three numeric values are present, they are interpreted as the lower, middle, and upper bounds of the triangular distribution. Should the input not conform to these patterns, the original tokens are returned unchanged. The method also outputs debug information if the global debug flag is enabled.

      :param tokens: The parsed elements representing a fuzzy number, which can be a single numeric value, a string identifier referencing a predefined number, or a list of three numeric values.
      :type tokens: pp.ParseResults

      :return: A ParseResults object wrapping a TriangularFuzzyNumber instance derived from the input tokens, or the original tokens if they cannot be parsed.

      :rtype: pp.ParseResults



   .. py:method:: _fuzzy_logic_parser(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method acts as a parsing action to process and apply a specified fuzzy logic type to the system. It extracts the first token from the parse results, converts it to a lowercase string, and instantiates a corresponding FuzzyLogic object. The method then updates the Knowledge Base associated with the parser by setting this logic, effectively configuring the reasoning engine for the session. It returns the original tokens unchanged, assuming the input grammar guarantees the presence of at least one token to define the logic.

      :param tokens: The parse results containing the identifier for the fuzzy logic type to be applied to the knowledge base.
      :type tokens: pp.ParseResults

      :return: The original parse results containing the fuzzy logic identifier.

      :rtype: pp.ParseResults



   .. py:method:: _get_modifier(m: str) -> fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier
      :staticmethod:


      Retrieves a `Modifier` object from the shared knowledge base corresponding to the given string name. This method verifies that the modifier is defined; if the knowledge base is uninitialized or the name is not found, it invokes an error handling routine to signal the issue. Furthermore, it outputs debug logging details if the debug print configuration is active.

      :param m: The name of the modifier to retrieve from the knowledge base.
      :type m: str

      :return: The `Modifier` object associated with the specified name.

      :rtype: Modifier



   .. py:method:: _parse_axioms(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Processes a list of parsed tokens representing Description Logic axioms and updates the global knowledge base accordingly. The method inspects the leading keyword to dispatch specific logic for various axiom types, including individual assertions, role relations, concept implications (supporting multiple fuzzy logic semantics such as Goedel, Lukasiewicz, and Zadeh), concept definitions, and disjointness constraints. Additionally, it manages role characteristics like domain, range, transitivity, symmetry, and inverse relationships, performing validation to ensure concrete roles are not used in invalid contexts. Fuzzy degrees are applied to assertions and implications where provided, defaulting to 1.0 otherwise. The method returns the original tokens to facilitate parsing pipeline continuity.

      :param tokens: The parsed result containing the axiom keyword and its associated arguments (e.g., concepts, individuals, roles) to be processed and added to the knowledge base.
      :type tokens: pp.ParseResults

      :return: The original parsed tokens, returned unchanged after updating the knowledge base.

      :rtype: pp.ParseResults



   .. py:method:: _parse_binary_concept(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Parses a binary or n-ary concept expression from the provided parse results, identifying the specific operation based on the first token. The method handles a variety of logical constructs, including conjunctions, disjunctions, implications, quantifiers, value restrictions, and approximation operators, dynamically selecting the appropriate implementation (e.g., Lukasiewicz, Goedel, or Zadeh) based on the current fuzzy logic setting in the knowledge base. It validates that operands are abstract concepts, ensures referenced roles and individuals exist, and enforces logic-specific constraints by raising errors if fuzzy-specific operators are used within a classical logic context. If the operator token is already a Concept object, the method returns the input tokens unchanged.

      :param tokens: The parsed structure containing the operator and operands for the binary concept.
      :type tokens: pp.ParseResults

      :return: A ParseResults object containing the specific Concept instance (e.g., OperatorConcept, ImpliesConcept) constructed from the input tokens.

      :rtype: pp.ParseResults



   .. py:method:: _parse_constraints(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method processes parsed tokens to apply variable constraints to the Mixed-Integer Linear Programming (MILP) model associated with the parser's knowledge base. It examines the first token to identify the constraint type; if the token indicates a binary or free variable, the method retrieves the corresponding variable object by name and updates its type definition. The function returns the original tokens unchanged, functioning as a parsing action that modifies the global model state rather than transforming the data stream.

      :param tokens: Parsed results containing the constraint definition, used to extract the variable type and identifier for updating the MILP model.
      :type tokens: pp.ParseResults

      :return: The input ParseResults object, returned unchanged.

      :rtype: pp.ParseResults



   .. py:method:: _parse_crisp_declarations(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method processes parsed tokens to identify and handle crisp declarations for either concepts or roles. Based on the leading keyword in the token list, it iterates through the remaining identifiers to update the global knowledge base. If the declaration targets concepts, it converts the identifiers to Concept objects and registers them as crisp; if it targets roles, it registers the role identifiers directly. The operation modifies the state of the knowledge base and returns the original tokens unchanged.

      :param tokens: The parsed results containing the declaration type keyword followed by the identifiers of the concepts or roles to be marked as crisp.
      :type tokens: pp.ParseResults

      :return: The ParseResults object containing the parsed crisp declaration tokens.

      :rtype: pp.ParseResults



   .. py:method:: _parse_datatype_restriction(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method processes a datatype restriction from the provided parse results, determining the restriction type (such as exact, at most, or at least) based on the operator token and identifying the associated concrete feature role. It validates that the role has been previously defined in the knowledge base and ensures that any triangular fuzzy numbers used have a defined range before proceeding. Depending on the value token's type, the method resolves strings to either existing fuzzy number concepts or new continuous variables, and handles triangular fuzzy numbers by extracting their crisp or fuzzy representations. The constructed restriction is then added to the global knowledge base, and the method returns a ParseResults object containing the added entity.

      :param tokens: The parsed components of the datatype restriction, containing the operator, the feature role, and the value or concept.
      :type tokens: pp.ParseResults

      :return: A ParseResults object containing the datatype restriction object that was added to the knowledge base.

      :rtype: pp.ParseResults



   .. py:method:: _parse_degree(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Converts raw parsing tokens into specific semantic Degree objects based on the type of the first token found in the input. If the token is a numeric value, the method returns a `DegreeNumeric` object; if it is an `Expression` instance, it returns a `DegreeExpression` object. For string tokens, the method consults the knowledge base to check for a defined truth constant, returning a `DegreeNumeric` if a match is found, or otherwise treating the string as a variable name to retrieve and return a `DegreeVariable`. The resulting object is wrapped in a `pp.ParseResults` container to ensure compatibility with the parsing pipeline, and debug information may be logged if enabled.

      :param tokens: The parsed output containing the raw degree data, expected to be a numeric value, an expression, or a variable name.
      :type tokens: pp.ParseResults

      :return: A ParseResults object containing the specific Degree instance (Numeric, Expression, or Variable) derived from the input tokens.

      :rtype: pp.ParseResults



   .. py:method:: _parse_expression(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Converts raw parsing results into a structured Expression object, specifically handling the construction of additive expressions. The method first normalizes the input by unwrapping nested list structures. If the resulting list contains a single Term, it wraps that term in an Expression; if it contains a sequence of Terms separated by addition operators, it aggregates them into a single Expression. If the token structure does not match these expected patterns, the original tokens are returned unchanged.

      :param tokens: The raw parsing result containing the terms and operators that constitute the expression.
      :type tokens: pp.ParseResults

      :return: A ParseResults object containing the constructed Expression if the tokens represent a valid single term or sum of terms, otherwise the original tokens.

      :rtype: pp.ParseResults



   .. py:method:: _parse_feature(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Processes a parsed feature definition to register a concrete feature within the global knowledge base. It inspects the provided token list to identify the feature's role and data type, dispatching to the appropriate definition method—such as defining integer or real ranges, or boolean and string types. This method mutates the knowledge base state by adding the new feature definition and returns the original tokens to allow the parsing process to continue.

      :param tokens: The parsed components of a feature definition, including the role name, data type, and optional numeric bounds.
      :type tokens: pp.ParseResults

      :return: A ParseResults object containing the list of tokens parsed from the feature definition.

      :rtype: pp.ParseResults



   .. py:method:: _parse_fuzzy_concept(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Parses a fuzzy concept definition from the provided tokens and registers the corresponding concrete concept object in the global knowledge base. The method validates that the concept name is not already defined and ensures that non-crisp concept types are not used with a classical reasoner. Depending on the keyword found in the tokens, it instantiates a specific concept class—such as `CrispConcreteConcept`, `TriangularConcreteConcept`, or `ModifiedConcreteConcept`—using the extracted parameters. For modified concepts, it verifies that the base concept exists prior to creation. As a side effect, adding a non-crisp concept sets a flag in the knowledge base indicating the presence of concrete fuzzy concepts. The original tokens are returned to allow parsing to continue.

      :param tokens: Parsed results containing the fuzzy concept definition, including the concept name, type keyword, and associated parameters or references.
      :type tokens: pp.ParseResults

      :return: The original ParseResults object, returned after adding the fuzzy concept to the knowledge base.

      :rtype: pp.ParseResults



   .. py:method:: _parse_fuzzy_equivalence(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Processes the parsed tokens corresponding to a fuzzy equivalence relation and updates the global knowledge base accordingly. This static method extracts the primary identifier from the token list and invokes the knowledge base's `add_equivalence_relation` method to register the relation. While it returns the original tokens to facilitate continued parsing, its primary effect is the mutation of the shared `DLParser.kb` state.

      :param tokens: The parsed results containing the fuzzy equivalence relation to be added to the knowledge base.
      :type tokens: pp.ParseResults

      :return: The original `ParseResults` object containing the fuzzy equivalence relation tokens.

      :rtype: pp.ParseResults



   .. py:method:: _parse_fuzzy_number_range(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Extracts the lower and upper bounds from the provided parsing tokens to configure the range for triangular fuzzy numbers. This static method converts the input `ParseResults` into a list and invokes the `TriangularFuzzyNumber.set_range` method with the first two elements, resulting in a side effect that updates the class-level state. It returns the token list wrapped in a new `ParseResults` object, assuming the input contains at least two elements to define the range boundaries.

      :param tokens: The parsed results containing the values that define the fuzzy number range.
      :type tokens: pp.ParseResults

      :return: A pyparsing ParseResults object containing the parsed tokens representing the fuzzy number range.

      :rtype: pp.ParseResults



   .. py:method:: _parse_fuzzy_similarity(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method processes a fuzzy similarity relation identified during the parsing phase. It extracts the primary identifier from the provided parse results and adds it to the parser's knowledge base as a similarity relation. The method returns the original tokens unchanged, serving primarily as a side-effect trigger that updates the internal state of the knowledge base.

      :param tokens: The parsed results containing the fuzzy similarity relation data extracted from the input string.
      :type tokens: pp.ParseResults

      :return: The original ParseResults object containing the parsed tokens.

      :rtype: pp.ParseResults



   .. py:method:: _parse_inequation(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Processes a set of parsing tokens representing an inequation to construct a formal constraint and update the underlying mathematical model. If the tokens contain a valid expression followed by an operator and a constant, the method normalizes the expression by subtracting the constant and determines the specific inequality type based on the operator string. It then registers this constraint within the MILP model associated with the current knowledge base. The method returns a ParseResults object wrapping the newly created Inequation instance; if the input does not start with an Expression, the tokens are returned unmodified.

      :param tokens: The parsed components of the inequation, consisting of an expression, a comparison operator, and a constant value.
      :type tokens: pp.ParseResults

      :return: A ParseResults object wrapping the parsed Inequation instance. If the input tokens do not represent a valid expression, the original tokens are returned.

      :rtype: pp.ParseResults



   .. py:method:: _parse_modifier(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method processes a parsed modifier definition by extracting the modifier type and parameters from the provided tokens. It distinguishes between linear and triangular modifiers based on the specific keyword present, instantiating the corresponding `LinearModifier` or `TriangularModifier` object with the extracted arguments. The constructed modifier is then registered with the global knowledge base (`DLParser.kb`), effectively updating the application's state. The method returns the original tokens unchanged, but assumes the input list contains sufficient elements for the specific modifier type, potentially raising an error if the token structure is invalid.

      :param tokens: The parsed components of a modifier definition, including the name, type keyword, and associated parameters.
      :type tokens: pp.ParseResults

      :return: The original input tokens, returned unchanged.

      :rtype: pp.ParseResults



   .. py:method:: _parse_modifier_concept(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method processes a sequence of tokens representing a modifier applied to a concept, expecting the input list to contain exactly two elements. It extracts the modifier from the first token and the base concept from the second, resolving them into their respective object instances. The method then applies the modification logic to the concept and returns the resulting modified concept encapsulated within a `pp.ParseResults` object.

      :param tokens: The parsed tokens containing the modifier and concept components to be combined.
      :type tokens: pp.ParseResults

      :return: A ParseResults object containing the Concept resulting from applying the parsed Modifier to the parsed Concept.

      :rtype: pp.ParseResults



   .. py:method:: _parse_owa_integral_concept(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Parses a fuzzy logic integral concept—specifically OWA, Choquet, Sugeno, or Q-Sugeno—from the provided parse results. The method extracts the operator from the first token and divides the remaining tokens into two equal lists representing weights and concepts, converting the latter into `Concept` objects. It performs validation on the weights, ensuring they sum to 1.0 for OWA operators and that the maximum weight is 1.0 for Choquet, Sugeno, and Q-Sugeno operators, reporting an error if these conditions are not met. The result is returned as a `pp.ParseResults` object wrapping the appropriate specialized concept instance.

      :param tokens: The parsed results containing the integral operator, associated weights, and the list of concepts to be aggregated.
      :type tokens: pp.ParseResults

      :return: A ParseResults object wrapping the specific integral concept instance (OwaConcept, ChoquetIntegral, SugenoIntegral, or QsugenoIntegral) parsed from the input tokens.

      :rtype: pp.ParseResults



   .. py:method:: _parse_q_owa_concept(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method processes a sequence of tokens to construct a Quantified OWA (Ordered Weighted Averaging) concept. It interprets the first token as the name of a fuzzy concrete concept, retrieving it from the knowledge base to serve as the aggregation function. The method enforces strict type checking, ensuring the retrieved function is either a `RightConcreteConcept` or `LeftConcreteConcept`, and triggers an error if the concept is undefined or of an incorrect type. Subsequent tokens are recursively parsed into standard `Concept` objects to serve as arguments. Finally, it returns a `ParseResults` object containing the fully initialized `QowaConcept`.

      :param tokens: Parsed results representing the components of a Q-OWA concept, comprising a fuzzy aggregation function identifier and a list of concepts to aggregate.
      :type tokens: pp.ParseResults

      :return: A ParseResults object containing the constructed QowaConcept instance.

      :rtype: pp.ParseResults



   .. py:method:: _parse_queries(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Parses a list of tokens representing a query definition and constructs the appropriate query object to be added to the parser's query list. The method identifies the specific query type—such as satisfiability, subsumption, instance checking, or defuzzification—by examining the first token. It then instantiates the corresponding query class (e.g., `KbSatisfiableQuery`, `MaxSubsumesQuery`) using subsequent tokens as arguments, converting strings to concepts or individuals as needed. During this process, it performs validation checks, such as ensuring roles are not concrete for related queries and that features are defined for defuzzification operations, raising errors if these conditions are not met. Additionally, it may update the knowledge base's abstract roles set. The method returns the original input tokens to facilitate further parsing.

      :param tokens: Parsed result containing the query keyword and its associated arguments (e.g., concepts, individuals, roles) used to construct a specific query object.
      :type tokens: pp.ParseResults

      :return: The original ParseResults object containing the query tokens.

      :rtype: pp.ParseResults



   .. py:method:: _parse_restrictions() -> Any

      This method processes a list of tokens generated by the parser to construct `FeatureFunction` objects representing various restriction types. It first normalizes the input by flattening nested lists and then inspects the token count and content to determine the specific structure to build. For single tokens, it wraps the value directly; for pairs starting with a number, it creates a weighted feature function. For longer sequences, it identifies specific keywords—such as multiplication, subtraction, or summation—to construct composite feature functions involving the surrounding operands. If the token structure does not match any of these defined patterns, the method returns the original tokens wrapped in a `ParseResults` object.

      :param tokens: The parsed tokens representing the components of a restriction expression, including operands and operators, used to construct FeatureFunction objects.
      :type tokens: pp.ParseResults

      :return: A pp.ParseResults object wrapping a FeatureFunction instance constructed from the tokens based on detected operators or structure, or the original tokens if no specific restriction pattern is identified.

      :rtype: typing.Any



   .. py:method:: _parse_sigma_count_concept(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Parses a sequence of tokens to construct a SigmaConcept, which represents a sigma count operation involving a specific role, concept, and set of individuals. The method extracts the role, the base concept, and a list of individuals from the input tokens, while the final token identifies a fuzzy concept used for the sigma count calculation. It performs validation to ensure the specified fuzzy concept exists in the knowledge base and is a concrete function type (specifically Left, Right, or Triangular), raising an error if these conditions are not met. The resulting SigmaConcept object is then wrapped in a ParseResults object and returned.

      :param tokens: The parsed output containing the role, concept, individuals, and fuzzy concept name required to construct a SigmaConcept.
      :type tokens: pp.ParseResults

      :return: A `pp.ParseResults` object containing the `SigmaConcept` instance constructed from the parsed tokens.

      :rtype: pp.ParseResults



   .. py:method:: _parse_term(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method processes a parsed token sequence representing a single term within a mathematical expression and constructs a corresponding Term object. It handles two specific structures: a standalone variable name, which is interpreted as having an implicit coefficient of 1.0, and a triple consisting of a coefficient, an operator, and a variable name. In both cases, the variable string is resolved to a specific variable object via the MILP knowledge base associated with the parser. The resulting Term object is wrapped in a pp.ParseResults container to maintain compatibility with the parsing framework.

      :param tokens: The parsed result containing the components of a mathematical term, representing either a single variable or a coefficient and variable pair.
      :type tokens: pp.ParseResults

      :return: A ParseResults object wrapping a Term instance representing the parsed coefficient and variable, or the original tokens if the input structure is unexpected.

      :rtype: pp.ParseResults



   .. py:method:: _parse_threshold_concept(tokens: pyparsing.ParseResults)
      :staticmethod:


      Parses a threshold concept definition from the provided parse results tokens and constructs the corresponding concept object. The method expects a token list containing a comparison operator, a threshold value (which can be a numeric literal or a string representing a MILP variable), and a concept identifier. It converts the identifier to a Concept instance, validates that the concept is not abstract, and then instantiates either a standard ThresholdConcept or an ExtThresholdConcept based on the operator type and value type. The resulting object is wrapped in a ParseResults container and returned. If debug printing is enabled, the input tokens are logged to the console.

      :param tokens: The parsed elements of a threshold expression, structured as an operator, a threshold value (numeric or variable), and a concept.
      :type tokens: pp.ParseResults



   .. py:method:: _parse_truth_constants(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method serves as a parsing action callback that processes tokens matched by a grammar rule for truth constants. It extracts the first two elements from the input `ParseResults` and updates the class-level knowledge base by invoking `set_truth_constants` with these values. The function returns the original tokens unchanged, allowing the parsing process to continue, though it assumes the input list contains at least two elements.

      :param tokens: The parsed results containing the truth constant values to be set in the knowledge base.
      :type tokens: pp.ParseResults

      :return: The input ParseResults object containing the parsed tokens.

      :rtype: pp.ParseResults



   .. py:method:: _parse_unary_concept(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method processes a parsed unary concept expression, transforming raw tokens into a specific Concept object based on the operator provided. If the operator is a negation (NOT), it retrieves the operand concept, converts it to a Concept object, and returns its negation. If the operator is a self-reference (SELF), it validates that the associated role is not concrete, registers the role as abstract within the global knowledge base, and constructs a SelfConcept instance. The method modifies the global knowledge base by adding roles to the set of abstract roles when processing self-concepts, and it raises an error if a self-concept is applied to a concrete role.

      :param tokens: The parsed input containing the unary operator and the concept or role it modifies.
      :type tokens: pp.ParseResults

      :return: A ParseResults object containing the constructed unary concept, such as a negated concept or a self-concept, or the original tokens.

      :rtype: pp.ParseResults



   .. py:method:: _parse_weighted_concept(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Parses a weighted concept expression from the provided parse results, expecting the first token to be an operator and subsequent tokens to be WeightedConcept instances. It extracts the weights and underlying concepts, then validates them based on the specific operator type: sum-based operators require the total weight to be less than or equal to 1.0, while min/max operators require the maximum weight to be exactly 1.0. If validation fails, an error is triggered via the utility function. Upon success, it returns a new ParseResults object containing the appropriate specialized concept object, such as WeightedSumConcept or WeightedMaxConcept.

      :param tokens: Parse results containing an operator keyword and a list of WeightedConcept objects to be combined.
      :type tokens: pp.ParseResults

      :return: A ParseResults object wrapping the constructed weighted concept (WeightedSumConcept, WeightedMaxConcept, WeightedMinConcept, or WeightedSumZeroConcept) based on the parsed operator.

      :rtype: pp.ParseResults



   .. py:method:: _parse_weighted_concept_simple(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method processes a sequence of parsed tokens to construct a WeightedConcept object, typically serving as a parsing action callback. It extracts the first token as a floating-point weight and converts the second token into a Concept object using the `_to_concept` helper method. The resulting WeightedConcept instance is then wrapped in a ParseResults object and returned. The method assumes the input tokens contain at least two elements and may output debug information if the debug flag is enabled.

      :param tokens: The parsed elements containing the weight and concept string, where the first element is the weight and the second is the concept.
      :type tokens: pp.ParseResults

      :return: A ParseResults object containing the constructed WeightedConcept instance.

      :rtype: pp.ParseResults



   .. py:method:: _set_fuzzy_number(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Processes a parsed fuzzy number definition to construct a TriangularFuzzyNumber instance and register it within the global knowledge base. The method supports direct assignment and arithmetic operations—specifically addition, subtraction, multiplication, and division—by resolving string identifiers in the input tokens to existing fuzzy number objects. It validates that the target name is unique, reporting an error if a fuzzy number with that name already exists. As a side effect, the method updates the knowledge base with the new definition and sets a flag indicating the presence of concrete fuzzy concepts. The resulting TriangularFuzzyNumber is returned wrapped in a ParseResults object.

      :param tokens: Parsed components of a fuzzy number definition, including the identifier, the defining expression (value or operator), and associated operands.
      :type tokens: pp.ParseResults

      :return: A ParseResults object containing the TriangularFuzzyNumber instance that was defined or calculated and added to the knowledge base.

      :rtype: pp.ParseResults



   .. py:method:: _show_abstract_fillers(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Parses the tokens associated with a 'show-abstract-fillers' statement to update the MILP model's display configuration. The method iterates over the roles specified in the input, ensuring they are abstract; if a concrete role is detected, an error is raised and that specific role is ignored. Successfully validated abstract roles are registered within the knowledge base's MILP structure to be included in the variable output.

      :param tokens: Parsed results containing the list of role identifiers extracted from the show-abstract-fillers statement.
      :type tokens: pp.ParseResults

      :return: The input tokens, returned to satisfy the pyparsing parse action contract.

      :rtype: pp.ParseResults



   .. py:method:: _show_abstract_fillers_for(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Processes a parsed 'show-abstract-fillers-for' statement to configure the MILP model output. It validates that all specified roles are abstract; if a concrete role is found, an error is raised. Upon successful validation, it registers the variables representing the fillers of these roles for the given individual within the knowledge base's MILP display configuration.

      :param tokens: Parsed result containing the abstract roles and individual name specified in the show-abstract-fillers-for statement.
      :type tokens: pp.ParseResults

      :return: The original ParseResults object containing the parsed tokens.

      :rtype: pp.ParseResults



   .. py:method:: _show_concepts(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method processes the tokens resulting from a "show-concepts" statement, extracting a list of individual names. It iterates through these names and updates the MILP model's configuration by adding each individual to the set of variables designated for display. The method returns the original tokens unchanged to facilitate parsing pipeline chaining and includes debug logging if enabled.

      :param tokens: Parsed results containing the list of individual identifiers to be displayed in the MILP model.
      :type tokens: pp.ParseResults

      :return: The input ParseResults object containing the list of individual names to show.

      :rtype: pp.ParseResults



   .. py:method:: _show_concrete_fillers(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Processes the parsed tokens of a 'show-concrete-fillers' statement to update the MILP model's display configuration. It iterates through the provided tokens, treating each as a role identifier, and validates that the role exists in the knowledge base's set of concrete roles. If the role is valid, it is added to the list of variables to be shown in the MILP model; otherwise, an error is triggered indicating that only concrete roles are supported. The method returns the original tokens to facilitate parsing pipeline continuity.

      :param tokens: The parsed tokens containing the concrete roles to be displayed in the MILP model.
      :type tokens: pp.ParseResults

      :return: The original ParseResults object containing the parsed tokens.

      :rtype: pp.ParseResults



   .. py:method:: _show_concrete_fillers_for(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Processes a parsed command to identify specific concrete role fillers associated with a given individual for display in the MILP model. The method extracts the individual name from the first token and iterates over the remaining tokens, treating them as role names. For each role, it verifies its existence within the knowledge base's set of concrete roles; if valid, it updates the MILP model's configuration to include the corresponding filler variable in the output. If a role is not concrete, an error is raised. The original tokens are returned to satisfy parsing requirements.

      :param tokens: The parsed results containing the individual name followed by the list of concrete roles to display fillers for.
      :type tokens: pp.ParseResults

      :return: The original ParseResults object passed as input.

      :rtype: pp.ParseResults



   .. py:method:: _show_concrete_instance_for(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method processes a parsed "show-concrete-instance-for" statement to update the MILP model's variable tracking configuration. It extracts the individual name, role, and a list of concept names from the input tokens, performing strict validation to ensure the role is defined as a concrete role and that the concepts are defined as concrete fuzzy concepts or fuzzy numbers within the knowledge base. If any validation fails, an error is raised. Upon success, it modifies the global knowledge base state by adding the specified concrete fillers to the list of variables to be displayed in the MILP model. The original tokens are returned to facilitate further parsing steps.

      :param tokens: Parsed results containing the individual name, role, and concrete concepts specified in the statement.
      :type tokens: pp.ParseResults

      :return: The ParseResults object containing the parsed tokens for the show-concrete-instance-for statement.

      :rtype: pp.ParseResults



   .. py:method:: _show_instances(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method processes a 'show-instances' statement by extracting the specified concepts from the parse results and registering them for display within the MILP model. It iterates through the provided tokens, converting each item into a Concept object and adding it to the model's configuration of variables to show. This operation has a side effect of modifying the internal state of the knowledge base's MILP solver to ensure the instances of these concepts are tracked. The method returns the original tokens unchanged, allowing the parsing process to continue.

      :param tokens: Parsed results from a show-instances statement, containing the concepts to be added to the MILP display list.
      :type tokens: pp.ParseResults

      :return: The original ParseResults object containing the tokens for the show-instances statement.

      :rtype: pp.ParseResults



   .. py:method:: _show_languages(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      This static method serves as a parsing action for a "show-languages" statement, modifying the state of the global knowledge base to indicate that language information should be displayed. It sets the `show_language` attribute of the `DLParser` knowledge base to `True`. Additionally, if debug mode is active, it logs the input tokens for troubleshooting purposes. The method returns the original tokens unchanged to allow the parsing process to continue.

      :param tokens: The parsed results representing the show-languages statement.
      :type tokens: pp.ParseResults

      :return: The ParseResults object containing the parsed tokens from the show-languages statement.

      :rtype: pp.ParseResults



   .. py:method:: _show_variables(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Processes the parsed tokens of a show-variables statement to identify and register specific variables for display. It iterates through the list of variable names contained in the input tokens, retrieves the corresponding `Variable` objects from the MILP model, and adds them to the model's collection of variables to show. This method modifies the state of the MILP model's `show_vars` attribute and assumes that all provided variable names exist within the current model context. The original tokens are returned unchanged to support parsing pipeline continuity.

      :param tokens: The parsed results containing the list of variable names extracted from the show-variables statement.
      :type tokens: pp.ParseResults

      :return: The parsed tokens representing the show-variables statement.

      :rtype: pp.ParseResults



   .. py:method:: _to_concept(c: Union[str, fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      This static method ensures that the provided argument is returned as a Concept object, handling both string identifiers and existing Concept instances. If the input is already a Concept, it is returned unchanged; otherwise, the method treats the input as a string and attempts to retrieve the corresponding Concept from the parser's knowledge base. The operation includes a side effect of printing debug information if debug mode is enabled.

      :param c: A string identifier or Concept object to be resolved into a Concept instance.
      :type c: typing.Union[str, Concept]

      :return: The Concept object corresponding to the input string, or the input object itself if it is already a Concept.

      :rtype: Concept



   .. py:method:: _to_number(tokens: pyparsing.ParseResults) -> float | int
      :staticmethod:


      Converts the first element of the provided parse results into a numeric type, prioritizing integers when appropriate. The method extracts the initial token, ensures it is a string, and attempts to parse it as a floating-point number. If the parsed value is mathematically an integer, it is returned as an `int`; otherwise, it is returned as a `float`. This function assumes the input token represents a valid numeric string and will raise a `ValueError` if the conversion fails.

      :param tokens: The parsed results containing the string representation of the number to be converted.
      :type tokens: pp.ParseResults

      :return: The numeric representation of the input token, returned as an int if the value is a whole number, or as a float otherwise.

      :rtype: float | int



   .. py:method:: _to_top_bottom_concept(tokens: pyparsing.ParseResults) -> pyparsing.ParseResults
      :staticmethod:


      Transforms the provided parse results into a specific concept object based on the content of the first token. If the token corresponds to the 'TOP' keyword, the method returns the universal truth concept; if it corresponds to 'BOTTOM', it returns the empty truth concept. For any other token, the method delegates the conversion to the internal `_to_concept` method to generate a standard Description Logic concept. The method may output debug information depending on the global configuration settings.

      :param tokens: Parsed results containing a keyword or identifier representing a top, bottom, or regular concept.
      :type tokens: pp.ParseResults

      :return: A ParseResults object containing the Top concept, Bottom concept, or a regular concept derived from the input tokens.

      :rtype: pp.ParseResults



   .. py:method:: get_grammatics() -> pyparsing.ParserElement
      :staticmethod:


      Constructs and returns the pyparsing grammar definition for the fuzzy Description Logic language. This static method assembles a comprehensive set of parsing rules that cover the language's syntax, including concept definitions, fuzzy logic operators, modifiers, datatype restrictions, axioms, and various query types. As a side effect, it enables left recursion support within the pyparsing library to accommodate the recursive nature of concept expressions and arithmetic operations defined in the grammar.

      :return: The root pyparsing ParserElement for the fuzzy DL language grammar, capable of parsing one or more valid statements or formulas.

      :rtype: pp.ParserElement



   .. py:method:: get_kb(*args) -> tuple[fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase, list[fuzzy_dl_owl2.fuzzydl.query.query.Query]]
      :staticmethod:


      Parses the input file specified by the arguments to construct a Knowledge Base and a list of Queries, initializing the necessary configuration and internal state. This method resets the class-level knowledge base and query list, sets the global logic semantics to Łukasiewicz fuzzy logic, and processes the file content using either a verbose line-by-line approach or an optimized path based on the debug configuration. It returns a tuple containing the populated `KnowledgeBase` object and the list of `Query` objects. Significant side effects include updates to class attributes and global constants; errors such as missing files or parsing failures are caught and logged rather than raised, resulting in a return value of None in those cases.

      :param args: Variable-length arguments where the first argument is the path to the input file, and any remaining arguments are passed to the configuration loader.
      :type args: typing.Any

      :return: A tuple containing the KnowledgeBase instance and the list of Query instances parsed from the input file.

      :rtype: tuple[KnowledgeBase, list[Query]]



   .. py:method:: load_config(*args) -> None
      :staticmethod:


      This static method acts as a wrapper to load specific configuration parameters from a predefined INI file located in the current working directory. It constructs the file path for 'CONFIG.ini' and delegates the actual parsing and parameter extraction to the `ConfigReader` class, passing along the provided arguments to determine which specific settings to retrieve. The function relies on the presence of the configuration file in the file system and triggers side effects within the `ConfigReader` rather than returning a value directly. By accepting a variable length argument list, it allows for selective loading of configuration data based on the caller's needs.

      :param args: Keys specifying which configuration parameters to load from the file.
      :type args: typing.Any



   .. py:method:: main(*args) -> None
      :staticmethod:


      Serves as the primary entry point for the DLParser program, orchestrating the loading, solving, and querying of a fuzzy description logic knowledge base. It accepts variable arguments to configure the loading process, retrieving the knowledge base and a list of queries via the `get_kb` method. The method first solves the knowledge base to prepare it for inference, then iterates through each query to generate solutions. Special handling is provided for `AllInstancesQuery` instances when the knowledge base lacks individuals, logging a specific informational message. For general queries, it evaluates consistency and logs the solution or a default value of 1.0 if the knowledge base is inconsistent. Additionally, it logs execution time and optionally the description logic language used. The method includes robust error handling, catching ontology inconsistency exceptions to report a default answer and logging stack traces for unexpected errors.

      :param args: Variable length positional arguments used to specify configuration parameters and the input file for parsing.
      :type args: typing.Any



   .. py:method:: parse_string(instring: str) -> pyparsing.ParseResults
      :staticmethod:


      This static method serves as the primary entry point for parsing input strings according to the grammar defined within the `DLParser` class. It retrieves the compiled grammar structure and attempts to match the entire input string, ensuring that no unparsed trailing characters remain; consequently, the operation will fail if the input does not fully conform to the grammar from start to finish. The method is decorated to handle unlimited recursion, allowing it to process deeply nested structures without hitting Python's recursion limit. Upon successful parsing, it returns a `pyparsing.ParseResults` object containing the structured data extracted from the input.

      :param instring: The text content to be parsed according to the defined grammar.
      :type instring: str

      :return: A `ParseResults` object containing the structured tokens extracted from the input string, representing a successful parse of the entire input against the defined grammar.

      :rtype: pp.ParseResults



   .. py:method:: parse_string_opt(filename: str) -> pyparsing.ParseResults
      :staticmethod:


      Reads the entire content of the file located at the specified path and processes it using the parser's defined grammar. The specific operation performed depends on the `DEBUG_PRINT` configuration flag: when disabled, the method executes a standard parse and returns the resulting structure; when enabled, it runs a test suite on the input string and writes the diagnostic output to a log file. This method involves file I/O operations and may raise exceptions if the file is inaccessible or if the input string fails to match the grammar rules.

      :param filename: Path to the file containing the content to be parsed.
      :type filename: str

      :return: A ParseResults object containing the results of parsing the file content according to the defined grammar.

      :rtype: pp.ParseResults



   .. py:attribute:: kb
      :type:  fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase
      :value: None



   .. py:attribute:: queries_list
      :type:  list[fuzzy_dl_owl2.fuzzydl.query.query.Query]
      :value: []



.. py:data:: FILENAME
   :type:  str

.. py:data:: LOG_DIR
   :type:  str

.. py:data:: TODAY
   :type:  datetime.datetime
