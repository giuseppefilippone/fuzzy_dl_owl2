fuzzy_dl_owl2.fuzzyowl2.parser.owl2_xml_parser
==============================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.parser.owl2_xml_parser



.. ── LLM-GENERATED DESCRIPTION START ──

A parser that converts FuzzyOWL2 XML annotations into the Python object model of a fuzzy description-logic ontology, handling fuzzy concepts, membership-function datatypes, modifiers, modified roles, axiom degrees, and ontology-level fuzzy logic declarations.


Description
-----------


**FuzzyOwl2XMLParser** acts as a stateless translation layer built entirely from static methods: it accepts an XML string representing a FuzzyOWL2 annotation and dispatches on the root element's fuzzy type attribute to construct the matching in-memory object. Concept annotations become modified, weighted, nominal, or aggregation-style definitions — including weighted min/max/sum combinations and OWA, Choquet, Sugeno, quasi-Sugeno, and quantified-OWA constructs assembled from explicit weight and concept-name lists — while datatype annotations are turned into membership functions such as triangular, trapezoidal, left-shoulder, right-shoulder, linear, crisp, and modifier-wrapped functions. Modifier annotations yield linear or triangular modifier objects, role annotations are constrained to modified properties, axiom annotations reduce to a plain float degree, and ontology annotations simply return the declared fuzzy logic as a string, so the return type is intentionally a broad union that mirrors the full FuzzyOWL2 vocabulary; anything outside that vocabulary raises a *ValueError* to signal unsupported input.

XML processing goes through *defusedxml* rather than the standard library's parser, a deliberate hardening choice when ingesting potentially untrusted ontology files, and attribute lookups are performed case-insensitively to tolerate variations in how annotations were serialised. A convenience entry point loads runtime settings from a CONFIG.ini file before delegating to the core parsing routine, and it wraps the whole operation in error handling that reports the exception and full traceback instead of propagating it, so a missing configuration file or malformed annotation degrades gracefully rather than crashing the caller. Centralising all type dispatch in one place makes the supported vocabulary easy to audit and extend, while the actual representation of each fuzzy construct is delegated to the dedicated owl_types classes, keeping the parsing logic focused purely on interpretation.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.parser.owl2_xml_parser.FuzzyOwl2XMLParser


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_parser_owl2_xml_parser_FuzzyOwl2XMLParser.png
       :alt: UML Class Diagram for FuzzyOwl2XMLParser
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FuzzyOwl2XMLParser**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_parser_owl2_xml_parser_FuzzyOwl2XMLParser.pdf
       :alt: UML Class Diagram for FuzzyOwl2XMLParser
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FuzzyOwl2XMLParser**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:class:: FuzzyOwl2XMLParser

   Bases: :py:obj:`object`


   This class serves as a specialized parser for converting FuzzyOWL2 XML annotations into corresponding Python data structures. It interprets XML strings to instantiate a variety of objects representing fuzzy logic elements, including concept definitions (such as weighted or modified concepts), fuzzy datatypes (like triangular or trapezoidal functions), and property definitions. The parsing logic relies on inspecting specific XML attributes to determine the correct object type to construct. Additionally, the class provides functionality to load configuration parameters from an external file and includes error handling mechanisms to manage parsing or file access issues gracefully.

   :raises ValueError: Raised when the parsed XML string contains an unsupported, unrecognized, or missing annotation type that does not correspond to any of the defined FuzzyOWL2 elements (Concept, Datatype, Modifier, Axiom, Ontology, or Role).


   .. py:method:: get_caseless_attrib(attrib: dict[str, str], key: str) -> Optional[str]
      :staticmethod:


      This static method retrieves a value from a dictionary of attributes by performing a case-insensitive lookup on the provided key. It scans the dictionary for keys that match the target key when both are converted to lowercase, returning the value associated with the first such match found. If no matching key exists, the method returns None. Note that if the input dictionary contains multiple keys that differ only by case, the value returned corresponds to the first match encountered during iteration, which depends on the dictionary's insertion order.

      :param attrib: A dictionary containing the attributes to search.
      :type attrib: dict[str, str]
      :param key: The name of the attribute to retrieve, matched case-insensitively.
      :type key: str

      :return: The value of the attribute if a case-insensitive match is found, otherwise None.

      :rtype: typing.Optional[str]



   .. py:method:: load_config(**kargs) -> None
      :staticmethod:


      This static method loads configuration parameters by reading a "CONFIG.ini" file located in the current working directory. It acts as a wrapper that forwards any provided arguments to the underlying `ConfigReader.load_parameters` method to facilitate the parsing and application of settings. The operation modifies the global or class-level configuration state but does not return a value. Note that this method relies on the specific execution context, as it will fail to locate the configuration file if the current working directory does not contain "CONFIG.ini".

      :param kargs: Additional arguments passed directly to the underlying configuration loader.
      :type kargs: typing.Any



   .. py:method:: main(annotation: str, *args) -> Union[fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition, fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype.FuzzyDatatype, fuzzy_dl_owl2.fuzzyowl2.owl_types.property_definition.PropertyDefinition, fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier.FuzzyModifier, float, str]
      :staticmethod:


      This static method serves as the primary entry point for parsing FuzzyOWL2 XML strings into structured Python objects. It initializes the parser's configuration using the provided arguments before processing the input annotation, ensuring that necessary settings are loaded prior to parsing. The method returns a parsed entity, which may be a ConceptDefinition, FuzzyDatatype, PropertyDefinition, FuzzyModifier, or a primitive value, depending on the content of the XML. In the event of a missing configuration file or a general parsing exception, the method logs the error and traceback details to the standard error output and returns None implicitly, allowing the program to handle failures gracefully without crashing.

      :param annotation: The FuzzyOWL2 XML string to be parsed.
      :type annotation: str
      :param args: Variable length argument list passed to the configuration loader, typically starting with the path to the configuration file.
      :type args: typing.Any

      :return: The parsed representation of the FuzzyOWL2 XML annotation, which may be a ConceptDefinition, FuzzyDatatype, PropertyDefinition, FuzzyModifier, float, or str depending on the input content. Returns None if parsing or configuration fails.

      :rtype: typing.Union[ConceptDefinition, FuzzyDatatype, PropertyDefinition, FuzzyModifier, float, str]



   .. py:method:: parse_string(instring: str) -> Union[fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition, fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype.FuzzyDatatype, fuzzy_dl_owl2.fuzzyowl2.owl_types.property_definition.PropertyDefinition, fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier.FuzzyModifier, float, str]
      :staticmethod:


      Parses a string containing FuzzyOWL2 XML and constructs the corresponding Python representation based on the structure and attributes of the XML. The method inspects the root element's type annotation to dispatch the parsing logic to specific handlers for concepts, datatypes, modifiers, axioms, ontology settings, or roles. Depending on the content, it returns specialized objects such as `ModifiedConcept`, `TriangularFunction`, or `LinearModifier`, or primitive values like floats for axiom degrees and strings for logic types. During execution, the method logs the XML structure for debugging purposes. It raises an `AssertionError` if the root element does not match the expected FuzzyOWL2 tag and a `ValueError` if the fuzzy type is unsupported.

      :param instring: A string containing the FuzzyOWL2 XML data to be parsed.
      :type instring: str

      :raises ValueError: Raised if the input XML string does not specify a valid or supported FuzzyOWL2 annotation type.

      :return: Returns a Python object representing the parsed FuzzyOWL2 element. The specific type is determined by the XML's `fuzzyType` attribute and may be a `ConceptDefinition`, `FuzzyDatatype`, `PropertyDefinition`, `FuzzyModifier`, a `float` (for axiom degrees), or a `str` (for ontology logic).

      :rtype: typing.Union[ConceptDefinition, FuzzyDatatype, PropertyDefinition, FuzzyModifier, float, str]


