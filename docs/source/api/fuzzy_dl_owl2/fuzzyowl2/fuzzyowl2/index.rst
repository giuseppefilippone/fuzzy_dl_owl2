fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2
=================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2



.. ── LLM-GENERATED DESCRIPTION START ──

A translator that converts OWL2 ontologies annotated with fuzzy logic semantics into a Fuzzy Description Logic representation suitable for reasoning.


Description
-----------


The ``FuzzyOwl2`` class acts as a bridge between standard OWL2 ontologies extended with fuzzy logic annotations and a specific Fuzzy Description Logic format used by reasoning engines. It loads an ontology, inspects entities like classes, properties, and datatypes for specific fuzzy annotations, and parses these annotations to construct corresponding fuzzy logic concepts, modifiers, and functions. The translation process involves iterating through the ontology's axioms—covering the TBox, RBox, and ABox components—to extract both structural definitions and fuzzy truth values. It distinguishes between crisp axioms and those carrying specific degrees of membership, ensuring that the output representation accurately reflects the uncertainty or vagueness defined in the source. By systematically processing ontology annotations and axioms, the system generates a serialized text output that encapsulates the fuzzy semantics required for downstream inference tasks.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2.FuzzyOwl2


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_fuzzyowl2_FuzzyOwl2.png
       :alt: UML Class Diagram for FuzzyOwl2
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FuzzyOwl2**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_fuzzyowl2_FuzzyOwl2.pdf
       :alt: UML Class Diagram for FuzzyOwl2
       :align: center
       :width: 10.2cm
       :class: uml-diagram

       UML Class Diagram for **FuzzyOwl2**

.. py:class:: FuzzyOwl2(input_file: str, output_file: str, base_iri: str = 'http://www.semanticweb.org/ontologies/fuzzydl_ontology#')

   Bases: :py:obj:`object`


   This class acts as a translator for converting OWL2 ontologies annotated with fuzzy logic into a Fuzzy Description Logic (DL) representation. It parses an input ontology to extract fuzzy semantics defined on concepts, properties, and datatypes—such as triangular functions, linear modifiers, and complex aggregation operators like OWA or Sugeno integrals—and writes the corresponding definitions to a specified output file. The translation process also handles axioms annotated with fuzzy degrees, distinguishing between standard crisp axioms and those carrying specific truth values, while ensuring duplicate axioms are not processed. To utilize this functionality, an instance should be created with paths for the input ontology and the output file, followed by a call to the `translate_owl2ontology` method to execute the full conversion pipeline.

   :param POS_INFINITY: A constant representing positive infinity (set to 10000.0), used as the default upper bound for fuzzy datatypes.
   :type POS_INFINITY: float
   :param NEG_INFINITY: A constant representing negative infinity, used as a default lower bound for fuzzy datatypes.
   :type NEG_INFINITY: float
   :param output_dl: The full file path where the translated fuzzy DL representation is written.
   :type output_dl: str
   :param defined_concepts: Stores the fuzzy concept definitions extracted from the ontology, keyed by concept name.
   :type defined_concepts: dict[str, ConceptDefinition]
   :param defined_properties: Maps property names to their fuzzy property definitions extracted from the ontology annotations.
   :type defined_properties: dict[str, ConceptDefinition]
   :param fuzzy_datatypes: Stores the fuzzy datatype definitions extracted from the ontology, mapping each datatype name to its specific membership function and parameters.
   :type fuzzy_datatypes: dict[str, ConceptDefinition]
   :param fuzzy_modifiers: A dictionary mapping modifier names to their corresponding ConceptDefinition objects, representing the fuzzy modifiers defined in the ontology.
   :type fuzzy_modifiers: dict[str, ConceptDefinition]
   :param processed_axioms: Tracks axioms that have already been processed and written to the output file to ensure no duplicates are generated during translation.
   :type processed_axioms: set[str]
   :param ontologies: A set of OWLOntology objects representing the main ontology and any imported ontologies that are being processed.
   :type ontologies: set[OWLOntology]
   :param ontology_path: Path to the input OWL2 ontology file to be processed.
   :type ontology_path: typing.Any
   :param ontology_iri: The Internationalized Resource Identifier (IRI) representing the identity and namespace of the ontology being processed.
   :type ontology_iri: typing.Any
   :param ontology: The primary OWLOntology instance loaded from the input file, serving as the main source for extracting axioms and annotations during translation.
   :type ontology: OWLOntology
   :param fuzzy_label: The specific annotation property used to identify fuzzy logic definitions within the ontology.
   :type fuzzy_label: OWLAnnotationProperty

   :raises ValueError: Raised when an annotation parsed from the ontology is invalid or unsupported for its context. This occurs if a datatype, concept, or property annotation does not correspond to a recognized fuzzy logic construct, if an axiom degree annotation cannot be interpreted as a number, or if an OWL class expression type is not handled by the translator.


   .. py:method:: __get_degree(axiom: pyowl2.abstracts.axiom.OWLAxiom) -> float

      Extracts the fuzzy membership degree associated with a specific OWL axiom by inspecting its annotations. If the axiom lacks annotations or the annotation set is empty, the method returns a default value of 1.0. When annotations are present, it attempts to parse the value of the first annotation into a float; if multiple annotations are detected, an error is logged, though the process continues using the first entry. The method validates that the parsed value is numeric, raising a ValueError if the parsing fails or the result is not a number.

      :param axiom: The OWL axiom to be inspected for annotations specifying its degree.
      :type axiom: OWLAxiom

      :raises ValueError: Raised if the parsed annotation value is not a number.

      :return: The degree of the axiom, parsed from its annotation, or 1.0 if no annotations are present.

      :rtype: float



   .. py:method:: __get_facets(name: str) -> list[float]

      Searches the loaded ontologies for a datatype definition matching the specified name and extracts its numeric lower and upper bounds. The method iterates through datatype definition axioms, handling both direct datatype restrictions and intersections of two restrictions to identify the relevant facets. It converts exclusive bounds to inclusive bounds by applying a small epsilon adjustment. If the datatype cannot be found or does not contain valid restriction facets, the method returns a list containing negative and positive infinity.

      :param name: The name of the datatype for which to retrieve restriction facets.
      :type name: str

      :return: A list of two floats representing the lower and upper bounds of the datatype, defaulting to negative and positive infinity if no restrictions are found. Exclusive bounds are adjusted by a small epsilon value.

      :rtype: list[float]



   .. py:method:: __write_class_assertion_axiom(ontology: pyowl2.ontology.OWLOntology, annotated: bool = True) -> None

      Processes class assertion axioms from the provided ontology, writing them to the output based on their fuzzy degree and the `annotated` flag. If `annotated` is True, the method specifically targets axioms with a degree different from 1.0, treating them as fuzzy assertions. If `annotated` is False, it processes axioms with a degree of 1.0, but only if they have not already been handled, as tracked by the `processed_axioms` set. This approach ensures that fuzzy and crisp assertions are handled separately without duplication, while modifying the internal state of the object to record processed items.

      :param ontology: The source ontology from which class assertion axioms are retrieved.
      :type ontology: OWLOntology
      :param annotated: Flag indicating whether to process fuzzy class assertions. If True, only axioms with degrees different from 1.0 are processed. If False, only crisp axioms (degree 1.0) that have not been processed previously are handled.
      :type annotated: bool



   .. py:method:: __write_data_property_assertion_axiom(ontology: pyowl2.ontology.OWLOntology, annotated: bool = True) -> None

      Iterates over all data property assertion axioms within the provided ontology to serialize them to the output, distinguishing between fuzzy and crisp assertions based on the `annotated` flag. When `annotated` is True, the method processes axioms with a fuzzy degree different from 1.0, writing them to the output and recording them in the internal set of processed axioms. When `annotated` is False, the method handles axioms with a degree of exactly 1.0, but only if they have not already been recorded in the processed set, thereby preventing duplicate writes. This method updates the internal state of processed axioms and delegates the actual writing logic to a lower-level writer function.

      :param ontology: The source ontology containing the data property assertion axioms to be written.
      :type ontology: OWLOntology
      :param annotated: Flag indicating whether to process fuzzy axioms. If True, processes axioms with degrees different from 1.0. If False, processes axioms with a degree of 1.0 that have not already been processed.
      :type annotated: bool



   .. py:method:: __write_negative_data_property_assertion_axiom(ontology: pyowl2.ontology.OWLOntology, annotated: bool = True) -> None

      Iterates over negative data property assertion axioms within the provided ontology and serializes them to the output file based on their fuzzy degree and the `annotated` flag. When `annotated` is True, the method processes only axioms with a fuzzy degree different from 1.0, representing non-crisp fuzzy constraints. Conversely, when `annotated` is False, it handles axioms with a degree of 1.0 (crisp assertions) but only if they have not already been processed, ensuring no duplication occurs. The method maintains an internal set of processed axioms to track this state and delegates the actual writing logic to a separate helper method.

      :param ontology: The source ontology containing the negative data property assertion axioms to be written.
      :type ontology: OWLOntology
      :param annotated: Determines whether to process annotated axioms with fuzzy degrees different from 1.0, or standard axioms with a degree of 1.0 that have not yet been processed.
      :type annotated: bool



   .. py:method:: __write_negative_object_property_assertion_axiom(ontology: pyowl2.ontology.OWLOntology, annotated: bool = True) -> None

      Iterates through negative object property assertion axioms within the provided ontology to serialize them to the output file, distinguishing between fuzzy and crisp assertions based on the `annotated` flag. When the flag is True, the method processes only axioms with a fuzzy degree different from 1.0; when False, it processes axioms with a degree of exactly 1.0, provided they have not already been handled in a previous pass. As a side effect, the method updates an internal set of processed axioms to prevent duplication and triggers debug logging for the items being written.

      :param ontology: The source ontology containing the negative object property assertion axioms to be processed.
      :type ontology: OWLOntology
      :param annotated: If True, processes fuzzy axioms with degrees different from 1.0. If False, processes non-annotated axioms or those with a degree of 1.0 that have not been processed previously.
      :type annotated: bool



   .. py:method:: __write_object_property_assertion_axiom(ontology: pyowl2.ontology.OWLOntology, annotated: bool = True) -> None

      Iterates through object property assertion axioms in the given ontology and writes them to the output file based on the specified annotation mode. If the `annotated` flag is set to True, the method processes only those axioms with a fuzzy degree different from 1.0; otherwise, it processes axioms with a degree of 1.0, provided they have not already been handled. To prevent duplication, the method maintains a record of processed assertions in the `processed_axioms` set and triggers debug logging for each axiom written.

      :param ontology: The source ontology from which to retrieve the object property assertion axioms.
      :type ontology: OWLOntology
      :param annotated: Flag indicating whether to process fuzzy axioms with degrees different from 1.0 (True) or standard axioms with a degree of 1.0 (False).
      :type annotated: bool



   .. py:method:: __write_subclass_of_axiom(ontology: pyowl2.ontology.OWLOntology, annotated: bool = True) -> None

      Processes subclass axioms from the provided ontology, separating them based on their associated fuzzy degree and the `annotated` flag. When `annotated` is True, the method writes axioms with degrees different from 1.0 to the output and records them as processed. Conversely, when `annotated` is False, it writes axioms with a degree of 1.0 only if they have not been previously processed, ensuring no duplication. This method relies on `__get_degree` to determine the fuzzy value and updates the internal `processed_axioms` set to track state.

      :param ontology: The source ontology containing the subclass axioms to be processed.
      :type ontology: OWLOntology
      :param annotated: Determines whether to process axioms annotated with fuzzy degrees. When True, only axioms with degrees different from 1.0 are processed; when False, only non-annotated axioms or those with a degree of 1.0 are processed.
      :type annotated: bool



   .. py:method:: __write_subdata_property_axiom(ontology: pyowl2.ontology.OWLOntology, annotated: bool = True) -> None

      Processes sub-data property axioms from the given ontology, filtering them based on the provided `annotated` flag to separate fuzzy degrees from standard relationships. If the flag is True, the method writes axioms that have a fuzzy degree different from 1.0. If the flag is False, it writes axioms with a degree of 1.0, provided they have not already been processed and recorded in the internal tracking set. This method ensures that each relevant axiom is serialized to the output file exactly once by updating the set of processed axioms upon writing.

      :param ontology: The source ontology containing the sub-data property axioms to be processed.
      :type ontology: OWLOntology
      :param annotated: Determines whether to process axioms annotated with fuzzy degrees. If True, processes axioms with degrees different from 1.0; if False, processes non-annotated axioms or those with a degree of 1.0 that have not been processed previously.
      :type annotated: bool



   .. py:method:: __write_subobject_property_axiom(ontology: pyowl2.ontology.OWLOntology, annotated: bool = True) -> None

      Iterates over the sub-object property axioms within the specified ontology to serialize them to the output file, distinguishing between standard axioms and those carrying fuzzy degrees. The method explicitly excludes axioms involving property chains from processing. Depending on the 'annotated' parameter, it either writes axioms with a fuzzy degree other than 1.0 or writes non-fuzzy axioms (degree 1.0) that have not been previously recorded. As a side effect, it updates the internal set of processed axioms to ensure that each relationship is written only once.

      :param ontology: The source ontology containing the sub-object property axioms to be processed.
      :type ontology: OWLOntology
      :param annotated: Flag indicating whether to process axioms with fuzzy degrees (non-1.0) or standard axioms (degree 1.0).
      :type annotated: bool



   .. py:method:: __write_subproperty_chain_of_axiom(ontology: pyowl2.ontology.OWLOntology, annotated: bool = True) -> None

      Iterates through the axioms of the provided ontology to identify and write sub-property chain axioms, specifically handling those involving object property chains. The behavior is controlled by the `annotated` flag: when set to True, the method processes and writes axioms with fuzzy degrees different from 1.0; when set to False, it processes axioms with a degree of exactly 1.0, provided they have not already been processed. In both cases, the method updates an internal set of processed axioms to prevent duplicate writes and delegates the actual writing logic to a separate helper method.

      :param ontology: The source ontology containing the sub-property chain axioms to be processed.
      :type ontology: OWLOntology
      :param annotated: Flag indicating whether to process axioms annotated with fuzzy degrees. If True, only axioms with degrees different from 1.0 are processed. If False, only non-annotated axioms or those with a degree of 1.0 that have not been processed previously are handled.
      :type annotated: bool



   .. py:method:: get_atomic_concept_name(c: pyowl2.base.owl_class.OWLClass) -> str

      Retrieves the short name for the specified OWL class and logs it to the utility info stream. Although the human-readable name is calculated, the method currently returns an empty string. The primary side effect of calling this method is the generation of an informational log entry containing the concept's name.

      :param c: The OWL class representing the atomic concept for which to retrieve the name.
      :type c: OWLClass

      :return:

      :rtype: str



   .. py:method:: get_atomic_data_property_name(p: pyowl2.expressions.data_property.OWLDataProperty) -> str

      Retrieves the short name of the provided OWL data property and logs the action of writing this property to the info stream. Although the method determines the human-readable identifier for the property, it currently returns an empty string, functioning primarily as a logging step within the broader serialization or processing workflow.

      :param p: The atomic data property for which to retrieve the human-readable name.
      :type p: OWLDataProperty

      :return: An empty string.

      :rtype: str



   .. py:method:: get_atomic_object_property_name(p: pyowl2.expressions.object_property.OWLObjectProperty) -> str

      Retrieves the short form identifier of the provided OWL object property and logs the action to the info stream. This method delegates the extraction of the identifier to `get_short_name` and triggers a side effect of logging the retrieved name. Despite calculating the name, the function currently returns an empty string.

      :param p: The atomic object property for which to retrieve the human-readable name.
      :type p: OWLObjectProperty

      :return: An empty string.

      :rtype: str



   .. py:method:: get_bottom_concept_name() -> str

      Retrieves the human-readable name of the bottom concept, which represents the empty set or contradiction within the ontology. This method is intended to provide a simplified string representation suitable for user interfaces or logging, rather than the full internal identifier. The method triggers an informational log message during execution and currently returns an empty string as a placeholder.

      :return: The human-readable name of the bottom concept.

      :rtype: str



   .. py:method:: get_bottom_data_property_name() -> str

      This method is intended to retrieve the human-readable name of the bottom data property within the ontology. However, the current implementation acts as a placeholder, logging an informational message via `Util.info` and returning an empty string. Consequently, it does not currently provide a valid property name, and callers should be aware that the return value is empty until the implementation is completed.

      :return: The human-readable name of the bottom data property.

      :rtype: str



   .. py:method:: get_bottom_object_property_name() -> str

      Retrieves the human-readable name of the bottom object property defined in the ontology. The current implementation acts as a stub, returning an empty string instead of a valid identifier. As a side effect, it logs an informational message indicating that the logic for writing the bottom object property is not yet implemented.

      :return: The human-readable name of the bottom object property.

      :rtype: str



   .. py:method:: get_class_name(c: pyowl2.abstracts.class_expression.OWLClassExpression) -> str

      Generates a human-readable name for a given OWL class expression by dispatching to specific helper methods based on the expression's type. This method handles atomic classes, including special cases for the top and bottom concepts, as well as complex expressions such as intersections, unions, complements, and various property restrictions (existential, universal, value, and cardinality). It supports both object and data property expressions, distinguishing between qualified and unqualified cardinality restrictions. If the provided expression is of an unsupported type, a ValueError is raised, and the method logs the input expression for debugging purposes.

      :param c: The OWL class expression to be converted into a human-readable name.
      :type c: OWLClassExpression

      :raises ValueError: Raised if the provided class expression is of an unsupported type that cannot be formatted into a human-readable name.

      :return: A human-readable string representation of the OWL class expression, formatted according to its specific type and structure.

      :rtype: str



   .. py:method:: get_data_all_values_from_name(p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, range: pyowl2.abstracts.data_range.OWLDataRange) -> str

      Constructs a human-readable string identifier for a universal data restriction defined by a specific property and range. This method processes an OWL data property expression and a data range to represent a DataAllValuesFrom constraint, where all values of the property are required to be within the given range. As a side effect, it logs the input components, though the current implementation returns an empty string placeholder.

      :param p: The data property expression acting as the property in the data all values from restriction.
      :type p: OWLDataPropertyExpression
      :param range: The data range that serves as the filler for the data all values from restriction.
      :type range: OWLDataRange

      :return: The human-readable name of the data all values from class expression defined by the given property and data range.

      :rtype: str



   .. py:method:: get_data_exact_cardinality_restriction(cardinality: int, p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, range: pyowl2.abstracts.data_range.OWLDataRange = None) -> str

      Constructs and logs a human-readable representation of an OWL Data Exact Cardinality Restriction using the specified cardinality, data property expression, and optional data range. The method formats the restriction details into a string and outputs it via the logging utility, handling cases where the data range is omitted by adjusting the output format accordingly. It returns an empty string, functioning primarily as a logging operation rather than a value retrieval method.

      :param cardinality: The exact number of data values the property must have.
      :type cardinality: int
      :param p: The data property expression upon which the exact cardinality restriction is applied.
      :type p: OWLDataPropertyExpression
      :param range: The data range that acts as the filler for the restriction, specifying the allowed data type for the property values.
      :type range: OWLDataRange

      :return: An empty string.

      :rtype: str



   .. py:method:: get_data_has_value_name(p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, literal: pyowl2.literal.literal.OWLLiteral) -> str

      Generates a human-readable name for a DataHasValue class expression, which represents the restriction of a data property to a specific literal value. This method logs the provided property and literal arguments to the information stream and returns a string formatted to describe this restriction.

      :param p: The data property expression that serves as the property in the data has value restriction.
      :type p: OWLDataPropertyExpression
      :param literal: The specific literal value that the data property expression is restricted to.
      :type literal: OWLLiteral

      :return:

      :rtype: str



   .. py:method:: get_data_max_cardinality_restriction(cardinality: int, p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, range: pyowl2.abstracts.data_range.OWLDataRange = None) -> str

      This method formats and logs a human-readable representation of a data maximum cardinality restriction using the specified cardinality, data property expression, and optional data range. It distinguishes between restrictions with a specific data range filler and those without, logging the appropriate format via the utility logger. While the method signature implies a return value, the implementation currently returns an empty string, indicating that its primary purpose is the side effect of logging the restriction details.

      :param cardinality: The maximum number of data values permitted for the data property.
      :type cardinality: int
      :param p: The data property expression to which the maximum cardinality restriction applies.
      :type p: OWLDataPropertyExpression
      :param range: The data range serving as the filler for the restriction, specifying the allowed values for the property.
      :type range: OWLDataRange

      :return: An empty string. The method prints the restriction details to the info log instead of returning them.

      :rtype: str



   .. py:method:: get_data_min_cardinality_restriction(cardinality: int, p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, range: pyowl2.abstracts.data_range.OWLDataRange = None) -> str

      Generates a human-readable representation of an OWL data minimum cardinality restriction defined by the specified cardinality, data property expression, and optional data range. Instead of returning the name, the method logs the formatted restriction details to the info stream, including the data range only if it is provided. The function returns an empty string as a placeholder.

      :param cardinality: The minimum number of values required for the data property.
      :type cardinality: int
      :param p: The data property expression defining the property of the restriction.
      :type p: OWLDataPropertyExpression
      :param range: The data range that serves as the filler of the restriction.
      :type range: OWLDataRange

      :return: An empty string. The function logs the restriction details to the info stream rather than returning a formatted name.

      :rtype: str



   .. py:method:: get_data_property_name(p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression) -> str

      Retrieves a human-readable string representation for a given OWL data property expression by inspecting its specific type. The method distinguishes between the universal top data property, the empty bottom data property, and standard atomic properties, delegating to the appropriate internal naming function for each case. This ensures that special ontology-level constructs are rendered distinctly from standard named properties. Additionally, the method logs the input expression for debugging purposes before processing.

      :param p: The data property expression to be resolved into a human-readable name.
      :type p: OWLDataPropertyExpression

      :return: The human-readable name of the data property expression, handling top, bottom, and atomic property types.

      :rtype: str



   .. py:method:: get_data_some_values_from_name(p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, range: pyowl2.abstracts.data_range.OWLDataRange) -> str

      Generates a human-readable name for a data property existential restriction, corresponding to an OWL 'DataSomeValuesFrom' class expression. The method utilizes a data property expression and a data range to construct this representation. As a side effect, it logs the details of the property and range to the system output.

      :param p: The data property expression that serves as the property for the data some values from restriction.
      :type p: OWLDataPropertyExpression
      :param range: The data range that serves as the filler for the data some values from restriction.
      :type range: OWLDataRange

      :return: The human-readable name of the data some values from class expression.

      :rtype: str



   .. py:method:: get_individual_name(i: pyowl2.abstracts.individual.OWLIndividual) -> Optional[str]

      Retrieves a human-readable name for the specified OWL individual by first checking if the individual is anonymous. If the individual is an instance of OWLAnonymousIndividual, the method returns None and logs an informational message indicating that anonymous individuals are not supported. For named individuals, the method obtains the short name via the `get_short_name` method and returns it as a string, while also logging the result.

      :param i: The ontology entity for which the human-readable name is to be retrieved.
      :type i: OWLIndividual

      :return: Returns None if the individual is anonymous, otherwise returns an empty string.

      :rtype: typing.Optional[str]



   .. py:method:: get_object_all_values_from_name(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression) -> str

      Generates a human-readable string representation for an OWL ObjectAllValuesFrom class expression, which represents a universal restriction on an object property. The method takes an object property expression and a class expression as inputs to define the scope of the restriction. As a side effect, it logs the details of the property and class being processed.

      :param p: The object property expression acting as the property in the ObjectAllValuesFrom restriction.
      :type p: OWLObjectPropertyExpression
      :param c: The class expression that serves as the filler for the ObjectAllValuesFrom restriction.
      :type c: OWLClassExpression

      :return: A human-readable string representation of the ObjectAllValuesFrom restriction defined by the provided property and class expression.

      :rtype: str



   .. py:method:: get_object_complement_of_name(c: pyowl2.abstracts.class_expression.OWLClassExpression) -> str

      Generates a human-readable name for the object complement of a given OWL class expression. This method accepts a class expression as the operand for the complement operation and returns a string representing that negation. As a side effect, it logs the details of the complement operation to the info stream before returning the result.

      :param c: The class expression serving as the operand for the object complement.
      :type c: OWLClassExpression

      :return: A human-readable string representing the name of the object complement of the provided class expression.

      :rtype: str



   .. py:method:: get_object_exact_cardinality_restriction(cardinality: int, p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression = None) -> str

      Generates a log entry representing an OWL object exact cardinality restriction based on the provided parameters. It accepts an integer cardinality, an object property expression, and an optional class expression filler. If the filler is provided, the log message includes all three components; otherwise, it includes only the cardinality and the property. While the method triggers this informational side effect, it returns an empty string.

      :param cardinality: The exact number of property relationships required by the restriction.
      :type cardinality: int
      :param p: The object property expression used as the property in the restriction.
      :type p: OWLObjectPropertyExpression
      :param c: The class expression serving as the filler of the restriction.
      :type c: OWLClassExpression

      :return: An empty string.

      :rtype: str



   .. py:method:: get_object_has_self_name(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> str

      Constructs a human-readable name for an OWL ObjectHasSelf class expression based on the supplied object property expression. This method is responsible for serializing the self-restriction concept into a string format, typically used for display or internal identification within the FuzzyOwl2 framework. It includes a side effect of logging the property expression, though the current implementation returns an empty string placeholder.

      :param p: The object property expression used to construct the ObjectHasSelf expression.
      :type p: OWLObjectPropertyExpression

      :return: The human-readable name of the ObjectHasSelf class expression for the given object property expression.

      :rtype: str



   .. py:method:: get_object_has_value_name(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, i: pyowl2.abstracts.individual.OWLIndividual) -> str

      Generates a human-readable string representation for an OWL ObjectHasValue class expression, which describes the class of individuals that have a specific relationship to a particular individual. This method accepts an object property expression and an OWL individual to formulate the name. As a side effect, it logs the input parameters to the info stream during execution.

      :param p: The object property expression that serves as the property in the object has value restriction.
      :type p: OWLObjectPropertyExpression
      :param i: The individual that is the value of the object property expression.
      :type i: OWLIndividual

      :return: An empty string.

      :rtype: str



   .. py:method:: get_object_intersection_of_name(operands: set[pyowl2.abstracts.class_expression.OWLClassExpression]) -> str

      This method is designed to generate a human-readable name for an object intersection defined by a set of OWL class expressions. It accepts the class expressions as operands and logs them for informational purposes. Currently, the method acts as a placeholder and returns an empty string instead of a formatted name.

      :param operands: The set of class expressions comprising the object intersection.
      :type operands: set[OWLClassExpression]

      :return: A human-readable string representing the object intersection of the provided class expressions.

      :rtype: str



   .. py:method:: get_object_max_cardinality_restriction(cardinality: int, p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression = None) -> str

      This method constructs a human-readable representation of an OWL Object Max Cardinality Restriction using the provided cardinality, object property expression, and optional class expression filler. It logs this representation to the info stream using `Util.info`, formatting the output to include the filler class only if it is explicitly provided. Despite its name implying a retrieval operation, the method performs a logging side effect and returns an empty string.

      :param cardinality: The maximum number of distinct individuals that can be related by the object property.
      :type cardinality: int
      :param p: The object property expression on which the maximum cardinality restriction is applied.
      :type p: OWLObjectPropertyExpression
      :param c: The class expression serving as the filler for the restriction.
      :type c: OWLClassExpression

      :return: An empty string.

      :rtype: str



   .. py:method:: get_object_min_cardinality_restriction(cardinality: int, p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression = None) -> str

      This method logs a human-readable representation of an object minimum cardinality restriction based on the provided cardinality, object property expression, and optional class expression filler. It handles the absence of the filler class by logging only the cardinality and property, whereas including the filler results in a more detailed log entry. The function performs a side effect of printing this information via the logging utility and returns an empty string.

      :param cardinality: The minimum cardinality value for the restriction.
      :type cardinality: int
      :param p: The object property expression that defines the property for the restriction.
      :type p: OWLObjectPropertyExpression
      :param c: The class expression that serves as the filler of the restriction.
      :type c: OWLClassExpression

      :return: An empty string.

      :rtype: str



   .. py:method:: get_object_one_of_name(ind_set: set[pyowl2.abstracts.individual.OWLIndividual]) -> str

      Generates a human-readable string representation for an OWL ObjectOneOf class expression based on the provided set of individuals. This method is intended to format the enumeration of individuals into a coherent name, which is useful for displaying or serializing class expressions within the FuzzyOwl2 module. During execution, it logs the input set to the info stream for debugging or tracking purposes. Note that the current implementation returns an empty string, acting as a placeholder for the actual formatting logic.

      :param ind_set: The set of individuals that constitute the enumeration for the ObjectOneOf class expression.
      :type ind_set: set[OWLIndividual]

      :return: A human-readable string representing the name of the ObjectOneOf class expression for the provided set of individuals.

      :rtype: str



   .. py:method:: get_object_property_name(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> str

      Retrieves a human-readable string representation for a given OWL object property expression, handling various types of properties appropriately. The method checks if the expression is the universal (top) or empty (bottom) property and delegates to specific helper methods to retrieve their designated names; otherwise, it treats the expression as an atomic property and retrieves its specific identifier. As a side effect, the method logs the input expression to aid in debugging.

      :param p: The object property expression (atomic, top, or bottom) to retrieve the human-readable name for.
      :type p: OWLObjectPropertyExpression

      :return: The human-readable name of the object property expression.

      :rtype: str



   .. py:method:: get_object_some_values_from_name(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression) -> str

      Generates a human-readable string representation for an OWL existential restriction, specifically the 'ObjectSomeValuesFrom' class expression, based on the provided object property and class filler. The method is designed to format the relationship between the property and the class into a coherent name. It also logs the input arguments for debugging purposes before returning the formatted string.

      :param p: The object property expression acting as the property in the ObjectSomeValuesFrom restriction.
      :type p: OWLObjectPropertyExpression
      :param c: The class expression that serves as the filler for the object some values from restriction.
      :type c: OWLClassExpression

      :return: A human-readable string representing the ObjectSomeValuesFrom restriction for the given property and class expression.

      :rtype: str



   .. py:method:: get_object_union_of_name(operands: set[pyowl2.abstracts.class_expression.OWLClassExpression]) -> str

      Generates a human-readable name for an object union of class expressions based on the provided set of operands. This method processes the input `OWLClassExpression` objects to construct a string representation of their union. The current implementation logs the operands and returns an empty string, serving as a placeholder for the actual naming logic.

      :param operands: The class expressions that constitute the components of the object union.
      :type operands: set[OWLClassExpression]

      :return: A human-readable string representing the name of the object union of the provided class expressions.

      :rtype: str



   .. py:method:: get_short_name(e: pyowl2.abstracts.entity.OWLEntity) -> str

      Computes a concise short name for the given OWL entity by parsing its Internationalized Resource Identifier (IRI). The method isolates the portion of the IRI string that follows the final hash symbol ('#'), effectively extracting the fragment identifier. If the IRI does not contain a hash symbol, the full string representation of the IRI is returned. This operation is side-effect free and is typically used to generate human-readable labels for ontology entities.

      :param e: The entity for which to compute the short name.
      :type e: OWLEntity

      :return: The short name of the entity, corresponding to the fragment identifier of its IRI (the substring after the last '#').

      :rtype: str



   .. py:method:: get_top_concept_name() -> str

      Retrieves the human-readable name of the top concept within the ontology hierarchy. This method is designed to provide the label or identifier of the root concept managed by the FuzzyOwl2 instance. It performs an informational logging operation as a side effect. If the top concept is not set or cannot be resolved, the method returns an empty string.

      :return: The human-readable name of the top concept.

      :rtype: str



   .. py:method:: get_top_data_property_name() -> str

      Retrieves the human-readable name of the top data property within the ontology. This method is intended to provide the identifier for the root data property, which serves as the default parent for the data property hierarchy. In its current state, the method acts as a placeholder that returns an empty string and logs a message, signaling that the implementation for determining the property name is incomplete or intended to be overridden.

      :return: The human-readable name of the top data property.

      :rtype: str



   .. py:method:: get_top_object_property_name() -> str

      This method retrieves the human-readable name of the top object property, which acts as the universal property within the ontology's object property hierarchy. It is typically used during ontology serialization or writing processes to identify the root of the property structure. As a side effect, the method triggers an informational log message and returns the property name as a string.

      :return: The human-readable name of the top object property.

      :rtype: str



   .. py:method:: process_concept_annotations() -> None

      Iterates through the loaded ontologies to identify and process class declarations that define fuzzy concepts via annotations. For each annotated class, the method extracts the annotation value, parses it into a concrete `ConceptDefinition` object, and retrieves the class's short name. Based on the specific type of the parsed concept (e.g., ModifiedConcept, WeightedConcept, or SugenoConcept), the method registers the concept in the `defined_concepts` dictionary and delegates to a specific write method to output the definition. The method includes validation logic that logs errors if a class has multiple annotations or if a fuzzy modifier is undefined, and it raises a ValueError if the parsed concept type does not match any known fuzzy concept categories.

      :raises ValueError: Raised if the parsed concept definition does not match any of the supported concept types.



   .. py:method:: process_datatype_annotations() -> None

      Iterates over the loaded ontologies to identify and process datatype declarations that contain annotations defining fuzzy logic concepts. For each annotated datatype, the method extracts the annotation string, parses it into a specific fuzzy concept (such as a fuzzy datatype or modifier), and retrieves associated numeric facets to define value ranges. The parsed concepts are stored in internal dictionaries, and corresponding definition files are generated based on the specific function type (e.g., triangular, trapezoidal). The method skips datatypes lacking annotations, logs an error if multiple annotations are present, and raises a ValueError if the annotation cannot be parsed into a valid fuzzy concept.

      :raises ValueError: Raised if the parsed annotation value is not a recognized fuzzy datatype or modifier type.



   .. py:method:: process_ontology_annotations() -> None

      Iterates through the loaded ontologies to identify and process annotations specifically associated with the fuzzy label property. For each ontology, it retrieves the available annotations and filters out any that do not match the configured fuzzy label or are missing. The string value of the matching annotations is parsed into a logic representation, which is then written to the output via the internal writer method. This process ensures that only relevant fuzzy logic definitions are extracted and persisted, while skipping ontologies or annotations that do not meet the criteria.



   .. py:method:: process_ontology_axioms() -> None

      Iterates through the loaded ontologies to systematically process and write axioms to the output file, covering the TBox, RBox, and ABox components of the knowledge base. It handles a wide variety of axiom types, including class declarations, property characteristics, and individual assertions, distinguishing between annotated and non-annotated versions of specific relationships. To ensure no redundancy, the method checks an internal set of processed axioms before writing; if an axiom has already been serialized, it is skipped. This process effectively flattens the ontology structure into a serialized format while preserving the logical distinctions defined in the source ontologies.



   .. py:method:: process_property_annotations() -> None

      Iterates through the axioms of all loaded ontologies to identify and process annotations attached to object and data property declarations. For each property, it extracts the annotation value, parses it into a `ModifiedProperty` object, and validates that the associated fuzzy modifier exists within the current context. The method skips properties without annotations and logs an error if multiple annotations are found, though it continues processing using the first one. If the annotation string fails to parse, the method returns immediately; if the parsed object is not a `ModifiedProperty`, a `ValueError` is raised. Upon successful validation, the property is stored in the `defined_properties` dictionary and its definition is written out.

      :raises ValueError: Raised when the parsed annotation for a property does not result in a valid modified property instance.



   .. py:method:: translate_owl2ontology() -> None

      Orchestrates the conversion of the loaded OWL2 ontology into a Fuzzy Description Logic (DL) representation. This method systematically processes various components of the ontology by handling annotations for the ontology itself, datatypes, concepts, and properties, before finally translating the core axioms. It acts as the main entry point for the translation workflow, ensuring that all structural elements are transformed to support fuzzy logic reasoning.



   .. py:method:: write_asymmetric_object_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None

      This method handles the output of an asymmetric object property axiom, indicating that the provided object property expression is asymmetric. It accepts a single argument representing the property and triggers an informational log message to record the axiom's generation. The method performs no validation on the input and returns None, with its primary side effect being the logging operation.

      :param p: The object property expression to be declared asymmetric.
      :type p: OWLObjectPropertyExpression



   .. py:method:: write_choquet_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept.ChoquetConcept) -> None

      Outputs a formatted log message representing the definition of a Choquet concept. This method constructs a string combining the provided name and the string representation of the concept object, then passes it to the logging utility. The primary side effect is the generation of this log entry, typically to standard output or a configured log stream, while the method itself returns no value. The readability of the output depends on the implementation of the string conversion for the provided concept object.

      :param name: The name or label assigned to the Choquet concept.
      :type name: str
      :param c: The Choquet concept instance to be written.
      :type c: ChoquetConcept



   .. py:method:: write_concept_assertion_axiom(i: pyowl2.abstracts.individual.OWLIndividual, c: pyowl2.abstracts.class_expression.OWLClassExpression, d: float) -> None

      This method logs a human-readable representation of a fuzzy concept assertion axiom, associating a specific individual with a class expression at a given degree of membership. It formats the individual, class, and degree into a string indicating the assertion and outputs this information via the logging utility. The function does not perform validation on the inputs or return a value, serving primarily as a diagnostic or informational output mechanism within the FuzzyOwl2 processing workflow.

      :param i: The individual instance that is the subject of the concept assertion.
      :type i: OWLIndividual
      :param c: The OWL class expression representing the concept that the individual is asserted to belong to.
      :type c: OWLClassExpression
      :param d: The degree of membership or truth value for the assertion, representing the extent to which the individual belongs to the concept.
      :type d: float



   .. py:method:: write_concept_declaration(c: pyowl2.abstracts.class_expression.OWLClassExpression) -> None

      Outputs a human-readable trace of a concept declaration by logging the provided OWL class expression. This method accepts an `OWLClassExpression` and generates an informational message containing the concept's string representation, serving as a status update or debug step within the serialization process. It produces no return value and relies on the underlying utility logger to handle the actual display or storage of the message.

      :param c: The OWL class expression to be declared.
      :type c: OWLClassExpression



   .. py:method:: write_crisp_function_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.crisp_function.CrispFunction) -> None

      Generates and logs a human-readable string representation of a specific crisp function definition. By utilizing the `Util.info` utility, this method outputs the provided name alongside the string representation of the `CrispFunction` object, effectively recording the function's details for user inspection or debugging. The operation does not modify any internal state or return a value, serving solely as an informational side effect.

      :param name: The name to assign to the crisp function definition.
      :type name: str
      :param dat: The crisp function instance to be written.
      :type dat: CrispFunction



   .. py:method:: write_data_property_assertion_axiom(i: pyowl2.abstracts.individual.OWLIndividual, lit: pyowl2.literal.literal.OWLLiteral, p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, d: float) -> None

      Generates and outputs a human-readable representation of a fuzzy data property assertion axiom, signifying that a specific data property relates an individual to a literal value with a certain degree of truth. The method constructs a formatted string that includes the individual, the literal, the property expression, and the minimum degree threshold. This representation is then passed to a logging utility to record or display the assertion.

      :param i: The individual that is the subject of the data property assertion.
      :type i: OWLIndividual
      :param lit: The literal value assigned to the individual via the data property.
      :type lit: OWLLiteral
      :param p: The data property expression representing the relationship being asserted between the individual and the literal.
      :type p: OWLDataPropertyExpression
      :param d: The degree (e.g., truth value or membership degree) representing the strength or certainty of the assertion.
      :type d: float



   .. py:method:: write_data_property_declaration(dp: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression) -> None

      Outputs a human-readable declaration for the specified OWL data property expression, typically for logging or serialization purposes. This method invokes the internal logging utility to record the property details, resulting in an I/O side effect rather than a return value. It serves as a specific handler within the FuzzyOwl2 module for visualizing data property structures during ontology processing.

      :param dp: The OWL data property expression to be declared.
      :type dp: OWLDataPropertyExpression



   .. py:method:: write_data_property_domain_axiom(p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression) -> None

      Outputs a human-readable representation of a data property domain axiom to the information log. This method asserts that the provided data property expression is associated with the specified class expression as its domain. The operation results in a side effect of logging the formatted relationship and returns None.

      :param p: The data property expression for which the domain is being specified.
      :type p: OWLDataPropertyExpression
      :param c: The class expression defining the domain of the data property.
      :type c: OWLClassExpression



   .. py:method:: write_data_property_range_axiom(p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, range: pyowl2.abstracts.data_range.OWLDataRange) -> None

      This method processes a data property range axiom by logging the association between a specific data property and its defined data range. It accepts an `OWLDataPropertyExpression` representing the property and an `OWLDataRange` representing the range, then generates an informational message using the `Util.info` utility to record the operation. The function does not return a value, and its primary side effect is the output of this log message, which serves as a human-readable record of the axiom being written.

      :param p: The data property expression for which the range is specified.
      :type p: OWLDataPropertyExpression
      :param range: The data range defining the permissible values for the data property.
      :type range: OWLDataRange



   .. py:method:: write_different_individuals_axiom(ind_set: set[pyowl2.abstracts.individual.OWLIndividual]) -> None

      This method outputs a human-readable representation of a DifferentIndividuals axiom, which asserts that all individuals within the provided set are mutually distinct. It accepts a set of OWLIndividual objects and formats them into a string that is logged via the utility function, serving as a side effect rather than returning a value. The method does not validate the cardinality of the input set; consequently, passing an empty set or a set containing a single individual will result in the logging of a logically vacuous or redundant axiom statement.

      :param ind_set: The collection of individuals asserted to be mutually distinct.
      :type ind_set: set[OWLIndividual]



   .. py:method:: write_disjoint_classes_axiom(class_set: set[pyowl2.abstracts.class_expression.OWLClassExpression]) -> None

      Generates and outputs a human-readable representation of a DisjointClasses axiom based on the provided set of OWL class expressions. The method formats the input set into a string resembling functional syntax and delegates the actual output to a logging utility. It does not perform logical validation on the set, such as checking for a minimum number of classes, and therefore simply serializes the provided arguments as-is.

      :param class_set: The set of classes that are mutually disjoint.
      :type class_set: set[OWLClassExpression]



   .. py:method:: write_disjoint_data_properties_axiom(class_set: set[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]) -> None

      This method processes a set of data properties to represent a disjoint data properties axiom in a human-readable format. It accepts a collection of data property expressions that are defined as mutually exclusive within the ontology. The primary side effect is the generation of an informational log entry detailing the specific properties involved in the axiom, while the method itself returns no value.

      :param class_set: The set of data properties to be declared as pairwise disjoint.
      :type class_set: set[OWLDataPropertyExpression]



   .. py:method:: write_disjoint_object_properties_axiom(class_set: set[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]) -> None

      Logs the processing of a disjoint object properties axiom for a set of object property expressions that are mutually exclusive. This method accepts a set of properties and outputs an informational message containing the set, serving as a notification step within the serialization pipeline. It does not enforce that the set contains sufficient elements to form a valid axiom and returns None.

      :param class_set: The set of object properties that are mutually disjoint.
      :type class_set: set[OWLObjectPropertyExpression]



   .. py:method:: write_disjoint_union_axiom(class_set: set[pyowl2.abstracts.class_expression.OWLClassExpression]) -> None

      Outputs a human-readable representation of a disjoint union axiom by logging the provided set of class expressions. This method utilizes a utility function to format and display the semantic relationship defined by the axiom, ensuring that the collection of classes is presented as a unified disjoint structure. The operation produces a side effect via logging rather than returning a value, and it relies on the standard string conversion of the input set to generate the output message.

      :param class_set: The set of class expressions that constitute the disjoint union.
      :type class_set: set[OWLClassExpression]



   .. py:method:: write_equivalent_classes_axiom(class_set: set[pyowl2.abstracts.class_expression.OWLClassExpression]) -> None

      This method generates a human-readable representation of an EquivalentClasses axiom, asserting that all provided class expressions are semantically identical. It accepts a set of OWLClassExpression objects and outputs the axiom structure to the logging utility. The operation results in a side effect where the axiom details are printed to the standard information stream, but it does not return a value. While the method processes any set of class expressions, the logical integrity of an equivalence axiom generally requires the set to contain at least two classes.

      :param class_set: The set of OWL class expressions that are mutually equivalent.
      :type class_set: set[OWLClassExpression]



   .. py:method:: write_equivalent_data_properties_axiom(class_set: set[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]) -> None

      This method generates a human-readable representation of an equivalent data properties axiom, indicating that all properties within the provided set are semantically equivalent. It accepts a collection of OWL data property expressions and delegates the actual output generation to a logging utility, formatting the input set into a standard string format. The operation produces a side effect of logging the axiom information but returns no value, and it does not perform logical validation on the contents of the property set, such as checking for emptiness or redundancy.

      :param class_set: The set of data property expressions that are asserted to be equivalent.
      :type class_set: set[OWLDataPropertyExpression]



   .. py:method:: write_equivalent_object_properties_axiom(class_set: set[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]) -> None

      Generates a log entry representing an equivalent object properties axiom for the given set of object property expressions. The method formats the input set into a human-readable string indicating the equivalence relationship and outputs it via a logging utility. This function does not return a value and its primary effect is the generation of this informational message.

      :param class_set: The set of object properties that are mutually equivalent in the axiom.
      :type class_set: set[OWLObjectPropertyExpression]



   .. py:method:: write_functional_data_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None

      Generates and logs a human-readable representation of a functional data property axiom, indicating that the provided property can have at most one value for a given individual. The method accepts a property expression as an argument and formats it into a specific string structure, which is then output via the logging utility. This operation results in a side effect of producing a log entry and does not return a value.

      :param p: The object property expression that is functional in the axiom.
      :type p: OWLObjectPropertyExpression



   .. py:method:: write_functional_object_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None

      This method serializes a functional object property axiom by generating a human-readable string representation of the provided object property expression. It formats the input property into a `FunctionalObjectProperty` declaration and outputs this string using the logging utility. The function does not return a value, acting instead as a side effect to record the axiom's definition within the current context.

      :param p: The object property expression to be asserted as functional.
      :type p: OWLObjectPropertyExpression



   .. py:method:: write_fuzzy_logic(logic: str) -> None

      This method outputs the specific fuzzy logic type utilized within the ontology, providing a human-readable confirmation of the configuration. It accepts a string representing the logic (such as Zadeh or Lukasiewicz) and logs this information to the console or log stream as a status update. The function performs no data validation or transformation beyond formatting the message for display and returns no value.

      :param logic: Name or type of the fuzzy logic system employed by the ontology.
      :type logic: str



   .. py:method:: write_fuzzy_nominal_concept_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_nominal_concept.FuzzyNominalConcept) -> None

      Outputs a human-readable representation of a fuzzy nominal concept definition to the logging stream. It constructs an informational message by combining the provided name with the string representation of the `FuzzyNominalConcept` object. This method serves as a side-effecting utility to display the concept definition during processing, rather than returning a value or writing to a file.

      :param name: Identifier for the fuzzy nominal concept being defined.
      :type name: str
      :param dat:
      :type dat: FuzzyNominalConcept



   .. py:method:: write_inverse_functional_object_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None

      Outputs a human-readable representation of an inverse functional object property axiom. This method accepts an object property expression and logs the axiom, indicating that the property is inverse functional—meaning no two distinct individuals can be related to the same individual via the inverse of this property. The operation relies on a utility function to handle the actual output and does not return a value.

      :param p: The object property expression to be declared as inverse functional.
      :type p: OWLObjectPropertyExpression



   .. py:method:: write_inverse_object_property_axiom(p1: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, p2: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None

      Generates and logs a human-readable representation of an inverse object property axiom, asserting that the first provided property is the inverse of the second. This method formats the relationship between the two object property expressions and outputs the result via a logging utility, serving as a side effect rather than returning a value. The operation relies on the string representations of the input properties to construct the output message.

      :param p1: The first object property expression involved in the inverse relationship.
      :type p1: OWLObjectPropertyExpression
      :param p2: The object property expression that serves as the inverse counterpart to the first property.
      :type p2: OWLObjectPropertyExpression



   .. py:method:: write_irreflexive_object_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None

      Outputs a human-readable representation of an irreflexive object property axiom, asserting that the specified property cannot relate an individual to itself. This method accepts an `OWLObjectPropertyExpression` as input and triggers a logging operation to record the axiom's structure. It does not return a value, serving primarily to document or serialize the semantic constraint that the property is irreflexive.

      :param p: The object property expression that is asserted to be irreflexive.
      :type p: OWLObjectPropertyExpression



   .. py:method:: write_left_shoulder_function_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.left_shoulder_function.LeftShoulderFunction) -> None

      Logs the definition of a left shoulder fuzzy logic function in a human-readable format, typically for debugging or informational purposes. It constructs a string representation of the function assignment by combining the provided name with the string representation of the `LeftShoulderFunction` object. The method delegates the output to the logging utility, resulting in a side effect of writing to the standard log stream without returning a value.

      :param name: The name to assign to the left shoulder function definition.
      :type name: str
      :param dat: The left shoulder function instance to be written.
      :type dat: LeftShoulderFunction



   .. py:method:: write_linear_function_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function.LinearFunction) -> None

      Outputs a human-readable representation of a linear function definition to the logging stream by combining the provided name with the string representation of the `LinearFunction` object. This method delegates the actual writing to the `Util.info` utility, formatting the message as "name = dat". It performs no file I/O directly and returns `None`, serving primarily as a diagnostic or informational tool within the broader context of the `FuzzyOwl2` module.

      :param name: The name to assign to the linear function in the definition.
      :type name: str
      :param dat: The linear function object to be defined.
      :type dat: LinearFunction



   .. py:method:: write_linear_modifier_definition(name: str, mod: fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier.LinearModifier) -> None

      Outputs a human-readable representation of a linear modifier definition to the logging stream. This method constructs a formatted string associating the specified name with the string representation of the modifier object and passes it to the logging utility. The operation is performed for side effects such as debugging or user feedback and does not return a value. The clarity of the output relies on the string conversion method of the provided `LinearModifier` instance.

      :param name: The identifier for the linear modifier.
      :type name: str
      :param mod:
      :type mod: fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier.LinearModifier



   .. py:method:: write_modified_concept_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_concept.ModifiedConcept) -> None

      Logs the definition of a modified concept to the standard information output stream. This method formats the provided concept name and the associated ModifiedConcept data structure into a human-readable string, which is then displayed via the utility logging function. It is primarily used for reporting or debugging purposes to visualize the current state of a concept, and it does not modify any internal object state or return a value.

      :param name: Identifier for the modified concept.
      :type name: str
      :param dat: The modified concept object to be written.
      :type dat: fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept.ModifiedConcept



   .. py:method:: write_modified_function_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_function.ModifiedFunction) -> None

      Outputs a human-readable representation of a modified function definition to the logging or information stream. This method constructs a formatted string containing the function name and the `ModifiedFunction` object, then delegates the display to the `Util.info` utility. It serves as a reporting or debugging aid to visualize the function's state without modifying the underlying data, assuming the `ModifiedFunction` object provides a meaningful string representation.

      :param name: The name of the modified function.
      :type name: str
      :param dat: The modified function object to be written.
      :type dat: ModifiedFunction



   .. py:method:: write_modified_property_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property.ModifiedProperty) -> None

      This method logs a human-readable representation of a modified property definition to the system's info output. It formats the provided property name and the `ModifiedProperty` data object into a descriptive string, which is then passed to the utility logging handler. The operation is primarily intended for debugging or tracking purposes, as it produces a side effect of logging without returning a value or modifying the input data.

      :param name: The name of the modified property being defined.
      :type name: str
      :param dat: The modified property object to be written.
      :type dat: ModifiedProperty



   .. py:method:: write_negative_data_property_assertion_axiom(i: pyowl2.abstracts.individual.OWLIndividual, lit: pyowl2.literal.literal.OWLLiteral, p: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, d: float) -> None

      This method generates and logs a human-readable representation of a negative data property assertion axiom within a fuzzy logic context. It constructs a string indicating that the specified individual does not possess the given data property with the provided literal value, associated with a specific degree of truth `d`. The function does not return a value but produces a side effect by invoking the utility logger to display the formatted axiom.

      :param i: The individual subject of the negative data property assertion.
      :type i: OWLIndividual
      :param lit: The literal value that the individual is asserted not to possess.
      :type lit: OWLLiteral
      :param p: The data property expression representing the relationship being negated in the assertion.
      :type p: OWLDataPropertyExpression
      :param d: The degree of truth or threshold value for the negative assertion.
      :type d: float



   .. py:method:: write_negative_object_property_assertion_axiom(i1: pyowl2.abstracts.individual.OWLIndividual, i2: pyowl2.abstracts.individual.OWLIndividual, p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, d: float) -> None

      Outputs a human-readable log entry for a negative object property assertion axiom, incorporating a fuzzy logic degree. The method constructs a string indicating that the specified object property does not relate the first individual to the second individual, accompanied by a threshold degree. This action produces a side effect by invoking `Util.info` to display the formatted axiom, and the function returns None.

      :param i1: The subject individual in the negative object property assertion.
      :type i1: OWLIndividual
      :param i2: The individual that is asserted not to be related to the first individual via the specified property.
      :type i2: OWLIndividual
      :param p: The object property expression representing the relationship being negated between the individuals.
      :type p: OWLObjectPropertyExpression
      :param d: The degree value representing the threshold for the negative assertion.
      :type d: float



   .. py:method:: write_object_property_assertion_axiom(i1: pyowl2.abstracts.individual.OWLIndividual, i2: pyowl2.abstracts.individual.OWLIndividual, p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, d: float) -> None

      Logs a formatted message representing a fuzzy object property assertion axiom that connects two individuals through a specific property. It incorporates a degree of truth value, reflecting the fuzzy nature of the logic, to quantify the strength of the relationship between the subject and object. This operation serves as a side effect to record or display the semantic assertion in a human-readable format without returning a value.

      :param i1: The subject individual of the object property assertion.
      :type i1: OWLIndividual
      :param i2: The individual acting as the object of the object property assertion.
      :type i2: OWLIndividual
      :param p: The object property expression representing the relationship asserted to hold between the two individuals.
      :type p: OWLObjectPropertyExpression
      :param d: The degree of truth or confidence for the assertion, representing a threshold value for the property relationship.
      :type d: float



   .. py:method:: write_object_property_declaration(op: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None

      This method handles the serialization of an object property declaration into a human-readable format, typically as part of generating an ontology representation. It accepts an `OWLObjectPropertyExpression` as input, which defines the property to be declared. During execution, the method logs the specific property being processed, indicating the start of the declaration writing procedure.

      :param op: The object property expression to be declared.
      :type op: OWLObjectPropertyExpression



   .. py:method:: write_object_property_domain_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression) -> None

      Generates and outputs a representation of an object property domain axiom, which constrains the subjects of the given object property to belong to the specified class expression. This method accepts the object property and the class expression as inputs and triggers an informational log entry detailing the relationship. It performs no validation on the inputs and does not return a value, serving primarily as a step in the serialization or processing pipeline for fuzzy OWL ontologies.

      :param p: The object property expression whose domain is being defined.
      :type p: OWLObjectPropertyExpression
      :param c: The class expression representing the domain of the object property.
      :type c: OWLClassExpression



   .. py:method:: write_object_property_range_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, c: pyowl2.abstracts.class_expression.OWLClassExpression) -> None

      This method handles the serialization of an object property range axiom, which defines the class of values that a specific object property can take. It accepts an object property expression and a class expression, formatting them into a descriptive string that represents the range constraint. The operation triggers a logging event to output this information, serving as a side effect rather than returning a value.

      :param p: The object property expression for which the range is being defined.
      :type p: OWLObjectPropertyExpression
      :param c: The class expression specifying the range of the object property.
      :type c: OWLClassExpression



   .. py:method:: write_owa_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept.OwaConcept) -> None

      Generates and outputs a human-readable representation of an Ordered Weighted Averaging (OWA) concept definition to the logging utility. It accepts a string name and the concept object, formatting them into a status message that reflects the current definition. This operation is intended for informational purposes, such as debugging or progress tracking, and does not alter the state of the input parameters or return a value.

      :param name: The identifier or label for the OWA concept being defined.
      :type name: str
      :param c: The OWA concept instance to be defined.
      :type c: fuzzy_dl_owl2.fuzzydl.concept.owa_concept.OwaConcept



   .. py:method:: write_qowa_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.qowa_concept.QowaConcept) -> None

      Outputs the definition of a quasi OWA concept to the logging or information stream. This method constructs a human-readable string by combining the provided name with the string representation of the `QowaConcept` object and passes it to the utility logger. It does not return a value or modify internal state, serving solely to display the concept definition for debugging or informational purposes.

      :param name: The identifier or label for the quasi OWA concept.
      :type name: str
      :param c: The quasi OWA concept to be defined.
      :type c: fuzzy_dl_owl2.fuzzydl.concept.qowa_concept.QowaConcept



   .. py:method:: write_quasi_sugeno_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept.QsugenoConcept) -> None

      Outputs a human-readable representation of a fuzzy logic concept definition by logging a formatted string that associates the provided name with the concept object. This operation relies on the string conversion of the concept instance to ensure readability and serves primarily as a diagnostic or informational step within the broader processing workflow. The method produces a side effect of generating log output and does not return any value.

      :param name: Label used to identify the quasi Sugeno concept in the definition.
      :type name: str
      :param c: The specific concept instance to be defined.
      :type c: QsugenoConcept



   .. py:method:: write_reflexive_object_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None

      Outputs a human-readable representation of a reflexive object property axiom, indicating that the specified property relates every individual in the domain to itself. This method accepts an object property expression and delegates the formatting and logging of the axiom to the utility handler. It functions as part of the ontology serialization process, ensuring that reflexive property constraints are explicitly recorded without returning a value.

      :param p: The object property expression to be asserted as reflexive.
      :type p: OWLObjectPropertyExpression



   .. py:method:: write_right_shoulder_function_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.right_shoulder_function.RightShoulderFunction) -> None

      Outputs a human-readable representation of a right shoulder function definition to the logging system. It accepts a string identifier for the function and the function object itself, formatting them into a descriptive message that associates the name with the function's parameters. The method performs this action as a side effect via a utility logger and returns no value.

      :param name: Identifier for the right shoulder function definition.
      :type name: str
      :param dat: The specific right shoulder function instance to be defined.
      :type dat: RightShoulderFunction



   .. py:method:: write_same_individual_axiom(ind_set: set[pyowl2.abstracts.individual.OWLIndividual]) -> None

      Outputs a log entry representing an assertion that a specific group of individuals are identical. The method accepts a collection of individual entities and formats them into a standardized string indicating a "SameIndividual" relationship. This operation is primarily for logging or display purposes, as it invokes a utility function to print the information rather than modifying the ontology structure directly or returning a result. The method relies on the string representation of the input set for formatting.

      :param ind_set: The set of individuals asserted to be identical.
      :type ind_set: set[OWLIndividual]



   .. py:method:: write_sub_data_property_of_axiom(subproperty: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, superproperty: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, d: float) -> None

      This method generates and logs a human-readable representation of a fuzzy sub-data-property axiom within the context of a Fuzzy OWL 2 ontology. It accepts a subproperty and a superproperty, both defined as OWL data property expressions, along with a floating-point value representing the degree of truth or membership for the relationship. The method constructs a string indicating that the subproperty is a subclass of the superproperty with a degree greater than or equal to the specified value and outputs this information using the `Util.info` logging utility. As a side effect, this operation produces a log entry but does not return a value.

      :param subproperty: The data property that is a subproperty of the superproperty.
      :type subproperty: OWLDataPropertyExpression
      :param superproperty: The more general data property expression that the subproperty is a subset of.
      :type superproperty: OWLDataPropertyExpression
      :param d: The degree or threshold value indicating the strength of the subproperty relationship.
      :type d: float



   .. py:method:: write_sub_object_property_of_axiom(subproperty: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, superproperty: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, d: float) -> None

      Outputs a human-readable log entry representing a fuzzy sub-object property axiom, asserting that the specified sub-property is a specialization of the super-property with a specific degree of truth. The method formats the sub-property, super-property, and the degree value into a descriptive string and passes it to the logging utility. This operation produces no return value and relies on the string representations of the input property expressions for the generated output.

      :param subproperty: The object property expression that is a subclass of the superproperty.
      :type subproperty: OWLObjectPropertyExpression
      :param superproperty: The object property expression representing the parent or more general property in the subproperty relationship.
      :type superproperty: OWLObjectPropertyExpression
      :param d: The degree of truth or threshold value associated with the subsumption relationship.
      :type d: float



   .. py:method:: write_sub_property_chain_of_axiom(chain: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression], superproperty: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, d: float) -> None

      Generates and logs a human-readable representation of a fuzzy sub-property chain axiom. This method constructs a string indicating that a specific chain of object properties is a sub-property of a given superproperty, associated with a specified degree of truth or membership. It outputs this formatted axiom using the logging utility, serving primarily as a diagnostic or informational action rather than modifying the ontology structure. The method relies on the string representations of the provided property expressions for the output format.

      :param chain: The sequence of object properties that compose the chain in the SubPropertyChainOf axiom.
      :type chain: list[OWLObjectPropertyExpression]
      :param superproperty: The object property expression that the property chain is a sub-property of.
      :type superproperty: OWLObjectPropertyExpression
      :param d: The degree or truth value associated with the sub property chain axiom.
      :type d: float



   .. py:method:: write_subclass_of_axiom(subclass: pyowl2.abstracts.class_expression.OWLClassExpression, superclass: pyowl2.abstracts.class_expression.OWLClassExpression, d: float) -> None

      Outputs a human-readable representation of a fuzzy subclass axiom defined by the given subclass, superclass, and degree of truth. The method formats the relationship as a threshold condition, indicating that the subclass relationship holds with a degree greater than or equal to the specified value. This operation results in a logging side effect via a utility function and does not return a value.

      :param subclass: The class expression representing the subclass in the axiom.
      :type subclass: OWLClassExpression
      :param superclass: The parent class or general concept that the subclass is asserted to be a subset of.
      :type superclass: OWLClassExpression
      :param d: The degree or threshold value representing the minimum level of truth or confidence for the subclass relationship.
      :type d: float



   .. py:method:: write_sugeno_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept.SugenoConcept) -> None

      Generates a human-readable log entry representing the definition of a specific Sugeno concept. It constructs an informational message by combining the provided name with the string representation of the SugenoConcept instance, effectively outputting the assignment syntax. This method serves as a utility for logging or debugging the current state of fuzzy logic definitions without modifying the underlying data structure.

      :param name: The identifier or label assigned to the Sugeno concept.
      :type name: str
      :param c:
      :type c: SugenoConcept



   .. py:method:: write_symmetric_object_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None

      This method generates and logs a human-readable representation of a symmetric object property axiom. It accepts an object property expression as input and formats it into a standard axiom string, which is then output via the logging utility. The function does not return a value and relies on the provided property expression being valid for string formatting. This serves as a step in the broader process of serializing ontology axioms in the FuzzyOwl2 environment.

      :param p: The object property expression that is symmetric.
      :type p: OWLObjectPropertyExpression



   .. py:method:: write_transitive_object_property_axiom(p: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression) -> None

      Serializes a transitive object property axiom to a human-readable format, indicating that the relationship defined by the given property is transitive. It accepts an object property expression representing the property to be characterized as transitive. Instead of returning a value, the method triggers a logging action via the utility module to output the formatted axiom string.

      :param p: The object property expression to be declared transitive.
      :type p: OWLObjectPropertyExpression



   .. py:method:: write_trapezoidal_function_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.trapezoidal_function.TrapezoidalFunction) -> None

      Outputs a human-readable representation of a trapezoidal function definition to the logging system. It constructs a log message combining the specified name and the trapezoidal function data structure, then passes this message to the utility info handler. This action is a side effect intended for informational tracking or debugging, as the method does not return a value or modify the input data.

      :param name: The name to assign to the trapezoidal function in the definition.
      :type name: str
      :param dat: The trapezoidal function to be defined.
      :type dat: TrapezoidalFunction



   .. py:method:: write_triangular_function_definition(name: str, dat: fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_function.TriangularFunction) -> None

      Logs the definition of a triangular function in a human-readable format for diagnostic or informational purposes. It constructs a string representation combining the provided name and the TriangularFunction object, then delegates the output to the `Util.info` utility. This method does not modify the object's state or return a value; its primary side effect is the generation of a log entry. The clarity of the output depends on the string representation implementation of the `TriangularFunction` instance.

      :param name: The identifier or label to assign to the triangular function in the generated definition string.
      :type name: str
      :param dat: The triangular function instance to be written.
      :type dat: TriangularFunction



   .. py:method:: write_triangular_modifier_definition(name: str, mod: fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_modifer.TriangularModifier) -> None

      This method generates a human-readable definition of a triangular modifier and outputs it via the logging utility. It constructs a string representation by combining the provided name with the string representation of the modifier object, formatted as "name = modifier". The primary side effect is the emission of this information to the standard output or log stream, which is useful for debugging or tracking the configuration of fuzzy logic components. The output format depends implicitly on the string conversion logic of the provided `TriangularModifier` instance.

      :param name: Identifier for the triangular modifier.
      :type name: str
      :param mod: The triangular modifier instance to be defined.
      :type mod: fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier.TriangularModifier



   .. py:method:: write_weighted_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_concept.WeightedConcept) -> None

      Logs a human-readable representation of a weighted concept definition to the information stream. The method constructs a message associating the provided name with the string representation of the WeightedConcept object, which is then processed by the logging utility. This operation serves as a side effect for debugging or status reporting and does not return a value or modify the input object.

      :param name: The name or identifier assigned to the weighted concept.
      :type name: str
      :param c: The weighted concept object to be defined.
      :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_concept.WeightedConcept



   .. py:method:: write_weighted_max_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_max_concept.WeightedMaxConcept) -> None

      Outputs a human-readable log entry representing the definition of a weighted max concept. It accepts a string identifier and the corresponding concept object, formatting them into a message that indicates the definition is being written. This method relies on the string representation of the concept object and produces no return value, serving primarily as a side effect to inform the user or system of the current state.

      :param name: The identifier assigned to the weighted max concept.
      :type name: str
      :param c: The weighted max concept instance to be defined.
      :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_max_concept.WeightedMaxConcept



   .. py:method:: write_weighted_min_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_min_concept.WeightedMinConcept) -> None

      Generates and logs a human-readable string representation of a weighted minimum concept definition using the provided name and concept object. The method formats the output as "name = concept" and delegates the actual writing to a utility logging function. This operation produces a side effect by outputting information to the standard info stream but does not modify the state of the instance or the concept object.

      :param name: The name to assign to the weighted min concept in the definition.
      :type name: str
      :param c: The weighted min concept instance to be written.
      :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept.WeightedMinConcept



   .. py:method:: write_weighted_sum_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_concept.WeightedSumConcept) -> None

      This method outputs a human-readable definition of a weighted sum concept to the logging system, serving primarily as a diagnostic or informational utility. It accepts a string identifier and a `WeightedSumConcept` instance, formatting them into a message that displays the concept's definition alongside its name. The operation relies on the `Util.info` method to handle the actual output, meaning the side effect is the generation of a log entry rather than a direct modification of system state or file content. The clarity of the output depends on the string representation implementation of the `WeightedSumConcept` object.

      :param name: Identifier for the weighted sum concept being defined.
      :type name: str
      :param c: The weighted sum concept to be defined.
      :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_concept.WeightedSumConcept



   .. py:method:: write_weighted_sum_zero_concept_definition(name: str, c: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_zero_concept.WeightedSumZeroConcept) -> None

      Outputs a log message describing the definition of a weighted sum zero concept in a human-readable format. This method formats the provided name and the concept object into a string indicating the definition is being written and passes it to the utility logging function. It produces a side effect of displaying information to the user or log stream without modifying the object's state or returning a value.

      :param name: The identifier or label for the weighted sum zero concept.
      :type name: str
      :param c: The weighted sum zero concept to be defined.
      :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_zero_concept.WeightedSumZeroConcept



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

