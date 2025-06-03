from __future__ import annotations

import os
import sys
import typing
from functools import partial

from rdflib import RDF, XSD, Literal, Namespace, URIRef

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

from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader


# @utils.timer_decorator
class FuzzydlToOwl2:
    """Convert FuzzyDL to OWL2"""

    def __init__(
        self,
        input_file: str,
        output_file: str,
        # base_iri: str = "http://www.semanticweb.org/ontologies/fuzzydl_ontology.owl",
        base_iri: str = "http://www.semanticweb.org/ontologies/fuzzydl_ontology#",
    ) -> None:
        self.num_classes: int = 0
        self.kb, _ = DLParser.get_kb(input_file)
        self.ontology_path: str = base_iri
        self.ontology_iri: IRI = IRI(Namespace(URIRef(base_iri)))
        self.ontology: OWLOntology = OWLOntology(
            self.ontology_iri, OWL1_annotations=True
        )
        self.fuzzyLabel: OWLAnnotationProperty = OWLAnnotationProperty(
            IRI(self.ontology_iri.namespace, ConfigReader.OWL_ANNOTATION_LABEL)
        )

        self.ontology.add_axiom(OWLDeclaration(self.fuzzyLabel))

        self.concepts: dict[str, OWLClassExpression] = dict()
        self.datatypes: dict[str, OWLDatatype] = dict()
        self.modifiers: dict[str, OWLDatatype] = dict()
        self.input_FDL: str = input_file
        self.output_FOWL: str = os.path.join(constants.RESULTS_PATH, output_file)

    def iri(self, o: object) -> IRI:
        """Convert object to IRI string"""
        return IRI(self.ontology_iri.namespace, str(o))

    def get_base(self, c: Concept) -> OWLClassExpression:
        """Get the base class for a concept"""
        if c.is_atomic():
            return self.get_class(str(c))
        return self.get_new_atomic_class(str(c))

    @typing.overload
    def get_class(self, name: str) -> OWLClassExpression: ...

    @typing.overload
    def get_class(self, c: Concept) -> OWLClassExpression: ...

    def get_class(self, arg: typing.Union[str, Concept]) -> OWLClassExpression:
        """Get or create an OWL class"""
        if isinstance(arg, str):
            return self.__get_class_1(arg)
        elif isinstance(arg, Concept):
            return self.__get_class_2(arg)
        else:
            raise ValueError("Argument must be a string or a Concept")

    def __get_class_1(self, name: str) -> OWLClassExpression:
        """Get or create an OWL class by name"""
        cls = OWLClass(self.iri(name))
        self.ontology.add_axiom(OWLDeclaration(cls))
        return cls

    def __get_class_2(self, c: Concept) -> OWLClassExpression:
        """Get or create an OWL class from a Concept"""
        Util.debug(f"Getting class for concept -> {c}")
        c_type: ConceptType = c.type
        if c_type in (ConceptType.ATOMIC, ConceptType.CONCRETE):
            cls = self.get_class(str(c))
            self.ontology.add_axiom(OWLDeclaration(cls))
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
            c3: OWLClassExpression = self.get_base(c.c1)
            self.concepts[str(c)] = c3

            main_xml = FuzzyXML.build_main_xml(FuzzyOWL2Keyword.CONCEPT.get_str_value())
            concept_xml = FuzzyXML.build_concept_xml(
                FuzzyOWL2Keyword.MODIFIED.get_str_value(),
                {
                    FuzzyOWL2Keyword.MODIFIER.get_str_value(): str(
                        self.modifiers[str(c)]
                    ),
                    FuzzyOWL2Keyword.BASE.get_str_value(): str(c3),
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
            c3: OWLClassExpression = self.get_base(c.c1)

            main_xml = FuzzyXML.build_main_xml(FuzzyOWL2Keyword.CONCEPT.get_str_value())
            concept_xml = FuzzyXML.build_concept_xml(
                FuzzyOWL2Keyword.WEIGHTED.get_str_value(),
                {
                    FuzzyOWL2Keyword.DEGREE_VALUE.get_str_value(): str(c.weight),
                    FuzzyOWL2Keyword.BASE.get_str_value(): str(c3),
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
        cls = OWLClass(self.iri(str(c)))
        self.ontology.add_axiom(OWLDeclaration(cls))
        return cls

    def __get_class_weighted_min_max_sum(self, c: Concept) -> OWLClassExpression:
        """Get the class for weighted min, max, sum, or sum zero"""
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
                    FuzzyOWL2Keyword.BASE.get_str_value(): str(c5),
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
        """Get the class for OWA, Quantified OWA, Choquet Integral, Sugeno Integral, or Quasi Sugeno Integral"""
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
        """Get the class for OWA, Quantified OWA, Choquet Integral, Sugeno Integral, or Quasi Sugeno Integral"""
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
        """Get or create a new atomic class"""
        Util.debug(f"Getting new atomic concept -> {name}")
        c = self.concepts.get(name)
        if c is not None:
            return c

        self.num_classes += 1
        Util.debug(f"Creating new atomic concept -> {name}")
        c2: OWLClass = OWLClass(self.iri(f"class__{self.num_classes}"))
        self.concepts[name] = c2
        self.ontology.add_axiom(OWLDeclaration(c2))
        return c2

    def exist_object_property(self, role: str) -> bool:
        """Check if an object property exists"""
        iri: IRI = self.iri(role)
        return self.ontology.getter.exists_object_property(iri.to_uriref())
        # return any(
        #     typing.cast(OWLObjectProperty, typing.cast(OWLDeclaration, prop).entity).iri
        #     == iri
        #     for prop in self.ontology.get_axioms(RDFXMLGetterTypes.OBJECT_PROPERTIES)
        # )

    def exist_data_property(self, role: str) -> bool:
        """Check if a data property exists"""
        iri: IRI = self.iri(role)
        return self.ontology.getter.exists_data_property(iri.to_uriref())
        # return any(
        #     typing.cast(OWLDataProperty, typing.cast(OWLDeclaration, prop).entity).iri
        #     == iri
        #     for prop in self.ontology.get_axioms(RDFXMLGetterTypes.DATA_PROPERTIES)
        # )

    def get_object_property(
        self, role: str
    ) -> typing.Union[OWLDataProperty, OWLObjectProperty]:
        """Get or create an object property"""
        Util.debug(f"Getting object property -> {role}")
        if self.exist_data_property(role):
            return self.get_data_property(role)
        obj = OWLObjectProperty(self.iri(role))
        self.ontology.add_axiom(OWLDeclaration(obj))
        return obj

    def get_data_property(
        self, role: str
    ) -> typing.Union[OWLDataProperty, OWLObjectProperty]:
        """Get or create a data property"""
        Util.debug(f"Getting data property -> {role}")
        if self.exist_object_property(role):
            return self.get_object_property(role)
        data = OWLDataProperty(self.iri(role))
        self.ontology.add_axiom(OWLDeclaration(data))
        return data

    def get_individual(self, name: str) -> OWLNamedIndividual:
        """Get or create a named individual"""
        Util.debug(f"Getting individual -> {name}")
        ind = OWLNamedIndividual(self.iri(f"{name}_Individual"))
        self.ontology.add_axiom(OWLDeclaration(ind))
        return ind

    def to_owl_annotation(self, annotation: str) -> OWLAnnotation:
        """Convert a string to an OWL annotation"""
        Util.debug(f"Converting annotation to OWL -> {annotation}")
        return OWLAnnotation(
            self.fuzzyLabel,
            OWLLiteral(
                Literal(annotation, datatype=RDF.PlainLiteral),
            ),
        )

    def add_ontology_annotation(self, annotation: str) -> None:
        """Add annotation to the ontology"""
        Util.debug(f"Adding annotation to ontology -> {annotation}")
        comment: OWLAnnotation = self.to_owl_annotation(annotation)
        self.ontology.add_annotation(comment)

    def add_entity_annotation(self, annotation: str, entity: OWLEntity) -> None:
        """Add annotation to an entity"""
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
        """Get annotations for an axiom with degree"""
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
        """Annotate a General Concept Inclusion (GCI)"""
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
        """Annotate a Primitive Concept Definition (PCD)"""
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
        """Execute the conversion process"""
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
        """Process a concrete concept"""
        Util.debug(f"Process concrete concept -> {c}")
        current_datatype: OWLDatatype = OWLDatatype(self.iri(c))
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
        self.ontology.add_axiom(OWLDeclaration(current_datatype))
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
        """Get concrete concept specific parameters"""
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
        """Process a modifier"""
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

        current_datatype: OWLDatatype = OWLDatatype(self.iri(mod))
        self.modifiers[str(mod)] = current_datatype
        self.ontology.add_axiom(OWLDeclaration(current_datatype))
        self.add_entity_annotation(annotation, current_datatype)

    def _process_assertion(self, ass: Assertion) -> None:
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
