import os
import typing

from rdflib import Namespace

from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.util import Util
from fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept import ChoquetConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.owl_types.crisp_function import CrispFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype import FuzzyDatatype
from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier import FuzzyModifier
from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_nominal_concept import FuzzyNominalConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.left_shoulder_function import (
    LeftShoulderFunction,
)
from fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function import LinearFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier import LinearModifier
from fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_concept import ModifiedConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_function import ModifiedFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property import ModifiedProperty
from fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept import OwaConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.qowa_concept import QowaConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept import QsugenoConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.right_shoulder_function import (
    RightShoulderFunction,
)
from fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept import SugenoConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.trapezoidal_function import TrapezoidalFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_function import TriangularFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_modifer import TriangularModifier
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_concept import WeightedConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_max_concept import WeightedMaxConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_min_concept import WeightedMinConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_concept import WeightedSumConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_zero_concept import (
    WeightedSumZeroConcept,
)
from fuzzy_dl_owl2.fuzzyowl2.parser.owl2_xml_parser import FuzzyOwl2XMLParser
from pyowl2.abstracts.annotation_value import OWLAnnotationValue
from pyowl2.abstracts.axiom import OWLAxiom
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.data_range import OWLDataRange
from pyowl2.abstracts.entity import OWLEntity
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.axioms.assertion.class_assertion import OWLClassAssertion
from pyowl2.axioms.assertion.data_property_assertion import OWLDataPropertyAssertion
from pyowl2.axioms.assertion.different_individuals import OWLDifferentIndividuals
from pyowl2.axioms.assertion.negative_data_property_assertion import (
    OWLNegativeDataPropertyAssertion,
)
from pyowl2.axioms.assertion.negative_object_property_assertion import (
    OWLNegativeObjectPropertyAssertion,
)
from pyowl2.axioms.assertion.object_property_assertion import OWLObjectPropertyAssertion
from pyowl2.axioms.assertion.same_individual import OWLSameIndividual
from pyowl2.axioms.class_axiom.disjoint_classes import OWLDisjointClasses
from pyowl2.axioms.class_axiom.disjoint_union import OWLDisjointUnion
from pyowl2.axioms.class_axiom.equivalent_classes import OWLEquivalentClasses
from pyowl2.axioms.class_axiom.sub_class_of import OWLSubClassOf
from pyowl2.axioms.data_property_axiom.data_property_domain import OWLDataPropertyDomain
from pyowl2.axioms.data_property_axiom.data_property_range import OWLDataPropertyRange
from pyowl2.axioms.data_property_axiom.disjoint_data_properties import (
    OWLDisjointDataProperties,
)
from pyowl2.axioms.data_property_axiom.equivalent_data_properties import (
    OWLEquivalentDataProperties,
)
from pyowl2.axioms.data_property_axiom.functional_data_property import (
    OWLFunctionalDataProperty,
)
from pyowl2.axioms.data_property_axiom.sub_data_property_of import OWLSubDataPropertyOf
from pyowl2.axioms.datatype_definition import OWLDatatypeDefinition
from pyowl2.axioms.declaration import OWLDeclaration
from pyowl2.axioms.object_property_axiom.asymmetric_object_property import (
    OWLAsymmetricObjectProperty,
)
from pyowl2.axioms.object_property_axiom.disjoint_object_properties import (
    OWLDisjointObjectProperties,
)
from pyowl2.axioms.object_property_axiom.equivalent_object_properties import (
    OWLEquivalentObjectProperties,
)
from pyowl2.axioms.object_property_axiom.functional_object_property import (
    OWLFunctionalObjectProperty,
)
from pyowl2.axioms.object_property_axiom.inverse_functional_object_property import (
    OWLInverseFunctionalObjectProperty,
)
from pyowl2.axioms.object_property_axiom.inverse_object_properties import (
    OWLInverseObjectProperties,
)
from pyowl2.axioms.object_property_axiom.irreflexive_object_property import (
    OWLIrreflexiveObjectProperty,
)
from pyowl2.axioms.object_property_axiom.object_property_chain import (
    OWLObjectPropertyChain,
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
from pyowl2.class_expression.data_exact_cardinality import OWLDataExactCardinality
from pyowl2.class_expression.data_has_value import OWLDataHasValue
from pyowl2.class_expression.data_max_cardinality import OWLDataMaxCardinality
from pyowl2.class_expression.data_min_cardinality import OWLDataMinCardinality
from pyowl2.class_expression.data_some_values_from import OWLDataSomeValuesFrom
from pyowl2.class_expression.object_all_values_from import OWLObjectAllValuesFrom
from pyowl2.class_expression.object_complement_of import OWLObjectComplementOf
from pyowl2.class_expression.object_exact_cardinality import OWLObjectExactCardinality
from pyowl2.class_expression.object_has_self import OWLObjectHasSelf
from pyowl2.class_expression.object_has_value import OWLObjectHasValue
from pyowl2.class_expression.object_intersection_of import OWLObjectIntersectionOf
from pyowl2.class_expression.object_max_cardinality import OWLObjectMaxCardinality
from pyowl2.class_expression.object_min_cardinality import OWLObjectMinCardinality
from pyowl2.class_expression.object_one_of import OWLObjectOneOf
from pyowl2.class_expression.object_some_values_from import OWLObjectSomeValuesFrom
from pyowl2.class_expression.object_union_of import OWLObjectUnionOf
from pyowl2.data_range.data_intersection_of import OWLDataIntersectionOf
from pyowl2.data_range.datatype_restriction import OWLDatatypeRestriction, OWLFacet
from pyowl2.expressions.data_property import OWLDataProperty
from pyowl2.expressions.object_property import OWLObjectProperty
from pyowl2.getter.rdf_xml_getter import AxiomsType
from pyowl2.individual.anonymous_individual import OWLAnonymousIndividual
from pyowl2.literal.literal import OWLLiteral
from pyowl2.ontology import OWLOntology


class FuzzyOwl2(object):
    """
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
    """

    POS_INFINITY: float = 10000.0
    NEG_INFINITY: float = -POS_INFINITY

    def __init__(
        self,
        input_file: str,
        output_file: str,
        base_iri: str = "http://www.semanticweb.org/ontologies/fuzzydl_ontology#",
    ) -> None:
        """
        Initializes the FuzzyOWL2 translator by configuring file paths, loading necessary resources, and preparing internal data structures for ontology processing. It accepts the path to an input OWL2 ontology file, a name for the output file where the translated fuzzy description logic will be written, and an optional base IRI used to construct the ontology's identifier. The constructor sets up dictionaries to track defined concepts, properties, datatypes, and modifiers, triggers the loading of the parser configuration, and immediately instantiates the underlying OWLOntology object from the input file. Additionally, it prepares an annotation property for fuzzy labels and registers the ontology within the internal collection.

        :param input_file: Path to the OWL2 ontology file to be processed.
        :type input_file: str
        :param output_file: The filename for the translated fuzzy DL output.
        :type output_file: str
        :param base_iri: The base Internationalized Resource Identifier (IRI) used as the namespace for the ontology. It defines the root identifier for the ontology and its entities.
        :type base_iri: str
        """

        self.output_dl: str = os.path.join(constants.RESULTS_PATH, output_file)

        self.defined_concepts: dict[str, ConceptDefinition] = dict()
        self.defined_properties: dict[str, ConceptDefinition] = dict()
        self.fuzzy_datatypes: dict[str, ConceptDefinition] = dict()
        self.fuzzy_modifiers: dict[str, ConceptDefinition] = dict()
        self.processed_axioms: set[str] = set()
        self.ontologies: set[OWLOntology] = set()

        FuzzyOwl2XMLParser.load_config()

        self.ontology_path = input_file
        self.ontology_iri = IRI(Namespace(base_iri))
        self.ontology: OWLOntology = OWLOntology(
            self.ontology_iri, self.ontology_path, OWL1_annotations=True
        )
        self.fuzzy_label: OWLAnnotationProperty = OWLAnnotationProperty(
            IRI(self.ontology_iri.namespace, ConfigReader.OWL_ANNOTATION_LABEL)
        )
        self.ontologies.add(self.ontology)
        # self.ontologies.update(self.manager.getImportsClosure(self.ontology))

    def get_short_name(self, e: OWLEntity) -> str:
        """
        Computes a concise short name for the given OWL entity by parsing its Internationalized Resource Identifier (IRI). The method isolates the portion of the IRI string that follows the final hash symbol ('#'), effectively extracting the fragment identifier. If the IRI does not contain a hash symbol, the full string representation of the IRI is returned. This operation is side-effect free and is typically used to generate human-readable labels for ontology entities.

        :param e: The entity for which to compute the short name.
        :type e: OWLEntity

        :return: The short name of the entity, corresponding to the fragment identifier of its IRI (the substring after the last '#').

        :rtype: str
        """

        return str(e.iri).split("#")[-1]

    def translate_owl2ontology(self) -> None:
        """Orchestrates the conversion of the loaded OWL2 ontology into a Fuzzy Description Logic (DL) representation. This method systematically processes various components of the ontology by handling annotations for the ontology itself, datatypes, concepts, and properties, before finally translating the core axioms. It acts as the main entry point for the translation workflow, ensuring that all structural elements are transformed to support fuzzy logic reasoning."""

        self.process_ontology_annotations()
        self.process_datatype_annotations()
        self.process_concept_annotations()
        self.process_property_annotations()
        self.process_ontology_axioms()

    def process_ontology_annotations(self) -> None:
        """Iterates through the loaded ontologies to identify and process annotations specifically associated with the fuzzy label property. For each ontology, it retrieves the available annotations and filters out any that do not match the configured fuzzy label or are missing. The string value of the matching annotations is parsed into a logic representation, which is then written to the output via the internal writer method. This process ensures that only relevant fuzzy logic definitions are extracted and persisted, while skipping ontologies or annotations that do not meet the criteria."""

        for ontology in self.ontologies:
            annotations: typing.Optional[set[OWLAnnotation]] = (
                ontology.getter.get_owl_ontology_annotations()
            )
            if annotations is None:
                continue
            for annotation in annotations:
                if annotation.annotation_property != self.fuzzy_label:
                    continue
                value: OWLAnnotationValue = annotation.annotation_value
                annotation_str: str = str(value)
                Util.debug(f"Annotation for ontology -> {annotation_str}")
                logic: typing.Optional[str] = FuzzyOwl2XMLParser.parse_string(
                    annotation_str
                )
                Util.debug(f"Parsed annotation -> {logic}")
                self.write_fuzzy_logic(logic)

    def __get_facets(self, name: str) -> list[float]:
        """
        Searches the loaded ontologies for a datatype definition matching the specified name and extracts its numeric lower and upper bounds. The method iterates through datatype definition axioms, handling both direct datatype restrictions and intersections of two restrictions to identify the relevant facets. It converts exclusive bounds to inclusive bounds by applying a small epsilon adjustment. If the datatype cannot be found or does not contain valid restriction facets, the method returns a list containing negative and positive infinity.

        :param name: The name of the datatype for which to retrieve restriction facets.
        :type name: str

        :return: A list of two floats representing the lower and upper bounds of the datatype, defaulting to negative and positive infinity if no restrictions are found. Exclusive bounds are adjusted by a small epsilon value.

        :rtype: list[float]
        """

        facets: list[float] = [float("-inf"), float("inf")]
        for ontology in self.ontologies:
            datatype_def_axioms: set[OWLDatatypeDefinition] = ontology.get_axioms(
                AxiomsType.DATATYPE_DEFINITION
            )
            if datatype_def_axioms is None:
                continue
            for axiom in datatype_def_axioms:
                Util.debug(f"Getting facets for axiom {axiom}...")
                assert isinstance(axiom, OWLDatatypeDefinition)
                datatype_name: str = self.get_short_name(axiom.datatype).replace(
                    ":", ""
                )
                if datatype_name != name:
                    continue
                f1: typing.Optional[OWLFacet] = None
                f2: typing.Optional[OWLFacet] = None
                Util.debug(f"Getting facets for data range {axiom.data_range}...")
                if isinstance(axiom.data_range, OWLDatatypeRestriction):
                    facets: list[OWLFacet] = list(axiom.data_range.restrictions)
                    f1: OWLFacet = facets[0]
                    f2: OWLFacet = facets[1]
                elif isinstance(axiom.data_range, OWLDataIntersectionOf):
                    data_range: OWLDataIntersectionOf = typing.cast(
                        OWLDataIntersectionOf, axiom.data_range
                    )
                    operands: list[OWLDataRange] = list(data_range.data_ranges)
                    if operands is None or len(operands) != 2:
                        continue
                    r1: OWLDataRange = operands[0]
                    r2: OWLDataRange = operands[1]
                    if not (
                        isinstance(r1, OWLDatatypeRestriction)
                        and isinstance(r2, OWLDatatypeRestriction)
                    ):
                        continue
                    restriction1: OWLDatatypeRestriction = typing.cast(
                        OWLDatatypeRestriction, r1
                    )
                    restriction2: OWLDatatypeRestriction = typing.cast(
                        OWLDatatypeRestriction, r2
                    )
                    facets1: list[OWLFacet] = restriction1.restrictions
                    facets2: list[OWLFacet] = restriction2.restrictions
                    if (
                        facets1 is None
                        or len(facets1) != 1
                        or facets2 is None
                        or len(facets2) != 1
                    ):
                        continue
                    f1: OWLFacet = facets1[0]
                    f2: OWLFacet = facets2[0]

                Util.debug(f"Facets 1 {f1}.")
                Util.debug(f"Facets 2 {f2}.")
                if f1:
                    if f1.constraint_to_uriref() == OWLFacet.MIN_INCLUSIVE:
                        facets[0] = float(str(f1.value.value))
                    elif f1.constraint_to_uriref() == OWLFacet.MIN_EXCLUSIVE:
                        facets[0] = float(str(f1.value.value)) + ConfigReader.EPSILON
                    elif f1.constraint_to_uriref() == OWLFacet.MAX_INCLUSIVE:
                        facets[1] = float(str(f1.value.value))
                    elif f1.constraint_to_uriref() == OWLFacet.MAX_EXCLUSIVE:
                        facets[1] = float(str(f1.value.value)) - ConfigReader.EPSILON
                if f2:
                    if f2.constraint_to_uriref() == OWLFacet.MIN_INCLUSIVE:
                        facets[0] = float(str(f2.value.value))
                    elif f2.constraint_to_uriref() == OWLFacet.MIN_EXCLUSIVE:
                        facets[0] = float(str(f2.value.value)) + ConfigReader.EPSILON
                    elif f2.constraint_to_uriref() == OWLFacet.MAX_INCLUSIVE:
                        facets[1] = float(str(f2.value.value))
                    elif f2.constraint_to_uriref() == OWLFacet.MAX_INCLUSIVE:
                        facets[1] = float(str(f2.value.value)) - ConfigReader.EPSILON
                return facets
        return facets

    def process_datatype_annotations(self) -> None:
        """
        Iterates over the loaded ontologies to identify and process datatype declarations that contain annotations defining fuzzy logic concepts. For each annotated datatype, the method extracts the annotation string, parses it into a specific fuzzy concept (such as a fuzzy datatype or modifier), and retrieves associated numeric facets to define value ranges. The parsed concepts are stored in internal dictionaries, and corresponding definition files are generated based on the specific function type (e.g., triangular, trapezoidal). The method skips datatypes lacking annotations, logs an error if multiple annotations are present, and raises a ValueError if the annotation cannot be parsed into a valid fuzzy concept.

        :raises ValueError: Raised if the parsed annotation value is not a recognized fuzzy datatype or modifier type.
        """

        for ontology in self.ontologies:
            for axiom in ontology.get_axioms(AxiomsType.DATATYPES):
                assert isinstance(axiom, OWLDeclaration)
                entity: OWLEntity = axiom.entity
                if not isinstance(entity, OWLDatatype):
                    continue
                Util.debug(f"Datatype for ontology -> {entity}")
                datatype: OWLDatatype = typing.cast(OWLDatatype, entity)
                annotations: set[OWLAnnotation] = axiom.axiom_annotations
                if annotations is None or len(annotations) == 0:
                    continue
                if len(annotations) > 1:
                    Util.error(
                        f"Error: There are {len(annotations)} datatype annotations for {datatype}"
                    )
                annotation: OWLAnnotation = list(annotations)[0].annotation_value
                annotation_str: str = str(annotation)
                Util.debug(f"Annotation for {datatype} -> {annotation_str}")
                datatype_name: str = self.get_short_name(datatype)
                facets: list[OWLFacet] = self.__get_facets(datatype_name)
                c: typing.Union[ConceptDefinition, FuzzyModifier] = (
                    FuzzyOwl2XMLParser.parse_string(annotation_str)
                )
                Util.debug(f"Parsed annotation -> {c}")
                if isinstance(c, FuzzyDatatype):
                    c.set_min_value(facets[0])
                    c.set_max_value(facets[1])
                    Util.debug(f"Concept for {datatype} -> {c}")
                    self.fuzzy_datatypes[datatype_name] = c
                    if isinstance(c, CrispFunction):
                        self.write_crisp_function_definition(datatype_name, c)
                    elif isinstance(c, LeftShoulderFunction):
                        self.write_left_shoulder_function_definition(datatype_name, c)
                    elif isinstance(c, RightShoulderFunction):
                        self.write_right_shoulder_function_definition(datatype_name, c)
                    elif isinstance(c, LinearFunction):
                        self.write_linear_function_definition(datatype_name, c)
                    elif isinstance(c, TriangularFunction):
                        self.write_triangular_function_definition(datatype_name, c)
                    elif isinstance(c, TrapezoidalFunction):
                        self.write_trapezoidal_function_definition(datatype_name, c)
                elif isinstance(c, LinearModifier):
                    self.fuzzy_modifiers[datatype_name] = c
                    self.write_linear_modifier_definition(datatype_name, c)
                elif isinstance(c, TriangularModifier):
                    self.fuzzy_modifiers[datatype_name] = c
                    self.write_triangular_modifier_definition(datatype_name, c)
                else:
                    raise ValueError

    def process_concept_annotations(self) -> None:
        """
        Iterates through the loaded ontologies to identify and process class declarations that define fuzzy concepts via annotations. For each annotated class, the method extracts the annotation value, parses it into a concrete `ConceptDefinition` object, and retrieves the class's short name. Based on the specific type of the parsed concept (e.g., ModifiedConcept, WeightedConcept, or SugenoConcept), the method registers the concept in the `defined_concepts` dictionary and delegates to a specific write method to output the definition. The method includes validation logic that logs errors if a class has multiple annotations or if a fuzzy modifier is undefined, and it raises a ValueError if the parsed concept type does not match any known fuzzy concept categories.

        :raises ValueError: Raised if the parsed concept definition does not match any of the supported concept types.
        """

        for ontology in self.ontologies:
            for axiom in ontology.get_axioms(AxiomsType.CLASSES):
                assert isinstance(axiom, OWLDeclaration)
                entity: OWLEntity = axiom.entity
                if not isinstance(entity, OWLClass):
                    continue
                cls: OWLClass = typing.cast(OWLClass, entity)
                Util.debug(f"Concept for ontology -> {cls}")
                annotations: set[OWLAnnotation] = axiom.axiom_annotations
                if annotations is None or len(annotations) == 0:
                    continue
                if len(annotations) > 1:
                    Util.error(
                        f"Error: There are {len(annotations)} class annotations for {cls}"
                    )
                annotation: OWLAnnotation = list(annotations)[0].annotation_value
                annotation_str: str = str(annotation)
                Util.debug(f"Annotation for concept {cls} -> {annotation_str}")
                concept: ConceptDefinition = FuzzyOwl2XMLParser.parse_string(
                    annotation_str
                )
                Util.debug(f"Parsed annotation -> {concept}")
                name: str = self.get_short_name(cls)
                if isinstance(concept, ModifiedConcept):
                    mod_name: str = concept.get_fuzzy_modifier()
                    if mod_name not in self.fuzzy_modifiers:
                        Util.error(f"Error: Fuzzy modifier {mod_name} not defined.")
                    self.defined_concepts[name] = concept
                    self.write_modified_concept_definition(name, concept)
                elif isinstance(concept, FuzzyNominalConcept):
                    self.defined_concepts[name] = concept
                    self.write_fuzzy_nominal_concept_definition(name, concept)
                elif isinstance(concept, WeightedConcept):
                    self.defined_concepts[name] = concept
                    self.write_weighted_concept_definition(name, concept)
                elif isinstance(concept, WeightedMaxConcept):
                    self.defined_concepts[name] = concept
                    self.write_weighted_max_concept_definition(name, concept)
                elif isinstance(concept, WeightedMinConcept):
                    self.defined_concepts[name] = concept
                    self.write_weighted_min_concept_definition(name, concept)
                elif isinstance(concept, WeightedSumConcept):
                    self.defined_concepts[name] = concept
                    self.write_weighted_sum_concept_definition(name, concept)
                elif isinstance(concept, WeightedSumZeroConcept):
                    self.defined_concepts[name] = concept
                    self.write_weighted_sum_zero_concept_definition(name, concept)
                elif isinstance(concept, OwaConcept):
                    self.defined_concepts[name] = concept
                    self.write_owa_concept_definition(name, concept)
                elif isinstance(concept, QowaConcept):
                    self.defined_concepts[name] = concept
                    self.write_qowa_concept_definition(name, concept)
                elif isinstance(concept, ChoquetConcept):
                    self.defined_concepts[name] = concept
                    self.write_choquet_concept_definition(name, concept)
                elif isinstance(concept, SugenoConcept):
                    self.defined_concepts[name] = concept
                    self.write_sugeno_concept_definition(name, concept)
                elif isinstance(concept, QsugenoConcept):
                    self.defined_concepts[name] = concept
                    self.write_quasi_sugeno_concept_definition(name, concept)
                else:
                    raise ValueError

    def process_property_annotations(self) -> None:
        """
        Iterates through the axioms of all loaded ontologies to identify and process annotations attached to object and data property declarations. For each property, it extracts the annotation value, parses it into a `ModifiedProperty` object, and validates that the associated fuzzy modifier exists within the current context. The method skips properties without annotations and logs an error if multiple annotations are found, though it continues processing using the first one. If the annotation string fails to parse, the method returns immediately; if the parsed object is not a `ModifiedProperty`, a `ValueError` is raised. Upon successful validation, the property is stored in the `defined_properties` dictionary and its definition is written out.

        :raises ValueError: Raised when the parsed annotation for a property does not result in a valid modified property instance.
        """

        for ontology in self.ontologies:
            for axiom in ontology.get_axioms(
                AxiomsType.OBJECT_PROPERTIES
            ) + ontology.get_axioms(AxiomsType.DATA_PROPERTIES):
                assert isinstance(axiom, OWLDeclaration)
                entity: OWLEntity = axiom.entity
                if not isinstance(entity, (OWLDataProperty, OWLObjectProperty)):
                    continue
                property: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    typing.cast(OWLObjectProperty, entity)
                    if isinstance(entity, OWLObjectProperty)
                    else typing.cast(OWLDataProperty, entity)
                )
                annotations: set[OWLAnnotation] = axiom.axiom_annotations
                if annotations is None or len(annotations) == 0:
                    continue
                if len(annotations) > 1:
                    Util.error(
                        f"Error: There are {len(annotations)} property annotations for {property}"
                    )
                annotation: OWLAnnotation = list(annotations)[0].annotation_value
                annotation_str: str = str(annotation)
                Util.debug(f"Annotation for property {property} -> {annotation_str}")
                prop: typing.Optional[ModifiedProperty] = (
                    FuzzyOwl2XMLParser.parse_string(annotation_str)
                )
                Util.debug(f"Parsed annotation -> {prop}")
                if prop is None:
                    return
                if not isinstance(prop, ModifiedProperty):
                    raise ValueError
                name: str = self.get_short_name(property)
                mod_name: str = prop.get_fuzzy_modifier()
                if mod_name not in self.fuzzy_modifiers:
                    Util.error(f"Error: Fuzzy modifier {mod_name} not defined.")
                self.defined_properties[name] = prop
                self.write_modified_property_definition(name, prop)

    def __get_degree(self, axiom: OWLAxiom) -> float:
        """
        Extracts the fuzzy membership degree associated with a specific OWL axiom by inspecting its annotations. If the axiom lacks annotations or the annotation set is empty, the method returns a default value of 1.0. When annotations are present, it attempts to parse the value of the first annotation into a float; if multiple annotations are detected, an error is logged, though the process continues using the first entry. The method validates that the parsed value is numeric, raising a ValueError if the parsing fails or the result is not a number.

        :param axiom: The OWL axiom to be inspected for annotations specifying its degree.
        :type axiom: OWLAxiom

        :raises ValueError: Raised if the parsed annotation value is not a number.

        :return: The degree of the axiom, parsed from its annotation, or 1.0 if no annotations are present.

        :rtype: float
        """

        if not axiom.axiom_annotations:
            return 1.0
        annotations: set[OWLAnnotation] = set(axiom.axiom_annotations)
        if annotations is None or len(annotations) == 0:
            return 1.0
        if len(annotations) > 1:
            Util.error(
                f"Error: There are {len(annotations)} annotations for axiom {axiom}."
            )
        annotation: OWLAnnotation = list(annotations)[0].annotation_value
        annotation_str: str = str(annotation)
        Util.debug(f"Annotation for degree -> {annotation_str}")
        deg: float = FuzzyOwl2XMLParser.parse_string(annotation_str)
        Util.debug(f"Parsed annotation -> {deg}")
        if not isinstance(deg, constants.NUMBER):
            raise ValueError
        return deg

    def __write_subclass_of_axiom(
        self, ontology: OWLOntology, annotated: bool = True
    ) -> None:
        """
        Processes subclass axioms from the provided ontology, separating them based on their associated fuzzy degree and the `annotated` flag. When `annotated` is True, the method writes axioms with degrees different from 1.0 to the output and records them as processed. Conversely, when `annotated` is False, it writes axioms with a degree of 1.0 only if they have not been previously processed, ensuring no duplication. This method relies on `__get_degree` to determine the fuzzy value and updates the internal `processed_axioms` set to track state.

        :param ontology: The source ontology containing the subclass axioms to be processed.
        :type ontology: OWLOntology
        :param annotated: Determines whether to process axioms annotated with fuzzy degrees. When True, only axioms with degrees different from 1.0 are processed; when False, only non-annotated axioms or those with a degree of 1.0 are processed.
        :type annotated: bool
        """

        for axiom in ontology.get_axioms(AxiomsType.SUBCLASSES):
            assert isinstance(axiom, OWLSubClassOf)
            subclass: OWLClassExpression = axiom.sub_class_expression
            superclass: OWLClassExpression = axiom.super_class_expression
            degree: float = self.__get_degree(axiom)
            if annotated:
                if degree == 1.0:
                    continue
                Util.debug(f"Subjclass of axiom -> {axiom}")
                self.write_subclass_of_axiom(subclass, superclass, degree)
                self.processed_axioms.add(f"{subclass} => {superclass}")
            else:
                if (
                    degree == 1.0
                    and f"{subclass} => {superclass}" not in self.processed_axioms
                ):
                    Util.debug(f"Not annotated subclass of axiom -> {axiom}")
                    self.processed_axioms.add(f"{subclass} => {superclass}")
                    self.write_subclass_of_axiom(subclass, superclass, degree)

    def __write_subobject_property_axiom(
        self, ontology: OWLOntology, annotated: bool = True
    ) -> None:
        """
        Iterates over the sub-object property axioms within the specified ontology to serialize them to the output file, distinguishing between standard axioms and those carrying fuzzy degrees. The method explicitly excludes axioms involving property chains from processing. Depending on the 'annotated' parameter, it either writes axioms with a fuzzy degree other than 1.0 or writes non-fuzzy axioms (degree 1.0) that have not been previously recorded. As a side effect, it updates the internal set of processed axioms to ensure that each relationship is written only once.

        :param ontology: The source ontology containing the sub-object property axioms to be processed.
        :type ontology: OWLOntology
        :param annotated: Flag indicating whether to process axioms with fuzzy degrees (non-1.0) or standard axioms (degree 1.0).
        :type annotated: bool
        """

        for axiom in ontology.get_axioms(AxiomsType.SUB_OBJECT_PROPERTIES):
            assert isinstance(axiom, OWLSubObjectPropertyOf)
            if isinstance(axiom.sub_object_property_expression, OWLObjectPropertyChain):
                continue
            sub_property: OWLObjectPropertyExpression = (
                axiom.sub_object_property_expression
            )
            super_property: OWLObjectPropertyExpression = (
                axiom.super_object_property_expression
            )
            degree: float = self.__get_degree(axiom)
            if annotated:
                if degree != 1.0:
                    Util.debug(f"Sub-object property axiom -> {axiom}")
                    self.write_sub_object_property_of_axiom(
                        sub_property, super_property, degree
                    )
                    self.processed_axioms.add(f"{sub_property} => {super_property}")
            else:
                if (
                    degree == 1.0
                    and f"{sub_property} => {super_property}"
                    not in self.processed_axioms
                ):
                    Util.debug(f"Not annotated sub-object property axiom -> {axiom}")
                    self.processed_axioms.add(f"{sub_property} => {super_property}")
                    self.write_sub_object_property_of_axiom(
                        sub_property, super_property, degree
                    )

    def __write_subdata_property_axiom(
        self, ontology: OWLOntology, annotated: bool = True
    ) -> None:
        """
        Processes sub-data property axioms from the given ontology, filtering them based on the provided `annotated` flag to separate fuzzy degrees from standard relationships. If the flag is True, the method writes axioms that have a fuzzy degree different from 1.0. If the flag is False, it writes axioms with a degree of 1.0, provided they have not already been processed and recorded in the internal tracking set. This method ensures that each relevant axiom is serialized to the output file exactly once by updating the set of processed axioms upon writing.

        :param ontology: The source ontology containing the sub-data property axioms to be processed.
        :type ontology: OWLOntology
        :param annotated: Determines whether to process axioms annotated with fuzzy degrees. If True, processes axioms with degrees different from 1.0; if False, processes non-annotated axioms or those with a degree of 1.0 that have not been processed previously.
        :type annotated: bool
        """

        for axiom in ontology.get_axioms(AxiomsType.SUB_DATA_PROPERTIES):
            assert isinstance(axiom, OWLSubDataPropertyOf)
            sub_property: OWLDataPropertyExpression = axiom.sub_data_property_expression
            super_property: OWLDataPropertyExpression = (
                axiom.super_data_property_expression
            )
            degree: float = self.__get_degree(axiom)
            if annotated:
                if degree != 1.0:
                    Util.debug(f"Sub-data property axiom -> {axiom}")
                    self.write_sub_data_property_of_axiom(
                        sub_property, super_property, degree
                    )
                    self.processed_axioms.add(f"{sub_property} => {super_property}")
            else:
                if (
                    degree == 1.0
                    and f"{sub_property} => {super_property}"
                    not in self.processed_axioms
                ):
                    Util.debug(f"Not annotated sub-data property axiom -> {axiom}")
                    self.processed_axioms.add(f"{sub_property} => {super_property}")
                    self.write_sub_data_property_of_axiom(
                        sub_property, super_property, degree
                    )

    def __write_subproperty_chain_of_axiom(
        self, ontology: OWLOntology, annotated: bool = True
    ) -> None:
        """
        Iterates through the axioms of the provided ontology to identify and write sub-property chain axioms, specifically handling those involving object property chains. The behavior is controlled by the `annotated` flag: when set to True, the method processes and writes axioms with fuzzy degrees different from 1.0; when set to False, it processes axioms with a degree of exactly 1.0, provided they have not already been processed. In both cases, the method updates an internal set of processed axioms to prevent duplicate writes and delegates the actual writing logic to a separate helper method.

        :param ontology: The source ontology containing the sub-property chain axioms to be processed.
        :type ontology: OWLOntology
        :param annotated: Flag indicating whether to process axioms annotated with fuzzy degrees. If True, only axioms with degrees different from 1.0 are processed. If False, only non-annotated axioms or those with a degree of 1.0 that have not been processed previously are handled.
        :type annotated: bool
        """

        for axiom in ontology.get_axioms(AxiomsType.SUB_OBJECT_PROPERTIES):
            assert isinstance(axiom, OWLSubObjectPropertyOf)
            if not isinstance(
                axiom.sub_object_property_expression, OWLObjectPropertyChain
            ):
                continue
            chain: list[OWLObjectPropertyExpression] = (
                axiom.sub_object_property_expression.chain
            )
            super_property: OWLObjectPropertyExpression = (
                axiom.super_object_property_expression
            )
            degree: float = self.__get_degree(axiom)
            if annotated:
                if degree != 1.0:
                    Util.debug(f"Sub property chain of axiom -> {axiom}")
                    self.write_sub_property_chain_of_axiom(
                        chain, super_property, degree
                    )
                    self.processed_axioms.add(f"{chain} => {super_property}")
            else:
                if (
                    degree == 1.0
                    and f"{chain} => {super_property}" not in self.processed_axioms
                ):
                    Util.debug(f"Not annotated sub property chain of axiom -> {axiom}")
                    self.processed_axioms.add(f"{chain} => {super_property}")
                    self.write_sub_property_chain_of_axiom(
                        chain, super_property, degree
                    )

    def __write_class_assertion_axiom(
        self, ontology: OWLOntology, annotated: bool = True
    ) -> None:
        """
        Processes class assertion axioms from the provided ontology, writing them to the output based on their fuzzy degree and the `annotated` flag. If `annotated` is True, the method specifically targets axioms with a degree different from 1.0, treating them as fuzzy assertions. If `annotated` is False, it processes axioms with a degree of 1.0, but only if they have not already been handled, as tracked by the `processed_axioms` set. This approach ensures that fuzzy and crisp assertions are handled separately without duplication, while modifying the internal state of the object to record processed items.

        :param ontology: The source ontology from which class assertion axioms are retrieved.
        :type ontology: OWLOntology
        :param annotated: Flag indicating whether to process fuzzy class assertions. If True, only axioms with degrees different from 1.0 are processed. If False, only crisp axioms (degree 1.0) that have not been processed previously are handled.
        :type annotated: bool
        """

        for axiom in ontology.get_axioms(AxiomsType.CLASS_ASSERTIONS):
            assert isinstance(axiom, OWLClassAssertion)
            cls: OWLClassExpression = axiom.class_expression
            ind: OWLIndividual = axiom.individual
            degree: float = self.__get_degree(axiom)
            if annotated:
                if degree != 1.0:
                    Util.debug(f"Class assertion axiom -> {axiom}")
                    self.write_concept_assertion_axiom(ind, cls, degree)
                    self.processed_axioms.add(f"{ind}:{cls}")
            else:
                if degree == 1.0 and f"{ind}:{cls}" not in self.processed_axioms:
                    Util.debug(f"Not annotated class assertion axiom -> {axiom}")
                    self.processed_axioms.add(f"{ind}:{cls}")
                    self.write_concept_assertion_axiom(ind, cls, degree)

    def __write_object_property_assertion_axiom(
        self, ontology: OWLOntology, annotated: bool = True
    ) -> None:
        """
        Iterates through object property assertion axioms in the given ontology and writes them to the output file based on the specified annotation mode. If the `annotated` flag is set to True, the method processes only those axioms with a fuzzy degree different from 1.0; otherwise, it processes axioms with a degree of 1.0, provided they have not already been handled. To prevent duplication, the method maintains a record of processed assertions in the `processed_axioms` set and triggers debug logging for each axiom written.

        :param ontology: The source ontology from which to retrieve the object property assertion axioms.
        :type ontology: OWLOntology
        :param annotated: Flag indicating whether to process fuzzy axioms with degrees different from 1.0 (True) or standard axioms with a degree of 1.0 (False).
        :type annotated: bool
        """

        for axiom in ontology.get_axioms(AxiomsType.OBJECT_PROPERTY_ASSERTIONS):
            assert isinstance(axiom, OWLObjectPropertyAssertion)
            ind1: OWLIndividual = axiom.source_individual
            ind2: OWLIndividual = axiom.target_individual
            prop: OWLObjectPropertyExpression = axiom.object_property_expression
            degree: float = self.__get_degree(axiom)
            if annotated:
                if degree != 1.0:
                    Util.debug(f"Object property assertion axiom -> {axiom}")
                    self.write_object_property_assertion_axiom(ind1, ind2, prop, degree)
                    self.processed_axioms.add(f"({ind1}, {ind2}):{prop}")
            else:
                if (
                    degree == 1.0
                    and f"({ind1}, {ind2}):{prop}" not in self.processed_axioms
                ):
                    Util.debug(
                        f"Not annotated object property assertion axiom -> {axiom}"
                    )
                    self.processed_axioms.add(f"({ind1}, {ind2}):{prop}")
                    self.write_object_property_assertion_axiom(ind1, ind2, prop, degree)

    def __write_data_property_assertion_axiom(
        self, ontology: OWLOntology, annotated: bool = True
    ) -> None:
        """
        Iterates over all data property assertion axioms within the provided ontology to serialize them to the output, distinguishing between fuzzy and crisp assertions based on the `annotated` flag. When `annotated` is True, the method processes axioms with a fuzzy degree different from 1.0, writing them to the output and recording them in the internal set of processed axioms. When `annotated` is False, the method handles axioms with a degree of exactly 1.0, but only if they have not already been recorded in the processed set, thereby preventing duplicate writes. This method updates the internal state of processed axioms and delegates the actual writing logic to a lower-level writer function.

        :param ontology: The source ontology containing the data property assertion axioms to be written.
        :type ontology: OWLOntology
        :param annotated: Flag indicating whether to process fuzzy axioms. If True, processes axioms with degrees different from 1.0. If False, processes axioms with a degree of 1.0 that have not already been processed.
        :type annotated: bool
        """

        for axiom in ontology.get_axioms(AxiomsType.DATA_PROPERTY_ASSERTIONS):
            assert isinstance(axiom, OWLDataPropertyAssertion)
            ind: OWLIndividual = axiom.source_individual
            value: OWLLiteral = axiom.target_value
            prop: OWLDataPropertyExpression = axiom.data_property_expression
            degree: float = self.__get_degree(axiom)
            if annotated:
                if degree != 1.0:
                    Util.debug(f"Data property assertion axiom -> {axiom}")
                    self.write_data_property_assertion_axiom(ind, value, prop, degree)
                    self.processed_axioms.add(f"({ind}, {value}):{prop}")
            else:
                if (
                    degree == 1.0
                    and f"({ind}, {value}):{prop}" not in self.processed_axioms
                ):
                    Util.debug(
                        f"Not annotated data property assertion axiom -> {axiom}"
                    )
                    self.processed_axioms.add(f"({ind}, {value}):{prop}")
                    self.write_data_property_assertion_axiom(ind, value, prop, degree)

    def __write_negative_object_property_assertion_axiom(
        self, ontology: OWLOntology, annotated: bool = True
    ) -> None:
        """
        Iterates through negative object property assertion axioms within the provided ontology to serialize them to the output file, distinguishing between fuzzy and crisp assertions based on the `annotated` flag. When the flag is True, the method processes only axioms with a fuzzy degree different from 1.0; when False, it processes axioms with a degree of exactly 1.0, provided they have not already been handled in a previous pass. As a side effect, the method updates an internal set of processed axioms to prevent duplication and triggers debug logging for the items being written.

        :param ontology: The source ontology containing the negative object property assertion axioms to be processed.
        :type ontology: OWLOntology
        :param annotated: If True, processes fuzzy axioms with degrees different from 1.0. If False, processes non-annotated axioms or those with a degree of 1.0 that have not been processed previously.
        :type annotated: bool
        """

        for axiom in ontology.get_axioms(
            AxiomsType.NEGATIVE_OBJECT_PROPERTY_ASSERTIONS
        ):
            assert isinstance(axiom, OWLNegativeObjectPropertyAssertion)
            ind1: OWLIndividual = axiom.source_individual
            ind2: OWLIndividual = axiom.target_individual
            prop: OWLObjectPropertyExpression = axiom.object_property_expression
            degree: float = self.__get_degree(axiom)
            if annotated:
                if degree != 1.0:
                    Util.debug(f"Negative object property assertion axiom -> {axiom}")
                    self.write_negative_object_property_assertion_axiom(
                        ind1, ind2, prop, degree
                    )
                    self.processed_axioms.add(f"({ind1}, {ind2}):not {prop}")
            else:
                if (
                    degree == 1.0
                    and f"({ind1}, {ind2}):not {prop}" not in self.processed_axioms
                ):
                    Util.debug(
                        f"Not annotated negative object property assertion axiom -> {axiom}"
                    )
                    self.processed_axioms.add(f"({ind1}, {ind2}):not {prop}")
                    self.write_negative_object_property_assertion_axiom(
                        ind1, ind2, prop, degree
                    )

    def __write_negative_data_property_assertion_axiom(
        self, ontology: OWLOntology, annotated: bool = True
    ) -> None:
        """
        Iterates over negative data property assertion axioms within the provided ontology and serializes them to the output file based on their fuzzy degree and the `annotated` flag. When `annotated` is True, the method processes only axioms with a fuzzy degree different from 1.0, representing non-crisp fuzzy constraints. Conversely, when `annotated` is False, it handles axioms with a degree of 1.0 (crisp assertions) but only if they have not already been processed, ensuring no duplication occurs. The method maintains an internal set of processed axioms to track this state and delegates the actual writing logic to a separate helper method.

        :param ontology: The source ontology containing the negative data property assertion axioms to be written.
        :type ontology: OWLOntology
        :param annotated: Determines whether to process annotated axioms with fuzzy degrees different from 1.0, or standard axioms with a degree of 1.0 that have not yet been processed.
        :type annotated: bool
        """

        for axiom in ontology.get_axioms(AxiomsType.NEGATIVE_DATA_PROPERTY_ASSERTIONS):
            assert isinstance(axiom, OWLNegativeDataPropertyAssertion)
            ind: OWLIndividual = axiom.source_individual
            value: OWLLiteral = axiom.target_value
            prop: OWLDataPropertyExpression = axiom.data_property_expression
            degree: float = self.__get_degree(axiom)
            if annotated:
                if degree != 1.0:
                    Util.debug(f"Negative data property assertion axiom -> {axiom}")
                    self.write_negative_data_property_assertion_axiom(
                        ind, value, prop, degree
                    )
                    self.processed_axioms.add(f"({ind}, {value}):not {prop}")
            else:
                if (
                    degree == 1.0
                    and f"({ind}, {value}):not {prop}" not in self.processed_axioms
                ):
                    Util.debug(
                        f"Not annotated negative data property assertion axiom -> {axiom}"
                    )
                    self.processed_axioms.add(f"({ind}, {value}):not {prop}")
                    self.write_negative_data_property_assertion_axiom(
                        ind, value, prop, degree
                    )

    def process_ontology_axioms(self) -> None:
        """Iterates through the loaded ontologies to systematically process and write axioms to the output file, covering the TBox, RBox, and ABox components of the knowledge base. It handles a wide variety of axiom types, including class declarations, property characteristics, and individual assertions, distinguishing between annotated and non-annotated versions of specific relationships. To ensure no redundancy, the method checks an internal set of processed axioms before writing; if an axiom has already been serialized, it is skipped. This process effectively flattens the ontology structure into a serialized format while preserving the logical distinctions defined in the source ontologies."""

        for ontology in self.ontologies:
            # ########
            #  TBox
            # ########
            for axiom in ontology.get_axioms(AxiomsType.DISJOINT_CLASSES):
                assert isinstance(axiom, OWLDisjointClasses)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Disjoint axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_disjoint_classes_axiom(axiom.class_expressions)
            for axiom in ontology.get_axioms(AxiomsType.DISJOINT_UNIONS):
                assert isinstance(axiom, OWLDisjointUnion)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Disjoint union axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_disjoint_union_axiom(
                        [axiom.union_class] + axiom.disjoint_class_expressions
                    )
            self.__write_subclass_of_axiom(ontology, annotated=True)
            for axiom in ontology.get_axioms(AxiomsType.EQUIVALENT_CLASSES):
                assert isinstance(axiom, OWLEquivalentClasses)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Equivalent classes axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_equivalent_classes_axiom(axiom.class_expressions)
            for axiom in ontology.get_axioms(AxiomsType.CLASSES):
                assert isinstance(axiom, OWLDeclaration)
                cls: OWLEntity = axiom.entity
                assert isinstance(cls, OWLClass)
                if cls != OWLClass.thing() and str(cls) not in self.processed_axioms:
                    Util.debug(f"Concept declaration axiom -> {cls}")
                    self.processed_axioms.add(str(cls))
                    self.write_concept_declaration(cls)
            # ########
            #  RBox
            # ########
            self.__write_subobject_property_axiom(ontology, annotated=True)
            self.__write_subdata_property_axiom(ontology, annotated=True)
            self.__write_subproperty_chain_of_axiom(ontology, annotated=True)
            for axiom in ontology.get_axioms(AxiomsType.EQUIVALENT_OBJECT_PROPERTIES):
                assert isinstance(axiom, OWLEquivalentObjectProperties)
                Util.debug(f"Equivalent object properties axiom -> {axiom}")
                if str(axiom) not in self.processed_axioms:
                    self.processed_axioms.add(str(axiom))
                    self.write_equivalent_object_properties_axiom(
                        axiom.object_property_expressions
                    )
            for axiom in ontology.get_axioms(AxiomsType.EQUIVALENT_DATA_PROPERTIES):
                assert isinstance(axiom, OWLEquivalentDataProperties)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Equivalent data properties axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_equivalent_data_properties_axiom(
                        axiom.data_property_expressions
                    )
            for axiom in ontology.get_axioms(AxiomsType.TRANSITIVE_OBJECT_PROPERTIES):
                assert isinstance(axiom, OWLTransitiveObjectProperty)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Transitive object property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_transitive_object_property_axiom(
                        axiom.object_property_expression
                    )
            for axiom in ontology.get_axioms(AxiomsType.SYMMETRIC_OBJECT_PROPERTIES):
                assert isinstance(axiom, OWLSymmetricObjectProperty)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Symmetric object property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_symmetric_object_property_axiom(
                        axiom.object_property_expression
                    )
            for axiom in ontology.get_axioms(AxiomsType.ASYMMETRIC_OBJECT_PROPERTIES):
                assert isinstance(axiom, OWLAsymmetricObjectProperty)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Asymmetric object property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_asymmetric_object_property_axiom(
                        axiom.object_property_expression
                    )
            for axiom in ontology.get_axioms(AxiomsType.REFLEXIVE_OBJECT_PROPERTIES):
                assert isinstance(axiom, OWLReflexiveObjectProperty)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Reflexive object property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_reflexive_object_property_axiom(
                        axiom.object_property_expression
                    )
            for axiom in ontology.get_axioms(AxiomsType.IRREFLEXIVE_OBJECT_PROPERTIES):
                assert isinstance(axiom, OWLIrreflexiveObjectProperty)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Irreflexive object property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_irreflexive_object_property_axiom(
                        axiom.object_property_expression
                    )
            for axiom in ontology.get_axioms(AxiomsType.FUNCTIONAL_OBJECT_PROPERTIES):
                assert isinstance(axiom, OWLFunctionalObjectProperty)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Functional object property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_functional_object_property_axiom(
                        axiom.object_property_expression
                    )
            for axiom in ontology.get_axioms(AxiomsType.FUNCIONAL_DATA_PROPERTIES):
                assert isinstance(axiom, OWLFunctionalDataProperty)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Functional data property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_functional_data_property_axiom(
                        axiom.data_property_expression
                    )
            for axiom in ontology.get_axioms(AxiomsType.INVERSE_OBJECT_PROPERTIES):
                assert isinstance(axiom, OWLInverseObjectProperties)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Inverse object properties axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_inverse_object_property_axiom(
                        axiom.object_property_expression,
                        axiom.inverse_object_property_expression,
                    )
            for axiom in ontology.get_axioms(
                AxiomsType.INVERSE_FUNCTIONAL_OBJECT_PROPERTIES
            ):
                assert isinstance(axiom, OWLInverseFunctionalObjectProperty)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Inverse functional object property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_inverse_functional_object_property_axiom(
                        axiom.object_property_expression
                    )
            for axiom in ontology.get_axioms(AxiomsType.OBJECT_PROPERTY_DOMAIN):
                assert isinstance(axiom, OWLObjectPropertyDomain)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Object property domain axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_object_property_domain_axiom(
                        axiom.object_property_expression, axiom.class_expression
                    )
            for axiom in ontology.get_axioms(AxiomsType.OBJECT_PROPERTY_RANGE):
                assert isinstance(axiom, OWLObjectPropertyRange)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Object property range axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_object_property_range_axiom(
                        axiom.object_property_expression, axiom.class_expression
                    )
            for axiom in ontology.get_axioms(AxiomsType.DATA_PROPERTY_DOMAIN):
                assert isinstance(axiom, OWLDataPropertyDomain)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Data property domain axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_data_property_domain_axiom(
                        axiom.data_property_expression, axiom.class_expression
                    )
            for axiom in ontology.get_axioms(AxiomsType.DATA_PROPERTY_RANGE):
                assert isinstance(axiom, OWLDataPropertyRange)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Data property range axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_data_property_range_axiom(
                        axiom.data_property_expression, axiom.data_range
                    )
            for axiom in ontology.get_axioms(AxiomsType.DISJOINT_OBJECT_PROPERTIES):
                assert isinstance(axiom, OWLDisjointObjectProperties)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Disjoint object properties axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_disjoint_object_properties_axiom(
                        axiom.object_property_expressions
                    )
            for axiom in ontology.get_axioms(AxiomsType.DISJOINT_DATA_PROPERTIES):
                assert isinstance(axiom, OWLDisjointDataProperties)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Disjoint data properties axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_disjoint_data_properties_axiom(
                        axiom.data_property_expressions
                    )
            # ########
            #  ABox
            # ########
            self.__write_class_assertion_axiom(ontology, annotated=True)
            self.__write_object_property_assertion_axiom(ontology, annotated=True)
            self.__write_data_property_assertion_axiom(ontology, annotated=True)
            self.__write_negative_object_property_assertion_axiom(
                ontology, annotated=True
            )
            self.__write_negative_data_property_assertion_axiom(
                ontology, annotated=True
            )
            for axiom in ontology.get_axioms(AxiomsType.SAME_INDIVIDUALS):
                assert isinstance(axiom, OWLSameIndividual)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Same individual axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_same_individual_axiom(axiom.individuals)
            for axiom in ontology.get_axioms(AxiomsType.DIFFERENT_INDIVIDUALS):
                assert isinstance(axiom, OWLDifferentIndividuals)
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Different individuals axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_different_individuals_axiom(axiom.individuals)
            # ########
            # Not annotated sublcass axioms
            # ########
            self.__write_subclass_of_axiom(ontology, annotated=False)
            self.__write_subobject_property_axiom(ontology, annotated=False)
            self.__write_subdata_property_axiom(ontology, annotated=False)
            self.__write_subproperty_chain_of_axiom(ontology, annotated=False)
            self.__write_class_assertion_axiom(ontology, annotated=False)
            self.__write_object_property_assertion_axiom(ontology, annotated=False)
            self.__write_data_property_assertion_axiom(ontology, annotated=False)
            self.__write_negative_object_property_assertion_axiom(
                ontology, annotated=False
            )
            self.__write_negative_data_property_assertion_axiom(
                ontology, annotated=False
            )

    def get_class_name(self, c: OWLClassExpression) -> str:
        """
        Generates a human-readable name for a given OWL class expression by dispatching to specific helper methods based on the expression's type. This method handles atomic classes, including special cases for the top and bottom concepts, as well as complex expressions such as intersections, unions, complements, and various property restrictions (existential, universal, value, and cardinality). It supports both object and data property expressions, distinguishing between qualified and unqualified cardinality restrictions. If the provided expression is of an unsupported type, a ValueError is raised, and the method logs the input expression for debugging purposes.

        :param c: The OWL class expression to be converted into a human-readable name.
        :type c: OWLClassExpression

        :raises ValueError: Raised if the provided class expression is of an unsupported type that cannot be formatted into a human-readable name.

        :return: A human-readable string representation of the OWL class expression, formatted according to its specific type and structure.

        :rtype: str
        """

        Util.debug(f"Getting class name for expression: {c}")
        if isinstance(c, OWLClass):
            d: OWLClass = typing.cast(OWLClass, c)
            if d.is_thing():
                return self.get_top_concept_name()
            if d.is_nothing():
                return self.get_bottom_concept_name()
            return self.get_atomic_concept_name(d)
        elif isinstance(c, OWLObjectIntersectionOf):
            operands: OWLObjectIntersectionOf = typing.cast(
                OWLObjectIntersectionOf, c
            ).classes_expressions
            return self.get_object_intersection_of_name(operands)
        elif isinstance(c, OWLObjectUnionOf):
            operands: OWLObjectUnionOf = typing.cast(
                OWLObjectUnionOf, c
            ).classes_expressions
            return self.get_object_union_of_name(operands)
        elif isinstance(c, OWLObjectSomeValuesFrom):
            obj_some: OWLObjectSomeValuesFrom = typing.cast(OWLObjectSomeValuesFrom, c)
            return self.get_object_some_values_from_name(
                obj_some.object_property_expression, obj_some.class_expression
            )
        elif isinstance(c, OWLObjectAllValuesFrom):
            obj_all: OWLObjectAllValuesFrom = typing.cast(OWLObjectAllValuesFrom, c)
            return self.get_object_all_values_from_name(
                obj_all.object_property_expression, obj_all.class_expression
            )
        elif isinstance(c, OWLDataSomeValuesFrom):
            data_some: OWLDataSomeValuesFrom = typing.cast(OWLDataSomeValuesFrom, c)
            return self.get_data_some_values_from_name(
                data_some.data_property_expressions[0], data_some.data_range
            )
        elif isinstance(c, OWLDataAllValuesFrom):
            data_all: OWLDataAllValuesFrom = typing.cast(OWLDataAllValuesFrom, c)
            return self.get_data_all_values_from_name(
                data_all.data_property_expressions[0], data_all.data_range
            )
        elif isinstance(c, OWLObjectComplementOf):
            complement: OWLObjectComplementOf = typing.cast(OWLObjectComplementOf, c)
            return self.get_object_complement_of_name(complement.expression)
        elif isinstance(c, OWLObjectHasSelf):
            has_self: OWLObjectHasSelf = typing.cast(OWLObjectHasSelf, c)
            return self.get_object_has_self_name(has_self.object_property_expression)
        elif isinstance(c, OWLObjectOneOf):
            one_of: OWLObjectOneOf = typing.cast(OWLObjectOneOf, c)
            return self.get_object_one_of_name(one_of.individuals)
        elif isinstance(c, OWLObjectHasValue):
            has_value: OWLObjectHasValue = typing.cast(OWLObjectHasValue, c)
            return self.get_object_has_value_name(
                has_value.object_property_expression, has_value.individual
            )
        elif isinstance(c, OWLDataHasValue):
            has_value: OWLDataHasValue = typing.cast(OWLDataHasValue, c)
            return self.get_data_has_value_name(
                has_value.data_property_expression, has_value.literal
            )
        elif isinstance(c, OWLObjectMinCardinality):
            min_card: OWLObjectMinCardinality = typing.cast(OWLObjectMinCardinality, c)
            if min_card.is_qualified:
                return self.get_object_min_cardinality_restriction(
                    min_card.cardinality,
                    min_card.object_property_expression,
                    min_card.class_expression,
                )
            else:
                return self.get_object_min_cardinality_restriction(
                    min_card.cardinality, min_card.object_property_expression
                )
        elif isinstance(c, OWLObjectMaxCardinality):
            max_card: OWLObjectMaxCardinality = typing.cast(OWLObjectMaxCardinality, c)
            if max_card.is_qualified:
                return self.get_object_max_cardinality_restriction(
                    max_card.cardinality,
                    max_card.object_property_expression,
                    max_card.class_expression,
                )
            else:
                return self.get_object_max_cardinality_restriction(
                    max_card.cardinality,
                    max_card.object_property_expression,
                )
        elif isinstance(c, OWLObjectExactCardinality):
            exact_card: OWLObjectExactCardinality = typing.cast(
                OWLObjectExactCardinality, c
            )
            if exact_card.is_qualified:
                return self.get_object_exact_cardinality_restriction(
                    exact_card.cardinality,
                    exact_card.object_property_expression,
                    exact_card.class_expression,
                )
            else:
                return self.get_object_exact_cardinality_restriction(
                    exact_card.cardinality,
                    exact_card.object_property_expression,
                )
        elif isinstance(c, OWLDataMinCardinality):
            min_card: OWLDataMinCardinality = typing.cast(OWLDataMinCardinality, c)
            if min_card.is_qualified:
                return self.get_data_min_cardinality_restriction(
                    min_card.cardinality,
                    min_card.data_property_expression,
                    min_card.data_range,
                )
            else:
                return self.get_data_min_cardinality_restriction(
                    min_card.cardinality,
                    min_card.data_property_expression,
                )
        elif isinstance(c, OWLDataMaxCardinality):
            max_card: OWLDataMaxCardinality = typing.cast(OWLDataMaxCardinality, c)
            if max_card.is_qualified:
                return self.get_data_max_cardinality_restriction(
                    max_card.cardinality,
                    max_card.data_property_expression,
                    max_card.data_range,
                )
            else:
                return self.get_data_max_cardinality_restriction(
                    max_card.cardinality, max_card.data_property_expression
                )
        elif isinstance(c, OWLDataExactCardinality):
            exact_card: OWLDataExactCardinality = typing.cast(
                OWLDataExactCardinality, c
            )
            if exact_card.is_qualified:
                return self.get_data_exact_cardinality_restriction(
                    exact_card.cardinality,
                    exact_card.data_property_expression,
                    exact_card.data_range,
                )
            else:
                return self.get_data_exact_cardinality_restriction(
                    exact_card.cardinality,
                    exact_card.data_property_expression,
                )
        else:
            raise ValueError

    def get_object_property_name(self, p: OWLObjectPropertyExpression) -> str:
        """
        Retrieves a human-readable string representation for a given OWL object property expression, handling various types of properties appropriately. The method checks if the expression is the universal (top) or empty (bottom) property and delegates to specific helper methods to retrieve their designated names; otherwise, it treats the expression as an atomic property and retrieves its specific identifier. As a side effect, the method logs the input expression to aid in debugging.

        :param p: The object property expression (atomic, top, or bottom) to retrieve the human-readable name for.
        :type p: OWLObjectPropertyExpression

        :return: The human-readable name of the object property expression.

        :rtype: str
        """

        Util.debug(f"Getting object property name for expression: {p}")
        if p.is_top_object_property():
            return self.get_top_object_property_name()
        elif p.is_bottom_object_property():
            return self.get_bottom_object_property_name()
        else:
            return self.get_atomic_object_property_name(p)

    def get_data_property_name(self, p: OWLDataPropertyExpression) -> str:
        """
        Retrieves a human-readable string representation for a given OWL data property expression by inspecting its specific type. The method distinguishes between the universal top data property, the empty bottom data property, and standard atomic properties, delegating to the appropriate internal naming function for each case. This ensures that special ontology-level constructs are rendered distinctly from standard named properties. Additionally, the method logs the input expression for debugging purposes before processing.

        :param p: The data property expression to be resolved into a human-readable name.
        :type p: OWLDataPropertyExpression

        :return: The human-readable name of the data property expression, handling top, bottom, and atomic property types.

        :rtype: str
        """

        Util.debug(f"Getting data property name for expression: {p}")
        if p.is_top_data_property():
            return self.get_top_data_property_name()
        elif p.is_bottom_data_property():
            return self.get_bottom_data_property_name()
        else:
            return self.get_atomic_data_property_name(p)

    def get_individual_name(self, i: OWLIndividual) -> typing.Optional[str]:
        """
        Retrieves a human-readable name for the specified OWL individual by first checking if the individual is anonymous. If the individual is an instance of OWLAnonymousIndividual, the method returns None and logs an informational message indicating that anonymous individuals are not supported. For named individuals, the method obtains the short name via the `get_short_name` method and returns it as a string, while also logging the result.

        :param i: The ontology entity for which the human-readable name is to be retrieved.
        :type i: OWLIndividual

        :return: Returns None if the individual is anonymous, otherwise returns an empty string.

        :rtype: typing.Optional[str]
        """

        Util.debug(f"Getting individual name for expression: {i}")
        if isinstance(i, OWLAnonymousIndividual):
            Util.info(f"Anonymous individual not supported")
            return None
        else:
            name: str = self.get_short_name(i)
            Util.info(f"Individual {name}")
            return ""

    def get_top_concept_name(self) -> str:
        """
        Retrieves the human-readable name of the top concept within the ontology hierarchy. This method is designed to provide the label or identifier of the root concept managed by the FuzzyOwl2 instance. It performs an informational logging operation as a side effect. If the top concept is not set or cannot be resolved, the method returns an empty string.

        :return: The human-readable name of the top concept.

        :rtype: str
        """

        Util.info(f"Print Top concept")
        return ""

    def get_bottom_concept_name(self) -> str:
        """
        Retrieves the human-readable name of the bottom concept, which represents the empty set or contradiction within the ontology. This method is intended to provide a simplified string representation suitable for user interfaces or logging, rather than the full internal identifier. The method triggers an informational log message during execution and currently returns an empty string as a placeholder.

        :return: The human-readable name of the bottom concept.

        :rtype: str
        """

        Util.info(f"Print Bottom concept")
        return ""

    def get_atomic_concept_name(self, c: OWLClass) -> str:
        """
        Retrieves the short name for the specified OWL class and logs it to the utility info stream. Although the human-readable name is calculated, the method currently returns an empty string. The primary side effect of calling this method is the generation of an informational log entry containing the concept's name.

        :param c: The OWL class representing the atomic concept for which to retrieve the name.
        :type c: OWLClass

        :return:

        :rtype: str
        """

        name: str = self.get_short_name(c)
        Util.info(f"Print Atomic concept {name}")
        return ""

    def get_object_intersection_of_name(self, operands: set[OWLClassExpression]) -> str:
        """
        This method is designed to generate a human-readable name for an object intersection defined by a set of OWL class expressions. It accepts the class expressions as operands and logs them for informational purposes. Currently, the method acts as a placeholder and returns an empty string instead of a formatted name.

        :param operands: The set of class expressions comprising the object intersection.
        :type operands: set[OWLClassExpression]

        :return: A human-readable string representing the object intersection of the provided class expressions.

        :rtype: str
        """

        Util.info(f"Print ObjectIntersectionOf {operands}")
        return ""

    def get_object_union_of_name(self, operands: set[OWLClassExpression]) -> str:
        """
        Generates a human-readable name for an object union of class expressions based on the provided set of operands. This method processes the input `OWLClassExpression` objects to construct a string representation of their union. The current implementation logs the operands and returns an empty string, serving as a placeholder for the actual naming logic.

        :param operands: The class expressions that constitute the components of the object union.
        :type operands: set[OWLClassExpression]

        :return: A human-readable string representing the name of the object union of the provided class expressions.

        :rtype: str
        """

        Util.info(f"Print ObjectUnionOf {operands}")
        return ""

    def get_object_some_values_from_name(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> str:
        """
        Generates a human-readable string representation for an OWL existential restriction, specifically the 'ObjectSomeValuesFrom' class expression, based on the provided object property and class filler. The method is designed to format the relationship between the property and the class into a coherent name. It also logs the input arguments for debugging purposes before returning the formatted string.

        :param p: The object property expression acting as the property in the ObjectSomeValuesFrom restriction.
        :type p: OWLObjectPropertyExpression
        :param c: The class expression that serves as the filler for the object some values from restriction.
        :type c: OWLClassExpression

        :return: A human-readable string representing the ObjectSomeValuesFrom restriction for the given property and class expression.

        :rtype: str
        """

        Util.info(f"Print ObjectSomeValuesFrom({p} {c})")
        return ""

    def get_object_all_values_from_name(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> str:
        """
        Generates a human-readable string representation for an OWL ObjectAllValuesFrom class expression, which represents a universal restriction on an object property. The method takes an object property expression and a class expression as inputs to define the scope of the restriction. As a side effect, it logs the details of the property and class being processed.

        :param p: The object property expression acting as the property in the ObjectAllValuesFrom restriction.
        :type p: OWLObjectPropertyExpression
        :param c: The class expression that serves as the filler for the ObjectAllValuesFrom restriction.
        :type c: OWLClassExpression

        :return: A human-readable string representation of the ObjectAllValuesFrom restriction defined by the provided property and class expression.

        :rtype: str
        """

        Util.info(f"Print ObjectAllValuesFrom({p} {c})")
        return ""

    def get_data_some_values_from_name(
        self, p: OWLDataPropertyExpression, range: OWLDataRange
    ) -> str:
        """
        Generates a human-readable name for a data property existential restriction, corresponding to an OWL 'DataSomeValuesFrom' class expression. The method utilizes a data property expression and a data range to construct this representation. As a side effect, it logs the details of the property and range to the system output.

        :param p: The data property expression that serves as the property for the data some values from restriction.
        :type p: OWLDataPropertyExpression
        :param range: The data range that serves as the filler for the data some values from restriction.
        :type range: OWLDataRange

        :return: The human-readable name of the data some values from class expression.

        :rtype: str
        """

        Util.info(f"Print DataSomeValuesFrom({p} {range})")
        return ""

    def get_data_all_values_from_name(
        self, p: OWLDataPropertyExpression, range: OWLDataRange
    ) -> str:
        """
        Constructs a human-readable string identifier for a universal data restriction defined by a specific property and range. This method processes an OWL data property expression and a data range to represent a DataAllValuesFrom constraint, where all values of the property are required to be within the given range. As a side effect, it logs the input components, though the current implementation returns an empty string placeholder.

        :param p: The data property expression acting as the property in the data all values from restriction.
        :type p: OWLDataPropertyExpression
        :param range: The data range that serves as the filler for the data all values from restriction.
        :type range: OWLDataRange

        :return: The human-readable name of the data all values from class expression defined by the given property and data range.

        :rtype: str
        """

        Util.info(f"Print DataAllValuesFrom({p} {range})")
        return ""

    def get_object_complement_of_name(self, c: OWLClassExpression) -> str:
        """
        Generates a human-readable name for the object complement of a given OWL class expression. This method accepts a class expression as the operand for the complement operation and returns a string representing that negation. As a side effect, it logs the details of the complement operation to the info stream before returning the result.

        :param c: The class expression serving as the operand for the object complement.
        :type c: OWLClassExpression

        :return: A human-readable string representing the name of the object complement of the provided class expression.

        :rtype: str
        """

        Util.info(f"Print ObjectComplement({c})")
        return ""

    def get_object_has_self_name(self, p: OWLObjectPropertyExpression) -> str:
        """
        Constructs a human-readable name for an OWL ObjectHasSelf class expression based on the supplied object property expression. This method is responsible for serializing the self-restriction concept into a string format, typically used for display or internal identification within the FuzzyOwl2 framework. It includes a side effect of logging the property expression, though the current implementation returns an empty string placeholder.

        :param p: The object property expression used to construct the ObjectHasSelf expression.
        :type p: OWLObjectPropertyExpression

        :return: The human-readable name of the ObjectHasSelf class expression for the given object property expression.

        :rtype: str
        """

        Util.info(f"Print ObjectHasSelf({p})")
        return ""

    def get_object_one_of_name(self, ind_set: set[OWLIndividual]) -> str:
        """
        Generates a human-readable string representation for an OWL ObjectOneOf class expression based on the provided set of individuals. This method is intended to format the enumeration of individuals into a coherent name, which is useful for displaying or serializing class expressions within the FuzzyOwl2 module. During execution, it logs the input set to the info stream for debugging or tracking purposes. Note that the current implementation returns an empty string, acting as a placeholder for the actual formatting logic.

        :param ind_set: The set of individuals that constitute the enumeration for the ObjectOneOf class expression.
        :type ind_set: set[OWLIndividual]

        :return: A human-readable string representing the name of the ObjectOneOf class expression for the provided set of individuals.

        :rtype: str
        """

        Util.info(f"Print ObjectOneOf({ind_set})")
        return ""

    def get_object_has_value_name(
        self, p: OWLObjectPropertyExpression, i: OWLIndividual
    ) -> str:
        """
        Generates a human-readable string representation for an OWL ObjectHasValue class expression, which describes the class of individuals that have a specific relationship to a particular individual. This method accepts an object property expression and an OWL individual to formulate the name. As a side effect, it logs the input parameters to the info stream during execution.

        :param p: The object property expression that serves as the property in the object has value restriction.
        :type p: OWLObjectPropertyExpression
        :param i: The individual that is the value of the object property expression.
        :type i: OWLIndividual

        :return: An empty string.

        :rtype: str
        """

        Util.info(f"Print ObjectHasValue({p} {i})")
        return ""

    def get_data_has_value_name(
        self, p: OWLDataPropertyExpression, literal: OWLLiteral
    ) -> str:
        """
        Generates a human-readable name for a DataHasValue class expression, which represents the restriction of a data property to a specific literal value. This method logs the provided property and literal arguments to the information stream and returns a string formatted to describe this restriction.

        :param p: The data property expression that serves as the property in the data has value restriction.
        :type p: OWLDataPropertyExpression
        :param literal: The specific literal value that the data property expression is restricted to.
        :type literal: OWLLiteral

        :return:

        :rtype: str
        """

        Util.info(f"Print DataHasValue({p} {literal})")
        return ""

    def get_object_min_cardinality_restriction(
        self,
        cardinality: int,
        p: OWLObjectPropertyExpression,
        c: OWLClassExpression = None,
    ) -> str:
        """
        This method logs a human-readable representation of an object minimum cardinality restriction based on the provided cardinality, object property expression, and optional class expression filler. It handles the absence of the filler class by logging only the cardinality and property, whereas including the filler results in a more detailed log entry. The function performs a side effect of printing this information via the logging utility and returns an empty string.

        :param cardinality: The minimum cardinality value for the restriction.
        :type cardinality: int
        :param p: The object property expression that defines the property for the restriction.
        :type p: OWLObjectPropertyExpression
        :param c: The class expression that serves as the filler of the restriction.
        :type c: OWLClassExpression

        :return: An empty string.

        :rtype: str
        """

        if c is not None:
            Util.info(f"Print ObjectMinCardinalityRestriction({cardinality} {p} {c})")
        else:
            Util.info(f"Print ObjectMinCardinalityRestriction({cardinality} {p})")
        return ""

    def get_object_max_cardinality_restriction(
        self,
        cardinality: int,
        p: OWLObjectPropertyExpression,
        c: OWLClassExpression = None,
    ) -> str:
        """
        This method constructs a human-readable representation of an OWL Object Max Cardinality Restriction using the provided cardinality, object property expression, and optional class expression filler. It logs this representation to the info stream using `Util.info`, formatting the output to include the filler class only if it is explicitly provided. Despite its name implying a retrieval operation, the method performs a logging side effect and returns an empty string.

        :param cardinality: The maximum number of distinct individuals that can be related by the object property.
        :type cardinality: int
        :param p: The object property expression on which the maximum cardinality restriction is applied.
        :type p: OWLObjectPropertyExpression
        :param c: The class expression serving as the filler for the restriction.
        :type c: OWLClassExpression

        :return: An empty string.

        :rtype: str
        """

        if c is not None:
            Util.info(f"Print ObjectMaxCardinalityRestriction({cardinality} {p} {c})")
        else:
            Util.info(f"Print ObjectMaxCardinalityRestriction({cardinality} {p})")
        return ""

    def get_object_exact_cardinality_restriction(
        self,
        cardinality: int,
        p: OWLObjectPropertyExpression,
        c: OWLClassExpression = None,
    ) -> str:
        """
        Generates a log entry representing an OWL object exact cardinality restriction based on the provided parameters. It accepts an integer cardinality, an object property expression, and an optional class expression filler. If the filler is provided, the log message includes all three components; otherwise, it includes only the cardinality and the property. While the method triggers this informational side effect, it returns an empty string.

        :param cardinality: The exact number of property relationships required by the restriction.
        :type cardinality: int
        :param p: The object property expression used as the property in the restriction.
        :type p: OWLObjectPropertyExpression
        :param c: The class expression serving as the filler of the restriction.
        :type c: OWLClassExpression

        :return: An empty string.

        :rtype: str
        """

        if c is not None:
            Util.info(f"Print ObjectExactCardinalityRestriction({cardinality} {p} {c})")
        else:
            Util.info(f"Print ObjectExactCardinalityRestriction({cardinality} {p})")
        return ""

    def get_data_min_cardinality_restriction(
        self, cardinality: int, p: OWLDataPropertyExpression, range: OWLDataRange = None
    ) -> str:
        """
        Generates a human-readable representation of an OWL data minimum cardinality restriction defined by the specified cardinality, data property expression, and optional data range. Instead of returning the name, the method logs the formatted restriction details to the info stream, including the data range only if it is provided. The function returns an empty string as a placeholder.

        :param cardinality: The minimum number of values required for the data property.
        :type cardinality: int
        :param p: The data property expression defining the property of the restriction.
        :type p: OWLDataPropertyExpression
        :param range: The data range that serves as the filler of the restriction.
        :type range: OWLDataRange

        :return: An empty string. The function logs the restriction details to the info stream rather than returning a formatted name.

        :rtype: str
        """

        if range is not None:
            Util.info(f"Print DataMinCardinalityRestriction({cardinality} {p} {range})")
        else:
            Util.info(f"Print DataMinCardinalityRestriction({cardinality} {p})")
        return ""

    def get_data_max_cardinality_restriction(
        self, cardinality: int, p: OWLDataPropertyExpression, range: OWLDataRange = None
    ) -> str:
        """
        This method formats and logs a human-readable representation of a data maximum cardinality restriction using the specified cardinality, data property expression, and optional data range. It distinguishes between restrictions with a specific data range filler and those without, logging the appropriate format via the utility logger. While the method signature implies a return value, the implementation currently returns an empty string, indicating that its primary purpose is the side effect of logging the restriction details.

        :param cardinality: The maximum number of data values permitted for the data property.
        :type cardinality: int
        :param p: The data property expression to which the maximum cardinality restriction applies.
        :type p: OWLDataPropertyExpression
        :param range: The data range serving as the filler for the restriction, specifying the allowed values for the property.
        :type range: OWLDataRange

        :return: An empty string. The method prints the restriction details to the info log instead of returning them.

        :rtype: str
        """

        if range is not None:
            Util.info(f"Print DataMaxCardinalityRestriction({cardinality} {p} {range})")
        else:
            Util.info(f"Print DataMaxCardinalityRestriction({cardinality} {p})")
        return ""

    def get_data_exact_cardinality_restriction(
        self, cardinality: int, p: OWLDataPropertyExpression, range: OWLDataRange = None
    ) -> str:
        """
        Constructs and logs a human-readable representation of an OWL Data Exact Cardinality Restriction using the specified cardinality, data property expression, and optional data range. The method formats the restriction details into a string and outputs it via the logging utility, handling cases where the data range is omitted by adjusting the output format accordingly. It returns an empty string, functioning primarily as a logging operation rather than a value retrieval method.

        :param cardinality: The exact number of data values the property must have.
        :type cardinality: int
        :param p: The data property expression upon which the exact cardinality restriction is applied.
        :type p: OWLDataPropertyExpression
        :param range: The data range that acts as the filler for the restriction, specifying the allowed data type for the property values.
        :type range: OWLDataRange

        :return: An empty string.

        :rtype: str
        """

        if range is not None:
            Util.info(
                f"Print DataExactCardinalityRestriction({cardinality} {p} {range})"
            )
        else:
            Util.info(f"Print DataExactCardinalityRestriction({cardinality} {p})")
        return ""

    def get_top_object_property_name(self) -> str:
        """
        This method retrieves the human-readable name of the top object property, which acts as the universal property within the ontology's object property hierarchy. It is typically used during ontology serialization or writing processes to identify the root of the property structure. As a side effect, the method triggers an informational log message and returns the property name as a string.

        :return: The human-readable name of the top object property.

        :rtype: str
        """

        Util.info("Write top object property")
        return ""

    def get_bottom_object_property_name(self) -> str:
        """
        Retrieves the human-readable name of the bottom object property defined in the ontology. The current implementation acts as a stub, returning an empty string instead of a valid identifier. As a side effect, it logs an informational message indicating that the logic for writing the bottom object property is not yet implemented.

        :return: The human-readable name of the bottom object property.

        :rtype: str
        """

        Util.info("Write bottom object property")
        return ""

    def get_atomic_object_property_name(self, p: OWLObjectProperty) -> str:
        """
        Retrieves the short form identifier of the provided OWL object property and logs the action to the info stream. This method delegates the extraction of the identifier to `get_short_name` and triggers a side effect of logging the retrieved name. Despite calculating the name, the function currently returns an empty string.

        :param p: The atomic object property for which to retrieve the human-readable name.
        :type p: OWLObjectProperty

        :return: An empty string.

        :rtype: str
        """

        name: str = self.get_short_name(p)
        Util.info(f"Write atomic object property {name}")
        return ""

    def get_top_data_property_name(self) -> str:
        """
        Retrieves the human-readable name of the top data property within the ontology. This method is intended to provide the identifier for the root data property, which serves as the default parent for the data property hierarchy. In its current state, the method acts as a placeholder that returns an empty string and logs a message, signaling that the implementation for determining the property name is incomplete or intended to be overridden.

        :return: The human-readable name of the top data property.

        :rtype: str
        """

        Util.info("Write top data property")
        return ""

    def get_bottom_data_property_name(self) -> str:
        """
        This method is intended to retrieve the human-readable name of the bottom data property within the ontology. However, the current implementation acts as a placeholder, logging an informational message via `Util.info` and returning an empty string. Consequently, it does not currently provide a valid property name, and callers should be aware that the return value is empty until the implementation is completed.

        :return: The human-readable name of the bottom data property.

        :rtype: str
        """

        Util.info("Write bottom data property")
        return ""

    def get_atomic_data_property_name(self, p: OWLDataProperty) -> str:
        """
        Retrieves the short name of the provided OWL data property and logs the action of writing this property to the info stream. Although the method determines the human-readable identifier for the property, it currently returns an empty string, functioning primarily as a logging step within the broader serialization or processing workflow.

        :param p: The atomic data property for which to retrieve the human-readable name.
        :type p: OWLDataProperty

        :return: An empty string.

        :rtype: str
        """

        name: str = self.get_short_name(p)
        Util.info(f"Write atomic data property {name}")
        return ""

    def write_fuzzy_logic(self, logic: str) -> None:
        """
        This method outputs the specific fuzzy logic type utilized within the ontology, providing a human-readable confirmation of the configuration. It accepts a string representing the logic (such as Zadeh or Lukasiewicz) and logs this information to the console or log stream as a status update. The function performs no data validation or transformation beyond formatting the message for display and returns no value.

        :param logic: Name or type of the fuzzy logic system employed by the ontology.
        :type logic: str
        """

        Util.info(f"Write fuzzy logic {logic}")

    def write_concept_declaration(self, c: OWLClassExpression) -> None:
        """
        Outputs a human-readable trace of a concept declaration by logging the provided OWL class expression. This method accepts an `OWLClassExpression` and generates an informational message containing the concept's string representation, serving as a status update or debug step within the serialization process. It produces no return value and relies on the underlying utility logger to handle the actual display or storage of the message.

        :param c: The OWL class expression to be declared.
        :type c: OWLClassExpression
        """

        Util.info(f"Write concept declaration {c}")

    def write_data_property_declaration(self, dp: OWLDataPropertyExpression) -> None:
        """
        Outputs a human-readable declaration for the specified OWL data property expression, typically for logging or serialization purposes. This method invokes the internal logging utility to record the property details, resulting in an I/O side effect rather than a return value. It serves as a specific handler within the FuzzyOwl2 module for visualizing data property structures during ontology processing.

        :param dp: The OWL data property expression to be declared.
        :type dp: OWLDataPropertyExpression
        """

        Util.info(f"Write data property declaration {dp}")

    def write_object_property_declaration(
        self, op: OWLObjectPropertyExpression
    ) -> None:
        """
        This method handles the serialization of an object property declaration into a human-readable format, typically as part of generating an ontology representation. It accepts an `OWLObjectPropertyExpression` as input, which defines the property to be declared. During execution, the method logs the specific property being processed, indicating the start of the declaration writing procedure.

        :param op: The object property expression to be declared.
        :type op: OWLObjectPropertyExpression
        """

        Util.info(f"Write object property declaration {op}")

    def write_concept_assertion_axiom(
        self, i: OWLIndividual, c: OWLClassExpression, d: float
    ) -> None:
        """
        This method logs a human-readable representation of a fuzzy concept assertion axiom, associating a specific individual with a class expression at a given degree of membership. It formats the individual, class, and degree into a string indicating the assertion and outputs this information via the logging utility. The function does not perform validation on the inputs or return a value, serving primarily as a diagnostic or informational output mechanism within the FuzzyOwl2 processing workflow.

        :param i: The individual instance that is the subject of the concept assertion.
        :type i: OWLIndividual
        :param c: The OWL class expression representing the concept that the individual is asserted to belong to.
        :type c: OWLClassExpression
        :param d: The degree of membership or truth value for the assertion, representing the extent to which the individual belongs to the concept.
        :type d: float
        """

        Util.info(f"Write concept assertion axiom {i}: {c} >= {d}")

    def write_object_property_assertion_axiom(
        self,
        i1: OWLIndividual,
        i2: OWLIndividual,
        p: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        """
        Logs a formatted message representing a fuzzy object property assertion axiom that connects two individuals through a specific property. It incorporates a degree of truth value, reflecting the fuzzy nature of the logic, to quantify the strength of the relationship between the subject and object. This operation serves as a side effect to record or display the semantic assertion in a human-readable format without returning a value.

        :param i1: The subject individual of the object property assertion.
        :type i1: OWLIndividual
        :param i2: The individual acting as the object of the object property assertion.
        :type i2: OWLIndividual
        :param p: The object property expression representing the relationship asserted to hold between the two individuals.
        :type p: OWLObjectPropertyExpression
        :param d: The degree of truth or confidence for the assertion, representing a threshold value for the property relationship.
        :type d: float
        """

        Util.info(f"Write object property assertion axiom ({i1}, {i2}): {p} >= {d}")

    def write_data_property_assertion_axiom(
        self,
        i: OWLIndividual,
        lit: OWLLiteral,
        p: OWLDataPropertyExpression,
        d: float,
    ) -> None:
        """
        Generates and outputs a human-readable representation of a fuzzy data property assertion axiom, signifying that a specific data property relates an individual to a literal value with a certain degree of truth. The method constructs a formatted string that includes the individual, the literal, the property expression, and the minimum degree threshold. This representation is then passed to a logging utility to record or display the assertion.

        :param i: The individual that is the subject of the data property assertion.
        :type i: OWLIndividual
        :param lit: The literal value assigned to the individual via the data property.
        :type lit: OWLLiteral
        :param p: The data property expression representing the relationship being asserted between the individual and the literal.
        :type p: OWLDataPropertyExpression
        :param d: The degree (e.g., truth value or membership degree) representing the strength or certainty of the assertion.
        :type d: float
        """

        Util.info(f"Write data property assertion axiom ({i}, {lit}): {p} >= {d}")

    def write_negative_object_property_assertion_axiom(
        self,
        i1: OWLIndividual,
        i2: OWLIndividual,
        p: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        """
        Outputs a human-readable log entry for a negative object property assertion axiom, incorporating a fuzzy logic degree. The method constructs a string indicating that the specified object property does not relate the first individual to the second individual, accompanied by a threshold degree. This action produces a side effect by invoking `Util.info` to display the formatted axiom, and the function returns None.

        :param i1: The subject individual in the negative object property assertion.
        :type i1: OWLIndividual
        :param i2: The individual that is asserted not to be related to the first individual via the specified property.
        :type i2: OWLIndividual
        :param p: The object property expression representing the relationship being negated between the individuals.
        :type p: OWLObjectPropertyExpression
        :param d: The degree value representing the threshold for the negative assertion.
        :type d: float
        """

        Util.info(
            f"Write negative object property assertion axiom ({i1}, {i2}): not {p} >= {d}"
        )

    def write_negative_data_property_assertion_axiom(
        self,
        i: OWLIndividual,
        lit: OWLLiteral,
        p: OWLDataPropertyExpression,
        d: float,
    ) -> None:
        """
        This method generates and logs a human-readable representation of a negative data property assertion axiom within a fuzzy logic context. It constructs a string indicating that the specified individual does not possess the given data property with the provided literal value, associated with a specific degree of truth `d`. The function does not return a value but produces a side effect by invoking the utility logger to display the formatted axiom.

        :param i: The individual subject of the negative data property assertion.
        :type i: OWLIndividual
        :param lit: The literal value that the individual is asserted not to possess.
        :type lit: OWLLiteral
        :param p: The data property expression representing the relationship being negated in the assertion.
        :type p: OWLDataPropertyExpression
        :param d: The degree of truth or threshold value for the negative assertion.
        :type d: float
        """

        Util.info(
            f"Write negative data property assertion axiom ({i}, {lit}): not {p} >= {d}"
        )

    def write_same_individual_axiom(self, ind_set: set[OWLIndividual]) -> None:
        """
        Outputs a log entry representing an assertion that a specific group of individuals are identical. The method accepts a collection of individual entities and formats them into a standardized string indicating a "SameIndividual" relationship. This operation is primarily for logging or display purposes, as it invokes a utility function to print the information rather than modifying the ontology structure directly or returning a result. The method relies on the string representation of the input set for formatting.

        :param ind_set: The set of individuals asserted to be identical.
        :type ind_set: set[OWLIndividual]
        """

        Util.info(f"Write axiom SameIndividual({ind_set})")

    def write_different_individuals_axiom(self, ind_set: set[OWLIndividual]) -> None:
        """
        This method outputs a human-readable representation of a DifferentIndividuals axiom, which asserts that all individuals within the provided set are mutually distinct. It accepts a set of OWLIndividual objects and formats them into a string that is logged via the utility function, serving as a side effect rather than returning a value. The method does not validate the cardinality of the input set; consequently, passing an empty set or a set containing a single individual will result in the logging of a logically vacuous or redundant axiom statement.

        :param ind_set: The collection of individuals asserted to be mutually distinct.
        :type ind_set: set[OWLIndividual]
        """

        Util.info(f"Write axiom DifferentIndividuals({ind_set})")

    def write_disjoint_classes_axiom(self, class_set: set[OWLClassExpression]) -> None:
        """
        Generates and outputs a human-readable representation of a DisjointClasses axiom based on the provided set of OWL class expressions. The method formats the input set into a string resembling functional syntax and delegates the actual output to a logging utility. It does not perform logical validation on the set, such as checking for a minimum number of classes, and therefore simply serializes the provided arguments as-is.

        :param class_set: The set of classes that are mutually disjoint.
        :type class_set: set[OWLClassExpression]
        """

        Util.info(f"Write axiom DisjointClasses({class_set})")

    def write_disjoint_union_axiom(self, class_set: set[OWLClassExpression]) -> None:
        """
        Outputs a human-readable representation of a disjoint union axiom by logging the provided set of class expressions. This method utilizes a utility function to format and display the semantic relationship defined by the axiom, ensuring that the collection of classes is presented as a unified disjoint structure. The operation produces a side effect via logging rather than returning a value, and it relies on the standard string conversion of the input set to generate the output message.

        :param class_set: The set of class expressions that constitute the disjoint union.
        :type class_set: set[OWLClassExpression]
        """

        Util.info(f"Write axiom DisjointUnion({class_set})")

    def write_subclass_of_axiom(
        self, subclass: OWLClassExpression, superclass: OWLClassExpression, d: float
    ) -> None:
        """
        Outputs a human-readable representation of a fuzzy subclass axiom defined by the given subclass, superclass, and degree of truth. The method formats the relationship as a threshold condition, indicating that the subclass relationship holds with a degree greater than or equal to the specified value. This operation results in a logging side effect via a utility function and does not return a value.

        :param subclass: The class expression representing the subclass in the axiom.
        :type subclass: OWLClassExpression
        :param superclass: The parent class or general concept that the subclass is asserted to be a subset of.
        :type superclass: OWLClassExpression
        :param d: The degree or threshold value representing the minimum level of truth or confidence for the subclass relationship.
        :type d: float
        """

        Util.info(
            f"Write axiom SubClassOf({subclass} is subclass of {superclass} >= {d})"
        )

    def write_equivalent_classes_axiom(
        self, class_set: set[OWLClassExpression]
    ) -> None:
        """
        This method generates a human-readable representation of an EquivalentClasses axiom, asserting that all provided class expressions are semantically identical. It accepts a set of OWLClassExpression objects and outputs the axiom structure to the logging utility. The operation results in a side effect where the axiom details are printed to the standard information stream, but it does not return a value. While the method processes any set of class expressions, the logical integrity of an equivalence axiom generally requires the set to contain at least two classes.

        :param class_set: The set of OWL class expressions that are mutually equivalent.
        :type class_set: set[OWLClassExpression]
        """

        Util.info(f"Write axiom EquivalentClasses({class_set})")

    def write_sub_object_property_of_axiom(
        self,
        subproperty: OWLObjectPropertyExpression,
        superproperty: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        """
        Outputs a human-readable log entry representing a fuzzy sub-object property axiom, asserting that the specified sub-property is a specialization of the super-property with a specific degree of truth. The method formats the sub-property, super-property, and the degree value into a descriptive string and passes it to the logging utility. This operation produces no return value and relies on the string representations of the input property expressions for the generated output.

        :param subproperty: The object property expression that is a subclass of the superproperty.
        :type subproperty: OWLObjectPropertyExpression
        :param superproperty: The object property expression representing the parent or more general property in the subproperty relationship.
        :type superproperty: OWLObjectPropertyExpression
        :param d: The degree of truth or threshold value associated with the subsumption relationship.
        :type d: float
        """

        Util.info(
            f"Write axiom SubObjectPropertyOf({subproperty} is subclass of {superproperty} >= {d})"
        )

    def write_sub_data_property_of_axiom(
        self,
        subproperty: OWLDataPropertyExpression,
        superproperty: OWLDataPropertyExpression,
        d: float,
    ) -> None:
        """
        This method generates and logs a human-readable representation of a fuzzy sub-data-property axiom within the context of a Fuzzy OWL 2 ontology. It accepts a subproperty and a superproperty, both defined as OWL data property expressions, along with a floating-point value representing the degree of truth or membership for the relationship. The method constructs a string indicating that the subproperty is a subclass of the superproperty with a degree greater than or equal to the specified value and outputs this information using the `Util.info` logging utility. As a side effect, this operation produces a log entry but does not return a value.

        :param subproperty: The data property that is a subproperty of the superproperty.
        :type subproperty: OWLDataPropertyExpression
        :param superproperty: The more general data property expression that the subproperty is a subset of.
        :type superproperty: OWLDataPropertyExpression
        :param d: The degree or threshold value indicating the strength of the subproperty relationship.
        :type d: float
        """

        Util.info(
            f"Write axiom SubDataPropertyOf({subproperty} is subclass of {superproperty} >= {d})"
        )

    def write_sub_property_chain_of_axiom(
        self,
        chain: list[OWLObjectPropertyExpression],
        superproperty: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        """
        Generates and logs a human-readable representation of a fuzzy sub-property chain axiom. This method constructs a string indicating that a specific chain of object properties is a sub-property of a given superproperty, associated with a specified degree of truth or membership. It outputs this formatted axiom using the logging utility, serving primarily as a diagnostic or informational action rather than modifying the ontology structure. The method relies on the string representations of the provided property expressions for the output format.

        :param chain: The sequence of object properties that compose the chain in the SubPropertyChainOf axiom.
        :type chain: list[OWLObjectPropertyExpression]
        :param superproperty: The object property expression that the property chain is a sub-property of.
        :type superproperty: OWLObjectPropertyExpression
        :param d: The degree or truth value associated with the sub property chain axiom.
        :type d: float
        """

        Util.info(
            f"Write axiom SubPropertyChainOf({chain} is subclass of {superproperty} >= {d})"
        )

    def write_equivalent_object_properties_axiom(
        self, class_set: set[OWLObjectPropertyExpression]
    ) -> None:
        """
        Generates a log entry representing an equivalent object properties axiom for the given set of object property expressions. The method formats the input set into a human-readable string indicating the equivalence relationship and outputs it via a logging utility. This function does not return a value and its primary effect is the generation of this informational message.

        :param class_set: The set of object properties that are mutually equivalent in the axiom.
        :type class_set: set[OWLObjectPropertyExpression]
        """

        Util.info(f"Write axiom EquivalentObjectProperties({class_set})")

    def write_equivalent_data_properties_axiom(
        self, class_set: set[OWLDataPropertyExpression]
    ) -> None:
        """
        This method generates a human-readable representation of an equivalent data properties axiom, indicating that all properties within the provided set are semantically equivalent. It accepts a collection of OWL data property expressions and delegates the actual output generation to a logging utility, formatting the input set into a standard string format. The operation produces a side effect of logging the axiom information but returns no value, and it does not perform logical validation on the contents of the property set, such as checking for emptiness or redundancy.

        :param class_set: The set of data property expressions that are asserted to be equivalent.
        :type class_set: set[OWLDataPropertyExpression]
        """

        Util.info(f"Write axiom EquivalentDataProperties({class_set})")

    def write_transitive_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        Serializes a transitive object property axiom to a human-readable format, indicating that the relationship defined by the given property is transitive. It accepts an object property expression representing the property to be characterized as transitive. Instead of returning a value, the method triggers a logging action via the utility module to output the formatted axiom string.

        :param p: The object property expression to be declared transitive.
        :type p: OWLObjectPropertyExpression
        """

        Util.info(f"Write axiom TransitiveObjectProperty({p})")

    def write_symmetric_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        This method generates and logs a human-readable representation of a symmetric object property axiom. It accepts an object property expression as input and formats it into a standard axiom string, which is then output via the logging utility. The function does not return a value and relies on the provided property expression being valid for string formatting. This serves as a step in the broader process of serializing ontology axioms in the FuzzyOwl2 environment.

        :param p: The object property expression that is symmetric.
        :type p: OWLObjectPropertyExpression
        """

        Util.info(f"Write axiom SymmetricObjectProperty({p})")

    def write_asymmetric_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        This method handles the output of an asymmetric object property axiom, indicating that the provided object property expression is asymmetric. It accepts a single argument representing the property and triggers an informational log message to record the axiom's generation. The method performs no validation on the input and returns None, with its primary side effect being the logging operation.

        :param p: The object property expression to be declared asymmetric.
        :type p: OWLObjectPropertyExpression
        """

        Util.info(f"Write axiom AsymmetricObjectProperty({p})")

    def write_reflexive_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        Outputs a human-readable representation of a reflexive object property axiom, indicating that the specified property relates every individual in the domain to itself. This method accepts an object property expression and delegates the formatting and logging of the axiom to the utility handler. It functions as part of the ontology serialization process, ensuring that reflexive property constraints are explicitly recorded without returning a value.

        :param p: The object property expression to be asserted as reflexive.
        :type p: OWLObjectPropertyExpression
        """

        Util.info(f"Write axiom ReflexiveObjectProperty({p})")

    def write_irreflexive_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        Outputs a human-readable representation of an irreflexive object property axiom, asserting that the specified property cannot relate an individual to itself. This method accepts an `OWLObjectPropertyExpression` as input and triggers a logging operation to record the axiom's structure. It does not return a value, serving primarily to document or serialize the semantic constraint that the property is irreflexive.

        :param p: The object property expression that is asserted to be irreflexive.
        :type p: OWLObjectPropertyExpression
        """

        Util.info(f"Write axiom IrreflexiveObjectProperty({p})")

    def write_functional_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        This method serializes a functional object property axiom by generating a human-readable string representation of the provided object property expression. It formats the input property into a `FunctionalObjectProperty` declaration and outputs this string using the logging utility. The function does not return a value, acting instead as a side effect to record the axiom's definition within the current context.

        :param p: The object property expression to be asserted as functional.
        :type p: OWLObjectPropertyExpression
        """

        Util.info(f"Write axiom FunctionalObjectProperty({p})")

    def write_functional_data_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        Generates and logs a human-readable representation of a functional data property axiom, indicating that the provided property can have at most one value for a given individual. The method accepts a property expression as an argument and formats it into a specific string structure, which is then output via the logging utility. This operation results in a side effect of producing a log entry and does not return a value.

        :param p: The object property expression that is functional in the axiom.
        :type p: OWLObjectPropertyExpression
        """

        Util.info(f"Write axiom FunctionalDataProperty({p})")

    def write_inverse_object_property_axiom(
        self, p1: OWLObjectPropertyExpression, p2: OWLObjectPropertyExpression
    ) -> None:
        """
        Generates and logs a human-readable representation of an inverse object property axiom, asserting that the first provided property is the inverse of the second. This method formats the relationship between the two object property expressions and outputs the result via a logging utility, serving as a side effect rather than returning a value. The operation relies on the string representations of the input properties to construct the output message.

        :param p1: The first object property expression involved in the inverse relationship.
        :type p1: OWLObjectPropertyExpression
        :param p2: The object property expression that serves as the inverse counterpart to the first property.
        :type p2: OWLObjectPropertyExpression
        """

        Util.info(f"Write inverse object property axiom - axiom ({p1} inverse of {p2})")

    def write_inverse_functional_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        Outputs a human-readable representation of an inverse functional object property axiom. This method accepts an object property expression and logs the axiom, indicating that the property is inverse functional—meaning no two distinct individuals can be related to the same individual via the inverse of this property. The operation relies on a utility function to handle the actual output and does not return a value.

        :param p: The object property expression to be declared as inverse functional.
        :type p: OWLObjectPropertyExpression
        """

        Util.info(f"Write axiom InverseFunctionalObjectProperty({p})")

    def write_object_property_domain_axiom(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> None:
        """
        Generates and outputs a representation of an object property domain axiom, which constrains the subjects of the given object property to belong to the specified class expression. This method accepts the object property and the class expression as inputs and triggers an informational log entry detailing the relationship. It performs no validation on the inputs and does not return a value, serving primarily as a step in the serialization or processing pipeline for fuzzy OWL ontologies.

        :param p: The object property expression whose domain is being defined.
        :type p: OWLObjectPropertyExpression
        :param c: The class expression representing the domain of the object property.
        :type c: OWLClassExpression
        """

        Util.info(f"Write axiom domain ({c} of object property {p})")

    def write_object_property_range_axiom(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> None:
        """
        This method handles the serialization of an object property range axiom, which defines the class of values that a specific object property can take. It accepts an object property expression and a class expression, formatting them into a descriptive string that represents the range constraint. The operation triggers a logging event to output this information, serving as a side effect rather than returning a value.

        :param p: The object property expression for which the range is being defined.
        :type p: OWLObjectPropertyExpression
        :param c: The class expression specifying the range of the object property.
        :type c: OWLClassExpression
        """

        Util.info(f"Write axiom range ({c} of object property {p})")

    def write_data_property_domain_axiom(
        self, p: OWLDataPropertyExpression, c: OWLClassExpression
    ) -> None:
        """
        Outputs a human-readable representation of a data property domain axiom to the information log. This method asserts that the provided data property expression is associated with the specified class expression as its domain. The operation results in a side effect of logging the formatted relationship and returns None.

        :param p: The data property expression for which the domain is being specified.
        :type p: OWLDataPropertyExpression
        :param c: The class expression defining the domain of the data property.
        :type c: OWLClassExpression
        """

        Util.info(f"Write axiom domain ({c} of data property {p})")

    def write_data_property_range_axiom(
        self, p: OWLDataPropertyExpression, range: OWLDataRange
    ) -> None:
        """
        This method processes a data property range axiom by logging the association between a specific data property and its defined data range. It accepts an `OWLDataPropertyExpression` representing the property and an `OWLDataRange` representing the range, then generates an informational message using the `Util.info` utility to record the operation. The function does not return a value, and its primary side effect is the output of this log message, which serves as a human-readable record of the axiom being written.

        :param p: The data property expression for which the range is specified.
        :type p: OWLDataPropertyExpression
        :param range: The data range defining the permissible values for the data property.
        :type range: OWLDataRange
        """

        Util.info(f"Write axiom range ({range} of data property {p})")

    def write_disjoint_object_properties_axiom(
        self, class_set: set[OWLObjectPropertyExpression]
    ) -> None:
        """
        Logs the processing of a disjoint object properties axiom for a set of object property expressions that are mutually exclusive. This method accepts a set of properties and outputs an informational message containing the set, serving as a notification step within the serialization pipeline. It does not enforce that the set contains sufficient elements to form a valid axiom and returns None.

        :param class_set: The set of object properties that are mutually disjoint.
        :type class_set: set[OWLObjectPropertyExpression]
        """

        Util.info(f"Write disjoint object properties axiom ({class_set})")

    def write_disjoint_data_properties_axiom(
        self, class_set: set[OWLDataPropertyExpression]
    ) -> None:
        """
        This method processes a set of data properties to represent a disjoint data properties axiom in a human-readable format. It accepts a collection of data property expressions that are defined as mutually exclusive within the ontology. The primary side effect is the generation of an informational log entry detailing the specific properties involved in the axiom, while the method itself returns no value.

        :param class_set: The set of data properties to be declared as pairwise disjoint.
        :type class_set: set[OWLDataPropertyExpression]
        """

        Util.info(f"Write disjoint data properties axiom ({class_set})")

    def write_triangular_modifier_definition(
        self, name: str, mod: TriangularModifier
    ) -> None:
        """
        This method generates a human-readable definition of a triangular modifier and outputs it via the logging utility. It constructs a string representation by combining the provided name with the string representation of the modifier object, formatted as "name = modifier". The primary side effect is the emission of this information to the standard output or log stream, which is useful for debugging or tracking the configuration of fuzzy logic components. The output format depends implicitly on the string conversion logic of the provided `TriangularModifier` instance.

        :param name: Identifier for the triangular modifier.
        :type name: str
        :param mod: The triangular modifier instance to be defined.
        :type mod: fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier.TriangularModifier
        """

        Util.info(f"Write triangular modifier definition {name} = {mod}")

    def write_linear_modifier_definition(self, name: str, mod: LinearModifier) -> None:
        """
        Outputs a human-readable representation of a linear modifier definition to the logging stream. This method constructs a formatted string associating the specified name with the string representation of the modifier object and passes it to the logging utility. The operation is performed for side effects such as debugging or user feedback and does not return a value. The clarity of the output relies on the string conversion method of the provided `LinearModifier` instance.

        :param name: The identifier for the linear modifier.
        :type name: str
        :param mod:
        :type mod: fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier.LinearModifier
        """

        Util.info(f"Write linear modifier definition {name} = {mod}")

    def write_crisp_function_definition(self, name: str, dat: CrispFunction) -> None:
        """
        Generates and logs a human-readable string representation of a specific crisp function definition. By utilizing the `Util.info` utility, this method outputs the provided name alongside the string representation of the `CrispFunction` object, effectively recording the function's details for user inspection or debugging. The operation does not modify any internal state or return a value, serving solely as an informational side effect.

        :param name: The name to assign to the crisp function definition.
        :type name: str
        :param dat: The crisp function instance to be written.
        :type dat: CrispFunction
        """

        Util.info(f"Write crisp function definition {name} = {dat}")

    def write_left_shoulder_function_definition(
        self, name: str, dat: LeftShoulderFunction
    ) -> None:
        """
        Logs the definition of a left shoulder fuzzy logic function in a human-readable format, typically for debugging or informational purposes. It constructs a string representation of the function assignment by combining the provided name with the string representation of the `LeftShoulderFunction` object. The method delegates the output to the logging utility, resulting in a side effect of writing to the standard log stream without returning a value.

        :param name: The name to assign to the left shoulder function definition.
        :type name: str
        :param dat: The left shoulder function instance to be written.
        :type dat: LeftShoulderFunction
        """

        Util.info(f"Write left shoulder function definition {name} = {dat}")

    def write_right_shoulder_function_definition(
        self, name: str, dat: RightShoulderFunction
    ) -> None:
        """
        Outputs a human-readable representation of a right shoulder function definition to the logging system. It accepts a string identifier for the function and the function object itself, formatting them into a descriptive message that associates the name with the function's parameters. The method performs this action as a side effect via a utility logger and returns no value.

        :param name: Identifier for the right shoulder function definition.
        :type name: str
        :param dat: The specific right shoulder function instance to be defined.
        :type dat: RightShoulderFunction
        """

        Util.info(f"Write right shoulder function definition {name} = {dat}")

    def write_linear_function_definition(self, name: str, dat: LinearFunction) -> None:
        """
        Outputs a human-readable representation of a linear function definition to the logging stream by combining the provided name with the string representation of the `LinearFunction` object. This method delegates the actual writing to the `Util.info` utility, formatting the message as "name = dat". It performs no file I/O directly and returns `None`, serving primarily as a diagnostic or informational tool within the broader context of the `FuzzyOwl2` module.

        :param name: The name to assign to the linear function in the definition.
        :type name: str
        :param dat: The linear function object to be defined.
        :type dat: LinearFunction
        """

        Util.info(f"Write linear function definition {name} = {dat}")

    def write_triangular_function_definition(
        self, name: str, dat: TriangularFunction
    ) -> None:
        """
        Logs the definition of a triangular function in a human-readable format for diagnostic or informational purposes. It constructs a string representation combining the provided name and the TriangularFunction object, then delegates the output to the `Util.info` utility. This method does not modify the object's state or return a value; its primary side effect is the generation of a log entry. The clarity of the output depends on the string representation implementation of the `TriangularFunction` instance.

        :param name: The identifier or label to assign to the triangular function in the generated definition string.
        :type name: str
        :param dat: The triangular function instance to be written.
        :type dat: TriangularFunction
        """

        Util.info(f"Write triangular function definition {name} = {dat}")

    def write_trapezoidal_function_definition(
        self, name: str, dat: TrapezoidalFunction
    ) -> None:
        """
        Outputs a human-readable representation of a trapezoidal function definition to the logging system. It constructs a log message combining the specified name and the trapezoidal function data structure, then passes this message to the utility info handler. This action is a side effect intended for informational tracking or debugging, as the method does not return a value or modify the input data.

        :param name: The name to assign to the trapezoidal function in the definition.
        :type name: str
        :param dat: The trapezoidal function to be defined.
        :type dat: TrapezoidalFunction
        """

        Util.info(f"Write trapezoidal function definition {name} = {dat}")

    def write_modified_function_definition(
        self, name: str, dat: ModifiedFunction
    ) -> None:
        """
        Outputs a human-readable representation of a modified function definition to the logging or information stream. This method constructs a formatted string containing the function name and the `ModifiedFunction` object, then delegates the display to the `Util.info` utility. It serves as a reporting or debugging aid to visualize the function's state without modifying the underlying data, assuming the `ModifiedFunction` object provides a meaningful string representation.

        :param name: The name of the modified function.
        :type name: str
        :param dat: The modified function object to be written.
        :type dat: ModifiedFunction
        """

        Util.info(f"Write modified function definition {name} = {dat}")

    def write_modified_property_definition(
        self, name: str, dat: ModifiedProperty
    ) -> None:
        """
        This method logs a human-readable representation of a modified property definition to the system's info output. It formats the provided property name and the `ModifiedProperty` data object into a descriptive string, which is then passed to the utility logging handler. The operation is primarily intended for debugging or tracking purposes, as it produces a side effect of logging without returning a value or modifying the input data.

        :param name: The name of the modified property being defined.
        :type name: str
        :param dat: The modified property object to be written.
        :type dat: ModifiedProperty
        """

        Util.info(f"Write modified property definition {name} = {dat}")

    def write_modified_concept_definition(
        self, name: str, dat: ModifiedConcept
    ) -> None:
        """
        Logs the definition of a modified concept to the standard information output stream. This method formats the provided concept name and the associated ModifiedConcept data structure into a human-readable string, which is then displayed via the utility logging function. It is primarily used for reporting or debugging purposes to visualize the current state of a concept, and it does not modify any internal object state or return a value.

        :param name: Identifier for the modified concept.
        :type name: str
        :param dat: The modified concept object to be written.
        :type dat: fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept.ModifiedConcept
        """

        Util.info(f"Write modified concept definition {name} = {dat}")

    def write_fuzzy_nominal_concept_definition(
        self, name: str, dat: FuzzyNominalConcept
    ) -> None:
        """
        Outputs a human-readable representation of a fuzzy nominal concept definition to the logging stream. It constructs an informational message by combining the provided name with the string representation of the `FuzzyNominalConcept` object. This method serves as a side-effecting utility to display the concept definition during processing, rather than returning a value or writing to a file.

        :param name: Identifier for the fuzzy nominal concept being defined.
        :type name: str
        :param dat:
        :type dat: FuzzyNominalConcept
        """

        Util.info(f"Write fuzzy nominal concept definition {name} = {dat}")

    def write_weighted_concept_definition(self, name: str, c: WeightedConcept) -> None:
        """
        Logs a human-readable representation of a weighted concept definition to the information stream. The method constructs a message associating the provided name with the string representation of the WeightedConcept object, which is then processed by the logging utility. This operation serves as a side effect for debugging or status reporting and does not return a value or modify the input object.

        :param name: The name or identifier assigned to the weighted concept.
        :type name: str
        :param c: The weighted concept object to be defined.
        :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_concept.WeightedConcept
        """

        Util.info(f"Write weighted concept definition {name} = {c}")

    def write_weighted_max_concept_definition(
        self, name: str, c: WeightedMaxConcept
    ) -> None:
        """
        Outputs a human-readable log entry representing the definition of a weighted max concept. It accepts a string identifier and the corresponding concept object, formatting them into a message that indicates the definition is being written. This method relies on the string representation of the concept object and produces no return value, serving primarily as a side effect to inform the user or system of the current state.

        :param name: The identifier assigned to the weighted max concept.
        :type name: str
        :param c: The weighted max concept instance to be defined.
        :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_max_concept.WeightedMaxConcept
        """

        Util.info(f"Write weighted max concept definition {name} = {c}")

    def write_weighted_min_concept_definition(
        self, name: str, c: WeightedMinConcept
    ) -> None:
        """
        Generates and logs a human-readable string representation of a weighted minimum concept definition using the provided name and concept object. The method formats the output as "name = concept" and delegates the actual writing to a utility logging function. This operation produces a side effect by outputting information to the standard info stream but does not modify the state of the instance or the concept object.

        :param name: The name to assign to the weighted min concept in the definition.
        :type name: str
        :param c: The weighted min concept instance to be written.
        :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept.WeightedMinConcept
        """

        Util.info(f"Write weighted min concept definition {name} = {c}")

    def write_weighted_sum_concept_definition(
        self, name: str, c: WeightedSumConcept
    ) -> None:
        """
        This method outputs a human-readable definition of a weighted sum concept to the logging system, serving primarily as a diagnostic or informational utility. It accepts a string identifier and a `WeightedSumConcept` instance, formatting them into a message that displays the concept's definition alongside its name. The operation relies on the `Util.info` method to handle the actual output, meaning the side effect is the generation of a log entry rather than a direct modification of system state or file content. The clarity of the output depends on the string representation implementation of the `WeightedSumConcept` object.

        :param name: Identifier for the weighted sum concept being defined.
        :type name: str
        :param c: The weighted sum concept to be defined.
        :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_concept.WeightedSumConcept
        """

        Util.info(f"Write weighted sum concept definition {name} = {c}")

    def write_weighted_sum_zero_concept_definition(
        self, name: str, c: WeightedSumZeroConcept
    ) -> None:
        """
        Outputs a log message describing the definition of a weighted sum zero concept in a human-readable format. This method formats the provided name and the concept object into a string indicating the definition is being written and passes it to the utility logging function. It produces a side effect of displaying information to the user or log stream without modifying the object's state or returning a value.

        :param name: The identifier or label for the weighted sum zero concept.
        :type name: str
        :param c: The weighted sum zero concept to be defined.
        :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_zero_concept.WeightedSumZeroConcept
        """

        Util.info(f"Write weighted sum zero concept definition {name} = {c}")

    def write_owa_concept_definition(self, name: str, c: OwaConcept) -> None:
        """
        Generates and outputs a human-readable representation of an Ordered Weighted Averaging (OWA) concept definition to the logging utility. It accepts a string name and the concept object, formatting them into a status message that reflects the current definition. This operation is intended for informational purposes, such as debugging or progress tracking, and does not alter the state of the input parameters or return a value.

        :param name: The identifier or label for the OWA concept being defined.
        :type name: str
        :param c: The OWA concept instance to be defined.
        :type c: fuzzy_dl_owl2.fuzzydl.concept.owa_concept.OwaConcept
        """

        Util.info(f"Write owa concept definition {name} = {c}")

    def write_choquet_concept_definition(self, name: str, c: ChoquetConcept) -> None:
        """
        Outputs a formatted log message representing the definition of a Choquet concept. This method constructs a string combining the provided name and the string representation of the concept object, then passes it to the logging utility. The primary side effect is the generation of this log entry, typically to standard output or a configured log stream, while the method itself returns no value. The readability of the output depends on the implementation of the string conversion for the provided concept object.

        :param name: The name or label assigned to the Choquet concept.
        :type name: str
        :param c: The Choquet concept instance to be written.
        :type c: ChoquetConcept
        """

        Util.info(f"Write choquet concept definition {name} = {c}")

    def write_sugeno_concept_definition(self, name: str, c: SugenoConcept) -> None:
        """
        Generates a human-readable log entry representing the definition of a specific Sugeno concept. It constructs an informational message by combining the provided name with the string representation of the SugenoConcept instance, effectively outputting the assignment syntax. This method serves as a utility for logging or debugging the current state of fuzzy logic definitions without modifying the underlying data structure.

        :param name: The identifier or label assigned to the Sugeno concept.
        :type name: str
        :param c:
        :type c: SugenoConcept
        """

        Util.info(f"Write sugeno concept definition {name} = {c}")

    def write_quasi_sugeno_concept_definition(
        self, name: str, c: QsugenoConcept
    ) -> None:
        """
        Outputs a human-readable representation of a fuzzy logic concept definition by logging a formatted string that associates the provided name with the concept object. This operation relies on the string conversion of the concept instance to ensure readability and serves primarily as a diagnostic or informational step within the broader processing workflow. The method produces a side effect of generating log output and does not return any value.

        :param name: Label used to identify the quasi Sugeno concept in the definition.
        :type name: str
        :param c: The specific concept instance to be defined.
        :type c: QsugenoConcept
        """

        Util.info(f"Write quasi sugeno concept definition {name} = {c}")

    def write_qowa_concept_definition(self, name: str, c: QowaConcept) -> None:
        """
        Outputs the definition of a quasi OWA concept to the logging or information stream. This method constructs a human-readable string by combining the provided name with the string representation of the `QowaConcept` object and passes it to the utility logger. It does not return a value or modify internal state, serving solely to display the concept definition for debugging or informational purposes.

        :param name: The identifier or label for the quasi OWA concept.
        :type name: str
        :param c: The quasi OWA concept to be defined.
        :type c: fuzzy_dl_owl2.fuzzydl.concept.qowa_concept.QowaConcept
        """

        Util.info(f"Write quasi owa concept definition {name} = {c}")
