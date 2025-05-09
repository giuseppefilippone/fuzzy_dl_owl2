from __future__ import annotations

import os
import pathlib
import sys
import typing
from functools import partial

import jpype
import jpype.types
import jpype.imports

if jpype.isJVMStarted():
    jpype.shutdownJVM()
jpype.startJVM(classpath=["./jars/*"])

from org.semanticweb.owlapi.apibinding import OWLManager
from org.semanticweb.owlapi.model import (
    IRI,
    AddAxiom,
    AddOntologyAnnotation,
    OWLAnnotation,
    OWLAnnotationAssertionAxiom,
    OWLAxiom,
    OWLClass,
    OWLClassAssertionAxiom,
    OWLClassExpression,
    OWLDataFactory,
    OWLDataIntersectionOf,
    OWLDataProperty,
    OWLDataPropertyAssertionAxiom,
    OWLDataRange,
    OWLDatatype,
    OWLDatatypeDefinitionAxiom,
    OWLDatatypeRestriction,
    OWLEntity,
    OWLLiteral,
    OWLNamedIndividual,
    OWLObjectProperty,
    OWLObjectPropertyAssertionAxiom,
    OWLOntology,
    OWLOntologyManager,
    OWLSubClassOfAxiom,
)
from org.semanticweb.owlapi.vocab import OWLFacet
from rdflib import RDF, XSD

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
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType, ConcreteFeatureType
from fuzzy_dl_owl2.fuzzydl.util.util import Util
from fuzzy_dl_owl2.fuzzyowl2.util.constants import FuzzyOWL2Keyword


class FuzzydlToOwl2:

    def __init__(
        self,
        input_file: str,
        output_file: str,
        base_iri: str = "http://www.semanticweb.org/ontologies/fuzzydl_ontology.owl",
    ) -> None:
        self.num_classes: int = 0
        self.kb, _ = DLParser.get_kb(input_file)
        self.ontology_path = base_iri
        self.ontology_iri = IRI.create(base_iri)
        self.manager: OWLOntologyManager = OWLManager.createOWLOntologyManager()
        self.data_factory: OWLDataFactory = self.manager.getOWLDataFactory()
        self.ontology: OWLOntology = self.manager.createOntology(self.ontology_iri)
        self.fuzzyLabel = self.data_factory.getOWLAnnotationProperty(
            IRI.create(f"{self.ontology_iri}#fuzzyLabel")
        )

        self.concepts: dict[str, OWLClassExpression] = dict()
        self.datatypes: dict[str, OWLDatatype] = dict()
        self.modifiers: dict[str, OWLDatatype] = dict()
        self.input_FDL: str = input_file
        self.output_FOWL: str = os.path.join(constants.RESULTS_PATH, output_file)

    def iri(self, o: object) -> str:
        """Convert object to IRI string"""
        return IRI.create(f"{self.ontology_path}#{str(o)}")

    def get_base(self, c: Concept) -> OWLClassExpression:
        if c.is_atomic():
            return self.get_class(str(c)).asOWLClass()
        return self.get_new_atomic_class(str(c))

    @typing.overload
    def get_class(self, name: str) -> OWLClassExpression: ...

    @typing.overload
    def get_class(self, c: Concept) -> OWLClassExpression: ...

    def get_class(self, *args) -> OWLClassExpression:
        assert len(args) == 1
        if isinstance(args[0], str):
            return self.__get_class_1(*args)
        elif isinstance(args[0], Concept):
            return self.__get_class_2(*args)
        else:
            raise ValueError

    def __get_class_1(self, name: str) -> OWLClassExpression:
        """Get or create an OWL class by name"""
        return self.data_factory.getOWLClass(self.iri(name))

    def __get_class_2(self, c: Concept) -> OWLClassExpression:
        Util.debug(f"Getting class for concept -> {c}")
        c_type: ConceptType = c.type
        if c_type in (ConceptType.ATOMIC, ConceptType.CONCRETE):
            return self.get_class(str(c))
        elif c_type == ConceptType.TOP:
            return self.data_factory.getOWLThing()
        elif c_type == ConceptType.BOTTOM:
            return self.data_factory.getOWLNothing()
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
            return self.data_factory.getOWLObjectComplementOf(self.get_class(-c))
        elif c_type in (
            ConceptType.AND,
            ConceptType.GOEDEL_AND,
            ConceptType.LUKASIEWICZ_AND,
        ):
            c: OperatorConcept = typing.cast(OperatorConcept, c)
            return self.data_factory.getOWLObjectIntersectionOf(
                {self.get_class(c1) for c1 in c.concepts}
            )
        elif c_type in (
            ConceptType.OR,
            ConceptType.GOEDEL_OR,
            ConceptType.LUKASIEWICZ_OR,
        ):
            c: OperatorConcept = typing.cast(OperatorConcept, c)
            return self.data_factory.getOWLObjectUnionOf(
                {self.get_class(c1) for c1 in c.concepts}
            )
        elif c_type == ConceptType.SOME:
            c: AllSomeConcept = typing.cast(AllSomeConcept, c)
            if str(c.curr_concept) in self.datatypes:
                dp: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_data_property(c.role)
                )
                assert isinstance(dp, OWLDataProperty)
                d: OWLDatatype = self.datatypes.get(str(c.curr_concept))
                return self.data_factory.getOWLDataSomeValuesFrom(dp, d)
            else:
                op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_object_property(c.role)
                )
                assert isinstance(op, OWLObjectProperty)
                c2: OWLClassExpression = self.get_class(c.curr_concept)
                return self.data_factory.getOWLObjectSomeValuesFrom(op, c2)
        elif c_type == ConceptType.ALL:
            c: AllSomeConcept = typing.cast(AllSomeConcept, c)
            if str(c.curr_concept) in self.datatypes:
                dp: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_data_property(c.role)
                )
                assert isinstance(dp, OWLDataProperty)
                d: OWLDatatype = self.datatypes.get(str(c.curr_concept))
                return self.data_factory.getOWLDataAllValuesFrom(dp, d)
            else:
                op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_object_property(c.role)
                )
                assert isinstance(op, OWLObjectProperty)
                c2: OWLClassExpression = self.get_class(c.curr_concept)
                return self.data_factory.getOWLObjectAllValuesFrom(op, c2)
        elif c_type == ConceptType.MODIFIED:
            c: ModifiedConcept = typing.cast(ModifiedConcept, c)
            if str(c) in self.concepts:
                return self.concepts.get(str(c))
            c4: OWLClassExpression = self.get_new_atomic_class(str(c))
            c3: OWLClassExpression = self.get_base(c.c1)
            self.concepts[str(c)] = c3
            annotation: str = (
                f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.CONCEPT.get_str_value()}">\n',
                f'\t<{FuzzyOWL2Keyword.CONCEPT.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{FuzzyOWL2Keyword.MODIFIED.get_str_value()}" {FuzzyOWL2Keyword.MODIFIER.get_str_value()}="{self.modifiers[str(c)]}" {FuzzyOWL2Keyword.BASE.get_str_value()}="{c3}"/>\n',
                f"</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>",
            )
            self.add_entity_annotation(annotation, c4)
            return c4
        elif c_type == ConceptType.SELF:
            c: SelfConcept = typing.cast(SelfConcept, c)
            owl_obj_property: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(c.role)
            )
            if isinstance(owl_obj_property, OWLObjectProperty):
                return self.data_factory.getOWLObjectHasSelf(owl_obj_property)
            else:
                return self.data_factory.getOWLDataHasSelf(owl_obj_property)
        elif c_type == ConceptType.HAS_VALUE:
            c: HasValueConcept = typing.cast(HasValueConcept, c)
            owl_obj_property: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(c.role)
            )
            assert isinstance(owl_obj_property, OWLObjectProperty)
            ind: OWLNamedIndividual = self.get_individual(str(c.value))
            return self.data_factory.getOWLObjectHasValue(owl_obj_property, ind)
        elif c_type in (
            ConceptType.AT_MOST_VALUE,
            ConceptType.AT_LEAST_VALUE,
            ConceptType.EXACT_VALUE,
        ):
            c: ValueConcept = typing.cast(ValueConcept, c)
            if isinstance(c.value, int):
                datatype: OWLDatatype = self.data_factory.getIntegerOWLDatatype()
                literal: OWLLiteral = self.data_factory.getOWLLiteral(
                    jpype.types.JInt(c.value)
                )
            elif isinstance(c.value, float):
                datatype: OWLDatatype = self.data_factory.getOWLDatatype(
                    IRI.create(XSD.decimal)
                )
                literal: OWLLiteral = self.data_factory.getOWLLiteral(
                    str(c.value), datatype
                )
            elif isinstance(c.value, str):
                datatype: OWLDatatype = self.data_factory.getRDFPlainLiteral()
                literal: OWLLiteral = self.data_factory.getOWLLiteral(
                    jpype.types.JString(c.value)
                )
            if c_type == ConceptType.AT_LEAST_VALUE:
                data_range: OWLDataRange = self.data_factory.getOWLDatatypeRestriction(
                    datatype, OWLFacet.MIN_INCLUSIVE, literal
                )
                return self.data_factory.getOWLDataSomeValuesFrom(
                    self.get_data_property(c.role), data_range
                )
            elif c_type == ConceptType.AT_MOST_VALUE:
                data_range: OWLDataRange = self.data_factory.getOWLDatatypeRestriction(
                    datatype, OWLFacet.MAX_INCLUSIVE, literal
                )
                return self.data_factory.getOWLDataSomeValuesFrom(
                    self.get_data_property(c.role), data_range
                )
            else:
                return self.data_factory.getOWLDataHasValue(
                    self.get_data_property(c.role), literal
                )
        elif c_type == ConceptType.WEIGHTED:
            c: WeightedConcept = typing.cast(WeightedConcept, c)
            c4: OWLClassExpression = self.get_new_atomic_class(str(c))
            c3: OWLClassExpression = self.get_base(c.c1)
            annotation: str = (
                f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.CONCEPT.get_str_value()}">\n',
                f'\t<{FuzzyOWL2Keyword.CONCEPT.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{FuzzyOWL2Keyword.WEIGHTED.get_str_value()}" {FuzzyOWL2Keyword.DEGREE_VALUE.get_str_value()}="{c.weight}" {FuzzyOWL2Keyword.BASE.get_str_value()}="{c3}"/>\n',
                f"</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>",
            )
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
            ConceptType.QUANTIFIED_OWA,
            ConceptType.CHOQUET_INTEGRAL,
            ConceptType.SUGENO_INTEGRAL,
            ConceptType.QUASI_SUGENO_INTEGRAL,
        ):
            return self.__get_class_weighted(c)
        return self.data_factory.getOWLClass(self.iri(str(c)))

    def __get_class_weighted_min_max_sum(self, c: Concept) -> OWLClassExpression:
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

        annotation: str = (
            f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.CONCEPT.get_str_value()}">\n',
            f'\t<{FuzzyOWL2Keyword.CONCEPT.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{type_dict[c.type]}">\n ',
        )
        for i in range(len(curr_concept.concepts)):
            c5: OWLClassExpression = self.get_base(curr_concept.concepts[i])
            annotation += f'\t\t<{FuzzyOWL2Keyword.CONCEPT.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{FuzzyOWL2Keyword.WEIGHTED.get_str_value()}" {FuzzyOWL2Keyword.DEGREE_VALUE.get_str_value()}="{curr_concept.weights[i]}" {FuzzyOWL2Keyword.BASE.get_str_value()}="{c5}" />\n'
        annotation: str = (
            f"\t</{FuzzyOWL2Keyword.CONCEPT.get_tag_name()} >\n</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} >"
        )
        self.add_entity_annotation(annotation, c3)
        return c3

    def __get_class_weighted(self, c: Concept) -> OWLClassExpression:
        type_dict: dict[ConceptType, str] = {
            ConceptType.OWA: FuzzyOWL2Keyword.OWA.get_str_value(),
            ConceptType.QUANTIFIED_OWA: FuzzyOWL2Keyword.Q_OWA.get_str_value(),
            ConceptType.CHOQUET_INTEGRAL: FuzzyOWL2Keyword.CHOQUET.get_str_value(),
            ConceptType.SUGENO_INTEGRAL: FuzzyOWL2Keyword.SUGENO.get_str_value(),
            ConceptType.QUASI_SUGENO_INTEGRAL: FuzzyOWL2Keyword.QUASI_SUGENO.get_str_value(),
        }
        type_cast: dict[ConceptType, typing.Callable] = {
            ConceptType.OWA: partial(typing.cast, OwaConcept),
            ConceptType.QUANTIFIED_OWA: partial(typing.cast, QowaConcept),
            ConceptType.CHOQUET_INTEGRAL: partial(typing.cast, ChoquetIntegral),
            ConceptType.SUGENO_INTEGRAL: partial(typing.cast, SugenoIntegral),
            ConceptType.QUASI_SUGENO_INTEGRAL: partial(typing.cast, QsugenoIntegral),
        }
        if c.type not in type_dict:
            return None
        curr_concept: HasWeightedConceptsInterface = type_cast[c.type](c)
        c4: OWLClassExpression = self.get_new_atomic_class(str(c))
        annotation: str = (
            f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.CONCEPT.get_str_value()}">\n',
            f'\t<{FuzzyOWL2Keyword.CONCEPT.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{type_dict[c.type]}">\n',
            f"\t\t<{FuzzyOWL2Keyword.WEIGHTS.get_tag_name()}>\n",
        )
        for d in curr_concept.weights:
            annotation += f"\t\t\t<{FuzzyOWL2Keyword.WEIGHT.get_tag_name()}>{d}</{FuzzyOWL2Keyword.WEIGHT.get_tag_name()}>\n"
        annotation += f"\t\t</{FuzzyOWL2Keyword.WEIGHTS.get_tag_name()}>\n\t\t<{FuzzyOWL2Keyword.CONCEPT_NAMES.get_tag_name()}>\n"
        for ci in curr_concept.concepts:
            c5: OWLClassExpression = self.get_base(ci)
            annotation += f"\t\t\t<{FuzzyOWL2Keyword.NAME.get_tag_name()}>{c5}</{FuzzyOWL2Keyword.NAME.get_tag_name()}>\n"
        annotation += f"\t\t</{FuzzyOWL2Keyword.CONCEPT_NAMES.get_tag_name()}>\n\t</{FuzzyOWL2Keyword.CONCEPT.get_tag_name()}>\n</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>"
        self.add_entity_annotation(annotation, c4)
        return c4

    def get_new_atomic_class(self, name: str) -> OWLClassExpression:
        """Get or create a new atomic class"""
        Util.debug(f"Getting new atomic concept -> {name}")
        c = self.concepts.get(name)
        if c is not None:
            return c

        self.num_classes += 1
        Util.debug(f"Creating new atomic concept -> {name}")
        c2: OWLClass = self.data_factory.getOWLClass(
            self.iri(f"class__{self.num_classes}")
        )
        self.concepts[name] = c2
        return c2

    def exist_object_property(self, role: str) -> bool:
        return any(
            prop.getIRI().equals(self.iri(role))
            for prop in self.ontology.getObjectPropertiesInSignature()
        )

    def exist_data_property(self, role: str) -> bool:
        return any(
            prop.getIRI().equals(self.iri(role))
            for prop in self.ontology.getDataPropertiesInSignature()
        )

    def get_object_property(
        self, role: str
    ) -> typing.Union[OWLDataProperty, OWLObjectProperty]:
        """Get or create an object property"""
        Util.debug(f"Getting object property -> {role}")
        if self.exist_data_property(role):
            return self.get_data_property(role)
        return self.data_factory.getOWLObjectProperty(self.iri(role))

    def get_data_property(
        self, role: str
    ) -> typing.Union[OWLDataProperty, OWLObjectProperty]:
        """Get or create a data property"""
        Util.debug(f"Getting data property -> {role}")
        if self.exist_object_property(role):
            return self.get_object_property(role)
        return self.data_factory.getOWLDataProperty(self.iri(role))

    def get_individual(self, name: str) -> OWLNamedIndividual:
        """Get or create a named individual"""
        Util.debug(f"Getting individual -> {name}")
        return self.data_factory.getOWLNamedIndividual(self.iri(f"{name}_Individual"))

    def add_ontology_annotation(self, annotation: str) -> None:
        """Add annotation to the ontology"""
        Util.debug(f"Adding annotation to ontology -> {annotation}")
        comment: OWLAnnotation = self.data_factory.getOWLAnnotation(
            self.fuzzyLabel,
            self.data_factory.getOWLLiteral(
                annotation,
                self.data_factory.getOWLDatatype(IRI.create(str(RDF.PlainLiteral))),
            ),
        )
        ann: AddOntologyAnnotation = AddOntologyAnnotation(self.ontology, comment)
        self.manager.applyChange(ann)

    def add_entity_annotation(self, annotation: str, entity: OWLEntity) -> None:
        """Add annotation to an entity"""
        # define_datatype_in_ontology(entity, self.iri(entity), self.ontology)
        Util.debug(f"Adding annotation to entity {entity} -> {annotation}")
        owl_annotation: OWLAnnotation = self.data_factory.getOWLAnnotation(
            self.fuzzyLabel,
            self.data_factory.getOWLLiteral(
                annotation,
                self.data_factory.getOWLDatatype(IRI.create(str(RDF.PlainLiteral))),
            ),
        )
        axiom: OWLAnnotationAssertionAxiom = (
            self.data_factory.getOWLAnnotationAssertionAxiom(
                entity.getIRI(), owl_annotation
            )
        )
        self.manager.applyChange(AddAxiom(self.ontology, axiom))

    def get_annotations_for_axiom(
        self, value: typing.Union[float, DegreeNumeric]
    ) -> set[OWLAnnotation]:
        """Get annotations for an axiom with degree"""
        if isinstance(value, float):
            n = value
        elif isinstance(value, DegreeNumeric):  # Degree object
            n = value.get_numerical_value()

        annotation_text: str = (
            f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.AXIOM.get_str_value()}">\n'
            f'\t<{FuzzyOWL2Keyword.DEGREE_DEF.get_tag_name()} {FuzzyOWL2Keyword.DEGREE_VALUE.get_str_value()}="{n}"/>\n'
            f"</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>"
        )
        annotation: OWLAnnotation = self.data_factory.getOWLAnnotation(
            self.fuzzyLabel,
            self.data_factory.getOWLLiteral(
                annotation_text,
                self.data_factory.getOWLDatatype(IRI.create(str(RDF.PlainLiteral))),
            ),
        )
        return set([annotation])

    def annotate_gci(self, gci: GeneralConceptInclusion) -> None:
        c1: OWLClassExpression = self.get_class(gci.get_subsumed())
        c2: OWLClassExpression = self.get_class(gci.get_subsumer())
        deg: Degree = gci.get_degree()
        Util.debug(f"Annotate GCI -> {c1} - {c2} - {deg}")
        if deg.is_number_not_one():
            new_annotations: set[OWLAnnotation] = self.get_annotations_for_axiom(deg)
            axiom: OWLSubClassOfAxiom = self.data_factory.getOWLSubClassOfAxiom(
                c1, c2, new_annotations
            )
        else:
            axiom: OWLSubClassOfAxiom = self.data_factory.getOWLSubClassOfAxiom(c1, c2)
        self.manager.applyChange(AddAxiom(self.ontology, axiom))

    def annotate_pcd(
        self, c1: OWLClassExpression, pcd: PrimitiveConceptDefinition
    ) -> None:
        c2: OWLClassExpression = self.get_class(pcd.get_definition())
        n: float = pcd.get_degree()
        Util.debug(f"Annotate PCD -> {c1} - {c2} - {n}")
        if n != 1.0:
            new_annotations: set[OWLAnnotation] = self.get_annotations_for_axiom(n)
            axiom: OWLSubClassOfAxiom = self.data_factory.getOWLSubClassOfAxiom(
                c1, c2, new_annotations
            )
        else:
            axiom: OWLSubClassOfAxiom = self.data_factory.getOWLSubClassOfAxiom(c1, c2)
        self.manager.applyChange(AddAxiom(self.ontology, axiom))

    def run(self) -> None:
        """Execute the conversion process"""
        # Set fuzzy logic type
        logic = str(constants.KNOWLEDGE_BASE_SEMANTICS)

        if logic:
            annotation: str = (
                f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.ONTOLOGY.get_str_value()}">\n'
                f'\t<{FuzzyOWL2Keyword.FUZZY_LOGIC.get_tag_name()} {FuzzyOWL2Keyword.LOGIC.get_str_value()}="{logic}" />\n'
                f"</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>"
            )
            self.add_ontology_annotation(annotation)

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
                axiom: OWLAxiom = self.data_factory.getOWLEquivalentClassesAxiom(
                    jpype.types.JArray(OWLClassExpression)([c1, c2])
                )
                self.manager.applyChange(AddAxiom(self.ontology, axiom))

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
            axiom: OWLAxiom = self.data_factory.getOWLEquivalentClassesAxiom(c1, c2)
            self.manager.applyChange(AddAxiom(self.ontology, axiom))

        for a in self.kb.t_disjoints:
            c1: OWLClassExpression = self.get_class(a)
            for disj_C in self.kb.t_disjoints[a]:
                Util.debug(f"Process t_dis -> {c1} - {disj_C}")
                if a >= disj_C:
                    continue
                c2: OWLClassExpression = self.get_class(disj_C)
                axiom: OWLAxiom = self.data_factory.getOWLDisjointClassesAxiom(c1, c2)
                self.manager.applyChange(AddAxiom(self.ontology, axiom))

        for r in self.kb.domain_restrictions:
            op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(r)
            )
            for c in self.kb.domain_restrictions[r]:
                Util.debug(f"Process domain restriction -> {c}")
                cl: OWLClassExpression = self.get_class(c)
                if isinstance(op, OWLObjectProperty):
                    axiom: OWLAxiom = self.data_factory.getOWLObjectPropertyDomainAxiom(
                        op, cl
                    )
                else:
                    axiom: OWLAxiom = self.data_factory.getOWLDataPropertyDomainAxiom(
                        op, cl
                    )
                self.manager.applyChange(AddAxiom(self.ontology, axiom))

        for r in self.kb.range_restrictions:
            op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(r)
            )
            for c in self.kb.range_restrictions[r]:
                Util.debug(f"Process range restriction -> {c}")
                cl: OWLClassExpression = self.get_class(c)
                if isinstance(op, OWLObjectProperty):
                    axiom: OWLAxiom = self.data_factory.getOWLObjectPropertyRangeAxiom(
                        op, cl
                    )
                else:
                    axiom: OWLAxiom = self.data_factory.getOWLDataPropertyRangeAxiom(
                        op, cl
                    )
                self.manager.applyChange(AddAxiom(self.ontology, axiom))

        for r in self.kb.reflexive_roles:
            Util.debug(f"Process reflexive role -> {r}")
            op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(r)
            )
            if isinstance(op, OWLObjectProperty):
                axiom: OWLAxiom = self.data_factory.getOWLReflexiveObjectPropertyAxiom(
                    op
                )
            else:
                axiom: OWLAxiom = self.data_factory.getOWLReflexiveDataPropertyAxiom(op)
            self.manager.applyChange(AddAxiom(self.ontology, axiom))

        for r in self.kb.symmetric_roles:
            Util.debug(f"Process symmetric role -> {r}")
            op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(r)
            )
            if isinstance(op, OWLObjectProperty):
                axiom: OWLAxiom = self.data_factory.getOWLSymmetricObjectPropertyAxiom(
                    op
                )
            else:
                axiom: OWLAxiom = self.data_factory.getOWLSymmetricDataPropertyAxiom(op)
            self.manager.applyChange(AddAxiom(self.ontology, axiom))

        for r in self.kb.transitive_roles:
            Util.debug(f"Process transitive role -> {r}")
            op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_object_property(r)
            )
            if isinstance(op, OWLObjectProperty):
                axiom: OWLAxiom = self.data_factory.getOWLTransitiveObjectPropertyAxiom(
                    op
                )
            else:
                axiom: OWLAxiom = self.data_factory.getOWLTransitiveDataPropertyAxiom(
                    op
                )
            self.manager.applyChange(AddAxiom(self.ontology, axiom))

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
                if isinstance(op, OWLObjectProperty) and isinstance(
                    op2, OWLObjectProperty
                ):
                    axiom: OWLAxiom = (
                        self.data_factory.getOWLInverseObjectPropertiesAxiom(op, op2)
                    )
                elif isinstance(op, OWLDataProperty) and isinstance(
                    op2, OWLDataProperty
                ):
                    axiom: OWLAxiom = (
                        self.data_factory.getOWLInverseDataPropertiesAxiom(op, op2)
                    )
                else:
                    raise ValueError
                self.manager.applyChange(AddAxiom(self.ontology, axiom))

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
                    axiom: OWLAxiom = self.data_factory.getOWLSubObjectPropertyOfAxiom(
                        op, op2
                    )
                elif isinstance(op, OWLDataProperty) and isinstance(
                    op2, OWLDataProperty
                ):
                    axiom: OWLAxiom = self.data_factory.getOWLSubDataPropertyOfAxiom(
                        op, op2
                    )
                else:
                    raise ValueError
                self.manager.applyChange(AddAxiom(self.ontology, axiom))

        for r in self.kb.functional_roles:
            Util.debug(f"Process functional role -> {r}")
            if r in self.kb.concrete_features:
                dp: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_data_property(r)
                )
                if isinstance(dp, OWLDataProperty):
                    axiom: OWLAxiom = (
                        self.data_factory.getOWLFunctionalDataPropertyAxiom(dp)
                    )
                else:
                    axiom: OWLAxiom = (
                        self.data_factory.getOWLFunctionalObjectPropertyAxiom(dp)
                    )
            else:
                op: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                    self.get_object_property(r)
                )
                if isinstance(op, OWLObjectProperty):
                    axiom: OWLAxiom = (
                        self.data_factory.getOWLFunctionalObjectPropertyAxiom(op)
                    )
                else:
                    axiom: OWLAxiom = (
                        self.data_factory.getOWLFunctionalDataPropertyAxiom(op)
                    )
            self.manager.applyChange(AddAxiom(self.ontology, axiom))

        for cf_name, cf in self.kb.concrete_features.items():
            if cf is None:
                continue
            Util.debug(f"Process concrete feature {cf_name} -> {cf}")
            cf_type: ConcreteFeatureType = cf.get_type()
            dp: typing.Union[OWLDataProperty, OWLObjectProperty] = (
                self.get_data_property(cf_name)
            )
            if cf_type == ConcreteFeatureType.BOOLEAN:
                dt: OWLDatatype = self.data_factory.getBooleanOWLDatatype()
            elif cf_type == ConcreteFeatureType.INTEGER:
                dt: OWLDatatype = self.data_factory.getIntegerOWLDatatype()
            elif cf_type == ConcreteFeatureType.REAL:
                dt: OWLDatatype = self.data_factory.getOWLDatatype(
                    IRI.create(XSD.decimal)
                )
            elif cf_type == ConcreteFeatureType.STRING:
                dt: OWLDatatype = self.data_factory.getRDFPlainLiteral()
                # Util.warning(
                #     "To Implement: String Datatype Property Range conversion"
                # )
            if isinstance(dp, OWLDataProperty):
                axiom: OWLAxiom = self.data_factory.getOWLDataPropertyRangeAxiom(dp, dt)
            else:
                axiom: OWLAxiom = self.data_factory.getOWLObjectPropertyRangeAxiom(
                    dp, dt
                )
            self.manager.applyChange(AddAxiom(self.ontology, axiom))

        # Save ontology
        try:
            self.manager.saveOntology(
                self.ontology,
                IRI.create(pathlib.Path(os.path.abspath(self.output_FOWL)).as_uri()),
            )
        except Exception as ex:
            Util.error(f"Error saving ontology: {ex}", file=sys.stderr)
            raise

    def _process_concrete_concept(self, c: FuzzyConcreteConcept) -> None:
        """Process a concrete concept"""
        Util.debug(f"Process concrete concept -> {c}")
        current_datatype: OWLDatatype = self.data_factory.getOWLDatatype(self.iri(c))
        self.datatypes[str(c)] = current_datatype

        specific: str = self._get_concrete_concept_specifics(c)

        int_datatype: OWLDatatype = self.data_factory.getIntegerOWLDatatype()
        decimal: OWLDatatype = self.data_factory.getOWLDatatype(IRI.create(XSD.decimal))
        greater_than: OWLDatatypeRestriction = (
            self.data_factory.getOWLDatatypeRestriction(
                int_datatype,
                OWLFacet.MIN_INCLUSIVE,
                self.data_factory.getOWLLiteral(str(c.k1), decimal),
            )
        )
        less_than: OWLDatatypeRestriction = self.data_factory.getOWLDatatypeRestriction(
            int_datatype,
            OWLFacet.MAX_INCLUSIVE,
            self.data_factory.getOWLLiteral(str(c.k2), decimal),
        )
        unit_interval: OWLDataIntersectionOf = (
            self.data_factory.getOWLDataIntersectionOf(greater_than, less_than)
        )
        definition: OWLDatatypeDefinitionAxiom = (
            self.data_factory.getOWLDatatypeDefinitionAxiom(
                current_datatype, unit_interval
            )
        )
        self.manager.applyChange(AddAxiom(self.ontology, definition))

        annotation: str = (
            f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.DATATYPE.get_str_value()}">\n'
            f'\t<{FuzzyOWL2Keyword.DATATYPE.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{specific}"/>\n'
            f"</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>"
        )
        self.add_entity_annotation(annotation, current_datatype)

    def _get_concrete_concept_specifics(self, c: FuzzyConcreteConcept) -> str:
        """Get concrete concept specific parameters"""
        if isinstance(c, CrispConcreteConcept):
            return f'{FuzzyOWL2Keyword.CRISP.get_str_value()}" {FuzzyOWL2Keyword.A.get_str_value()}="{c.a}" {FuzzyOWL2Keyword.B.get_str_value()}="{c.b}'
        elif isinstance(c, LeftConcreteConcept):
            return f'{FuzzyOWL2Keyword.LEFT_SHOULDER.get_str_value()}" {FuzzyOWL2Keyword.A.get_str_value()}="{c.a}" {FuzzyOWL2Keyword.B.get_str_value()}="{c.b}'
        elif isinstance(c, RightConcreteConcept):
            return f'{FuzzyOWL2Keyword.RIGHT_SHOULDER.get_str_value()}" {FuzzyOWL2Keyword.A.get_str_value()}="{c.a}" {FuzzyOWL2Keyword.B.get_str_value()}="{c.b}'
        elif isinstance(c, TriangularConcreteConcept):
            return f'{FuzzyOWL2Keyword.TRIANGULAR.get_str_value()}" {FuzzyOWL2Keyword.A.get_str_value()}="{c.a}" {FuzzyOWL2Keyword.B.get_str_value()}="{c.b}" {FuzzyOWL2Keyword.C.get_str_value()}="{c.c}'
        elif isinstance(c, TrapezoidalConcreteConcept):
            return f'{FuzzyOWL2Keyword.TRAPEZOIDAL.get_str_value()}" {FuzzyOWL2Keyword.A.get_str_value()}="{c.a}" {FuzzyOWL2Keyword.B.get_str_value()}="{c.b}" {FuzzyOWL2Keyword.C.get_str_value()}="{c.c}" {FuzzyOWL2Keyword.D.get_str_value()}="{c.d}'
        return ""

    def _process_modifier(self, mod: Modifier) -> None:
        """Process a modifier"""
        Util.debug(f"Process modifier -> {mod}")
        if isinstance(mod, LinearModifier):
            annotation: str = (
                f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.MODIFIER.get_str_value()}">\n'
                f'\t<{FuzzyOWL2Keyword.MODIFIER.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{FuzzyOWL2Keyword.LINEAR.get_str_value()}" {FuzzyOWL2Keyword.C.get_str_value()}="{mod.c}"/>\n'
                f"</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>"
            )
        elif isinstance(mod, TriangularModifier):
            annotation: str = (
                f'<{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()} {FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()}="{FuzzyOWL2Keyword.MODIFIER.get_str_value()}">\n'
                f'\t<{FuzzyOWL2Keyword.MODIFIER.get_tag_name()} {FuzzyOWL2Keyword.TYPE.get_str_value()}="{FuzzyOWL2Keyword.TRIANGULAR.get_str_value()}" {FuzzyOWL2Keyword.A.get_str_value()}="{mod.a}" {FuzzyOWL2Keyword.B.get_str_value()}="{mod.b}" {FuzzyOWL2Keyword.C.get_str_value()}="{mod.c}"/>\n'
                f"</{FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value()}>"
            )
        else:
            raise ValueError

        current_datatype: OWLDatatype = self.data_factory.getOWLDatatype(self.iri(mod))
        self.modifiers[str(mod)] = current_datatype
        self.add_entity_annotation(annotation, current_datatype)

    def _process_assertion(self, ass: Assertion) -> None:
        Util.debug(f"Process assertion -> {ass}")
        i: OWLNamedIndividual = self.get_individual(str(ass.get_individual()))
        c: OWLClassExpression = self.get_class(ass.get_concept())
        deg: Degree = ass.get_lower_limit()
        if deg.is_number_not_one():
            new_ann: set[OWLAnnotation] = self.get_annotations_for_axiom(deg)
            axiom: OWLClassAssertionAxiom = self.data_factory.getOWLClassAssertionAxiom(
                c, i, new_ann
            )
        else:
            axiom: OWLClassAssertionAxiom = self.data_factory.getOWLClassAssertionAxiom(
                c, i
            )
        self.manager.applyChange(AddAxiom(self.ontology, axiom))

    def _process_individual(self, ind: Individual) -> None:
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
                    factory_call: typing.Callable = (
                        self.data_factory.getOWLObjectPropertyAssertionAxiom
                    )
                else:
                    factory_call: typing.Callable = (
                        self.data_factory.getOWLDataPropertyAssertionAxiom
                    )

                if deg.is_number_not_one():  # If the degree is not 1
                    # Create annotations
                    new_annotations: set[OWLAnnotation] = (
                        self.get_annotations_for_axiom(deg)
                    )
                    axiom: typing.Union[
                        OWLObjectPropertyAssertionAxiom, OWLDataPropertyAssertionAxiom
                    ] = factory_call(r, i, i2, new_annotations)
                else:
                    axiom: typing.Union[
                        OWLObjectPropertyAssertionAxiom, OWLDataPropertyAssertionAxiom
                    ] = factory_call(r, i, i2)
                self.manager.applyChange(AddAxiom(self.ontology, axiom))


def main():
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
