import os
import typing

import jpype
import jpype.types
import jpype.imports

if jpype.isJVMStarted():
    jpype.shutdownJVM()

jpype.startJVM(classpath=["./jars/*"])

from java.io import File
from org.semanticweb.owlapi.apibinding import OWLManager
from org.semanticweb.owlapi.model import (
    IRI,
    AxiomType,
    ClassExpressionType,
    DataRangeType,
    OWLAnnotation,
    OWLAnnotationValue,
    OWLAxiom,
    OWLClass,
    OWLClassExpression,
    OWLDataAllValuesFrom,
    OWLDataExactCardinality,
    OWLDataFactory,
    OWLDataHasValue,
    OWLDataIntersectionOf,
    OWLDataMaxCardinality,
    OWLDataMinCardinality,
    OWLDataProperty,
    OWLDataPropertyExpression,
    OWLDataRange,
    OWLDataSomeValuesFrom,
    OWLDatatype,
    OWLDatatypeDefinitionAxiom,
    OWLDatatypeRestriction,
    OWLEntity,
    OWLFacetRestriction,
    OWLIndividual,
    OWLLiteral,
    OWLObjectAllValuesFrom,
    OWLObjectComplementOf,
    OWLObjectExactCardinality,
    OWLObjectHasSelf,
    OWLObjectHasValue,
    OWLObjectIntersectionOf,
    OWLObjectMaxCardinality,
    OWLObjectMinCardinality,
    OWLObjectOneOf,
    OWLObjectProperty,
    OWLObjectPropertyExpression,
    OWLObjectSomeValuesFrom,
    OWLObjectUnionOf,
    OWLOntology,
    OWLOntologyManager,
    OWLProperty,
)
from org.semanticweb.owlapi.util import QNameShortFormProvider
from org.semanticweb.owlapi.vocab import OWLFacet

from fuzzy_reasoner.fuzzydl.util import constants
from fuzzy_reasoner.fuzzydl.util.util import Util
from fuzzy_reasoner.fuzzyowl2.owl_types.choquet_concept import ChoquetConcept
from fuzzy_reasoner.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_reasoner.fuzzyowl2.owl_types.fuzzy_datatype import FuzzyDatatype
from fuzzy_reasoner.fuzzyowl2.owl_types.fuzzy_modifier import FuzzyModifier
from fuzzy_reasoner.fuzzyowl2.owl_types.fuzzy_nominal_concept import FuzzyNominalConcept
from fuzzy_reasoner.fuzzyowl2.owl_types.left_shoulder_function import (
    LeftShoulderFunction,
)
from fuzzy_reasoner.fuzzyowl2.owl_types.linear_function import LinearFunction
from fuzzy_reasoner.fuzzyowl2.owl_types.linear_modifier import LinearModifier
from fuzzy_reasoner.fuzzyowl2.owl_types.modified_concept import ModifiedConcept
from fuzzy_reasoner.fuzzyowl2.owl_types.modified_function import ModifiedFunction
from fuzzy_reasoner.fuzzyowl2.owl_types.modified_property import ModifiedProperty
from fuzzy_reasoner.fuzzyowl2.owl_types.owa_concept import OwaConcept
from fuzzy_reasoner.fuzzyowl2.owl_types.qowa_concept import QowaConcept
from fuzzy_reasoner.fuzzyowl2.owl_types.quasi_sugeno_concept import QsugenoConcept
from fuzzy_reasoner.fuzzyowl2.owl_types.right_shoulder_function import (
    RightShoulderFunction,
)
from fuzzy_reasoner.fuzzyowl2.owl_types.sugeno_concept import SugenoConcept
from fuzzy_reasoner.fuzzyowl2.owl_types.trapezoidal_function import TrapezoidalFunction
from fuzzy_reasoner.fuzzyowl2.owl_types.triangular_function import TriangularFunction
from fuzzy_reasoner.fuzzyowl2.owl_types.triangular_modifer import TriangularModifier
from fuzzy_reasoner.fuzzyowl2.owl_types.weighted_concept import WeightedConcept
from fuzzy_reasoner.fuzzyowl2.owl_types.weighted_max_concept import WeightedMaxConcept
from fuzzy_reasoner.fuzzyowl2.owl_types.weighted_min_concept import WeightedMinConcept
from fuzzy_reasoner.fuzzyowl2.owl_types.weighted_sum_concept import WeightedSumConcept
from fuzzy_reasoner.fuzzyowl2.owl_types.weighted_sum_zero_concept import (
    WeightedSumZeroConcept,
)
from fuzzy_reasoner.fuzzyowl2.parser.owl2_parser import FuzzyOwl2Parser


class FuzzyOwl2(object):
    POS_INFINITY: float = 10000.0
    NEG_INFINITY: float = -POS_INFINITY

    def __init__(
        self,
        input_file: str,
        output_file: str,
        base_iri: str = "http://www.semanticweb.org/ontologies/fuzzydl_ontology.owl",
    ) -> None:
        self.output_dl: str = os.path.join(constants.RESULTS_PATH, output_file)

        self.defined_concepts: dict[str, ConceptDefinition] = dict()
        self.defined_properties: dict[str, ConceptDefinition] = dict()
        self.fuzzy_datatypes: dict[str, ConceptDefinition] = dict()
        self.fuzzy_modifiers: dict[str, ConceptDefinition] = dict()
        self.processed_axioms: set[str] = set()
        self.ontologies: set[OWLOntology] = set()

        FuzzyOwl2Parser.load_config()

        self.ontology_path = base_iri
        self.ontology_iri = IRI.create(base_iri)
        self.manager: OWLOntologyManager = OWLManager.createOWLOntologyManager()
        self.data_factory: OWLDataFactory = self.manager.getOWLDataFactory()
        self.ontology: OWLOntology = self.manager.loadOntologyFromOntologyDocument(
            IRI.create(File(input_file))
        )
        self.fuzzy_label = self.data_factory.getOWLAnnotationProperty(
            IRI.create(f"{self.ontology_iri}#fuzzyLabel")
        )
        # self.pm: SimpleShortFormProvider = SimpleShortFormProvider()
        self.pm: QNameShortFormProvider = QNameShortFormProvider()

        # self.ontology.set_base_iri(self.ontology_path + "#", rename_entities=True)

        self.ontologies.add(self.ontology)
        self.ontologies.update(self.manager.getImportsClosure(self.ontology))

    def get_short_name(self, e: OWLEntity) -> str:
        return self.pm.getShortForm(e)

    def translate_owl2ontology(self) -> None:
        self.process_ontology_annotations()
        self.process_datatype_annotations()
        self.process_concept_annotations()
        self.process_property_annotations()
        self.process_ontology_axioms()

    def process_ontology_annotations(self) -> None:
        for ontology in self.ontologies:
            annotations: set[OWLAnnotation] = ontology.getAnnotations()
            for annotation in annotations:
                if annotation.getProperty() != self.fuzzy_label:
                    continue
                value: OWLAnnotationValue = annotation.getValue()
                annotation_str: str = str(value.getLiteral().replace('"', ""))
                Util.debug(f"Annotation for ontology -> {annotation_str}")
                self.write_fuzzy_logic(FuzzyOwl2Parser.parse_string(annotation_str)[0])

    def __get_facets(self, name: str) -> list[float]:
        facets: list[float] = [float("-inf"), float("inf")]
        for ontology in self.ontologies:
            datatype_def_axioms: set[OWLDatatypeDefinitionAxiom] = ontology.getAxioms(
                AxiomType.DATATYPE_DEFINITION
            )
            if datatype_def_axioms is None:
                continue
            for axiom in datatype_def_axioms:
                datatype_name: str = self.get_short_name(axiom.getDatatype()).replace(
                    ":", ""
                )
                if datatype_name != name:
                    continue
                if (
                    axiom.getDataRange().getDataRangeType()
                    == DataRangeType.DATATYPE_RESTRICTION
                ):
                    facets: list[OWLFacetRestriction] = list(
                        axiom.getDataRange().getFacetRestrictions()
                    )
                    f1: OWLFacetRestriction = facets[0]
                    f2: OWLFacetRestriction = facets[1]
                elif (
                    axiom.getDataRange().getDataRangeType()
                    == DataRangeType.DATA_INTERSECTION_OF
                ):
                    data_range: OWLDataIntersectionOf = typing.cast(
                        OWLDataIntersectionOf, axiom.getDataRange()
                    )
                    operands: list[OWLDataRange] = list(data_range.getOperands())
                    if operands is None or len(operands) != 2:
                        continue
                    r1: OWLDataRange = operands[0]
                    r2: OWLDataRange = operands[1]
                    if not (
                        r1.getDataRangeType() == DataRangeType.DATATYPE_RESTRICTION
                        and r2.getDataRangeType() == DataRangeType.DATATYPE_RESTRICTION
                    ):
                        continue
                    restriction1: OWLDatatypeRestriction = typing.cast(
                        OWLDatatypeRestriction, r1
                    )
                    restriction2: OWLDatatypeRestriction = typing.cast(
                        OWLDatatypeRestriction, r2
                    )
                    facets1: set[OWLFacetRestriction] = (
                        restriction1.getFacetRestrictions()
                    )
                    facets2: set[OWLFacetRestriction] = (
                        restriction2.getFacetRestrictions()
                    )
                    if (
                        facets1 is None
                        or len(facets1) != 1
                        or facets2 is None
                        or len(facets2) != 1
                    ):
                        continue
                    f1: OWLFacetRestriction = list(facets1)[0]
                    f2: OWLFacetRestriction = list(facets2)[0]
                if f1.getFacet() == OWLFacet.MIN_INCLUSIVE:
                    facets[0] = float(str(f1.getFacetValue().getLiteral()))
                elif f1.getFacet() == OWLFacet.MAX_INCLUSIVE:
                    facets[1] = float(str(f1.getFacetValue().getLiteral()))
                if f2.getFacet() == OWLFacet.MIN_INCLUSIVE:
                    facets[0] = float(str(f2.getFacetValue().getLiteral()))
                elif f2.getFacet() == OWLFacet.MAX_INCLUSIVE:
                    facets[1] = float(str(f2.getFacetValue().getLiteral()))
                return facets
        return facets

    def __get_annotation_for_class(
        self, ontology: OWLOntology, cls: OWLClass
    ) -> typing.Generator[typing.Optional[OWLAnnotation], None, None]:
        for axiom in ontology.getAxioms(AxiomType.ANNOTATION_ASSERTION):
            if axiom.getProperty() != self.fuzzy_label:
                continue
            subject = axiom.getSubject()
            try:
                if subject.isIRI() and str(subject.asIRI().get()) == str(cls.getIRI()):
                    yield axiom.getAnnotation()
            except:
                if subject == cls:
                    yield axiom.getAnnotation()
        return None

    def process_datatype_annotations(self) -> None:
        for ontology in self.ontologies:
            for axiom in ontology.getAxioms(AxiomType.DECLARATION):
                entity: OWLEntity = axiom.getEntity()
                if not entity.isOWLDatatype():
                    continue
                Util.debug(f"Datatype for ontology -> {entity}")
                datatype: OWLDatatype = entity.asOWLDatatype()
                annotations: set[OWLAnnotation] = set(
                    self.__get_annotation_for_class(ontology, datatype)
                )
                if annotations is None or len(annotations) == 0:
                    continue
                if len(annotations) > 1:
                    Util.error(
                        f"Error: There are {len(annotations)} datatype annotations for {datatype}"
                    )
                annotation: OWLAnnotation = list(annotations)[0].getValue()
                annotation_str: str = str(annotation.getLiteral().replace('"', ""))
                Util.debug(f"Annotation for {datatype} -> {annotation_str}")
                datatype_name: str = self.get_short_name(datatype)
                facets: list[float] = self.__get_facets(datatype_name)
                c: typing.Union[ConceptDefinition, FuzzyModifier] = (
                    FuzzyOwl2Parser.parse_string(annotation_str)[0]
                )
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
            for axiom in ontology.getAxioms(AxiomType.DECLARATION):
                entity: OWLEntity = axiom.getEntity()
                if not entity.isOWLClass():
                    continue
                cls: OWLClass = entity.asOWLClass()
                Util.debug(f"Concept for ontology -> {cls}")
                annotations: set[OWLAnnotation] = set(
                    self.__get_annotation_for_class(ontology, cls)
                )
                if annotations is None or len(annotations) == 0:
                    continue
                if len(annotations) > 1:
                    Util.error(
                        f"Error: There are {len(annotations)} class annotations for {cls}"
                    )
                annotation: OWLAnnotation = list(annotations)[0].getValue()
                annotation_str: str = str(annotation.getLiteral().replace('"', ""))
                Util.debug(f"Annotation for concept {cls} -> {annotation_str}")
                concept: ConceptDefinition = FuzzyOwl2Parser.parse_string(
                    annotation_str
                )[0]
                Util.debug(f"Concept -> {concept}")
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
            for axiom in ontology.getAxioms(AxiomType.DECLARATION):
                entity: OWLEntity = axiom.getEntity()
                if not (entity.isOWLDataProperty() or entity.isOWLObjectProperty()):
                    continue
                property: OWLProperty = (
                    entity.asOWLObjectProperty()
                    if entity.isOWLObjectProperty()
                    else entity.asOWLDataProperty()
                )
                annotations: set[OWLAnnotation] = set(
                    self.__get_annotation_for_class(ontology, property)
                )
                if annotations is None or len(annotations) == 0:
                    continue
                if len(annotations) > 1:
                    Util.error(
                        f"Error: There are {len(annotations)} property annotations for {property}"
                    )
                annotation: OWLAnnotation = list(annotations)[0].getValue()
                annotation_str: str = str(annotation.getLiteral().replace('"', ""))
                Util.debug(f"Annotation for property {property} -> {annotation_str}")
                prop: typing.Optional[ModifiedProperty] = (
                    FuzzyOwl2Parser.parse_string(annotation_str)
                )[0]
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
        annotations: set[OWLAnnotation] = set(axiom.getAnnotations())
        if annotations is None or len(annotations) == 0:
            return 1.0
        if len(annotations) > 1:
            Util.error(
                f"Error: There are {len(annotations)} annotations for axiom {axiom}."
            )
        annotation: OWLAnnotation = list(annotations)[0].getValue()
        annotation_str: str = str(annotation.getLiteral().replace('"', ""))
        Util.debug(f"Annotation for degree -> {annotation_str}")
        deg: float = FuzzyOwl2Parser.parse_string(annotation_str)[0]
        Util.debug(f"Degree for axiom -> {deg}")
        if not isinstance(deg, float):
            raise ValueError
        return deg

    def __write_subclass_of_axiom(
        self, ontology: OWLOntology, annotated: bool = True
    ) -> None:
        for axiom in ontology.getAxioms(AxiomType.SUBCLASS_OF):
            subclass: OWLClassExpression = axiom.getSubClass()
            superclass: OWLClassExpression = axiom.getSuperClass()
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
        for axiom in ontology.getAxioms(AxiomType.SUB_OBJECT_PROPERTY):
            sub_property: OWLObjectPropertyExpression = axiom.getSubProperty()
            super_property: OWLObjectPropertyExpression = axiom.getSuperProperty()
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
        for axiom in ontology.getAxioms(AxiomType.SUB_DATA_PROPERTY):
            sub_property: OWLDataPropertyExpression = axiom.getSubProperty()
            super_property: OWLDataPropertyExpression = axiom.getSuperProperty()
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
        for axiom in ontology.getAxioms(AxiomType.SUB_PROPERTY_CHAIN_OF):
            chain: list[OWLObjectPropertyExpression] = axiom.getPropertyChain()
            super_property: OWLDataPropertyExpression = axiom.getSuperProperty()
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
        for axiom in ontology.getAxioms(AxiomType.CLASS_ASSERTION):
            cls: OWLClassExpression = axiom.getClassExpression()
            ind: OWLIndividual = axiom.getIndividual()
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
        for axiom in ontology.getAxioms(AxiomType.OBJECT_PROPERTY_ASSERTION):
            ind1: OWLIndividual = axiom.getSubject()
            ind2: OWLIndividual = axiom.getObject()
            prop: OWLObjectPropertyExpression = axiom.getProperty()
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
        for axiom in ontology.getAxioms(AxiomType.DATA_PROPERTY_ASSERTION):
            ind1: OWLIndividual = axiom.getSubject()
            ind2: OWLIndividual = axiom.getObject()
            prop: OWLDataPropertyExpression = axiom.getProperty()
            degree: float = self.__get_degree(axiom)
            if annotated:
                if degree != 1.0:
                    Util.debug(f"Data property assertion axiom -> {axiom}")
                    self.write_data_property_assertion_axiom(ind1, ind2, prop, degree)
                    self.processed_axioms.add(f"({ind1}, {ind2}):{prop}")
            else:
                if (
                    degree == 1.0
                    and f"({ind1}, {ind2}):{prop}" not in self.processed_axioms
                ):
                    Util.debug(
                        f"Not annotated data property assertion axiom -> {axiom}"
                    )
                    self.processed_axioms.add(f"({ind1}, {ind2}):{prop}")
                    self.write_data_property_assertion_axiom(ind1, ind2, prop, degree)

    def __write_negative_object_property_assertion_axiom(
        self, ontology: OWLOntology, annotated: bool = True
    ) -> None:
        for axiom in ontology.getAxioms(AxiomType.NEGATIVE_OBJECT_PROPERTY_ASSERTION):
            ind1: OWLIndividual = axiom.getSubject()
            ind2: OWLIndividual = axiom.getObject()
            prop: OWLObjectPropertyExpression = axiom.getProperty()
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
        for axiom in ontology.getAxioms(AxiomType.NEGATIVE_DATA_PROPERTY_ASSERTION):
            ind1: OWLIndividual = axiom.getSubject()
            ind2: OWLIndividual = axiom.getObject()
            prop: OWLDataPropertyExpression = axiom.getProperty()
            degree: float = self.__get_degree(axiom)
            if annotated:
                if degree != 1.0:
                    Util.debug(f"Negative data property assertion axiom -> {axiom}")
                    self.write_negative_data_property_assertion_axiom(
                        ind1, ind2, prop, degree
                    )
                    self.processed_axioms.add(f"({ind1}, {ind2}):not {prop}")
            else:
                if (
                    degree == 1.0
                    and f"({ind1}, {ind2}):not {prop}" not in self.processed_axioms
                ):
                    Util.debug(
                        f"Not annotated negative data property assertion axiom -> {axiom}"
                    )
                    self.processed_axioms.add(f"({ind1}, {ind2}):not {prop}")
                    self.write_negative_data_property_assertion_axiom(
                        ind1, ind2, prop, degree
                    )

    def process_ontology_axioms(self) -> None:
        for ontology in self.ontologies:
            # ########
            #  TBox
            # ########
            for axiom in ontology.getAxioms(AxiomType.DISJOINT_CLASSES):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Disjoint axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_disjoint_classes_axiom(axiom.getClassExpressions())
            for axiom in ontology.getAxioms(AxiomType.DISJOINT_UNION):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Disjoint union axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_disjoint_union_axiom(axiom.getClassExpressions())
            self.__write_subclass_of_axiom(ontology, annotated=True)
            for axiom in ontology.getAxioms(AxiomType.EQUIVALENT_CLASSES):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Equivalent classes axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_equivalent_classes_axiom(axiom.getClassExpressions())
            for cls in ontology.getClassesInSignature():
                if not cls.isTopEntity() and str(cls) not in self.processed_axioms:
                    Util.debug(f"Concept declaration axiom -> {cls}")
                    self.processed_axioms.add(str(cls))
                    self.write_concept_declaration(cls)
            # ########
            #  RBox
            # ########
            self.__write_subobject_property_axiom(ontology, annotated=True)
            self.__write_subdata_property_axiom(ontology, annotated=True)
            self.__write_subproperty_chain_of_axiom(ontology, annotated=True)
            for axiom in ontology.getAxioms(AxiomType.EQUIVALENT_OBJECT_PROPERTIES):
                Util.debug(f"Equivalent object properties axiom -> {axiom}")
                if str(axiom) not in self.processed_axioms:
                    self.processed_axioms.add(str(axiom))
                    self.write_equivalent_object_properties_axiom(axiom.getProperties())
            for axiom in ontology.getAxioms(AxiomType.EQUIVALENT_DATA_PROPERTIES):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Equivalent data properties axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_equivalent_data_properties_axiom(axiom.getProperties())
            for axiom in ontology.getAxioms(AxiomType.TRANSITIVE_OBJECT_PROPERTY):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Transitive object property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_transitive_object_property_axiom(axiom.getProperty())
            for axiom in ontology.getAxioms(AxiomType.SYMMETRIC_OBJECT_PROPERTY):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Symmetric object property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_symmetric_object_property_axiom(axiom.getProperty())
            for axiom in ontology.getAxioms(AxiomType.ASYMMETRIC_OBJECT_PROPERTY):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Asymmetric object property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_asymmetric_object_property_axiom(axiom.getProperty())
            for axiom in ontology.getAxioms(AxiomType.REFLEXIVE_OBJECT_PROPERTY):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Reflexive object property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_reflexive_object_property_axiom(axiom.getProperty())
            for axiom in ontology.getAxioms(AxiomType.IRREFLEXIVE_OBJECT_PROPERTY):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Irreflexive object property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_irreflexive_object_property_axiom(axiom.getProperty())
            for axiom in ontology.getAxioms(AxiomType.FUNCTIONAL_OBJECT_PROPERTY):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Functional object property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_functional_object_property_axiom(axiom.getProperty())
            for axiom in ontology.getAxioms(AxiomType.FUNCTIONAL_DATA_PROPERTY):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Functional data property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_functional_data_property_axiom(axiom.getProperty())
            for axiom in ontology.getAxioms(AxiomType.INVERSE_OBJECT_PROPERTIES):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Inverse object properties axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_inverse_object_property_axiom(
                        axiom.getFirstProperty(), axiom.getSecondProperty()
                    )
            for axiom in ontology.getAxioms(
                AxiomType.INVERSE_FUNCTIONAL_OBJECT_PROPERTY
            ):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Inverse functional object property axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_inverse_functional_object_property_axiom(
                        axiom.getProperty()
                    )
            for axiom in ontology.getAxioms(AxiomType.OBJECT_PROPERTY_DOMAIN):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Object property domain axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_object_property_domain_axiom(
                        axiom.getProperty(), axiom.getDomain()
                    )
            for axiom in ontology.getAxioms(AxiomType.OBJECT_PROPERTY_RANGE):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Object property range axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_object_property_range_axiom(
                        axiom.getProperty(), axiom.getRange()
                    )
            for axiom in ontology.getAxioms(AxiomType.DATA_PROPERTY_DOMAIN):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Data property domain axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_data_property_domain_axiom(
                        axiom.getProperty(), axiom.getDomain()
                    )
            for axiom in ontology.getAxioms(AxiomType.DATA_PROPERTY_RANGE):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Data property range axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_data_property_range_axiom(
                        axiom.getProperty(), axiom.getRange()
                    )
            for axiom in ontology.getAxioms(AxiomType.DISJOINT_OBJECT_PROPERTIES):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Disjoint object properties axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_disjoint_object_properties_axiom(axiom.getProperties())
            for axiom in ontology.getAxioms(AxiomType.DISJOINT_DATA_PROPERTIES):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Disjoint data properties axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_disjoint_data_properties_axiom(axiom.getProperties())
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
            for axiom in ontology.getAxioms(AxiomType.SAME_INDIVIDUAL):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Same individual axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_same_individual_axiom(axiom.getIndividuals())
            for axiom in ontology.getAxioms(AxiomType.DIFFERENT_INDIVIDUALS):
                if str(axiom) not in self.processed_axioms:
                    Util.debug(f"Different individuals axiom -> {axiom}")
                    self.processed_axioms.add(str(axiom))
                    self.write_different_individuals_axiom(axiom.getIndividuals())
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
        c_type: ClassExpressionType = c.getClassExpressionType()
        if c_type == ClassExpressionType.OWL_CLASS:
            d: OWLClass = typing.cast(OWLClass, c)
            if d.isOWLThing():
                return self.get_top_concept_name()
            if d.isOWLNothing():
                return self.get_bottom_concept_name()
            return self.get_atomic_concept_name(d)
        elif c_type == ClassExpressionType.OBJECT_INTERSECTION_OF:
            operands: OWLObjectIntersectionOf = typing.cast(
                OWLObjectIntersectionOf, c
            ).getOperands()
            return self.get_object_intersection_of_name(operands)
        elif c_type == ClassExpressionType.OBJECT_UNION_OF:
            operands: OWLObjectUnionOf = typing.cast(OWLObjectUnionOf, c).getOperands()
            return self.get_object_union_of_name(operands)
        elif c_type == ClassExpressionType.OBJECT_SOME_VALUES_FROM:
            some: OWLObjectSomeValuesFrom = typing.cast(OWLObjectSomeValuesFrom, c)
            return self.get_object_some_values_from_name(
                some.getProperty(), some.getFiller()
            )
        elif c_type == ClassExpressionType.OBJECT_ALL_VALUES_FROM:
            all: OWLObjectAllValuesFrom = typing.cast(OWLObjectAllValuesFrom, c)
            return self.get_object_all_values_from_name(
                all.getProperty(), all.getFiller()
            )
        elif c_type == ClassExpressionType.DATA_SOME_VALUES_FROM:
            some: OWLDataSomeValuesFrom = typing.cast(OWLDataSomeValuesFrom, c)
            return self.get_data_some_values_from_name(
                some.getProperty(), some.getFiller()
            )
        elif c_type == ClassExpressionType.DATA_ALL_VALUES_FROM:
            all: OWLDataAllValuesFrom = typing.cast(OWLDataAllValuesFrom, c)
            return self.get_data_all_values_from_name(
                all.getProperty(), all.getFiller()
            )
        elif c_type == ClassExpressionType.OBJECT_COMPLEMENT_OF:
            complement: OWLObjectComplementOf = typing.cast(OWLObjectComplementOf, c)
            return self.get_object_complement_of_name(complement.getOperand())
        elif c_type == ClassExpressionType.OBJECT_HAS_SELF:
            has_self: OWLObjectHasSelf = typing.cast(OWLObjectHasSelf, c)
            return self.get_object_has_self_name(has_self.getProperty())
        elif c_type == ClassExpressionType.OBJECT_ONE_OF:
            one_of: OWLObjectOneOf = typing.cast(OWLObjectOneOf, c)
            return self.get_object_one_of_name(one_of.getIndividuals())
        elif c_type == ClassExpressionType.OBJECT_HAS_VALUE:
            has_value: OWLObjectHasValue = typing.cast(OWLObjectHasValue, c)
            return self.get_object_has_value_name(
                has_value.getProperty(), has_value.getValue()
            )
        elif c_type == ClassExpressionType.DATA_HAS_VALUE:
            has_value: OWLDataHasValue = typing.cast(OWLDataHasValue, c)
            return self.get_data_has_value_name(
                has_value.getProperty(), has_value.getValue()
            )
        elif c_type == ClassExpressionType.OBJECT_MIN_CARDINALITY:
            min_card: OWLObjectMinCardinality = typing.cast(OWLObjectMinCardinality, c)
            if min_card.isQualified():
                return self.get_object_min_cardinality_restriction(
                    min_card.getCardinality(),
                    min_card.getProperty(),
                    min_card.getFiller(),
                )
            else:
                return self.get_object_min_cardinality_restriction(
                    min_card.getCardinality(), min_card.getProperty()
                )
        elif c_type == ClassExpressionType.OBJECT_MAX_CARDINALITY:
            max_card: OWLObjectMaxCardinality = typing.cast(OWLObjectMaxCardinality, c)
            if max_card.isQualified():
                return self.get_object_max_cardinality_restriction(
                    max_card.getCardinality(),
                    max_card.getProperty(),
                    max_card.getFiller(),
                )
            else:
                return self.get_object_max_cardinality_restriction(
                    max_card.getCardinality(), max_card.getProperty()
                )
        elif c_type == ClassExpressionType.OBJECT_EXACT_CARDINALITY:
            exact_card: OWLObjectExactCardinality = typing.cast(
                OWLObjectExactCardinality, c
            )
            if exact_card.isQualified():
                return self.get_object_exact_cardinality_restriction(
                    exact_card.getCardinality(),
                    exact_card.getProperty(),
                    exact_card.getFiller(),
                )
            else:
                return self.get_object_exact_cardinality_restriction(
                    exact_card.getCardinality(), exact_card.getProperty()
                )
        elif c_type == ClassExpressionType.DATA_MIN_CARDINALITY:
            min_card: OWLDataMinCardinality = typing.cast(OWLDataMinCardinality, c)
            if min_card.isQualified():
                return self.get_data_min_cardinality_restriction(
                    min_card.getCardinality(),
                    min_card.getProperty(),
                    min_card.getFiller(),
                )
            else:
                return self.get_data_min_cardinality_restriction(
                    min_card.getCardinality(), min_card.getProperty()
                )
        elif c_type == ClassExpressionType.DATA_MAX_CARDINALITY:
            max_card: OWLDataMaxCardinality = typing.cast(OWLDataMaxCardinality, c)
            if max_card.isQualified():
                return self.get_data_max_cardinality_restriction(
                    max_card.getCardinality(),
                    max_card.getProperty(),
                    max_card.getFiller(),
                )
            else:
                return self.get_data_max_cardinality_restriction(
                    max_card.getCardinality(), max_card.getProperty()
                )
        elif c_type == ClassExpressionType.DATA_EXACT_CARDINALITY:
            exact_card: OWLDataExactCardinality = typing.cast(
                OWLDataExactCardinality, c
            )
            if exact_card.isQualified():
                return self.get_data_exact_cardinality_restriction(
                    exact_card.getCardinality(),
                    exact_card.getProperty(),
                    exact_card.getFiller(),
                )
            else:
                return self.get_data_exact_cardinality_restriction(
                    exact_card.getCardinality(), exact_card.getProperty()
                )
        else:
            raise ValueError

    def get_object_property_name(self, p: OWLObjectPropertyExpression) -> str:
        if p.isOWLTopObjectProperty():
            return self.get_top_object_property_name()
        elif p.isOWLBottomObjectProperty():
            return self.get_bottom_object_property_name()
        else:
            return self.get_atomic_object_property_name(p.asOWLObjectProperty())

    def get_data_property_name(self, p: OWLDataPropertyExpression) -> str:
        if p.isOWLTopDataProperty():
            return self.get_top_data_property_name()
        elif p.isOWLBottomDataProperty():
            return self.get_bottom_data_property_name()
        else:
            return self.get_atomic_data_property_name(p.asOWLDataProperty())

    def get_individual_name(self, i: OWLIndividual) -> typing.Optional[str]:
        if i.isAnonymous():
            Util.info(f"Anonymous individual not supported")
            return None
        else:
            name: str = self.get_short_name(i.asOWLNamedIndividual())
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
        i1: OWLIndividual,
        i2: OWLIndividual,
        p: OWLDataPropertyExpression,
        d: float,
    ) -> None:
        Util.info(f"Write axiom ({i1}, {i2}): {p} >= {d}")

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
        i1: OWLIndividual,
        i2: OWLIndividual,
        p: OWLDataPropertyExpression,
        d: float,
    ) -> None:
        Util.info(f"Write axiom ({i1}, {i2}): not {p} >= {d}")

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
