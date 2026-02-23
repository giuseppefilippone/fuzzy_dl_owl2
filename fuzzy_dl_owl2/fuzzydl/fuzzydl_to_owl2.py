from __future__ import annotations

import os
import sys
import typing
import urllib
import urllib.parse
from functools import partial

from rdflib import RDF, RDFS, XSD, Literal, Namespace, URIRef

from fuzzy_dl_owl2.fuzzydl.assertion.assertion import Assertion
from fuzzy_dl_owl2.fuzzydl.concept.all_some_concept import AllSomeConcept
from fuzzy_dl_owl2.fuzzydl.concept.choquet_integral import ChoquetIntegral
from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.concrete.crisp_concrete_concept import (
    CrispConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.left_concrete_concept import (
    LeftConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.right_concrete_concept import (
    RightConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.trapezoidal_concrete_concept import (
    TrapezoidalConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept import (
    TriangularConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.has_value_concept import HasValueConcept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface import (
    HasWeightedConceptsInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept import ModifiedConcept
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.concept.owa_concept import OwaConcept
from fuzzy_dl_owl2.fuzzydl.concept.qowa_concept import QowaConcept
from fuzzy_dl_owl2.fuzzydl.concept.quasi_sugeno_integral import QsugenoIntegral
from fuzzy_dl_owl2.fuzzydl.concept.self_concept import SelfConcept
from fuzzy_dl_owl2.fuzzydl.concept.sugeno_integral import SugenoIntegral
from fuzzy_dl_owl2.fuzzydl.concept.value_concept import ValueConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_concept import WeightedConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_max_concept import WeightedMaxConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept import WeightedMinConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_concept import WeightedSumConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_zero_concept import (
    WeightedSumZeroConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept_equivalence import ConceptEquivalence
from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.degree.degree_numeric import DegreeNumeric
from fuzzy_dl_owl2.fuzzydl.general_concept_inclusion import GeneralConceptInclusion
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier import LinearModifier
from fuzzy_dl_owl2.fuzzydl.modifier.modifier import Modifier
from fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier import TriangularModifier
from fuzzy_dl_owl2.fuzzydl.parser.dl_parser import DLParser
from fuzzy_dl_owl2.fuzzydl.primitive_concept_definition import (
    PrimitiveConceptDefinition,
)
from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType, ConcreteFeatureType
from fuzzy_dl_owl2.fuzzydl.util.util import Util
from fuzzy_dl_owl2.fuzzyowl2.util.constants import FuzzyOWL2Keyword
from fuzzy_dl_owl2.fuzzyowl2.util.fuzzy_xml import FuzzyXML
from pyowl2.abstracts.axiom import OWLAxiom
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_range import OWLDataRange
from pyowl2.abstracts.entity import OWLEntity
from pyowl2.axioms.assertion import OWLDataPropertyAssertion, OWLObjectPropertyAssertion
from pyowl2.axioms.assertion.class_assertion import OWLClassAssertion
from pyowl2.axioms.class_axiom.disjoint_classes import OWLDisjointClasses
from pyowl2.axioms.class_axiom.equivalent_classes import OWLEquivalentClasses
from pyowl2.axioms.class_axiom.sub_class_of import OWLSubClassOf
from pyowl2.axioms.data_property_axiom.data_property_domain import OWLDataPropertyDomain
from pyowl2.axioms.data_property_axiom.data_property_range import OWLDataPropertyRange
from pyowl2.axioms.data_property_axiom.functional_data_property import (
    OWLFunctionalDataProperty,
)
from pyowl2.axioms.data_property_axiom.sub_data_property_of import OWLSubDataPropertyOf
from pyowl2.axioms.datatype_definition import OWLDatatypeDefinition
from pyowl2.axioms.declaration import OWLDeclaration
from pyowl2.axioms.object_property_axiom.functional_object_property import (
    OWLFunctionalObjectProperty,
)
from pyowl2.axioms.object_property_axiom.inverse_object_properties import (
    OWLInverseObjectProperties,
)
from pyowl2.axioms.object_property_axiom.object_property_domain import (
    OWLObjectPropertyDomain,
)
from pyowl2.axioms.object_property_axiom.object_property_range import (
    OWLObjectPropertyRange,
)
from pyowl2.axioms.object_property_axiom.reflexive_object_property import (
    OWLReflexiveObjectProperty,
)
from pyowl2.axioms.object_property_axiom.sub_object_property_of import (
    OWLSubObjectPropertyOf,
)
from pyowl2.axioms.object_property_axiom.symmetric_object_property import (
    OWLSymmetricObjectProperty,
)
from pyowl2.axioms.object_property_axiom.transitive_object_property import (
    OWLTransitiveObjectProperty,
)
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.annotation_property import OWLAnnotationProperty
from pyowl2.base.datatype import OWLDatatype
from pyowl2.base.iri import IRI
from pyowl2.base.owl_class import OWLClass
from pyowl2.class_expression.data_all_values_from import OWLDataAllValuesFrom
from pyowl2.class_expression.data_has_value import OWLDataHasValue
from pyowl2.class_expression.data_some_values_from import OWLDataSomeValuesFrom
from pyowl2.class_expression.object_all_values_from import OWLObjectAllValuesFrom
from pyowl2.class_expression.object_complement_of import OWLObjectComplementOf
from pyowl2.class_expression.object_has_self import OWLObjectHasSelf
from pyowl2.class_expression.object_has_value import OWLObjectHasValue
from pyowl2.class_expression.object_intersection_of import OWLObjectIntersectionOf
from pyowl2.class_expression.object_some_values_from import OWLObjectSomeValuesFrom
from pyowl2.class_expression.object_union_of import OWLObjectUnionOf
from pyowl2.data_range.data_intersection_of import OWLDataIntersectionOf
from pyowl2.data_range.datatype_restriction import OWLDatatypeRestriction, OWLFacet
from pyowl2.expressions.data_property import OWLDataProperty
from pyowl2.expressions.object_property import OWLObjectProperty
from pyowl2.individual.named_individual import OWLNamedIndividual
from pyowl2.literal.literal import OWLLiteral
from pyowl2.ontology import OWLOntology


# @utils.timer_decorator
class FuzzydlToOwl2:
    """
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
    """

    def __init__(
        self,
        input_file: str,
        output_file: str,
        # base_iri: str = "http://www.semanticweb.org/ontologies/fuzzydl_ontology.owl",
        base_iri: str = "http://www.semanticweb.org/ontologies/fuzzydl_ontology#",
    ) -> None:
        """
        Initializes the converter by parsing the specified FuzzyDL input file to load the knowledge base and preparing a new OWL 2 ontology structure. It normalizes the provided base IRI by removing trailing delimiters and uses it to instantiate the ontology object, ensuring a valid namespace for the generated entities. The constructor also declares and registers a specific annotation property for fuzzy labels within the ontology. Additionally, it sets up internal dictionaries to map FuzzyDL concepts, datatypes, and modifiers to their OWL equivalents, and configures the destination path for the resulting ontology file.

        :param input_file: Path to the input file containing the Fuzzy Description Logic (FDL) knowledge base definitions.
        :type input_file: str
        :param output_file: The filename or relative path for the generated output file, which will be saved in the results directory.
        :type output_file: str
        :param base_iri: The base Internationalized Resource Identifier (IRI) used as the namespace prefix for the generated ontology.
        :type base_iri: str
        """

        base_iri = urllib.parse.urlparse(base_iri).geturl().rstrip("/").rstrip("#")

        self.num_classes: int = 0
        self.kb, _ = DLParser.get_kb(input_file)
        self.ontology_path: str = f"{base_iri}#"
        self.ontology_iri: IRI = IRI(Namespace(URIRef(self.ontology_path)))
        self.ontology: OWLOntology = OWLOntology(
            self.ontology_iri, OWL1_annotations=True
        )
        self.fuzzyLabel: OWLAnnotationProperty = OWLAnnotationProperty(
            IRI(self.ontology_iri.namespace, ConfigReader.OWL_ANNOTATION_LABEL)
        )

        self.ontology.add_axiom(
            OWLDeclaration(
                self.fuzzyLabel,
                [
                    OWLAnnotation(
                        OWLAnnotationProperty(URIRef(RDFS.label)),
                        OWLLiteral(
                            Literal(ConfigReader.OWL_ANNOTATION_LABEL, lang="en")
                        ),
                    )
                ],
            )
        )

        self.concepts: dict[str, OWLClassExpression] = dict()
        self.datatypes: dict[str, OWLDatatype] = dict()
        self.modifiers: dict[str, OWLDatatype] = dict()
        self.input_FDL: str = input_file
        self.output_FOWL: str = os.path.join(constants.RESULTS_PATH, output_file)

    def iri(self, o: object, iri_type: type = OWLClass) -> IRI:
        """
        Generates an Internationalized Resource Identifier (IRI) for a given object by determining the appropriate namespace based on the specified OWL entity type. The method checks the `iri_type` against standard OWL constructs—such as classes, properties, individuals, datatypes, and annotation properties—and constructs a specific namespace suffix derived from the ontology's base path. If the provided type does not match these specific categories, the method defaults to the ontology's base namespace. The resulting IRI is created by combining this calculated namespace with the string representation of the input object.

        :param o: The object to be converted to an IRI, using its string representation as the local identifier.
        :type o: object
        :param iri_type: Specifies the category of the IRI to generate, determining the specific namespace segment (e.g., class, property, or individual).
        :type iri_type: type

        :return: An IRI object representing the fully qualified identifier for the input object, constructed using a namespace specific to the provided `iri_type`.

        :rtype: IRI
        """

        namespace: URIRef = self.ontology_iri.namespace
        if iri_type == OWLClass:
            namespace = Namespace(f"{self.ontology_path[:-1]}/class#")
        elif iri_type == OWLDataProperty:
            namespace = Namespace(f"{self.ontology_path[:-1]}/data-property#")
        elif iri_type == OWLObjectProperty:
            namespace = Namespace(f"{self.ontology_path[:-1]}/object-property#")
        elif iri_type == OWLNamedIndividual:
            namespace = Namespace(f"{self.ontology_path[:-1]}/individual#")
        elif iri_type == OWLDatatype:
            namespace = Namespace(f"{self.ontology_path[:-1]}/datatype#")
        elif iri_type == OWLAnnotationProperty:
            namespace = Namespace(f"{self.ontology_path[:-1]}/annotation-property#")
        return IRI(namespace, str(o))

    def individual_iri(self, o: object) -> IRI:
        """
        Generates an Internationalized Resource Identifier (IRI) for a given individual object within the OWL2 ontology context. This method delegates the construction of the IRI to the class's generic `iri` method, specifically passing the `OWLNamedIndividual` type to ensure the resulting identifier adheres to the structure required for named individuals. It returns the constructed IRI, relying on the underlying implementation to handle the specific formatting and validation of the input object.

        :param o: The object representing an OWL named individual to be converted to an IRI.
        :type o: object

        :return: The IRI uniquely identifying the provided individual object.

        :rtype: IRI
        """

        return self.iri(o, OWLNamedIndividual)

    def class_iri(self, o: object) -> IRI:
        """
        Generates an Internationalized Resource Identifier (IRI) corresponding to a specific class object during the translation from FuzzyDL to OWL2. This method acts as a specialized wrapper around the generic IRI generation logic, passing the provided object along with the `OWLClass` type indicator to ensure the resulting identifier is formatted correctly for an OWL class. While the method itself does not perform direct validation or mutation of the input object, it relies on the underlying `iri` method to handle the specific string construction and namespace management.

        :param o: The object representing the class to be converted to an IRI.
        :type o: object

        :return: The IRI string representing the provided class object.

        :rtype: IRI
        """

        return self.iri(o, OWLClass)

    def data_property_iri(self, o: object) -> IRI:
        """
        Generates an Internationalized Resource Identifier (IRI) for a given data property object, facilitating its representation within an OWL2 ontology. This method delegates the core logic to the internal `iri` method, passing the `OWLDataProperty` type constant to ensure the resulting identifier is semantically typed correctly. It serves as a specific handler for data properties during the broader translation of FuzzyDL entities into OWL2.

        :param o: The data property object to be converted to an IRI string.
        :type o: object

        :return: The IRI representing the OWL data property corresponding to the input object.

        :rtype: IRI
        """

        return self.iri(o, OWLDataProperty)

    def object_property_iri(self, o: object) -> IRI:
        """
        Generates an Internationalized Resource Identifier (IRI) for an object property during the translation to OWL2. This method serves as a specialized wrapper around the general `iri` generation logic, ensuring that the input object is processed specifically as an `OWLObjectProperty`. It accepts a representation of the property from the source format and returns the formal IRI required for ontology representation, relying on the underlying `iri` method to handle the specific construction and validation of the identifier.

        :param o: The object property to be converted to an IRI string.
        :type o: object

        :return: The IRI corresponding to the provided object property.

        :rtype: IRI
        """

        return self.iri(o, OWLObjectProperty)

    def datatype_iri(self, o: object) -> IRI:
        """
        Generates an Internationalized Resource Identifier (IRI) for a specific datatype object provided as input. This process involves delegating to the underlying `iri` method, supplying the object and the `OWLDatatype` type hint to ensure the resulting identifier adheres to the appropriate OWL2 standards and namespaces. The method serves as a specialized wrapper to handle the conversion of datatype entities specifically, distinguishing them from other ontology elements.

        :param o: The datatype object to be converted to an IRI.
        :type o: object

        :return: The IRI corresponding to the specified datatype object.

        :rtype: IRI
        """

        return self.iri(o, OWLDatatype)

    def annotation_property_iri(self, o: object) -> IRI:
        """
        Generates an Internationalized Resource Identifier (IRI) for a given annotation property object during the conversion process. This method acts as a specialized wrapper that delegates the core logic to the internal `iri` method, explicitly passing the `OWLAnnotationProperty` type to ensure the resulting IRI conforms to the specific naming conventions and structure required for annotation properties in OWL2. The behavior and validity of the returned IRI depend on the underlying implementation of the `iri` method and the structure of the input object.

        :param o: The annotation property object to convert to an IRI.
        :type o: object

        :return: The IRI corresponding to the provided annotation property object.

        :rtype: IRI
        """

        return self.iri(o, OWLAnnotationProperty)

    def get_base(self, c: Concept) -> OWLClassExpression:
        """
        Retrieves or generates an OWL class expression corresponding to the provided FuzzyDL concept. If the input concept is atomic, the method returns the standard OWL class associated with the concept's string identifier. Conversely, if the concept is non-atomic (complex), the method creates a new atomic OWL class to serve as a proxy for the complex expression, effectively nominalizing it for the target ontology. This process may involve side effects such as registering new class declarations within the translation context to ensure the generated class is valid and accessible.

        :param c: The concept to be mapped to its corresponding OWL class expression.
        :type c: Concept

        :return: The OWL class expression representing the base class of the concept. Returns an existing class if the concept is atomic, or a newly generated atomic class otherwise.

        :rtype: OWLClassExpression
        """

        if c.is_atomic():
            return self.get_class(str(c))
        return self.get_new_atomic_class(str(c))

    @typing.overload
    def get_class(self, name: str) -> OWLClassExpression: ...

    @typing.overload
    def get_class(self, c: Concept) -> OWLClassExpression: ...

    def get_class(self, arg: typing.Union[str, Concept]) -> OWLClassExpression:
        """
        Retrieves or constructs an OWL class expression based on the provided input, which can be either a string identifier or a Concept object. The method delegates the specific logic to internal helper methods depending on the type of the argument. It enforces strict type checking and raises a ValueError if the input is not a string or a Concept instance.

        :param arg: The class name as a string or a Concept object.
        :type arg: typing.Union[str, Concept]

        :raises ValueError: If the provided argument is not a string or a Concept object.

        :return: The OWL class expression corresponding to the provided name or concept, creating it if it does not already exist.

        :rtype: OWLClassExpression
        """

        if isinstance(arg, str):
            return self.__get_class_1(arg)
        elif isinstance(arg, Concept):
            return self.__get_class_2(arg)
        else:
            raise ValueError("Argument must be a string or a Concept")

    def __get_class_1(self, name: str) -> OWLClassExpression:
        """
        Creates an OWL class expression for the specified name by generating an IRI and instantiating an OWLClass object. This method modifies the ontology by adding a declaration axiom for the class, which includes an RDFS label annotation set to the input name. It returns the resulting OWL class, ensuring it is explicitly defined within the ontology's structure.

        :param name: The identifier for the class, used to construct its IRI and assign its English RDFS label.
        :type name: str

        :return: The OWL class instance created for the specified name.

        :rtype: OWLClassExpression
        """

        cls = OWLClass(self.class_iri(name))
        self.ontology.add_axiom(
            OWLDeclaration(
                cls,
                [
                    OWLAnnotation(
                        OWLAnnotationProperty(URIRef(RDFS.label)),
                        OWLLiteral(Literal(name, lang="en")),
                    )
                ],
            )
        )
        return cls

    def __get_class_2(self, c: Concept) -> OWLClassExpression:
        """
        Converts a FuzzyDL `Concept` instance into the corresponding OWL 2 `OWLClassExpression` by inspecting the concept's type and recursively processing its components. For atomic concepts, it retrieves or creates an `OWLClass` and adds a declaration axiom with an RDFS label to the ontology. Logical constructs such as conjunctions, disjunctions, and complements are mapped to OWL intersection, union, and complement expressions, respectively. The method distinguishes between object and data properties when handling existential (`SOME`) and universal (`ALL`) restrictions. Fuzzy logic-specific constructs, including modified concepts, weighted concepts, and various aggregators, are handled by generating new atomic classes and attaching specialized XML annotations to preserve fuzzy semantics. Additionally, it manages value restrictions and self-restrictions, delegating complex fuzzy aggregators to helper methods.

        :param c: The concept to be converted into an OWL class expression.
        :type c: Concept

        :return: The OWL 2 class expression corresponding to the input Concept, handling atomic classes, logical operators, restrictions, and fuzzy logic extensions.

        :rtype: OWLClassExpression
        """

        Util.debug(f"Getting class for concept -> {c}")
        c_type: ConceptType = c.type
        if c_type in (ConceptType.ATOMIC, ConceptType.CONCRETE):
            cls = self.get_class(str(c))
            self.ontology.add_axiom(
                OWLDeclaration(
                    cls,
                    [
                        OWLAnnotation(
                            OWLAnnotationProperty(URIRef(RDFS.label)),
                            OWLLiteral(Literal(str(c), lang="en")),
                        )
                    ],
                )
            )
            return cls
        elif c_type == ConceptType.TOP:
            return OWLClass.thing()
        elif c_type == ConceptType.BOTTOM:
            return OWLClass.nothing()
        elif c_type in (
            ConceptType.COMPLEMENT,
            ConceptType.NOT_AT_MOST_VALUE,
            ConceptType.NOT_AT_LEAST_VALUE,
            ConceptType.NOT_EXACT_VALUE,
            ConceptType.NOT_WEIGHTED,
            ConceptType.NOT_W_SUM,
            ConceptType.CONCRETE_COMPLEMENT,
            ConceptType.MODIFIED_COMPLEMENT,
            ConceptType.NOT_OWA,
            ConceptType.NOT_QUANTIFIED_OWA,
            ConceptType.NOT_CHOQUET_INTEGRAL,
            ConceptType.NOT_SUGENO_INTEGRAL,
            ConceptType.NOT_QUASI_SUGENO_INTEGRAL,
            ConceptType.NOT_W_MAX,
            ConceptType.NOT_W_MIN,
            ConceptType.NOT_W_SUM_ZERO,
            ConceptType.NOT_SELF,
            ConceptType.NOT_HAS_VALUE,
        ):
            return OWLObjectComplementOf(self.get_class(-c))
        elif c_type in (
            ConceptType.AND,
            ConceptType.GOEDEL_AND,
            ConceptType.LUKASIEWICZ_AND,
        ):
            c: OperatorConcept = typing.cast(OperatorConcept, c)
            return OWLObjectIntersectionOf([self.get_class(c1) for c1 in c.concepts])
        elif c_type in (
            ConceptType.OR,
            ConceptType.GOEDEL_OR,
            ConceptType.LUKASIEWICZ_OR,
        ):
            c: OperatorConcept = typing.cast(OperatorConcept, c)
            return OWLObjectUnionOf([self.get_class(c1) for c1 in c.concepts])
        elif c_type == ConceptType.SOME:
            c: AllSomeConcept = typing.cast(AllSomeConcept, c)
            if str(c.curr_concept) in self.datatypes:
                dp: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_data_property(c.role)
                )
                assert isinstance(dp, OWLDataProperty)
                d: OWLDatatype = self.datatypes.get(str(c.curr_concept))
                return OWLDataSomeValuesFrom([dp], d)
            else:
                op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_object_property(c.role)
                )
                assert isinstance(op, OWLObjectProperty)
                c2: OWLClassExpression = self.get_class(c.curr_concept)
                return OWLObjectSomeValuesFrom(op, c2)
        elif c_type == ConceptType.ALL:
            c: AllSomeConcept = typing.cast(AllSomeConcept, c)
            if str(c.curr_concept) in self.datatypes:
                dp: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_data_property(c.role)
                )
                assert isinstance(dp, OWLDataProperty)
                d: OWLDatatype = self.datatypes.get(str(c.curr_concept))
                return OWLDataAllValuesFrom([dp], d)
            else:
                op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_object_property(c.role)
                )
                assert isinstance(op, OWLObjectProperty)
                c2: OWLClassExpression = self.get_class(c.curr_concept)
                return OWLObjectAllValuesFrom(op, c2)
        elif c_type == ConceptType.MODIFIED:
            c: ModifiedConcept = typing.cast(ModifiedConcept, c)
            if str(c) in self.concepts:
                return self.concepts.get(str(c))
            c4: OWLClassExpression = self.get_new_atomic_class(str(c))
            c3: OWLClassExpression = self.get_base(c.curr_concept)
            self.concepts[str(c)] = c3
            main_xml = FuzzyXML.build_main_xml(FuzzyOWL2Keyword.CONCEPT.get_str_value())
            concept_xml = FuzzyXML.build_concept_xml(
                FuzzyOWL2Keyword.MODIFIED.get_str_value(),
                {
                    FuzzyOWL2Keyword.MODIFIER.get_str_value(): str(
                        self.modifiers[str(c.modifier)].iri.value
                    ),
                    FuzzyOWL2Keyword.BASE.get_str_value(): str(c3.iri.value),
                },
            )
            main_xml.append(concept_xml)
            annotation: str = FuzzyXML.to_str(main_xml)
            # annotation: str = (
            #     f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.CONCEPT.get_str_value()}">\n',
            #     f'\t<{FuzzyOWL2Keyword.CONCEPT.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{FuzzyOWL2Keyword.MODIFIED.get_str_value()}" {FuzzyOWL2Keyword.MODIFIER.get_str_value()}="{self.modifiers[str(c)]}" {FuzzyOWL2Keyword.BASE.get_str_value()}="{c3}"/>\n',
            #     f"</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>",
            # )
            self.add_entity_annotation(annotation, c4)
            return c4
        elif c_type == ConceptType.SELF:
            c: SelfConcept = typing.cast(SelfConcept, c)
            owl_obj_property: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(c.role)
            )
            assert isinstance(owl_obj_property, OWLObjectProperty)
            return OWLObjectHasSelf(owl_obj_property)
        elif c_type == ConceptType.HAS_VALUE:
            c: HasValueConcept = typing.cast(HasValueConcept, c)
            owl_obj_property: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(c.role)
            )
            assert isinstance(owl_obj_property, OWLObjectProperty)
            ind: OWLNamedIndividual = self.get_individual(str(c.value))
            return OWLObjectHasValue(owl_obj_property, ind)
        elif c_type in (
            ConceptType.AT_MOST_VALUE,
            ConceptType.AT_LEAST_VALUE,
            ConceptType.EXACT_VALUE,
        ):
            c: ValueConcept = typing.cast(ValueConcept, c)
            if isinstance(c.value, int):
                datatype: OWLDatatype = OWLDatatype(XSD.integer)
                literal: OWLLiteral = OWLLiteral(Literal(c.value, datatype=XSD.integer))
            elif isinstance(c.value, float):
                datatype: OWLDatatype = OWLDatatype(XSD.decimal)
                literal: OWLLiteral = OWLLiteral(Literal(c.value, datatype=XSD.decimal))
            elif isinstance(c.value, str):
                datatype: OWLDatatype = OWLDatatype(RDF.PlainLiteral)
                literal: OWLLiteral = OWLLiteral(
                    Literal(c.value, datatype=RDF.PlainLiteral)
                )
            if c_type == ConceptType.AT_LEAST_VALUE:
                data_range: OWLDataRange = OWLDatatypeRestriction(
                    datatype, [OWLFacet(OWLFacet.MIN_INCLUSIVE, literal)]
                )
                return OWLDataSomeValuesFrom(self.get_data_property(c.role), data_range)
            elif c_type == ConceptType.AT_MOST_VALUE:
                data_range: OWLDataRange = OWLDatatypeRestriction(
                    datatype, [OWLFacet(OWLFacet.MAX_INCLUSIVE, literal)]
                )
                return OWLDataSomeValuesFrom(self.get_data_property(c.role), data_range)
            else:
                return OWLDataHasValue(self.get_data_property(c.role), literal)
        elif c_type == ConceptType.WEIGHTED:
            c: WeightedConcept = typing.cast(WeightedConcept, c)
            c4: OWLClassExpression = self.get_new_atomic_class(str(c))
            c3: OWLClassExpression = self.get_base(c.curr_concept)

            main_xml = FuzzyXML.build_main_xml(FuzzyOWL2Keyword.CONCEPT.get_str_value())
            concept_xml = FuzzyXML.build_concept_xml(
                FuzzyOWL2Keyword.WEIGHTED.get_str_value(),
                {
                    FuzzyOWL2Keyword.DEGREE_VALUE.get_str_value(): str(c.weight),
                    FuzzyOWL2Keyword.BASE.get_str_value(): str(c3.iri.value),
                },
            )
            main_xml.append(concept_xml)
            annotation: str = FuzzyXML.to_str(main_xml)
            # annotation: str = (
            #     f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.CONCEPT.get_str_value()}">\n',
            #     f'\t<{FuzzyOWL2Keyword.CONCEPT.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{FuzzyOWL2Keyword.WEIGHTED.get_str_value()}" {FuzzyOWL2Keyword.DEGREE_VALUE.get_str_value()}="{c.weight}" {FuzzyOWL2Keyword.BASE.get_str_value()}="{c3}"/>\n',
            #     f"</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>",
            # )
            self.add_entity_annotation(annotation, c3)
            return c4
        elif c_type in (
            ConceptType.W_MAX,
            ConceptType.W_MIN,
            ConceptType.W_SUM,
            ConceptType.W_SUM_ZERO,
        ):
            return self.__get_class_weighted_min_max_sum(c)
        elif c_type in (
            ConceptType.OWA,
            # ConceptType.QUANTIFIED_OWA,
            ConceptType.CHOQUET_INTEGRAL,
            ConceptType.SUGENO_INTEGRAL,
            ConceptType.QUASI_SUGENO_INTEGRAL,
        ):
            return self.__get_class_weighted(c)
        elif c_type == ConceptType.QUANTIFIED_OWA:
            return self.__get_class_q_owa(c)
        cls = OWLClass(self.class_iri(str(c)))
        self.ontology.add_axiom(
            OWLDeclaration(
                cls,
                [
                    OWLAnnotation(
                        OWLAnnotationProperty(URIRef(RDFS.label)),
                        OWLLiteral(Literal(str(c), lang="en")),
                    )
                ],
            )
        )
        return cls

    def __get_class_weighted_min_max_sum(self, c: Concept) -> OWLClassExpression:
        """
        Converts a FuzzyDL concept representing a weighted aggregation operation—specifically weighted minimum, maximum, sum, or sum zero—into a corresponding OWL 2 class expression. This process involves creating a new atomic class to serve as the representation of the fuzzy concept and attaching a detailed XML annotation to it. The annotation encodes the specific type of aggregation, the weights assigned to each sub-concept, and the IRIs of the base concepts involved in the operation. If the input concept's type does not match one of the supported weighted aggregation types, the method returns None. As a side effect, this method modifies the ontology by adding the generated annotation to the newly created class entity.

        :param c: The fuzzy concept defining a weighted aggregation operation (min, max, sum, or sum zero) containing the sub-concepts and their associated weights.
        :type c: Concept

        :return: A new OWL class expression representing the fuzzy weighted concept, annotated with the aggregation type, weights, and base concepts. Returns None if the input concept type is not supported.

        :rtype: OWLClassExpression
        """

        type_dict: dict[ConceptType, str] = {
            ConceptType.W_MAX: FuzzyOWL2Keyword.WEIGHTED_MAXIMUM.get_str_value(),
            ConceptType.W_MIN: FuzzyOWL2Keyword.WEIGHTED_MINIMUM.get_str_value(),
            ConceptType.W_SUM: FuzzyOWL2Keyword.WEIGHTED_SUM.get_str_value(),
            ConceptType.W_SUM_ZERO: FuzzyOWL2Keyword.WEIGHTED_SUMZERO.get_str_value(),
        }
        type_cast: dict[ConceptType, typing.Callable] = {
            ConceptType.W_MAX: partial(typing.cast, WeightedMaxConcept),
            ConceptType.W_MIN: partial(typing.cast, WeightedMinConcept),
            ConceptType.W_SUM: partial(typing.cast, WeightedSumConcept),
            ConceptType.W_SUM_ZERO: partial(typing.cast, WeightedSumZeroConcept),
        }
        if c.type not in type_dict:
            return None
        curr_concept: HasWeightedConceptsInterface = type_cast[c.type](c)
        c3: OWLClassExpression = self.get_new_atomic_class(str(curr_concept))

        main_xml = FuzzyXML.build_main_xml(FuzzyOWL2Keyword.CONCEPT.get_str_value())
        concept_xml = FuzzyXML.build_concept_xml(type_dict[c.type])
        for i in range(len(curr_concept.concepts)):
            c5: OWLClassExpression = self.get_base(curr_concept.concepts[i])
            sub_concept_xml = FuzzyXML.build_concept_xml(
                FuzzyOWL2Keyword.WEIGHTED.get_str_value(),
                {
                    FuzzyOWL2Keyword.DEGREE_VALUE.get_str_value(): str(
                        curr_concept.weights[i]
                    ),
                    FuzzyOWL2Keyword.BASE.get_str_value(): str(c5.iri.value),
                },
            )
            concept_xml.append(sub_concept_xml)
        main_xml.append(concept_xml)
        annotation: str = FuzzyXML.to_str(main_xml)

        # annotation: str = (
        #     f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.CONCEPT.get_str_value()}">\n',
        #     f'\t<{FuzzyOWL2Keyword.CONCEPT.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{type_dict[c.type]}">\n ',
        # )
        # for i in range(len(curr_concept.concepts)):
        #     c5: OWLClassExpression = self.get_base(curr_concept.concepts[i])
        #     annotation += f'\t\t<{FuzzyOWL2Keyword.CONCEPT.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{FuzzyOWL2Keyword.WEIGHTED.get_str_value()}" {FuzzyOWL2Keyword.DEGREE_VALUE.get_str_value()}="{curr_concept.weights[i]}" {FuzzyOWL2Keyword.BASE.get_str_value()}="{c5}" />\n'
        # annotation: str = (
        #     f"\t</{FuzzyOWL2Keyword.CONCEPT.get_tag_name()} >\n</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} >"
        # )
        self.add_entity_annotation(annotation, c3)
        return c3

    def __get_class_weighted(self, c: Concept) -> OWLClassExpression:
        """
        Generates an OWL class expression for specific weighted fuzzy concept types, including OWA, Choquet Integral, Sugeno Integral, and Quasi Sugeno Integral. The method creates a new atomic class corresponding to the input concept and attaches a detailed XML annotation to it; this annotation encodes the specific aggregation type, the list of weights, and the base concepts involved in the aggregation. If the input concept type is not one of the supported weighted types, the method returns None.

        :param c: The weighted concept (e.g., OWA, Choquet, or Sugeno Integral) providing the weights and constituent concepts required to construct the OWL class expression.
        :type c: Concept

        :return: An OWL class expression representing the input weighted concept, annotated with the specific fuzzy logic definition (weights and sub-concepts).

        :rtype: OWLClassExpression
        """

        type_dict: dict[ConceptType, str] = {
            ConceptType.OWA: FuzzyOWL2Keyword.OWA.get_str_value(),
            # ConceptType.QUANTIFIED_OWA: FuzzyOWL2Keyword.Q_OWA.get_str_value(),
            ConceptType.CHOQUET_INTEGRAL: FuzzyOWL2Keyword.CHOQUET.get_str_value(),
            ConceptType.SUGENO_INTEGRAL: FuzzyOWL2Keyword.SUGENO.get_str_value(),
            ConceptType.QUASI_SUGENO_INTEGRAL: FuzzyOWL2Keyword.QUASI_SUGENO.get_str_value(),
        }
        type_cast: dict[ConceptType, typing.Callable] = {
            ConceptType.OWA: partial(typing.cast, OwaConcept),
            # ConceptType.QUANTIFIED_OWA: partial(typing.cast, QowaConcept),
            ConceptType.CHOQUET_INTEGRAL: partial(typing.cast, ChoquetIntegral),
            ConceptType.SUGENO_INTEGRAL: partial(typing.cast, SugenoIntegral),
            ConceptType.QUASI_SUGENO_INTEGRAL: partial(typing.cast, QsugenoIntegral),
        }
        if c.type not in type_dict:
            return None
        curr_concept: HasWeightedConceptsInterface = type_cast[c.type](c)
        c4: OWLClassExpression = self.get_new_atomic_class(str(c))

        main_xml = FuzzyXML.build_main_xml(FuzzyOWL2Keyword.CONCEPT.get_str_value())
        concept_xml = FuzzyXML.build_concept_xml(type_dict[c.type])
        weights_xml = FuzzyXML.build_weights_xml(curr_concept.weights)
        names_xml = FuzzyXML.build_names_xml(
            [self.get_base(ci) for ci in curr_concept.concepts]
        )
        concept_xml.append(weights_xml)
        concept_xml.append(names_xml)
        main_xml.append(concept_xml)
        annotation: str = FuzzyXML.to_str(main_xml)

        # annotation: str = (
        #     f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.CONCEPT.get_str_value()}">\n',
        #     f'\t<{FuzzyOWL2Keyword.CONCEPT.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{type_dict[c.type]}">\n',
        #     f"\t\t<{FuzzyOWL2Keyword.WEIGHTS.get_tag_name()}>\n",
        # )
        # for d in curr_concept.weights:
        #     annotation += f"\t\t\t<{FuzzyOWL2Keyword.WEIGHT.get_tag_name()}>{d}</{FuzzyOWL2Keyword.WEIGHT.get_tag_name()}>\n"
        # annotation += f"\t\t</{FuzzyOWL2Keyword.WEIGHTS.get_tag_name()}>\n\t\t<{FuzzyOWL2Keyword.CONCEPT_NAMES.get_tag_name()}>\n"
        # for ci in curr_concept.concepts:
        #     c5: OWLClassExpression = self.get_base(ci)
        #     annotation += f"\t\t\t<{FuzzyOWL2Keyword.NAME.get_tag_name()}>{c5}</{FuzzyOWL2Keyword.NAME.get_tag_name()}>\n"
        # annotation += f"\t\t</{FuzzyOWL2Keyword.CONCEPT_NAMES.get_tag_name()}>\n\t</{FuzzyOWL2Keyword.CONCEPT.get_tag_name()}>\n</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>"

        self.add_entity_annotation(annotation, c4)
        return c4

    def __get_class_q_owa(self, c: Concept) -> OWLClassExpression:
        """
        Converts a `Concept` object representing a Quantified Ordered Weighted Averaging (OWA) operator into a corresponding `OWLClassExpression`. The method first verifies that the input concept is of the correct type; if the type does not match `QUANTIFIED_OWA`, it returns `None`. Upon validation, it generates a new atomic OWL class and constructs a specific XML annotation that encapsulates the fuzzy logic semantics, including the quantifier value and the list of constituent concepts. This XML annotation is then attached to the new class entity as a side effect before the class expression is returned.

        :param c: The Quantified OWA concept providing the quantifier and constituent concepts required to generate the OWL class expression.
        :type c: Concept

        :return: Returns a new atomic OWL class expression representing the Quantified OWA concept, annotated with the quantifier and constituent concepts.

        :rtype: OWLClassExpression
        """

        type_dict: dict[ConceptType, str] = {
            ConceptType.QUANTIFIED_OWA: FuzzyOWL2Keyword.Q_OWA.get_str_value(),
        }
        type_cast: dict[ConceptType, typing.Callable] = {
            ConceptType.QUANTIFIED_OWA: partial(typing.cast, QowaConcept),
        }
        if c.type not in type_dict:
            return None
        curr_concept: QowaConcept = type_cast[c.type](c)
        c4: OWLClassExpression = self.get_new_atomic_class(str(c))

        main_xml = FuzzyXML.build_main_xml(FuzzyOWL2Keyword.CONCEPT.get_str_value())
        concept_xml = FuzzyXML.build_concept_xml(
            type_dict[c.type],
            {FuzzyOWL2Keyword.QUANTIFIER.get_str_value(): str(curr_concept.quantifier)},
        )
        names_xml = FuzzyXML.build_names_xml(
            [self.get_base(ci) for ci in curr_concept.concepts]
        )
        concept_xml.append(names_xml)
        main_xml.append(concept_xml)
        annotation: str = FuzzyXML.to_str(main_xml)
        # annotation: str = (
        #     f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.CONCEPT.get_str_value()}">\n',
        #     f'\t<{FuzzyOWL2Keyword.CONCEPT.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{type_dict[c.type]}" {FuzzyOWL2Keyword.QUANTIFIER.get_str_value()}="{curr_concept.quantifier}">\n',
        #     f"\t\t<{FuzzyOWL2Keyword.CONCEPT_NAMES.get_tag_name()}>\n",
        # )
        # for ci in curr_concept.concepts:
        #     c5: OWLClassExpression = self.get_base(ci)
        #     annotation += f"\t\t\t<{FuzzyOWL2Keyword.NAME.get_tag_name()}>{c5}</{FuzzyOWL2Keyword.NAME.get_tag_name()}>\n"
        # annotation += f"\t\t</{FuzzyOWL2Keyword.CONCEPT_NAMES.get_tag_name()}>\n\t</{FuzzyOWL2Keyword.CONCEPT.get_tag_name()}>\n</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>"
        self.add_entity_annotation(annotation, c4)
        return c4

    def get_new_atomic_class(self, name: str) -> OWLClassExpression:
        """
        Retrieves an existing OWL class expression associated with the specified name or generates a new one if it does not already exist in the internal registry. If the class is new, the method increments the internal class counter, constructs a unique IRI, and stores the mapping between the name and the new `OWLClass` instance. Additionally, it modifies the underlying ontology by adding a declaration axiom for the new class, annotated with an RDFS label containing the original name to maintain readability and traceability.

        :param name: The logical identifier for the atomic class, used as the internal lookup key and assigned as the RDFS label for the resulting OWL class.
        :type name: str

        :return: The OWL class expression associated with the given name. If a class with this name already exists, it is returned; otherwise, a new atomic class is created, registered, and returned.

        :rtype: OWLClassExpression
        """

        Util.debug(f"Getting new atomic concept -> {name}")
        c = self.concepts.get(name)
        if c is not None:
            return c

        self.num_classes += 1
        Util.debug(f"Creating new atomic concept -> {name}")
        c2: OWLClass = OWLClass(self.class_iri(f"class__{self.num_classes}"))
        self.concepts[name] = c2
        self.ontology.add_axiom(
            OWLDeclaration(
                c2,
                [
                    OWLAnnotation(
                        OWLAnnotationProperty(URIRef(RDFS.label)),
                        OWLLiteral(Literal(name, lang="en")),
                    )
                ],
            )
        )
        return c2

    def exist_object_property(self, role: str) -> bool:
        """
        Verifies the presence of an object property within the loaded ontology by resolving the provided role name to its corresponding Internationalized Resource Identifier (IRI). This method performs a read-only query against the underlying data structure, returning True if the property is found and False otherwise. It relies on the internal IRI generation logic to correctly map the input string to the ontology's namespace, and it does not modify the ontology's contents during the check.

        :param role: The name of the object property to check for existence.
        :type role: str

        :return: True if the object property identified by the given role exists in the ontology, False otherwise.

        :rtype: bool
        """

        iri: IRI = self.object_property_iri(role)
        return self.ontology.getter.exists_object_property(iri.to_uriref())
        # return any(
        #     typing.cast(OWLObjectProperty, typing.cast(OWLDeclaration, prop).entity).iri
        #     == iri
        #     for prop in self.ontology.get_axioms(RDFXMLGetterTypes.OBJECT_PROPERTIES)
        # )

    def exist_data_property(self, role: str) -> bool:
        """
        Verifies the existence of a data property within the loaded ontology by resolving the provided string identifier to its corresponding IRI. This method acts as a wrapper around the ontology's internal getter, translating the human-readable role name into a formal URI reference to perform the check. The operation is read-only and has no side effects on the ontology state; it returns `True` if the property is found and `False` otherwise, handling cases where the input name does not map to any defined entity.

        :param role: The name of the data property to check for existence.
        :type role: str

        :return: True if the data property identified by the specified role exists, False otherwise.

        :rtype: bool
        """

        iri: IRI = self.data_property_iri(role)
        return self.ontology.getter.exists_data_property(iri.to_uriref())
        # return any(
        #     typing.cast(OWLDataProperty, typing.cast(OWLDeclaration, prop).entity).iri
        #     == iri
        #     for prop in self.ontology.get_axioms(RDFXMLGetterTypes.DATA_PROPERTIES)
        # )

    def get_object_property(
        self, role: str
    ) -> typing.Union[OWLDataProperty, OWLObjectProperty]:
        """
        Retrieves an existing property or creates a new object property associated with the given role name. The method first verifies whether a data property with the specified name already exists within the ontology; if so, it returns that data property to maintain consistency. If no such property exists, it constructs a new OWLObjectProperty using the generated IRI for the role, adds a declaration axiom to the ontology with an RDFS label annotation, and returns the newly created object property. This process ensures that property definitions are reused where possible and that the ontology is updated with the necessary metadata for new properties.

        :param role: The name or identifier of the property to retrieve or create.
        :type role: str

        :return: The property associated with the role name. Returns an existing data property if one exists, otherwise a newly created object property.

        :rtype: typing.Union[OWLDataProperty, OWLObjectProperty]
        """

        Util.debug(f"Getting object property -> {role}")
        if self.exist_data_property(role):
            return self.get_data_property(role)
        obj = OWLObjectProperty(self.object_property_iri(role))
        self.ontology.add_axiom(
            OWLDeclaration(
                obj,
                [
                    OWLAnnotation(
                        OWLAnnotationProperty(URIRef(RDFS.label)),
                        OWLLiteral(Literal(role, lang="en")),
                    )
                ],
            )
        )
        return obj

    def get_data_property(
        self, role: str
    ) -> typing.Union[OWLDataProperty, OWLObjectProperty]:
        """
        Retrieves or creates an OWL data property corresponding to the specified role name. If a property with the same name is already registered as an object property, the method returns that existing object property instead of creating a new data property. When a new data property is created, the method updates the ontology by adding a declaration axiom and an RDFS label annotation derived from the role name.

        :param role: The identifier for the data property, used to generate its IRI and RDFS label. If a property with this name already exists, it is returned instead of creating a new one.
        :type role: str

        :return: The property corresponding to the role name. Returns an existing object property if found, otherwise creates and returns a new data property.

        :rtype: typing.Union[OWLDataProperty, OWLObjectProperty]
        """

        Util.debug(f"Getting data property -> {role}")
        if self.exist_object_property(role):
            return self.get_object_property(role)
        data = OWLDataProperty(self.data_property_iri(role))
        self.ontology.add_axiom(
            OWLDeclaration(
                data,
                [
                    OWLAnnotation(
                        OWLAnnotationProperty(URIRef(RDFS.label)),
                        OWLLiteral(Literal(role, lang="en")),
                    )
                ],
            )
        )
        return data

    def get_individual(self, name: str) -> OWLNamedIndividual:
        """
        Retrieves or instantiates a named individual within the ontology using the provided string identifier. The method generates an IRI for the individual and ensures its formal declaration by adding a corresponding axiom to the ontology's internal structure. As a side effect, it also attaches an RDFS label annotation to the individual, using the input name as the literal value with an English language tag. This process modifies the ontology state, potentially resulting in duplicate declarations if the individual already exists.

        :param name: The identifier used to generate the individual's IRI and set its rdfs:label.
        :type name: str

        :return: The OWLNamedIndividual instance representing the entity with the specified name, which is declared in the ontology.

        :rtype: OWLNamedIndividual
        """

        Util.debug(f"Getting individual -> {name}")
        ind = OWLNamedIndividual(self.individual_iri(f"{name}"))
        self.ontology.add_axiom(
            OWLDeclaration(
                ind,
                [
                    OWLAnnotation(
                        OWLAnnotationProperty(URIRef(RDFS.label)),
                        OWLLiteral(Literal(name, lang="en")),
                    )
                ],
            )
        )
        return ind

    def to_owl_annotation(self, annotation: str) -> OWLAnnotation:
        """
        Transforms a provided text string into a structured OWL annotation object suitable for ontology representation. The method utilizes the instance's `fuzzyLabel` attribute as the annotation property and encapsulates the input text as an RDF PlainLiteral. This process includes a debug logging step to track the conversion.

        :param annotation: The text content to be converted into an OWL annotation literal.
        :type annotation: str

        :return: An OWLAnnotation object representing the input string as a plain literal, associated with the instance's fuzzy label property.

        :rtype: OWLAnnotation
        """

        Util.debug(f"Converting annotation to OWL -> {annotation}")
        return OWLAnnotation(
            self.fuzzyLabel,
            OWLLiteral(
                Literal(annotation, datatype=RDF.PlainLiteral),
            ),
        )

    def add_ontology_annotation(self, annotation: str) -> None:
        """
        Appends a descriptive annotation to the OWL 2 ontology currently being constructed by the converter. This method accepts a string representing the annotation text, transforms it into a formal `OWLAnnotation` object using the internal `to_owl_annotation` utility, and directly mutates the internal ontology state by attaching the result. The operation modifies the ontology in place, ensuring the metadata is integrated into the final structure without returning a value.

        :param annotation: The textual content of the annotation to be added to the ontology.
        :type annotation: str
        """

        Util.debug(f"Adding annotation to ontology -> {annotation}")
        comment: OWLAnnotation = self.to_owl_annotation(annotation)
        self.ontology.add_annotation(comment)

    def add_entity_annotation(self, annotation: str, entity: OWLEntity) -> None:
        """
        Associates a textual annotation with a specific OWL entity within the internal ontology structure. The method accepts a string representing the annotation content and the target entity, converting the string into a formal OWLAnnotation object before attaching it. This operation directly mutates the ontology by adding the annotation to the specified element, ensuring the metadata is persisted as part of the entity's definition.

        :param annotation: The text content of the annotation to be added.
        :type annotation: str
        :param entity: The target OWL entity to which the annotation will be attached.
        :type entity: OWLEntity
        """

        # define_datatype_in_ontology(entity, self.iri(entity), self.ontology)
        Util.debug(f"Adding annotation to entity {entity} -> {annotation}")
        owl_annotation: OWLAnnotation = self.to_owl_annotation(annotation)
        # axiom: OWLAnnotationAssertion = OWLAnnotationAssertion(
        #     entity.iri, self.fuzzyLabel, owl_annotation
        # )
        # self.ontology.add_axiom(axiom)
        self.ontology.add_annotation_to_element(entity, [owl_annotation])

    def get_annotations_for_axiom(
        self, value: typing.Union[float, DegreeNumeric]
    ) -> set[OWLAnnotation]:
        """
        This method constructs an OWL annotation that encapsulates the degree of truth for a fuzzy logic axiom, facilitating the translation of fuzzy constraints into the OWL2 format. It accepts either a raw numeric value or a `DegreeNumeric` object, extracting the underlying numerical representation in the latter case. By generating a specific XML structure that defines the axiom type and its associated degree value, the method converts this data into an `OWLAnnotation` object. The resulting annotation is returned within a set to conform to standard OWL API expectations for axiom annotations.

        :param value: The degree value for the axiom, provided as either a float or a DegreeNumeric object.
        :type value: typing.Union[float, DegreeNumeric]

        :return: A singleton set containing an OWLAnnotation that represents the specified fuzzy degree value for an axiom.

        :rtype: set[OWLAnnotation]
        """

        if isinstance(value, constants.NUMBER):
            n = value
        elif isinstance(value, DegreeNumeric):  # Degree object
            n = value.get_numerical_value()

        main_xml = FuzzyXML.build_main_xml(FuzzyOWL2Keyword.AXIOM.get_str_value())
        degree_xml = FuzzyXML.build_degree_xml(n)
        main_xml.append(degree_xml)
        annotation_text: str = FuzzyXML.to_str(main_xml)

        # annotation_text: str = (
        #     f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.AXIOM.get_str_value()}">\n'
        #     f'\t<{FuzzyOWL2Keyword.DEGREE_DEF.get_tag_name()} {FuzzyOWL2Keyword.DEGREE_VALUE.get_str_value()}="{n}"/>\n'
        #     f"</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>"
        # )
        annotation: OWLAnnotation = self.to_owl_annotation(annotation_text)
        return set([annotation])

    def annotate_gci(self, gci: GeneralConceptInclusion) -> None:
        """
        Converts a General Concept Inclusion (GCI) into an OWL 2 SubClassOf axiom and adds it to the internal ontology. The method retrieves the subsumed and subsumer concepts from the provided GCI and checks its associated degree. If the degree is not equal to one, indicating a non-crisp fuzzy relationship, the method generates specific annotations representing that degree and attaches them to the axiom; otherwise, a standard unannotated axiom is created. This process directly modifies the ontology by persisting the newly constructed axiom.

        :param gci: The General Concept Inclusion object providing the subsumed class, subsumer class, and degree information required to construct an OWL subclass axiom.
        :type gci: GeneralConceptInclusion
        """

        c1: OWLClassExpression = self.get_class(gci.get_subsumed())
        c2: OWLClassExpression = self.get_class(gci.get_subsumer())
        deg: Degree = gci.get_degree()
        Util.debug(f"Annotate GCI -> {c1} - {c2} - {deg}")
        if deg.is_number_not_one():
            new_annotations: set[OWLAnnotation] = self.get_annotations_for_axiom(deg)
            axiom: OWLSubClassOf = OWLSubClassOf(c1, c2, list(new_annotations))
        else:
            axiom: OWLSubClassOf = OWLSubClassOf(c1, c2)
        self.ontology.add_axiom(axiom)

    def annotate_pcd(
        self, c1: OWLClassExpression, pcd: PrimitiveConceptDefinition
    ) -> None:
        """
        This method processes a Primitive Concept Definition (PCD) to generate and register a subclass axiom within the ontology. It constructs an axiom asserting that the provided class expression is a subclass of the class defined within the PCD. If the PCD specifies a degree of membership that is not exactly 1.0, indicating a non-crisp relationship, the method generates and attaches specific annotations to the axiom to encode this fuzzy value. The resulting axiom is then added to the internal ontology, modifying its state.

        :param c1: The class expression to serve as the subclass in the generated axiom.
        :type c1: OWLClassExpression
        :param pcd: The primitive concept definition providing the definition and degree used to construct and annotate the subclass axiom.
        :type pcd: PrimitiveConceptDefinition
        """

        c2: OWLClassExpression = self.get_class(pcd.get_definition())
        n: float = pcd.get_degree()
        Util.debug(f"Annotate PCD -> {c1} - {c2} - {n}")
        if n != 1.0:
            new_annotations: set[OWLAnnotation] = self.get_annotations_for_axiom(n)
            axiom: OWLSubClassOf = OWLSubClassOf(c1, c2, list(new_annotations))
        else:
            axiom: OWLSubClassOf = OWLSubClassOf(c1, c2)
        self.ontology.add_axiom(axiom)

    def run(self) -> None:
        """
        Orchestrates the complete conversion of the internal FuzzyDL knowledge base into an OWL 2 ontology, modifying the internal ontology state and persisting the result to a file. The process begins by annotating the ontology with the specific fuzzy logic type defined in the knowledge base semantics. It then systematically processes and declares atomic concepts, concrete concepts, modifiers, assertions, and named individuals. The method translates various logical axioms—including concept equivalence, subsumption, and disjointness—into their corresponding OWL representations. Additionally, it establishes property characteristics such as domains, ranges, reflexivity, symmetry, transitivity, inverse relationships, sub-property hierarchies, and functionality for both object and data properties. Concrete features are mapped to appropriate XSD datatypes based on their type. The method concludes by saving the populated ontology to the specified output path, raising exceptions for issues such as mismatched property types or failures during file serialization.

        :raises Exception: If an unexpected error occurs during the conversion process, including failures when saving the ontology to the output file.
        :raises ValueError: Raised when a sub-property relationship is defined between properties of incompatible types, such as an object property and a data property.
        """

        # Set fuzzy logic type
        logic = str(constants.KNOWLEDGE_BASE_SEMANTICS)

        if logic:
            main_xml = FuzzyXML.build_main_xml(
                FuzzyOWL2Keyword.ONTOLOGY.get_str_value()
            )
            logic_xml = FuzzyXML.build_logic_xml(logic)
            main_xml.append(logic_xml)
            annotation: str = FuzzyXML.to_str(main_xml)
            # annotation: str = (
            #     f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.ONTOLOGY.get_str_value()}">\n'
            #     f'\t<{FuzzyOWL2Keyword.FUZZY_LOGIC.get_tag_name()} {FuzzyOWL2Keyword.LOGIC.get_str_value()}="{logic}" />\n'
            #     f"</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>"
            # )
            self.add_ontology_annotation(annotation)

        # Process atomic concepts
        # TODO
        for c in self.kb.atomic_concepts.values():
            self.ontology.add_axiom(
                OWLDeclaration(
                    self.get_class(str(c)),
                    [
                        OWLAnnotation(
                            OWLAnnotationProperty(URIRef(RDFS.label)),
                            OWLLiteral(Literal(str(c), lang="en")),
                        )
                    ],
                )
            )

        # Process concrete concepts
        for c in self.kb.concrete_concepts.values():
            self._process_concrete_concept(c)

        # Process modifiers
        for mod in self.kb.modifiers.values():
            self._process_modifier(mod)

        # Process assertions
        for ass in self.kb.assertions:
            self._process_assertion(ass)

        # Process individuals
        for ind in self.kb.individuals.values():
            self._process_individual(ind)

        for a in self.kb.axioms_A_equiv_C:
            c1: OWLClassExpression = self.get_class(a)
            for c in self.kb.axioms_A_equiv_C[a]:
                c2: OWLClassExpression = self.get_class(c)
                Util.debug(f"Process axioms_A_equiv_C -> {c1} - {c2}")
                axiom: OWLAxiom = OWLEquivalentClasses([c1, c2])
                self.ontology.add_axiom(axiom)

        for a in self.kb.axioms_A_is_a_B:
            c1: OWLClassExpression = self.get_class(a)
            for pcd in self.kb.axioms_A_is_a_B[a]:
                Util.debug(f"Process axioms_A_is_a_B -> {c1} - {pcd}")
                self.annotate_pcd(c1, pcd)

        for a in self.kb.axioms_A_is_a_C:
            c1: OWLClassExpression = self.get_class(a)
            for pcd in self.kb.axioms_A_is_a_C[a]:
                Util.debug(f"Process axioms_A_is_a_C -> {c1} - {pcd}")
                self.annotate_pcd(c1, pcd)

        for gcis in self.kb.axioms_C_is_a_D.values():
            for gci in gcis:
                Util.debug(f"Process axioms_C_is_a_D -> {gci}")
                self.annotate_gci(gci)

        for gcis in self.kb.axioms_C_is_a_A.values():
            for gci in gcis:
                Util.debug(f"Process axioms_C_is_a_A -> {gci}")
                self.annotate_gci(gci)

        for ce in self.kb.axioms_C_equiv_D:
            ce: ConceptEquivalence = typing.cast(ConceptEquivalence, ce)
            Util.debug(f"Process axioms_C_equiv_D -> {ce}")
            c1: OWLClassExpression = self.get_class(ce.get_c1())
            c2: OWLClassExpression = self.get_class(ce.get_c2())
            axiom: OWLAxiom = OWLEquivalentClasses([c1, c2])
            self.ontology.add_axiom(axiom)

        for a in self.kb.t_disjoints:
            c1: OWLClassExpression = self.get_class(a)
            for disj_C in self.kb.t_disjoints[a]:
                Util.debug(f"Process t_dis -> {c1} - {disj_C}")
                if a >= disj_C:
                    continue
                c2: OWLClassExpression = self.get_class(disj_C)
                axiom: OWLAxiom = OWLDisjointClasses([c1, c2])
                self.ontology.add_axiom(axiom)

        for r in self.kb.domain_restrictions:
            op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(r)
            )
            for c in self.kb.domain_restrictions[r]:
                Util.debug(f"Process domain restriction -> {c}")
                cl: OWLClassExpression = self.get_class(c)
                if isinstance(op, OWLObjectProperty):
                    axiom: OWLAxiom = OWLObjectPropertyDomain(op, cl)
                else:
                    axiom: OWLAxiom = OWLDataPropertyDomain(op, cl)
                self.ontology.add_axiom(axiom)

        for r in self.kb.range_restrictions:
            op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(r)
            )
            for c in self.kb.range_restrictions[r]:
                Util.debug(f"Process range restriction -> {c}")
                cl: OWLClassExpression = self.get_class(c)
                if isinstance(op, OWLObjectProperty):
                    axiom: OWLAxiom = OWLObjectPropertyRange(op, cl)
                else:
                    axiom: OWLAxiom = OWLDataPropertyRange(op, cl)
                self.ontology.add_axiom(axiom)

        for r in self.kb.reflexive_roles:
            Util.debug(f"Process reflexive role -> {r}")
            op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(r)
            )
            assert isinstance(op, OWLObjectProperty)
            axiom: OWLAxiom = OWLReflexiveObjectProperty(op)
            self.ontology.add_axiom(axiom)

        for r in self.kb.symmetric_roles:
            Util.debug(f"Process symmetric role -> {r}")
            op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(r)
            )
            assert isinstance(op, OWLObjectProperty)
            axiom: OWLAxiom = OWLSymmetricObjectProperty(op)
            self.ontology.add_axiom(axiom)

        for r in self.kb.transitive_roles:
            Util.debug(f"Process transitive role -> {r}")
            op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(r)
            )
            assert isinstance(op, OWLObjectProperty)
            axiom: OWLAxiom = OWLTransitiveObjectProperty(op)
            self.ontology.add_axiom(axiom)

        for r, r_set in self.kb.inverse_roles.items():
            Util.debug(f"Process inverse role -> inv_role = {r}")
            op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(r)
            )
            for s in r_set:
                Util.debug(f"Process inverse role -> role = {s}")
                op2: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_object_property(s)
                )
                assert isinstance(op, OWLObjectProperty) and isinstance(
                    op2, OWLObjectProperty
                )
                axiom: OWLAxiom = OWLInverseObjectProperties(op, op2)
                self.ontology.add_axiom(axiom)

        for r in self.kb.roles_with_parents:
            Util.debug(f"Process role with parents -> role = {r}")
            op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(r)
            )
            par: dict[str, float] = self.kb.roles_with_parents.get(r, dict())
            for s in par:
                Util.debug(f"Process role with parents -> parent = {s}")
                op2: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_object_property(s)
                )
                if isinstance(op, OWLObjectProperty) and isinstance(
                    op2, OWLObjectProperty
                ):
                    axiom: OWLAxiom = OWLSubObjectPropertyOf(op, op2)
                elif isinstance(op, OWLDataProperty) and isinstance(
                    op2, OWLDataProperty
                ):
                    axiom: OWLAxiom = OWLSubDataPropertyOf(op, op2)
                else:
                    raise ValueError(
                        f"Invalid property types: {type(op)} and {type(op2)}"
                    )
                self.ontology.add_axiom(axiom)

        for r in self.kb.functional_roles:
            Util.debug(f"Process functional role -> {r}")
            if r in self.kb.concrete_features:
                dp: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_data_property(r)
                )
                if isinstance(dp, OWLDataProperty):
                    axiom: OWLAxiom = OWLFunctionalDataProperty(dp)
                else:
                    axiom: OWLAxiom = OWLFunctionalObjectProperty(dp)
            else:
                op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_object_property(r)
                )
                if isinstance(op, OWLObjectProperty):
                    axiom: OWLAxiom = OWLFunctionalObjectProperty(op)
                else:
                    axiom: OWLAxiom = OWLFunctionalDataProperty(op)
            self.ontology.add_axiom(axiom)

        for cf_name, cf in self.kb.concrete_features.items():
            if cf is None:
                continue
            Util.debug(f"Process concrete feature {cf_name} -> {cf}")
            cf_type: ConcreteFeatureType = cf.get_type()
            dp: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_data_property(cf_name)
            )
            if cf_type == ConcreteFeatureType.BOOLEAN:
                dt: OWLDatatype = OWLDatatype(XSD.boolean)
            elif cf_type == ConcreteFeatureType.INTEGER:
                dt: OWLDatatype = OWLDatatype(XSD.integer)
            elif cf_type == ConcreteFeatureType.REAL:
                dt: OWLDatatype = OWLDatatype(XSD.decimal)
            elif cf_type == ConcreteFeatureType.STRING:
                dt: OWLDatatype = OWLDatatype(RDF.PlainLiteral)
                # Util.warning(
                #     "To Implement: String Datatype Property Range conversion"
                # )
            if isinstance(dp, OWLDataProperty):
                axiom: OWLAxiom = OWLDataPropertyRange(dp, dt)
            else:
                axiom: OWLAxiom = OWLObjectPropertyRange(dp, dt)
            self.ontology.add_axiom(axiom)

        # Save ontology
        try:
            self.ontology.save(os.path.abspath(self.output_FOWL))
        except Exception as ex:
            Util.error(f"Error saving ontology: {ex}", file=sys.stderr)
            raise ex

    def _process_concrete_concept(self, c: FuzzyConcreteConcept) -> None:
        """
        Processes a FuzzyDL concrete concept by generating a corresponding OWL2 datatype definition restricted to a specific numeric interval. The method creates a datatype identified by the concept's IRI and constrains it to values between `c.k1` and `c.k2` using XSD integer facets. It adds the necessary declaration and datatype definition axioms to the ontology, including an RDFS label for the concept. Furthermore, it constructs a FuzzyXML annotation describing the datatype specifics and attaches it to the entity. As a side effect, the method updates the internal `datatypes` dictionary to map the concept string to the newly created OWL datatype.

        :param c: The fuzzy concrete concept providing the interval bounds and specific details required to define and register the corresponding OWL datatype.
        :type c: FuzzyConcreteConcept
        """

        Util.debug(f"Process concrete concept -> {c}")
        current_datatype: OWLDatatype = OWLDatatype(self.datatype_iri(c))
        self.datatypes[str(c)] = current_datatype

        # specific: str = self._get_concrete_concept_specifics(c)
        specific: tuple[str, dict[str, str]] = self._get_concrete_concept_specifics(c)

        int_datatype: OWLDatatype = OWLDatatype(XSD.integer)
        greater_than: OWLDatatypeRestriction = OWLDatatypeRestriction(
            int_datatype,
            [
                OWLFacet(
                    OWLFacet.MIN_INCLUSIVE,
                    OWLLiteral(Literal(str(c.k1), datatype=XSD.decimal)),
                )
            ],
        )
        less_than: OWLDatatypeRestriction = OWLDatatypeRestriction(
            int_datatype,
            [
                OWLFacet(
                    OWLFacet.MAX_INCLUSIVE,
                    OWLLiteral(Literal(str(c.k2), datatype=XSD.decimal)),
                )
            ],
        )
        unit_interval: OWLDataIntersectionOf = OWLDataIntersectionOf(
            [greater_than, less_than]
        )
        definition: OWLDatatypeDefinition = OWLDatatypeDefinition(
            current_datatype, unit_interval
        )
        self.ontology.add_axiom(
            OWLDeclaration(
                current_datatype,
                [
                    OWLAnnotation(
                        OWLAnnotationProperty(URIRef(RDFS.label)),
                        OWLLiteral(Literal(str(c), lang="en")),
                    )
                ],
            )
        )
        self.ontology.add_axiom(definition)

        main_xml = FuzzyXML.build_main_xml(FuzzyOWL2Keyword.DATATYPE.get_str_value())
        datatype_xml = FuzzyXML.build_datatype_xml(specific[0], specific[1])
        main_xml.append(datatype_xml)
        annotation: str = FuzzyXML.to_str(main_xml)

        # annotation: str = (
        #     f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.DATATYPE.get_str_value()}">\n'
        #     f'\t<{FuzzyOWL2Keyword.DATATYPE.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{specific}"/>\n'
        #     f"</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>"
        # )
        self.add_entity_annotation(annotation, current_datatype)

    def _get_concrete_concept_specifics(
        self, c: FuzzyConcreteConcept
    ) -> tuple[str, dict[str, str]]:
        """
        Extracts the type identifier and associated parameters for a given fuzzy concrete concept to facilitate translation into the OWL2 format. The method inspects the runtime type of the input concept to determine the appropriate fuzzy shape—such as crisp, left-shoulder, right-shoulder, triangular, or trapezoidal—and maps its numeric attributes to a standardized dictionary keyed by OWL2 keywords. If the input concept does not correspond to any of the expected concrete types, the method returns an empty type string and an empty parameter dictionary as a fallback.

        :param c: The fuzzy concrete concept instance to be processed to extract its specific type and parameters.
        :type c: FuzzyConcreteConcept

        :return: A tuple containing the concept type identifier and a dictionary of its specific parameters. If the concept type is not recognized, returns an empty string and an empty dictionary.

        :rtype: tuple[str, dict[str, str]]
        """

        if isinstance(c, CrispConcreteConcept):
            return FuzzyOWL2Keyword.CRISP.get_str_value(), {
                FuzzyOWL2Keyword.A.get_str_value(): str(c.a),
                FuzzyOWL2Keyword.B.get_str_value(): str(c.b),
            }
        elif isinstance(c, LeftConcreteConcept):
            return FuzzyOWL2Keyword.LEFT_SHOULDER.get_str_value(), {
                FuzzyOWL2Keyword.A.get_str_value(): str(c.a),
                FuzzyOWL2Keyword.B.get_str_value(): str(c.b),
            }
        elif isinstance(c, RightConcreteConcept):
            return FuzzyOWL2Keyword.RIGHT_SHOULDER.get_str_value(), {
                FuzzyOWL2Keyword.A.get_str_value(): str(c.a),
                FuzzyOWL2Keyword.B.get_str_value(): str(c.b),
            }
        elif isinstance(c, TriangularConcreteConcept):
            return FuzzyOWL2Keyword.TRIANGULAR.get_str_value(), {
                FuzzyOWL2Keyword.A.get_str_value(): str(c.a),
                FuzzyOWL2Keyword.B.get_str_value(): str(c.b),
                FuzzyOWL2Keyword.C.get_str_value(): str(c.c),
            }
        elif isinstance(c, TrapezoidalConcreteConcept):
            return FuzzyOWL2Keyword.TRAPEZOIDAL.get_str_value(), {
                FuzzyOWL2Keyword.A.get_str_value(): str(c.a),
                FuzzyOWL2Keyword.B.get_str_value(): str(c.b),
                FuzzyOWL2Keyword.C.get_str_value(): str(c.c),
                FuzzyOWL2Keyword.D.get_str_value(): str(c.d),
            }
        return "", dict()

    # def _get_concrete_concept_specifics(self, c: FuzzyConcreteConcept) -> str:
    #     """Get concrete concept specific parameters"""
    #     if isinstance(c, CrispConcreteConcept):
    #         return f'{FuzzyOWL2Keyword.CRISP.get_str_value()}" {FuzzyOWL2Keyword.A.get_str_value()}="{c.a}" {FuzzyOWL2Keyword.B.get_str_value()}="{c.b}'
    #     elif isinstance(c, LeftConcreteConcept):
    #         return f'{FuzzyOWL2Keyword.LEFT_SHOULDER.get_str_value()}" {FuzzyOWL2Keyword.A.get_str_value()}="{c.a}" {FuzzyOWL2Keyword.B.get_str_value()}="{c.b}'
    #     elif isinstance(c, RightConcreteConcept):
    #         return f'{FuzzyOWL2Keyword.RIGHT_SHOULDER.get_str_value()}" {FuzzyOWL2Keyword.A.get_str_value()}="{c.a}" {FuzzyOWL2Keyword.B.get_str_value()}="{c.b}'
    #     elif isinstance(c, TriangularConcreteConcept):
    #         return f'{FuzzyOWL2Keyword.TRIANGULAR.get_str_value()}" {FuzzyOWL2Keyword.A.get_str_value()}="{c.a}" {FuzzyOWL2Keyword.B.get_str_value()}="{c.b}" {FuzzyOWL2Keyword.C.get_str_value()}="{c.c}'
    #     elif isinstance(c, TrapezoidalConcreteConcept):
    #         return f'{FuzzyOWL2Keyword.TRAPEZOIDAL.get_str_value()}" {FuzzyOWL2Keyword.A.get_str_value()}="{c.a}" {FuzzyOWL2Keyword.B.get_str_value()}="{c.b}" {FuzzyOWL2Keyword.C.get_str_value()}="{c.c}" {FuzzyOWL2Keyword.D.get_str_value()}="{c.d}'
    #     return ""

    def _process_modifier(self, mod: Modifier) -> None:
        """
        Converts a fuzzy logic modifier into an OWL 2 datatype representation and integrates it into the current ontology. The method constructs an XML annotation specific to the modifier's type—supporting linear and triangular shapes—and uses it to annotate the newly created datatype. It registers the datatype within the internal modifiers dictionary and adds a declaration axiom with an English label to the ontology. If the provided modifier is not a recognized type, a ValueError is raised.

        :param mod: The fuzzy logic modifier instance (e.g., Linear or Triangular) containing parameters required to construct the corresponding OWL datatype and XML representation.
        :type mod: Modifier

        :raises ValueError: Raised when the provided modifier is not an instance of `LinearModifier` or `TriangularModifier`.
        """

        Util.debug(f"Process modifier -> {mod}")

        main_xml = FuzzyXML.build_main_xml(FuzzyOWL2Keyword.MODIFIER.get_str_value())

        if isinstance(mod, LinearModifier):
            modifier_xml = FuzzyXML.build_modifier_xml(
                FuzzyOWL2Keyword.LINEAR.get_str_value(),
                {FuzzyOWL2Keyword.C.get_str_value(): str(mod.c)},
            )
            # annotation: str = (
            #     f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.MODIFIER.get_str_value()}">\n'
            #     f'\t<{FuzzyOWL2Keyword.MODIFIER.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{FuzzyOWL2Keyword.LINEAR.get_str_value()}" {FuzzyOWL2Keyword.C.get_str_value()}="{mod.c}"/>\n'
            #     f"</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>"
            # )
        elif isinstance(mod, TriangularModifier):
            modifier_xml = FuzzyXML.build_modifier_xml(
                FuzzyOWL2Keyword.TRIANGULAR.get_str_value(),
                {
                    FuzzyOWL2Keyword.A.get_str_value(): str(mod.a),
                    FuzzyOWL2Keyword.B.get_str_value(): str(mod.b),
                    FuzzyOWL2Keyword.C.get_str_value(): str(mod.c),
                },
            )
            # annotation: str = (
            #     f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.MODIFIER.get_str_value()}">\n'
            #     f'\t<{FuzzyOWL2Keyword.MODIFIER.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{FuzzyOWL2Keyword.TRIANGULAR.get_str_value()}" {FuzzyOWL2Keyword.A.get_str_value()}="{mod.a}" {FuzzyOWL2Keyword.B.get_str_value()}="{mod.b}" {FuzzyOWL2Keyword.C.get_str_value()}="{mod.c}"/>\n'
            #     f"</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>"
            # )
        else:
            raise ValueError(f"Unknown modifier type: {type(mod)}")

        main_xml.append(modifier_xml)
        annotation: str = FuzzyXML.to_str(main_xml)

        current_datatype: OWLDatatype = OWLDatatype(self.datatype_iri(mod))
        self.modifiers[str(mod)] = current_datatype
        self.ontology.add_axiom(
            OWLDeclaration(
                current_datatype,
                [
                    OWLAnnotation(
                        OWLAnnotationProperty(URIRef(RDFS.label)),
                        OWLLiteral(Literal(str(mod), lang="en")),
                    )
                ],
            )
        )
        self.add_entity_annotation(annotation, current_datatype)

    def _process_assertion(self, ass: Assertion) -> None:
        """
        Converts a FuzzyDL assertion into an OWL 2 Class Assertion Axiom and adds it to the internal ontology. The method retrieves the corresponding OWL individual and class expression for the assertion's subject and concept. It specifically handles fuzzy membership degrees by checking the assertion's lower limit; if the degree is not exactly 1.0, it generates and attaches annotations to the axiom to represent this fuzzy value. The resulting axiom is then persisted to the ontology as a side effect of this operation.

        :param ass: The assertion object providing the individual, concept, and degree data used to construct an OWL class assertion axiom.
        :type ass: Assertion
        """

        Util.debug(f"Process assertion -> {ass}")
        i: OWLNamedIndividual = self.get_individual(str(ass.get_individual()))
        c: OWLClassExpression = self.get_class(ass.get_concept())
        deg: Degree = ass.get_lower_limit()
        if deg.is_number_not_one():
            new_ann: set[OWLAnnotation] = self.get_annotations_for_axiom(deg)
            axiom: OWLClassAssertion = OWLClassAssertion(c, i, list(new_ann))
        else:
            axiom: OWLClassAssertion = OWLClassAssertion(c, i)
        self.ontology.add_axiom(axiom)

    def _process_individual(self, ind: Individual) -> None:
        """
        Converts a FuzzyDL individual into corresponding OWL 2 axioms and adds them to the ontology. The method retrieves or creates the primary OWL named individual and iterates through its associated role relations. For each relation, it ensures the corresponding property and target individual exist, then constructs a property assertion axiom. If the relation has a fuzzy degree value other than one, the method attaches annotations to the axiom before adding it to the ontology.

        :param ind: The individual object containing role relations to be transformed into OWL property assertions and added to the ontology.
        :type ind: Individual
        """

        Util.debug(f"Process individual -> {ind}")
        i: OWLClassExpression = self.get_individual(str(ind))
        for a in ind.role_relations.values():
            for rel in a:
                r: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_object_property(rel.get_role_name())
                )  # Retrieve or create the object property
                i2: OWLNamedIndividual = self.get_individual(
                    str(rel.get_object_individual())
                )  # Retrieve or create the related individual

                deg: Degree = rel.get_degree()
                if isinstance(r, OWLObjectProperty):
                    factory_call: typing.Callable = OWLObjectPropertyAssertion
                else:
                    factory_call: typing.Callable = OWLDataPropertyAssertion
                if deg.is_number_not_one():  # If the degree is not 1
                    # Create annotations
                    new_annotations: set[OWLAnnotation] = (
                        self.get_annotations_for_axiom(deg)
                    )
                    axiom: typing.Union[
                        OWLObjectPropertyAssertion, OWLDataPropertyAssertion
                    ] = factory_call(r, i, i2, new_annotations)
                else:
                    axiom: typing.Union[
                        OWLObjectPropertyAssertion, OWLDataPropertyAssertion
                    ] = factory_call(r, i, i2)
                self.ontology.add_axiom(axiom)


def main():
    """Serves as the command-line entry point for the script, initiating the conversion process from FuzzyDL ontology files to OWL2 format. It strictly enforces that exactly two command-line arguments are supplied: the input path for the FuzzyDL ontology and the output path for the generated OWL2 ontology. If the argument count is invalid, the function prints a usage instruction to standard error and terminates the application with an error code. When arguments are valid, it instantiates the FuzzydlToOwl2 converter with the specified paths and triggers the conversion routine, resulting in file system modifications."""

    if len(sys.argv) != 3:
        Util.error(
            "Error. Use: python fuzzydl_to_owl2.py <fuzzyDLOntology> <Owl2Ontology>",
            file=sys.stderr,
        )
        sys.exit(-1)

    converter = FuzzydlToOwl2(sys.argv[1], sys.argv[2])
    converter.run()


if __name__ == "__main__":
    main()
