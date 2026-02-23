fuzzy_dl_owl2.fuzzyowl2.parser.owl2_xml_parser
==============================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.parser.owl2_xml_parser



.. ── LLM-GENERATED DESCRIPTION START ──

Converts FuzzyOWL2 XML annotations into Python objects representing fuzzy logic concepts, datatypes, and modifiers.


Description
-----------


The software utilizes the standard library's ElementTree to interpret XML strings containing fuzzy logic definitions, mapping specific tags and attributes to a hierarchy of Python classes representing fuzzy concepts, datatypes, and modifiers. By examining the root element's type annotation, the logic dispatches the parsing process to construct appropriate objects, ranging from simple triangular functions to complex weighted or aggregated concepts like OWA and Sugeno integrals. Configuration parameters are loaded from an external file to ensure the parsing environment is correctly initialized before processing the input data. Robust error handling is integrated to manage file access issues or malformed XML structures, logging detailed tracebacks to aid in debugging while preventing runtime crashes during the conversion process.

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



   .. py:method:: load_config(*args) -> None
      :staticmethod:


      This static method loads configuration parameters by reading a "CONFIG.ini" file located in the current working directory. It acts as a wrapper that forwards any provided arguments to the underlying `ConfigReader.load_parameters` method to facilitate the parsing and application of settings. The operation modifies the global or class-level configuration state but does not return a value. Note that this method relies on the specific execution context, as it will fail to locate the configuration file if the current working directory does not contain "CONFIG.ini".

      :param args: Additional arguments passed directly to the underlying configuration loader.
      :type args: typing.Any



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


