fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser
==========================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser



.. ── LLM-GENERATED DESCRIPTION START ──

A parser implementation that interprets Fuzzy OWL 2 annotation strings and transforms them into structured KnowledgeBase and Query objects using the pyparsing library.


Description
-----------


The software constructs a comprehensive grammar using the pyparsing library to recognize and interpret the syntax of Fuzzy OWL 2 annotations, which include complex fuzzy logic operators, modifiers, and data types. It defines a set of parsing actions that transform raw token streams into specific domain objects, such as modified concepts, weighted aggregations, and various fuzzy datatype functions like triangular or trapezoidal shapes. The central class orchestrates the parsing process by enabling left recursion to handle nested concept definitions and managing the conversion of these definitions into a KnowledgeBase and a list of Query instances. Error handling and configuration loading are integrated into the main execution flow to ensure robust processing of input strings and proper initialization of the underlying reasoning system.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser.FuzzyOwl2Parser


Functions
---------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser._parse_fuzzy_datatype
   fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser._parse_fuzzy_nominal
   fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser._parse_integral_concept
   fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser._parse_modified_concept
   fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser._parse_modifier_function
   fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser._parse_property
   fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser._parse_q_owa_concept
   fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser._parse_weighted_complex_concept
   fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser._parse_weighted_concept
   fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser._to_number


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_parser_owl2_parser_FuzzyOwl2Parser.png
       :alt: UML Class Diagram for FuzzyOwl2Parser
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FuzzyOwl2Parser**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_parser_owl2_parser_FuzzyOwl2Parser.pdf
       :alt: UML Class Diagram for FuzzyOwl2Parser
       :align: center
       :width: 12.0cm
       :class: uml-diagram

       UML Class Diagram for **FuzzyOwl2Parser**

.. py:class:: FuzzyOwl2Parser

   Bases: :py:obj:`object`


   This class provides a specialized parser for the Fuzzy OWL 2 ontology language, designed to interpret XML-based annotation strings and transform them into structured data objects, specifically a KnowledgeBase and a list of Query instances. It leverages the pyparsing library to construct a detailed grammar capable of handling complex fuzzy logic constructs, such as modified concepts, weighted aggregations (including OWA and Choquet integrals), fuzzy datatypes (e.g., triangular or trapezoidal), and axioms with degree definitions. The primary interface is the static main method, which orchestrates configuration loading and parsing while managing error handling, though direct access to the underlying grammar and parsing logic is available via get_grammatics and parse_string.


   .. py:method:: get_grammatics() -> pyparsing.ParserElement
      :staticmethod:


      This function generate the grammatics to parse the predicate wih formula "formula".

      :param formula:
      :type formula: :class:`= The predicate formula used for the parsing.`

      :rtype: :class:`The parsed result given by pyparsing.`



   .. py:method:: load_config(*args) -> None
      :staticmethod:



   .. py:method:: main(annotation: str, *args) -> tuple[fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase, list[fuzzy_dl_owl2.fuzzydl.query.query.Query]]
      :staticmethod:



   .. py:method:: parse_string(instring: str, parse_all: bool = False, *, parseAll: bool = False) -> pyparsing.ParseResults
      :staticmethod:



.. py:function:: _parse_fuzzy_datatype(tokens: pyparsing.ParseResults) -> fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype.FuzzyDatatype

   Parses a list of tokens resulting from a grammar parsing operation to construct a specific fuzzy datatype object. The function inspects the first token to determine the type of fuzzy function to instantiate, supporting left shoulder, right shoulder, linear, triangular, and trapezoidal functions. It extracts the necessary parameters from the subsequent tokens to initialize the corresponding function objects. If the first token does not match a known fuzzy keyword, the original tokens are returned unchanged. Additionally, the function logs the input tokens for debugging purposes.

   :param tokens: Parsed tokens representing a fuzzy datatype definition, containing the function type keyword and its associated numeric parameters.
   :type tokens: pp.ParseResults

   :return: A specific FuzzyDatatype instance (such as LeftShoulderFunction or TriangularFunction) constructed from the parsed tokens based on the identified keyword. Returns the original tokens if the input does not match a known fuzzy datatype pattern.

   :rtype: FuzzyDatatype


.. py:function:: _parse_fuzzy_nominal(tokens: pyparsing.ParseResults) -> fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition

   This internal parsing function constructs a FuzzyNominalConcept instance from a pyparsing.ParseResults object. It converts the input tokens into a standard list and extracts the first two elements to serve as arguments for the concept constructor. The function triggers a debug log operation with the input tokens before returning the new concept definition. Note that the function assumes the input list contains at least two elements; otherwise, an IndexError will occur.

   :param tokens: Parsed results containing the elements required to construct a FuzzyNominalConcept.
   :type tokens: pp.ParseResults

   :return: A FuzzyNominalConcept instance constructed from the parsed tokens, representing a fuzzy nominal concept definition.

   :rtype: ConceptDefinition


.. py:function:: _parse_integral_concept(tokens: pyparsing.ParseResults) -> fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition

   This internal helper function processes a list of parsed tokens to construct a specific fuzzy integral concept definition based on the identified keyword. It inspects the first element of the token list to determine the integral type—checking against OWA, Sugeno, Quasi-Sugeno, or Choquet keywords—and instantiates the corresponding `ConceptDefinition` subclass, passing the second and third elements of the list as arguments to the constructor. The function logs the input tokens for debugging purposes; however, it assumes the token list contains at least three elements and matches one of the expected keywords, potentially raising an `IndexError` or returning `None` implicitly if these conditions are not met.

   :param tokens: The parsed results containing the integral type keyword followed by the necessary arguments to construct the concept definition.
   :type tokens: pp.ParseResults

   :return: A specific ConceptDefinition instance (OwaConcept, SugenoConcept, QsugenoConcept, or ChoquetConcept) corresponding to the integral type identified in the tokens.

   :rtype: ConceptDefinition


.. py:function:: _parse_modified_concept(tokens: pyparsing.ParseResults) -> fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition

   This internal helper function serves as a parsing callback to construct a domain object from raw pyparsing tokens. It converts the input `ParseResults` into a list and instantiates a `ModifiedConcept` using the first two elements found in the token sequence. The function performs a side effect of logging the input tokens for debugging purposes. It assumes that the input tokens contain at least two elements; failure to meet this condition will result in an IndexError.

   :param tokens: The parsed results containing the matched tokens that constitute the modified concept.
   :type tokens: pp.ParseResults

   :return: A `ModifiedConcept` instance representing the parsed modified concept, constructed from the first two elements of the input tokens.

   :rtype: ConceptDefinition


.. py:function:: _parse_modifier_function(tokens: pyparsing.ParseResults) -> fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier.FuzzyModifier

   This internal helper function processes a list of parsing tokens to construct a specific fuzzy modifier object based on the keyword found at the beginning of the list. If the first token corresponds to a linear modifier, it instantiates a `LinearModifier` using the subsequent token as an argument. If the first token indicates a triangular modifier, it instantiates a `TriangularModifier` using the following three tokens as parameters. In cases where the keyword is unrecognized, the function returns the original input tokens unchanged. Additionally, the function logs the incoming tokens for debugging purposes.

   :param tokens: Parsed elements containing the modifier keyword and the associated arguments used to instantiate a specific FuzzyModifier object.
   :type tokens: pp.ParseResults

   :return: A FuzzyModifier instance (LinearModifier or TriangularModifier) initialized with the parsed parameters, or the raw tokens if the modifier type is unrecognized.

   :rtype: FuzzyModifier


.. py:function:: _parse_property(tokens: pyparsing.ParseResults) -> fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property.ModifiedProperty

   This internal helper function processes parsing results to construct a `ModifiedProperty` instance. It expects the input tokens to contain a `ModifiedConcept` object as the first element; otherwise, it raises an `AssertionError`. The function extracts the fuzzy modifier and fuzzy concept from this `ModifiedConcept` and uses them to instantiate the new `ModifiedProperty`. Additionally, it logs the incoming tokens for debugging purposes.

   :param tokens: The parsed results expected to contain a `ModifiedConcept` as the primary element.
   :type tokens: pp.ParseResults

   :return: A ModifiedProperty instance constructed from the fuzzy modifier and concept extracted from the parsed tokens.

   :rtype: ModifiedProperty


.. py:function:: _parse_q_owa_concept(tokens: pyparsing.ParseResults) -> fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition

   This internal function processes the results of a pyparsing match to construct a `QowaConcept` instance. It converts the input `ParseResults` object into a standard list and extracts the first two elements to pass as arguments to the `QowaConcept` constructor. The function logs the incoming tokens for debugging purposes before returning the constructed concept definition. It assumes the input tokens contain at least two elements; otherwise, an `IndexError` will occur.

   :param tokens: The parsed result object containing the sequence of elements extracted from the input, specifically the first two elements which are used to construct the QowaConcept.
   :type tokens: pp.ParseResults

   :return: A ConceptDefinition object representing the parsed Q-OWA concept, initialized with the first two elements of the parsed tokens.

   :rtype: ConceptDefinition


.. py:function:: _parse_weighted_complex_concept(tokens: pyparsing.ParseResults) -> fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition

   Constructs a specific weighted complex concept definition from a list of parsed tokens, typically used as a callback or action within a parsing grammar. The function interprets the first element of the token list as a fuzzy OWL2 keyword determining the aggregation logic—such as weighted maximum, minimum, sum, or sum-zero—and treats all subsequent elements as operands. It asserts that these operands are instances of WeightedConcept before instantiating and returning the appropriate concrete class (e.g., WeightedMaxConcept or WeightedSumConcept) containing the list of weighted concepts. This process includes a debug logging step and will raise an AssertionError if the operand types are invalid.

   :param tokens: Parsed elements where the first item is the aggregation operator keyword and the remaining items are WeightedConcept instances.
   :type tokens: pp.ParseResults

   :return: Returns a ConceptDefinition object representing a weighted aggregation (maximum, minimum, sum, or sum-zero) of the parsed weighted concepts.

   :rtype: ConceptDefinition


.. py:function:: _parse_weighted_concept(tokens: pyparsing.ParseResults) -> fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition

   This function serves as a parse action to transform raw parsing tokens into a structured `WeightedConcept` object. It accepts a `pyparsing.ParseResults` object, converts it into a list, and extracts the first two elements to initialize the `WeightedConcept`. The function logs the input tokens for debugging purposes before performing the conversion. Note that if the input token list contains fewer than two elements, this function will raise an `IndexError`.

   :param tokens: Parsed results containing the concept and weight components required to construct a WeightedConcept.
   :type tokens: pp.ParseResults

   :return: A `WeightedConcept` instance representing the parsed weighted concept, constructed from the first two elements of the provided tokens.

   :rtype: ConceptDefinition


.. py:function:: _to_number(tokens: pyparsing.ParseResults) -> float | int

   Converts the first element of a pyparsing `ParseResults` object into a numeric value, returning either an integer or a float. The function extracts the initial token, converts it to a float, and checks if the value is mathematically an integer; if so, it returns an `int`, otherwise it returns the `float`. This is typically employed as a parse action to transform string matches into their appropriate Python numeric types, though it will raise errors if the token list is empty or the string is not a valid number representation.

   :param tokens: Parsed results containing the string representation of the numeric value to be converted.
   :type tokens: pp.ParseResults

   :return: The numeric value of the first parsed token, returned as an int if the value is an integer, otherwise as a float.

   :rtype: float | int

