import os
import typing

from rdflib import Namespace

from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.util import Util
from fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept import ChoquetConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
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

from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader


class FuzzyOwl2(object):
    POS_INFINITY: float = 10000.0
    NEG_INFINITY: float = -POS_INFINITY

    def __init__(
        self,
        input_file: str,
        output_file: str,
        base_iri: str = "http://www.semanticweb.org/ontologies/fuzzydl_ontology#",
    ) -> None:
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
        return str(e.iri).split("#")[-1]

    def translate_owl2ontology(self) -> None:
        self.process_ontology_annotations()
        self.process_datatype_annotations()
        self.process_concept_annotations()
        self.process_property_annotations()
        self.process_ontology_axioms()

    def process_ontology_annotations(self) -> None:
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
        facets: list[float] = [float("-inf"), float("inf")]
        for ontology in self.ontologies:
            datatype_def_axioms: set[OWLDatatypeDefinition] = ontology.get_axioms(
                AxiomsType.DATATYPE_DEFINITION
            )
            if datatype_def_axioms is None:
                continue
            for axiom in datatype_def_axioms:
                assert isinstance(axiom, OWLDatatypeDefinition)
                datatype_name: str = self.get_short_name(axiom.datatype).replace(
                    ":", ""
                )
                if datatype_name != name:
                    continue
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
                if f1.constraint_to_uriref() == OWLFacet.MIN_INCLUSIVE:
                    facets[0] = float(str(f1.value.value))
                elif f1.constraint_to_uriref() == OWLFacet.MAX_INCLUSIVE:
                    facets[1] = float(str(f1.value.value))
                if f2.constraint_to_uriref() == OWLFacet.MIN_INCLUSIVE:
                    facets[0] = float(str(f2.value.value))
                elif f2.constraint_to_uriref() == OWLFacet.MAX_INCLUSIVE:
                    facets[1] = float(str(f2.value.value))
                return facets
        return facets

    def process_datatype_annotations(self) -> None:
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
                    if isinstance(c, LeftShoulderFunction):
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
        if p.is_top_object_property():
            return self.get_top_object_property_name()
        elif p.is_bottom_object_property():
            return self.get_bottom_object_property_name()
        else:
            return self.get_atomic_object_property_name(p)

    def get_data_property_name(self, p: OWLDataPropertyExpression) -> str:
        if p.is_top_data_property():
            return self.get_top_data_property_name()
        elif p.is_bottom_data_property():
            return self.get_bottom_data_property_name()
        else:
            return self.get_atomic_data_property_name(p)

    def get_individual_name(self, i: OWLIndividual) -> typing.Optional[str]:
        if isinstance(i, OWLAnonymousIndividual):
            Util.info(f"Anonymous individual not supported")
            return None
        else:
            name: str = self.get_short_name(i)
            Util.info(f"Individual {name}")
            return ""

    def get_top_concept_name(self) -> str:
        Util.info(f"Print Top concept")
        return ""

    def get_bottom_concept_name(self) -> str:
        Util.info(f"Print Bottom concept")
        return ""

    def get_atomic_concept_name(self, c: OWLClass) -> str:
        name: str = self.get_short_name(c)
        Util.info(f"Print Atomic concept {name}")
        return ""

    def get_object_intersection_of_name(self, operands: set[OWLClassExpression]) -> str:
        Util.info(f"Print ObjectIntersectionOf {operands}")
        return ""

    def get_object_union_of_name(self, operands: set[OWLClassExpression]) -> str:
        Util.info(f"Print ObjectUnionOf {operands}")
        return ""

    def get_object_some_values_from_name(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> str:
        Util.info(f"Print ObjectSomeValuesFrom({p} {c})")
        return ""

    def get_object_all_values_from_name(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> str:
        Util.info(f"Print ObjectAllValuesFrom({p} {c})")
        return ""

    def get_data_some_values_from_name(
        self, p: OWLDataPropertyExpression, range: OWLDataRange
    ) -> str:
        Util.info(f"Print DataSomeValuesFrom({p} {range})")
        return ""

    def get_data_all_values_from_name(
        self, p: OWLDataPropertyExpression, range: OWLDataRange
    ) -> str:
        Util.info(f"Print DataAllValuesFrom({p} {range})")
        return ""

    def get_object_complement_of_name(self, c: OWLClassExpression) -> str:
        Util.info(f"Print ObjectComplement({c})")
        return ""

    def get_object_has_self_name(self, p: OWLObjectPropertyExpression) -> str:
        Util.info(f"Print ObjectHasSelf({p})")
        return ""

    def get_object_one_of_name(self, ind_set: set[OWLIndividual]) -> str:
        Util.info(f"Print ObjectOneOf({ind_set})")
        return ""

    def get_object_has_value_name(
        self, p: OWLObjectPropertyExpression, i: OWLIndividual
    ) -> str:
        Util.info(f"Print ObjectHasValue({p} {i})")
        return ""

    def get_data_has_value_name(
        self, p: OWLDataPropertyExpression, literal: OWLLiteral
    ) -> str:
        Util.info(f"Print DataHasValue({p} {literal})")
        return ""

    def get_object_min_cardinality_restriction(
        self,
        cardinality: int,
        p: OWLObjectPropertyExpression,
        c: OWLClassExpression = None,
    ) -> str:
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
        if c is not None:
            Util.info(f"Print ObjectExactCardinalityRestriction({cardinality} {p} {c})")
        else:
            Util.info(f"Print ObjectExactCardinalityRestriction({cardinality} {p})")
        return ""

    def get_data_min_cardinality_restriction(
        self, cardinality: int, p: OWLDataPropertyExpression, range: OWLDataRange = None
    ) -> str:
        if range is not None:
            Util.info(f"Print DataMinCardinalityRestriction({cardinality} {p} {range})")
        else:
            Util.info(f"Print DataMinCardinalityRestriction({cardinality} {p})")
        return ""

    def get_data_max_cardinality_restriction(
        self, cardinality: int, p: OWLDataPropertyExpression, range: OWLDataRange = None
    ) -> str:
        if range is not None:
            Util.info(f"Print DataMaxCardinalityRestriction({cardinality} {p} {range})")
        else:
            Util.info(f"Print DataMaxCardinalityRestriction({cardinality} {p})")
        return ""

    def get_data_exact_cardinality_restriction(
        self, cardinality: int, p: OWLDataPropertyExpression, range: OWLDataRange = None
    ) -> str:
        if range is not None:
            Util.info(
                f"Print DataExactCardinalityRestriction({cardinality} {p} {range})"
            )
        else:
            Util.info(f"Print DataExactCardinalityRestriction({cardinality} {p})")
        return ""

    def get_top_object_property_name(self) -> str:
        Util.info("Write top object property")
        return ""

    def get_bottom_object_property_name(self) -> str:
        Util.info("Write bottom object property")
        return ""

    def get_atomic_object_property_name(self, p: OWLObjectProperty) -> str:
        name: str = self.get_short_name(p)
        Util.info(f"Write object property {name}")
        return ""

    def get_top_data_property_name(self) -> str:
        Util.info("Write top data property")
        return ""

    def get_bottom_data_property_name(self) -> str:
        Util.info("Write bottom data property")
        return ""

    def get_atomic_data_property_name(self, p: OWLDataProperty) -> str:
        name: str = self.get_short_name(p)
        Util.info(f"Write data property {name}")
        return ""

    def write_fuzzy_logic(self, logic: str) -> None:
        Util.info(f"Write fuzzy logic {logic}")

    def write_concept_declaration(self, c: OWLClassExpression) -> None:
        Util.info(f"Write declaration {c}")

    def write_data_property_declaration(self, dp: OWLDataPropertyExpression) -> None:
        Util.info(f"Write declaration {dp}")

    def write_object_property_declaration(
        self, op: OWLObjectPropertyExpression
    ) -> None:
        Util.info(f"Write declaration {op}")

    def write_concept_assertion_axiom(
        self, i: OWLIndividual, c: OWLClassExpression, d: float
    ) -> None:
        Util.info(f"Write axiom {i}: {c} >= {d}")

    def write_object_property_assertion_axiom(
        self,
        i1: OWLIndividual,
        i2: OWLIndividual,
        p: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        Util.info(f"Write axiom ({i1}, {i2}): {p} >= {d}")

    def write_data_property_assertion_axiom(
        self,
        i: OWLIndividual,
        lit: OWLLiteral,
        p: OWLDataPropertyExpression,
        d: float,
    ) -> None:
        Util.info(f"Write axiom ({i}, {lit}): {p} >= {d}")

    def write_negative_object_property_assertion_axiom(
        self,
        i1: OWLIndividual,
        i2: OWLIndividual,
        p: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        Util.info(f"Write axiom ({i1}, {i2}): not {p} >= {d}")

    def write_negative_data_property_assertion_axiom(
        self,
        i: OWLIndividual,
        lit: OWLLiteral,
        p: OWLDataPropertyExpression,
        d: float,
    ) -> None:
        Util.info(f"Write axiom ({i}, {lit}): not {p} >= {d}")

    def write_same_individual_axiom(self, ind_set: set[OWLIndividual]) -> None:
        Util.info(f"Write axiom SameIndividual({ind_set})")

    def write_different_individuals_axiom(self, ind_set: set[OWLIndividual]) -> None:
        Util.info(f"Write axiom DifferentIndividuals({ind_set})")

    def write_disjoint_classes_axiom(self, class_set: set[OWLClassExpression]) -> None:
        Util.info(f"Write axiom DisjointClasses({class_set})")

    def write_disjoint_union_axiom(self, class_set: set[OWLClassExpression]) -> None:
        Util.info(f"Write axiom DisjointUnion({class_set})")

    def write_subclass_of_axiom(
        self, subclass: OWLClassExpression, superclass: OWLClassExpression, d: float
    ) -> None:
        Util.info(
            f"Write axiom SubClassOf({subclass} is subclass of {superclass} >= {d})"
        )

    def write_equivalent_classes_axiom(
        self, class_set: set[OWLClassExpression]
    ) -> None:
        Util.info(f"Write axiom EquivalentClasses({class_set})")

    def write_sub_object_property_of_axiom(
        self,
        subproperty: OWLObjectPropertyExpression,
        superproperty: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        Util.info(
            f"Write axiom SubObjectPropertyOf({subproperty} is subclass of {superproperty} >= {d})"
        )

    def write_sub_data_property_of_axiom(
        self,
        subproperty: OWLDataPropertyExpression,
        superproperty: OWLDataPropertyExpression,
        d: float,
    ) -> None:
        Util.info(
            f"Write axiom SubDataPropertyOf({subproperty} is subclass of {superproperty} >= {d})"
        )

    def write_sub_property_chain_of_axiom(
        self,
        chain: list[OWLObjectPropertyExpression],
        superproperty: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        Util.info(
            f"Write axiom SubPropertyChainOf({chain} is subclass of {superproperty} >= {d})"
        )

    def write_equivalent_object_properties_axiom(
        self, class_set: set[OWLObjectPropertyExpression]
    ) -> None:
        Util.info(f"Write axiom EquivalentObjectProperties({class_set})")

    def write_equivalent_data_properties_axiom(
        self, class_set: set[OWLDataPropertyExpression]
    ) -> None:
        Util.info(f"Write axiom EquivalentDataProperties({class_set})")

    def write_transitive_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        Util.info(f"Write axiom TransitiveObjectProperty({p})")

    def write_symmetric_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        Util.info(f"Write axiom SymmetricObjectProperty({p})")

    def write_asymmetric_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        Util.info(f"Write axiom AsymmetricObjectProperty({p})")

    def write_reflexive_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        Util.info(f"Write axiom ReflexiveObjectProperty({p})")

    def write_irreflexive_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        Util.info(f"Write axiom IrreflexiveObjectProperty({p})")

    def write_functional_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        Util.info(f"Write axiom FunctionalObjectProperty({p})")

    def write_functional_data_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        Util.info(f"Write axiom FunctionalDataProperty({p})")

    def write_inverse_object_property_axiom(
        self, p1: OWLObjectPropertyExpression, p2: OWLObjectPropertyExpression
    ) -> None:
        Util.info(f"Write axiom ({p1} inverse of {p2})")

    def write_inverse_functional_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        Util.info(f"Write axiom InverseFunctionalObjectProperty({p})")

    def write_object_property_domain_axiom(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> None:
        Util.info(f"Write axiom domain ({c} of object property {p})")

    def write_object_property_range_axiom(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> None:
        Util.info(f"Write axiom range ({c} of object property {p})")

    def write_data_property_domain_axiom(
        self, p: OWLDataPropertyExpression, c: OWLClassExpression
    ) -> None:
        Util.info(f"Write axiom domain ({c} of data property {p})")

    def write_data_property_range_axiom(
        self, p: OWLDataPropertyExpression, range: OWLDataRange
    ) -> None:
        Util.info(f"Write axiom range ({range} of data property {p})")

    def write_disjoint_object_properties_axiom(
        self, class_set: set[OWLObjectPropertyExpression]
    ) -> None:
        Util.info(f"Write axiom ({class_set})")

    def write_disjoint_data_properties_axiom(
        self, class_set: set[OWLDataPropertyExpression]
    ) -> None:
        Util.info(f"Write axiom ({class_set})")

    def write_triangular_modifier_definition(
        self, name: str, mod: TriangularModifier
    ) -> None:
        Util.info(f"Write definition {name} = {mod}")

    def write_linear_modifier_definition(self, name: str, mod: LinearModifier) -> None:
        Util.info(f"Write definition {name} = {mod}")

    def write_left_shoulder_function_definition(
        self, name: str, dat: LeftShoulderFunction
    ) -> None:
        Util.info(f"Write definition {name} = {dat}")

    def write_right_shoulder_function_definition(
        self, name: str, dat: RightShoulderFunction
    ) -> None:
        Util.info(f"Write definition {name} = {dat}")

    def write_linear_function_definition(self, name: str, dat: LinearFunction) -> None:
        Util.info(f"Write definition {name} = {dat}")

    def write_triangular_function_definition(
        self, name: str, dat: TriangularFunction
    ) -> None:
        Util.info(f"Write definition {name} = {dat}")

    def write_trapezoidal_function_definition(
        self, name: str, dat: TrapezoidalFunction
    ) -> None:
        Util.info(f"Write definition {name} = {dat}")

    def write_modified_function_definition(
        self, name: str, dat: ModifiedFunction
    ) -> None:
        Util.info(f"Write definition {name} = {dat}")

    def write_modified_property_definition(
        self, name: str, dat: ModifiedProperty
    ) -> None:
        Util.info(f"Write definition {name} = {dat}")

    def write_modified_concept_definition(
        self, name: str, dat: ModifiedConcept
    ) -> None:
        Util.info(f"Write definition {name} = {dat}")

    def write_fuzzy_nominal_concept_definition(
        self, name: str, dat: FuzzyNominalConcept
    ) -> None:
        Util.info(f"Write definition {name} = {dat}")

    def write_weighted_concept_definition(self, name: str, c: WeightedConcept) -> None:
        Util.info(f"Write definition {name} = {c}")

    def write_weighted_max_concept_definition(
        self, name: str, c: WeightedMaxConcept
    ) -> None:
        Util.info(f"Write definition {name} = {c}")

    def write_weighted_min_concept_definition(
        self, name: str, c: WeightedMinConcept
    ) -> None:
        Util.info(f"Write definition {name} = {c}")

    def write_weighted_sum_concept_definition(
        self, name: str, c: WeightedSumConcept
    ) -> None:
        Util.info(f"Write definition {name} = {c}")

    def write_weighted_sum_zero_concept_definition(
        self, name: str, c: WeightedSumZeroConcept
    ) -> None:
        Util.info(f"Write definition {name} = {c}")

    def write_owa_concept_definition(self, name: str, c: OwaConcept) -> None:
        Util.info(f"Write definition {name} = {c}")

    def write_choquet_concept_definition(self, name: str, c: ChoquetConcept) -> None:
        Util.info(f"Write definition {name} = {c}")

    def write_sugeno_concept_definition(self, name: str, c: SugenoConcept) -> None:
        Util.info(f"Write definition {name} = {c}")

    def write_quasi_sugeno_concept_definition(
        self, name: str, c: QsugenoConcept
    ) -> None:
        Util.info(f"Write definition {name} = {c}")

    def write_qowa_concept_definition(self, name: str, c: QowaConcept) -> None:
        Util.info(f"Write definition {name} = {c}")
