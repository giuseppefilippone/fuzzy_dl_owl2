fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2
=====================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2



.. ── LLM-GENERATED DESCRIPTION START ──

Converts a FuzzyDL knowledge base into a standard OWL2 ontology by mapping fuzzy logic concepts, roles, and axioms to their semantic web equivalents while preserving fuzzy semantics through XML annotations.


Description
-----------


A specialized translation engine transforms FuzzyDL knowledge bases into OWL2 ontologies, bridging the gap between fuzzy description logic and standard semantic web formats. Because standard OWL2 lacks native support for fuzzy logic, the software preserves the semantics of fuzzy modifiers, weighted concepts, and truth degrees by embedding them as structured XML annotations within the generated ontology entities. The process involves parsing the input file to extract definitions of concepts, roles, and individuals, then systematically mapping these to OWL classes, properties, and named individuals. Complex fuzzy constructs, such as quantified OWA or Choquet integrals, are nominalized into new atomic classes that carry the specific fuzzy logic definitions as metadata. Finally, the resulting ontology, populated with axioms ranging from subclass relationships to property assertions, is serialized to a specified output file for use in standard semantic web applications.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2.FuzzydlToOwl2


Functions
---------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2.main


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_fuzzydl_to_owl2_FuzzydlToOwl2.png
       :alt: UML Class Diagram for FuzzydlToOwl2
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FuzzydlToOwl2**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_fuzzydl_to_owl2_FuzzydlToOwl2.pdf
       :alt: UML Class Diagram for FuzzydlToOwl2
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FuzzydlToOwl2**

.. py:class:: FuzzydlToOwl2(input_file: str, output_file: str, base_iri: str = 'http://www.semanticweb.org/ontologies/fuzzydl_ontology#')

   This class acts as a converter that transforms a FuzzyDL knowledge base into an OWL2 ontology, bridging the gap between fuzzy logic representations and standard semantic web structures. It parses the input FuzzyDL file to extract elements such as concepts, roles, individuals, and axioms, mapping them to corresponding OWL2 entities like classes, properties, and named individuals. Because standard OWL2 does not natively support fuzzy logic, the class preserves the original semantics by embedding fuzzy logic details—such as truth degrees, modifiers, and complex concept definitions—directly into the ontology as annotations. The conversion process is initiated by instantiating the class with the input and output file paths and an optional base IRI, followed by calling the `run` method to populate the ontology and save the result.

   :param base_iri: The base Internationalized Resource Identifier (IRI) defining the namespace for the OWL2 ontology, used to generate unique identifiers for classes, properties, and individuals.
   :type base_iri: typing.Any
   :param num_classes: Counter used to track the number of newly generated atomic classes and assign unique identifiers to them.
   :type num_classes: int
   :param kb: The FuzzyDL knowledge base object parsed from the input file, serving as the source data for the OWL2 ontology conversion.
   :type kb: typing.Any
   :param _: A throwaway variable used to discard the second return value from the DLParser.get_kb method.
   :type _: typing.Any
   :param ontology_path: The base IRI string for the ontology, used to construct IRIs for ontology entities.
   :type ontology_path: str
   :param ontology_iri: The IRI identifying the generated OWL2 ontology, serving as the base namespace for constructing IRIs for ontology entities.
   :type ontology_iri: IRI
   :param ontology: The OWL2 ontology instance that holds the axioms, classes, and properties generated from the FuzzyDL knowledge base.
   :type ontology: OWLOntology
   :param fuzzyLabel: The annotation property used to attach fuzzy logic semantics, such as degrees or modifiers, to entities and axioms within the generated ontology.
   :type fuzzyLabel: OWLAnnotationProperty
   :param concepts: Registry mapping concept names to their corresponding OWL class expressions to ensure consistent reuse during the conversion process.
   :type concepts: dict[str, OWLClassExpression]
   :param datatypes: A dictionary mapping string representations of FuzzyDL concrete concepts to their corresponding OWL datatype objects, used to track and retrieve datatypes during the conversion process.
   :type datatypes: dict[str, OWLDatatype]
   :param modifiers: A mapping of modifier names to the OWL datatypes representing them in the ontology.
   :type modifiers: dict[str, OWLDatatype]
   :param input_FDL: The path to the input FuzzyDL knowledge base file.
   :type input_FDL: str
   :param output_FOWL: The file path where the generated OWL2 ontology will be saved, constructed by combining the results directory with the output filename.
   :type output_FOWL: str

   :raises Exception: Raised when an unexpected error occurs during the conversion process, specifically if the ontology cannot be saved to the output file.
   :raises ValueError: Raised if the argument provided to `get_class` is not a string or a `Concept` object, if incompatible property types are used in a sub-property relationship, or if an unknown modifier type is encountered during processing.


   .. py:method:: __get_class_1(name: str) -> pyowl2.abstracts.class_expression.OWLClassExpression

      Creates an OWL class expression for the specified name by generating an IRI and instantiating an OWLClass object. This method modifies the ontology by adding a declaration axiom for the class, which includes an RDFS label annotation set to the input name. It returns the resulting OWL class, ensuring it is explicitly defined within the ontology's structure.

      :param name: The identifier for the class, used to construct its IRI and assign its English RDFS label.
      :type name: str

      :return: The OWL class instance created for the specified name.

      :rtype: OWLClassExpression



   .. py:method:: __get_class_2(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> pyowl2.abstracts.class_expression.OWLClassExpression

      Converts a FuzzyDL `Concept` instance into the corresponding OWL 2 `OWLClassExpression` by inspecting the concept's type and recursively processing its components. For atomic concepts, it retrieves or creates an `OWLClass` and adds a declaration axiom with an RDFS label to the ontology. Logical constructs such as conjunctions, disjunctions, and complements are mapped to OWL intersection, union, and complement expressions, respectively. The method distinguishes between object and data properties when handling existential (`SOME`) and universal (`ALL`) restrictions. Fuzzy logic-specific constructs, including modified concepts, weighted concepts, and various aggregators, are handled by generating new atomic classes and attaching specialized XML annotations to preserve fuzzy semantics. Additionally, it manages value restrictions and self-restrictions, delegating complex fuzzy aggregators to helper methods.

      :param c: The concept to be converted into an OWL class expression.
      :type c: Concept

      :return: The OWL 2 class expression corresponding to the input Concept, handling atomic classes, logical operators, restrictions, and fuzzy logic extensions.

      :rtype: OWLClassExpression



   .. py:method:: __get_class_q_owa(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> pyowl2.abstracts.class_expression.OWLClassExpression

      Converts a `Concept` object representing a Quantified Ordered Weighted Averaging (OWA) operator into a corresponding `OWLClassExpression`. The method first verifies that the input concept is of the correct type; if the type does not match `QUANTIFIED_OWA`, it returns `None`. Upon validation, it generates a new atomic OWL class and constructs a specific XML annotation that encapsulates the fuzzy logic semantics, including the quantifier value and the list of constituent concepts. This XML annotation is then attached to the new class entity as a side effect before the class expression is returned.

      :param c: The Quantified OWA concept providing the quantifier and constituent concepts required to generate the OWL class expression.
      :type c: Concept

      :return: Returns a new atomic OWL class expression representing the Quantified OWA concept, annotated with the quantifier and constituent concepts.

      :rtype: OWLClassExpression



   .. py:method:: __get_class_weighted(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> pyowl2.abstracts.class_expression.OWLClassExpression

      Generates an OWL class expression for specific weighted fuzzy concept types, including OWA, Choquet Integral, Sugeno Integral, and Quasi Sugeno Integral. The method creates a new atomic class corresponding to the input concept and attaches a detailed XML annotation to it; this annotation encodes the specific aggregation type, the list of weights, and the base concepts involved in the aggregation. If the input concept type is not one of the supported weighted types, the method returns None.

      :param c: The weighted concept (e.g., OWA, Choquet, or Sugeno Integral) providing the weights and constituent concepts required to construct the OWL class expression.
      :type c: Concept

      :return: An OWL class expression representing the input weighted concept, annotated with the specific fuzzy logic definition (weights and sub-concepts).

      :rtype: OWLClassExpression



   .. py:method:: __get_class_weighted_min_max_sum(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> pyowl2.abstracts.class_expression.OWLClassExpression

      Converts a FuzzyDL concept representing a weighted aggregation operation—specifically weighted minimum, maximum, sum, or sum zero—into a corresponding OWL 2 class expression. This process involves creating a new atomic class to serve as the representation of the fuzzy concept and attaching a detailed XML annotation to it. The annotation encodes the specific type of aggregation, the weights assigned to each sub-concept, and the IRIs of the base concepts involved in the operation. If the input concept's type does not match one of the supported weighted aggregation types, the method returns None. As a side effect, this method modifies the ontology by adding the generated annotation to the newly created class entity.

      :param c: The fuzzy concept defining a weighted aggregation operation (min, max, sum, or sum zero) containing the sub-concepts and their associated weights.
      :type c: Concept

      :return: A new OWL class expression representing the fuzzy weighted concept, annotated with the aggregation type, weights, and base concepts. Returns None if the input concept type is not supported.

      :rtype: OWLClassExpression



   .. py:method:: _get_concrete_concept_specifics(c: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept) -> tuple[str, dict[str, str]]

      Extracts the type identifier and associated parameters for a given fuzzy concrete concept to facilitate translation into the OWL2 format. The method inspects the runtime type of the input concept to determine the appropriate fuzzy shape—such as crisp, left-shoulder, right-shoulder, triangular, or trapezoidal—and maps its numeric attributes to a standardized dictionary keyed by OWL2 keywords. If the input concept does not correspond to any of the expected concrete types, the method returns an empty type string and an empty parameter dictionary as a fallback.

      :param c: The fuzzy concrete concept instance to be processed to extract its specific type and parameters.
      :type c: FuzzyConcreteConcept

      :return: A tuple containing the concept type identifier and a dictionary of its specific parameters. If the concept type is not recognized, returns an empty string and an empty dictionary.

      :rtype: tuple[str, dict[str, str]]



   .. py:method:: _process_assertion(ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None

      Converts a FuzzyDL assertion into an OWL 2 Class Assertion Axiom and adds it to the internal ontology. The method retrieves the corresponding OWL individual and class expression for the assertion's subject and concept. It specifically handles fuzzy membership degrees by checking the assertion's lower limit; if the degree is not exactly 1.0, it generates and attaches annotations to the axiom to represent this fuzzy value. The resulting axiom is then persisted to the ontology as a side effect of this operation.

      :param ass: The assertion object providing the individual, concept, and degree data used to construct an OWL class assertion axiom.
      :type ass: Assertion



   .. py:method:: _process_concrete_concept(c: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept) -> None

      Processes a FuzzyDL concrete concept by generating a corresponding OWL2 datatype definition restricted to a specific numeric interval. The method creates a datatype identified by the concept's IRI and constrains it to values between `c.k1` and `c.k2` using XSD integer facets. It adds the necessary declaration and datatype definition axioms to the ontology, including an RDFS label for the concept. Furthermore, it constructs a FuzzyXML annotation describing the datatype specifics and attaches it to the entity. As a side effect, the method updates the internal `datatypes` dictionary to map the concept string to the newly created OWL datatype.

      :param c: The fuzzy concrete concept providing the interval bounds and specific details required to define and register the corresponding OWL datatype.
      :type c: FuzzyConcreteConcept



   .. py:method:: _process_individual(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual) -> None

      Converts a FuzzyDL individual into corresponding OWL 2 axioms and adds them to the ontology. The method retrieves or creates the primary OWL named individual and iterates through its associated role relations. For each relation, it ensures the corresponding property and target individual exist, then constructs a property assertion axiom. If the relation has a fuzzy degree value other than one, the method attaches annotations to the axiom before adding it to the ontology.

      :param ind: The individual object containing role relations to be transformed into OWL property assertions and added to the ontology.
      :type ind: Individual



   .. py:method:: _process_modifier(mod: fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier) -> None

      Converts a fuzzy logic modifier into an OWL 2 datatype representation and integrates it into the current ontology. The method constructs an XML annotation specific to the modifier's type—supporting linear and triangular shapes—and uses it to annotate the newly created datatype. It registers the datatype within the internal modifiers dictionary and adds a declaration axiom with an English label to the ontology. If the provided modifier is not a recognized type, a ValueError is raised.

      :param mod: The fuzzy logic modifier instance (e.g., Linear or Triangular) containing parameters required to construct the corresponding OWL datatype and XML representation.
      :type mod: Modifier

      :raises ValueError: Raised when the provided modifier is not an instance of `LinearModifier` or `TriangularModifier`.



   .. py:method:: add_entity_annotation(annotation: str, entity: pyowl2.abstracts.entity.OWLEntity) -> None

      Associates a textual annotation with a specific OWL entity within the internal ontology structure. The method accepts a string representing the annotation content and the target entity, converting the string into a formal OWLAnnotation object before attaching it. This operation directly mutates the ontology by adding the annotation to the specified element, ensuring the metadata is persisted as part of the entity's definition.

      :param annotation: The text content of the annotation to be added.
      :type annotation: str
      :param entity: The target OWL entity to which the annotation will be attached.
      :type entity: OWLEntity



   .. py:method:: add_ontology_annotation(annotation: str) -> None

      Appends a descriptive annotation to the OWL 2 ontology currently being constructed by the converter. This method accepts a string representing the annotation text, transforms it into a formal `OWLAnnotation` object using the internal `to_owl_annotation` utility, and directly mutates the internal ontology state by attaching the result. The operation modifies the ontology in place, ensuring the metadata is integrated into the final structure without returning a value.

      :param annotation: The textual content of the annotation to be added to the ontology.
      :type annotation: str



   .. py:method:: annotate_gci(gci: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion) -> None

      Converts a General Concept Inclusion (GCI) into an OWL 2 SubClassOf axiom and adds it to the internal ontology. The method retrieves the subsumed and subsumer concepts from the provided GCI and checks its associated degree. If the degree is not equal to one, indicating a non-crisp fuzzy relationship, the method generates specific annotations representing that degree and attaches them to the axiom; otherwise, a standard unannotated axiom is created. This process directly modifies the ontology by persisting the newly constructed axiom.

      :param gci: The General Concept Inclusion object providing the subsumed class, subsumer class, and degree information required to construct an OWL subclass axiom.
      :type gci: GeneralConceptInclusion



   .. py:method:: annotate_pcd(c1: pyowl2.abstracts.class_expression.OWLClassExpression, pcd: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition) -> None

      This method processes a Primitive Concept Definition (PCD) to generate and register a subclass axiom within the ontology. It constructs an axiom asserting that the provided class expression is a subclass of the class defined within the PCD. If the PCD specifies a degree of membership that is not exactly 1.0, indicating a non-crisp relationship, the method generates and attaches specific annotations to the axiom to encode this fuzzy value. The resulting axiom is then added to the internal ontology, modifying its state.

      :param c1: The class expression to serve as the subclass in the generated axiom.
      :type c1: OWLClassExpression
      :param pcd: The primitive concept definition providing the definition and degree used to construct and annotate the subclass axiom.
      :type pcd: PrimitiveConceptDefinition



   .. py:method:: annotation_property_iri(o: object) -> pyowl2.base.iri.IRI

      Generates an Internationalized Resource Identifier (IRI) for a given annotation property object during the conversion process. This method acts as a specialized wrapper that delegates the core logic to the internal `iri` method, explicitly passing the `OWLAnnotationProperty` type to ensure the resulting IRI conforms to the specific naming conventions and structure required for annotation properties in OWL2. The behavior and validity of the returned IRI depend on the underlying implementation of the `iri` method and the structure of the input object.

      :param o: The annotation property object to convert to an IRI.
      :type o: object

      :return: The IRI corresponding to the provided annotation property object.

      :rtype: IRI



   .. py:method:: class_iri(o: object) -> pyowl2.base.iri.IRI

      Generates an Internationalized Resource Identifier (IRI) corresponding to a specific class object during the translation from FuzzyDL to OWL2. This method acts as a specialized wrapper around the generic IRI generation logic, passing the provided object along with the `OWLClass` type indicator to ensure the resulting identifier is formatted correctly for an OWL class. While the method itself does not perform direct validation or mutation of the input object, it relies on the underlying `iri` method to handle the specific string construction and namespace management.

      :param o: The object representing the class to be converted to an IRI.
      :type o: object

      :return: The IRI string representing the provided class object.

      :rtype: IRI



   .. py:method:: data_property_iri(o: object) -> pyowl2.base.iri.IRI

      Generates an Internationalized Resource Identifier (IRI) for a given data property object, facilitating its representation within an OWL2 ontology. This method delegates the core logic to the internal `iri` method, passing the `OWLDataProperty` type constant to ensure the resulting identifier is semantically typed correctly. It serves as a specific handler for data properties during the broader translation of FuzzyDL entities into OWL2.

      :param o: The data property object to be converted to an IRI string.
      :type o: object

      :return: The IRI representing the OWL data property corresponding to the input object.

      :rtype: IRI



   .. py:method:: datatype_iri(o: object) -> pyowl2.base.iri.IRI

      Generates an Internationalized Resource Identifier (IRI) for a specific datatype object provided as input. This process involves delegating to the underlying `iri` method, supplying the object and the `OWLDatatype` type hint to ensure the resulting identifier adheres to the appropriate OWL2 standards and namespaces. The method serves as a specialized wrapper to handle the conversion of datatype entities specifically, distinguishing them from other ontology elements.

      :param o: The datatype object to be converted to an IRI.
      :type o: object

      :return: The IRI corresponding to the specified datatype object.

      :rtype: IRI



   .. py:method:: exist_data_property(role: str) -> bool

      Verifies the existence of a data property within the loaded ontology by resolving the provided string identifier to its corresponding IRI. This method acts as a wrapper around the ontology's internal getter, translating the human-readable role name into a formal URI reference to perform the check. The operation is read-only and has no side effects on the ontology state; it returns `True` if the property is found and `False` otherwise, handling cases where the input name does not map to any defined entity.

      :param role: The name of the data property to check for existence.
      :type role: str

      :return: True if the data property identified by the specified role exists, False otherwise.

      :rtype: bool



   .. py:method:: exist_object_property(role: str) -> bool

      Verifies the presence of an object property within the loaded ontology by resolving the provided role name to its corresponding Internationalized Resource Identifier (IRI). This method performs a read-only query against the underlying data structure, returning True if the property is found and False otherwise. It relies on the internal IRI generation logic to correctly map the input string to the ontology's namespace, and it does not modify the ontology's contents during the check.

      :param role: The name of the object property to check for existence.
      :type role: str

      :return: True if the object property identified by the given role exists in the ontology, False otherwise.

      :rtype: bool



   .. py:method:: get_annotations_for_axiom(value: Union[float, fuzzy_dl_owl2.fuzzydl.degree.degree_numeric.DegreeNumeric]) -> set[pyowl2.base.annotation.OWLAnnotation]

      This method constructs an OWL annotation that encapsulates the degree of truth for a fuzzy logic axiom, facilitating the translation of fuzzy constraints into the OWL2 format. It accepts either a raw numeric value or a `DegreeNumeric` object, extracting the underlying numerical representation in the latter case. By generating a specific XML structure that defines the axiom type and its associated degree value, the method converts this data into an `OWLAnnotation` object. The resulting annotation is returned within a set to conform to standard OWL API expectations for axiom annotations.

      :param value: The degree value for the axiom, provided as either a float or a DegreeNumeric object.
      :type value: typing.Union[float, DegreeNumeric]

      :return: A singleton set containing an OWLAnnotation that represents the specified fuzzy degree value for an axiom.

      :rtype: set[OWLAnnotation]



   .. py:method:: get_base(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> pyowl2.abstracts.class_expression.OWLClassExpression

      Retrieves or generates an OWL class expression corresponding to the provided FuzzyDL concept. If the input concept is atomic, the method returns the standard OWL class associated with the concept's string identifier. Conversely, if the concept is non-atomic (complex), the method creates a new atomic OWL class to serve as a proxy for the complex expression, effectively nominalizing it for the target ontology. This process may involve side effects such as registering new class declarations within the translation context to ensure the generated class is valid and accessible.

      :param c: The concept to be mapped to its corresponding OWL class expression.
      :type c: Concept

      :return: The OWL class expression representing the base class of the concept. Returns an existing class if the concept is atomic, or a newly generated atomic class otherwise.

      :rtype: OWLClassExpression



   .. py:method:: get_class(name: str) -> pyowl2.abstracts.class_expression.OWLClassExpression
                  get_class(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> pyowl2.abstracts.class_expression.OWLClassExpression

      Retrieves or constructs an OWL class expression based on the provided input, which can be either a string identifier or a Concept object. The method delegates the specific logic to internal helper methods depending on the type of the argument. It enforces strict type checking and raises a ValueError if the input is not a string or a Concept instance.

      :param arg: The class name as a string or a Concept object.
      :type arg: typing.Union[str, Concept]

      :raises ValueError: If the provided argument is not a string or a Concept object.

      :return: The OWL class expression corresponding to the provided name or concept, creating it if it does not already exist.

      :rtype: OWLClassExpression



   .. py:method:: get_data_property(role: str) -> Union[pyowl2.expressions.data_property.OWLDataProperty, pyowl2.expressions.object_property.OWLObjectProperty]

      Retrieves or creates an OWL data property corresponding to the specified role name. If a property with the same name is already registered as an object property, the method returns that existing object property instead of creating a new data property. When a new data property is created, the method updates the ontology by adding a declaration axiom and an RDFS label annotation derived from the role name.

      :param role: The identifier for the data property, used to generate its IRI and RDFS label. If a property with this name already exists, it is returned instead of creating a new one.
      :type role: str

      :return: The property corresponding to the role name. Returns an existing object property if found, otherwise creates and returns a new data property.

      :rtype: typing.Union[OWLDataProperty, OWLObjectProperty]



   .. py:method:: get_individual(name: str) -> pyowl2.individual.named_individual.OWLNamedIndividual

      Retrieves or instantiates a named individual within the ontology using the provided string identifier. The method generates an IRI for the individual and ensures its formal declaration by adding a corresponding axiom to the ontology's internal structure. As a side effect, it also attaches an RDFS label annotation to the individual, using the input name as the literal value with an English language tag. This process modifies the ontology state, potentially resulting in duplicate declarations if the individual already exists.

      :param name: The identifier used to generate the individual's IRI and set its rdfs:label.
      :type name: str

      :return: The OWLNamedIndividual instance representing the entity with the specified name, which is declared in the ontology.

      :rtype: OWLNamedIndividual



   .. py:method:: get_new_atomic_class(name: str) -> pyowl2.abstracts.class_expression.OWLClassExpression

      Retrieves an existing OWL class expression associated with the specified name or generates a new one if it does not already exist in the internal registry. If the class is new, the method increments the internal class counter, constructs a unique IRI, and stores the mapping between the name and the new `OWLClass` instance. Additionally, it modifies the underlying ontology by adding a declaration axiom for the new class, annotated with an RDFS label containing the original name to maintain readability and traceability.

      :param name: The logical identifier for the atomic class, used as the internal lookup key and assigned as the RDFS label for the resulting OWL class.
      :type name: str

      :return: The OWL class expression associated with the given name. If a class with this name already exists, it is returned; otherwise, a new atomic class is created, registered, and returned.

      :rtype: OWLClassExpression



   .. py:method:: get_object_property(role: str) -> Union[pyowl2.expressions.data_property.OWLDataProperty, pyowl2.expressions.object_property.OWLObjectProperty]

      Retrieves an existing property or creates a new object property associated with the given role name. The method first verifies whether a data property with the specified name already exists within the ontology; if so, it returns that data property to maintain consistency. If no such property exists, it constructs a new OWLObjectProperty using the generated IRI for the role, adds a declaration axiom to the ontology with an RDFS label annotation, and returns the newly created object property. This process ensures that property definitions are reused where possible and that the ontology is updated with the necessary metadata for new properties.

      :param role: The name or identifier of the property to retrieve or create.
      :type role: str

      :return: The property associated with the role name. Returns an existing data property if one exists, otherwise a newly created object property.

      :rtype: typing.Union[OWLDataProperty, OWLObjectProperty]



   .. py:method:: individual_iri(o: object) -> pyowl2.base.iri.IRI

      Generates an Internationalized Resource Identifier (IRI) for a given individual object within the OWL2 ontology context. This method delegates the construction of the IRI to the class's generic `iri` method, specifically passing the `OWLNamedIndividual` type to ensure the resulting identifier adheres to the structure required for named individuals. It returns the constructed IRI, relying on the underlying implementation to handle the specific formatting and validation of the input object.

      :param o: The object representing an OWL named individual to be converted to an IRI.
      :type o: object

      :return: The IRI uniquely identifying the provided individual object.

      :rtype: IRI



   .. py:method:: iri(o: object, iri_type: type = OWLClass) -> pyowl2.base.iri.IRI

      Generates an Internationalized Resource Identifier (IRI) for a given object by determining the appropriate namespace based on the specified OWL entity type. The method checks the `iri_type` against standard OWL constructs—such as classes, properties, individuals, datatypes, and annotation properties—and constructs a specific namespace suffix derived from the ontology's base path. If the provided type does not match these specific categories, the method defaults to the ontology's base namespace. The resulting IRI is created by combining this calculated namespace with the string representation of the input object.

      :param o: The object to be converted to an IRI, using its string representation as the local identifier.
      :type o: object
      :param iri_type: Specifies the category of the IRI to generate, determining the specific namespace segment (e.g., class, property, or individual).
      :type iri_type: type

      :return: An IRI object representing the fully qualified identifier for the input object, constructed using a namespace specific to the provided `iri_type`.

      :rtype: IRI



   .. py:method:: object_property_iri(o: object) -> pyowl2.base.iri.IRI

      Generates an Internationalized Resource Identifier (IRI) for an object property during the translation to OWL2. This method serves as a specialized wrapper around the general `iri` generation logic, ensuring that the input object is processed specifically as an `OWLObjectProperty`. It accepts a representation of the property from the source format and returns the formal IRI required for ontology representation, relying on the underlying `iri` method to handle the specific construction and validation of the identifier.

      :param o: The object property to be converted to an IRI string.
      :type o: object

      :return: The IRI corresponding to the provided object property.

      :rtype: IRI



   .. py:method:: run() -> None

      Orchestrates the complete conversion of the internal FuzzyDL knowledge base into an OWL 2 ontology, modifying the internal ontology state and persisting the result to a file. The process begins by annotating the ontology with the specific fuzzy logic type defined in the knowledge base semantics. It then systematically processes and declares atomic concepts, concrete concepts, modifiers, assertions, and named individuals. The method translates various logical axioms—including concept equivalence, subsumption, and disjointness—into their corresponding OWL representations. Additionally, it establishes property characteristics such as domains, ranges, reflexivity, symmetry, transitivity, inverse relationships, sub-property hierarchies, and functionality for both object and data properties. Concrete features are mapped to appropriate XSD datatypes based on their type. The method concludes by saving the populated ontology to the specified output path, raising exceptions for issues such as mismatched property types or failures during file serialization.

      :raises Exception: If an unexpected error occurs during the conversion process, including failures when saving the ontology to the output file.
      :raises ValueError: Raised when a sub-property relationship is defined between properties of incompatible types, such as an object property and a data property.



   .. py:method:: to_owl_annotation(annotation: str) -> pyowl2.base.annotation.OWLAnnotation

      Transforms a provided text string into a structured OWL annotation object suitable for ontology representation. The method utilizes the instance's `fuzzyLabel` attribute as the annotation property and encapsulates the input text as an RDF PlainLiteral. This process includes a debug logging step to track the conversion.

      :param annotation: The text content to be converted into an OWL annotation literal.
      :type annotation: str

      :return: An OWLAnnotation object representing the input string as a plain literal, associated with the instance's fuzzy label property.

      :rtype: OWLAnnotation



   .. py:attribute:: concepts
      :type:  dict[str, pyowl2.abstracts.class_expression.OWLClassExpression]


   .. py:attribute:: datatypes
      :type:  dict[str, pyowl2.base.datatype.OWLDatatype]


   .. py:attribute:: fuzzyLabel
      :type:  pyowl2.base.annotation_property.OWLAnnotationProperty


   .. py:attribute:: input_FDL
      :type:  str


   .. py:attribute:: modifiers
      :type:  dict[str, pyowl2.base.datatype.OWLDatatype]


   .. py:attribute:: num_classes
      :type:  int
      :value: 0



   .. py:attribute:: ontology
      :type:  pyowl2.ontology.OWLOntology


   .. py:attribute:: ontology_iri
      :type:  pyowl2.base.iri.IRI


   .. py:attribute:: ontology_path
      :type:  str
      :value: 'Uninferable#'



   .. py:attribute:: output_FOWL
      :type:  str


.. py:function:: main()

   Serves as the command-line entry point for the script, initiating the conversion process from FuzzyDL ontology files to OWL2 format. It strictly enforces that exactly two command-line arguments are supplied: the input path for the FuzzyDL ontology and the output path for the generated OWL2 ontology. If the argument count is invalid, the function prints a usage instruction to standard error and terminates the application with an error code. When arguments are valid, it instantiates the FuzzydlToOwl2 converter with the specified paths and triggers the conversion routine, resulting in file system modifications.

