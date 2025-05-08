import os
import re
import string
import typing

from fuzzy_reasoner.fuzzydl.util.constants import FuzzyDLKeyword
from fuzzy_reasoner.fuzzydl.util.util import Util
from fuzzy_reasoner.fuzzyowl2.fuzzyowl2_java import FuzzyOwl2
from fuzzy_reasoner.fuzzyowl2.owl_types.choquet_concept import ChoquetConcept
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

try:
    from org.semanticweb.owlapi.model import (
        ClassExpressionType,
        DataRangeType,
        OWLClass,
        OWLClassExpression,
        OWLDataIntersectionOf,
        OWLDataOneOf,
        OWLDataProperty,
        OWLDataPropertyExpression,
        OWLDataRange,
        OWLDatatype,
        OWLEntity,
        OWLFacetRestriction,
        OWLIndividual,
        OWLLiteral,
        OWLObjectProperty,
        OWLObjectPropertyExpression,
    )
    from org.semanticweb.owlapi.vocab import OWLFacet
except:
    pass


class FuzzyOwl2ToFuzzyDL(FuzzyOwl2):
    EPSILON: float = 0.001

    INTEGER_MAX_VALUE: int = 100000000  # 0x7FFFFFFF
    INTEGER_MIN_VALUE: int = -INTEGER_MAX_VALUE
    DOUBLE_MAX_VALUE: float = 1000 * float(INTEGER_MAX_VALUE)
    DOUBLE_MIN_VALUE: float = -DOUBLE_MAX_VALUE

    def __init__(
        self,
        input_file: str,
        output_file: str,
        base_iri: str = "http://www.semanticweb.org/ontologies/fuzzydl_ontology.owl",
    ) -> None:
        super().__init__(input_file, output_file, base_iri)

        if os.path.exists(self.output_dl):
            os.remove(self.output_dl)

        self.boolean_datatypes: set[str] = set()
        self.numerical_datatypes: set[str] = set()
        self.string_datatypes: set[str] = set()
        self.data_properties: set[str] = set()
        self.object_properties: set[str] = set()
        self.processed_functional_data_properties: set[str] = set()
        self.processed_functional_object_properties: set[str] = set()

    @staticmethod
    def is_reserved_word(s: str) -> bool:
        if s in (
            FuzzyDLKeyword.LINEAR,
            FuzzyDLKeyword.TRIANGULAR,
            FuzzyDLKeyword.CRISP,
            FuzzyDLKeyword.TRAPEZOIDAL,
            FuzzyDLKeyword.CLASSICAL,
            FuzzyDLKeyword.DISJOINT,
            FuzzyDLKeyword.DISJOINT,
            FuzzyDLKeyword.INSTANCE,
            FuzzyDLKeyword.RELATED,
            FuzzyDLKeyword.DOMAIN,
            FuzzyDLKeyword.RANGE,
        ):
            return True
        # avoid numbers
        try:
            _ = float(s)
            return True
        except:
            return False

    def __write(self, line: str) -> None:
        with open(self.output_dl, "a") as file:
            file.write(f"{line}\n")

    def get_short_name(self, s: typing.Union[OWLEntity, str]):
        if isinstance(s, OWLEntity):
            # s = str(self.pm.getShortForm(s))
            s = str(s.toString().replaceAll("\\<", "").replaceAll("\\>", "")).replace(
                f"{self.ontology_path}#", ""
            )
        s = s.replace(r"\\(", "")
        s = s.replace(r"\\)", "")
        if FuzzyOwl2ToFuzzyDL.is_reserved_word(s):
            return f"_{s}"
        else:
            return s

    def __get_facets(self, name: str) -> list[float]:
        facets: list[float] = [
            FuzzyOwl2ToFuzzyDL.INTEGER_MIN_VALUE,
            FuzzyOwl2ToFuzzyDL.INTEGER_MAX_VALUE,
        ]
        if name == "xsd:nonPositiveInteger":
            facets[1] = 0
        elif name == "xsd:NegativeInteger":
            facets[1] = -1
        elif name == "xsd:nonNegativeInteger":
            facets[0] = 0
        elif name == "xsd:positiveInteger":
            facets[0] = 1
        return facets

    def __is_real_datatype(self, d: typing.Union[OWLDatatype, OWLLiteral]) -> bool:
        if d.isDouble() or d.isFloat():
            return True
        name: str = str(d.toString())
        return "owl:real" in name or "owl:rational" in name or "xsd:decimal" in name

    def __is_integer_datatype(self, d: typing.Union[OWLDatatype, OWLLiteral]) -> bool:
        if d.isInteger():
            return True
        name: str = str(d.toString())
        return (
            name == "xsd:integer"
            or name == "xsd:nonNegativeInteger"
            or name == "xsd:nonPositiveInteger"
            or name == "xsd:positiveInteger"
            or name == "xsd:negativeInteger"
            or name == "xsd:long"
            or name == "xsd:int"
            or name == "xsd:short"
            or name == "xsd:byte"
            or name == "xsd:unsignedLong"
            or name == "xsd:unsignedInt"
            or name == "xsd:unsignedShort"
            or name == "xsd:unsignedByte"
        )

    def get_individual_name(self, i: OWLIndividual) -> str:
        if i.isAnonymous():
            return str(i.toString())
        else:
            return self.get_short_name(i.asOWLNamedIndividual())

    def get_top_concept_name(self) -> str:
        return "*top*"

    def get_bottom_concept_name(self) -> str:
        return "*bottom*"

    def get_atomic_concept_name(self, c: OWLClass) -> str:
        return self.get_short_name(c)

    def get_object_intersection_of_name(self, operands: set[OWLClassExpression]) -> str:
        if len(operands) == 1:
            return self.get_class_name(operands.pop())
        return f"(and {' '.join([self.get_class_name(c) for     c in operands])})"

    def get_object_union_of_name(self, operands: set[OWLClassExpression]) -> str:
        if len(operands) == 1:
            return self.get_class_name(operands.pop())
        return f"(or {' '.join([self.get_class_name(c) for     c in operands])})"

    def get_object_some_values_from_name(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> str:
        return f"(some {self.get_object_property_name(p)} {self.get_class_name(c)})"

    def get_object_all_values_from_name(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> str:
        return f"(all {self.get_object_property_name(p)} {self.get_class_name(c)})"

    def get_data_some_values_from_name(
        self, p: OWLDataPropertyExpression, range: OWLDataRange
    ) -> str:
        type: DataRangeType = range.getDataRangeType()
        if type == DataRangeType.DATATYPE:
            datatype_name: str = self.get_short_name(range.asOWLDatatype())
            if datatype_name in self.fuzzy_datatypes:
                return f"(some {self.get_data_property_name(p)} {datatype_name})"
            else:
                d: OWLDatatype = range.asOWLDatatype()
                dp_name: str = self.get_data_property_name(p)
                if self.__is_real_datatype(d) or self.__is_integer_datatype(d):
                    if dp_name not in self.numerical_datatypes:
                        self.numerical_datatypes.add(dp_name)
                        if self.__is_real_datatype(d):
                            self.__write(
                                f"(range {dp_name} *real* {FuzzyOwl2ToFuzzyDL.DOUBLE_MIN_VALUE} {FuzzyOwl2ToFuzzyDL.DOUBLE_MAX_VALUE})"
                            )
                        else:
                            facets: list[float] = self.__get_facets(str(d.toString()))
                            self.__write(
                                f"(range {dp_name} *integer* {facets[0]} {facets[1]})"
                            )
                    if self.__is_real_datatype(d):
                        return f"(>= {dp_name} {FuzzyOwl2ToFuzzyDL.DOUBLE_MIN_VALUE})"
                    else:
                        return f"(>= {dp_name} {FuzzyOwl2ToFuzzyDL.INTEGER_MIN_VALUE})"
                elif d.isBoolean():
                    return f"(= {self.get_data_property_name(p)} {d})"
        elif type == DataRangeType.DATA_ONE_OF:
            o: OWLDataOneOf = typing.cast(OWLDataOneOf, range)
            literat_set: set[OWLLiteral] = o.getValues()
            if len(literat_set) > 0:
                return f"(= {self.get_data_property_name(p)} {list(literat_set)[0].getLiteral()})"
        Util.error(
            f"Data some values restriction with range {range} and type {type} not supported -- DataSomeValuesFrom({p} {range})"
        )
        return None

    def get_data_all_values_from_name(
        self, p: OWLDataPropertyExpression, range: OWLDataRange
    ) -> str:
        type: DataRangeType = range.getDataRangeType()
        if type == DataRangeType.DATATYPE:
            datatype_name: str = self.get_short_name(range.asOWLDatatype())
            if datatype_name in self.fuzzy_datatypes:
                return f"(all {self.get_data_property_name(p)} {datatype_name})"
        Util.error(
            f"Data all values restriction with range {range} and type {type} not supported -- DataAllValuesFrom({p} {range})"
        )
        return None

    def get_object_complement_of_name(self, c: OWLClassExpression) -> str:
        return f"(not {self.get_class_name(c)})"

    def get_object_has_self_name(self, p: OWLObjectPropertyExpression) -> str:
        return f"(self {self.get_object_property_name(p)})"

    def __get_set_name(self, curr_set: set) -> str:
        return str(
            curr_set.toString()
            .replaceAll("\\[", "")
            .replaceAll("\\]", "")
            .replaceAll(", ", " ")
        )

    def get_object_one_of_name(self, ind_set: set[OWLIndividual]) -> str:
        Util.error(
            f"OneOf concept not supported -- (OneOf {self.__get_set_name(ind_set)})"
        )
        return None

    def get_object_has_value_name(
        self, p: OWLObjectPropertyExpression, i: OWLIndividual
    ) -> str:
        return (
            f"(b-some {self.get_object_property_name(p)} {self.get_individual_name(i)})"
        )

    def get_data_has_value_name(
        self, p: OWLDataPropertyExpression, literal: OWLLiteral
    ) -> str:
        dp_name: str = self.get_data_property_name(p)
        if self.__is_integer_datatype(literal) or self.__is_real_datatype(literal):
            if dp_name not in self.numerical_datatypes:
                self.numerical_datatypes.add(dp_name)
                self.write_functional_data_property_axiom(p)
                if self.__is_real_datatype(literal):
                    self.__write(
                        f"(range {dp_name} *real* {FuzzyOwl2ToFuzzyDL.DOUBLE_MIN_VALUE} {FuzzyOwl2ToFuzzyDL.DOUBLE_MAX_VALUE})"
                    )
                else:
                    facets: list[float] = self.__get_facets(str(literal.toString()))
                    self.__write(f"(range {dp_name} *integer* {facets[0]} {facets[1]})")
            return f"(= {dp_name} {literal.getLiteral()})"
        elif literal.isBoolean():
            if dp_name not in self.boolean_datatypes:
                self.boolean_datatypes.add(dp_name)
                self.write_functional_data_property_axiom(p)
                self.__write(f"(range {dp_name} *boolean*)")
            return f"(= {dp_name} {literal.getLiteral()})"
        else:
            Util.error(
                f"Data hasValue restriction with literal {literal} not supported -- DataHasValue({p} {literal})"
            )
            return None

    def get_object_min_cardinality_restriction(
        self,
        cardinality: int,
        p: OWLObjectPropertyExpression,
        c: OWLClassExpression = None,
    ) -> str:
        if c is not None:
            Util.error(
                (
                    f"Object min cardinality restriction not supported -- ObjectMaxCardinalityRestriction({cardinality} {p} {c})"
                )
            )
        else:
            Util.error(
                (
                    f"Object min cardinality restriction not supported -- ObjectMaxCardinalityRestriction({cardinality} {p})"
                )
            )
        return None

    def get_object_max_cardinality_restriction(
        self,
        cardinality: int,
        p: OWLObjectPropertyExpression,
        c: OWLClassExpression = None,
    ) -> str:
        if c is not None:
            Util.error(
                (
                    f"Object max cardinality restriction not supported -- ObjectMaxCardinalityRestriction({cardinality} {p} {c})"
                )
            )
        else:
            Util.error(
                (
                    f"Object max cardinality restriction not supported -- ObjectMaxCardinalityRestriction({cardinality} {p})"
                )
            )
        return None

    def get_object_exact_cardinality_restriction(
        self,
        cardinality: int,
        p: OWLObjectPropertyExpression,
        c: OWLClassExpression = None,
    ) -> str:
        if c is not None:
            Util.error(
                (
                    f"Object exact cardinality restriction not supported -- ObjectExactCardinalityRestriction({cardinality} {p} {c})"
                )
            )
        else:
            Util.error(
                (
                    f"Object exact cardinality restriction not supported -- ObjectExactCardinalityRestriction({cardinality} {p})"
                )
            )
        return None

    def get_data_min_cardinality_restriction(
        self, cardinality: int, p: OWLDataPropertyExpression, range: OWLDataRange = None
    ) -> str:
        if range is not None:
            Util.error(
                (
                    f"Data min cardinality restriction not supported -- DataMinCardinalityRestriction({cardinality} {p} {c})"
                )
            )
        else:
            Util.error(
                (
                    f"Data min cardinality restriction not supported -- DataMinCardinalityRestriction({cardinality} {p})"
                )
            )
        return None

    def get_data_max_cardinality_restriction(
        self, cardinality: int, p: OWLDataPropertyExpression, range: OWLDataRange = None
    ) -> str:
        if range is not None:
            Util.error(
                (
                    f"Data max cardinality restriction not supported -- DataMaxCardinalityRestriction({cardinality} {p} {c})"
                )
            )
        else:
            Util.error(
                (
                    f"Data max cardinality restriction not supported -- DataMaxCardinalityRestriction({cardinality} {p})"
                )
            )
        return None

    def get_data_exact_cardinality_restriction(
        self, cardinality: int, p: OWLDataPropertyExpression, range: OWLDataRange = None
    ) -> str:
        if range is not None:
            Util.error(
                (
                    f"Data exact cardinality restriction not supported -- DataExactCardinalityRestriction({cardinality} {p} {c})"
                )
            )
        else:
            Util.error(
                (
                    f"Data exact cardinality restriction not supported -- DataExactCardinalityRestriction({cardinality} {p})"
                )
            )
        return None

    def get_top_object_property_name(self) -> str:
        Util.error("Top object property not supported")
        return None

    def get_bottom_object_property_name(self) -> str:
        Util.error("Bottom object property not supported")
        return None

    def get_atomic_object_property_name(self, p: OWLObjectProperty) -> str:
        name: str = self.get_short_name(p)
        if name in self.data_properties:
            name = f"_op@{name}"
        else:
            self.object_properties.add(name)
        return name

    def get_top_data_property_name(self) -> str:
        Util.error("Top data property not supported")
        return None

    def get_bottom_data_property_name(self) -> str:
        Util.error("Bottom data property not supported")
        return None

    def get_atomic_data_property_name(self, p: OWLDataProperty) -> str:
        name: str = self.get_short_name(p)
        if name in self.object_properties:
            name = f"_dp@{name}"
        else:
            self.data_properties.add(name)
        return name

    def write_fuzzy_logic(self, logic: str) -> None:
        self.__write("(define-fuzzy-logic " + logic + ")")

    def write_concept_declaration(self, c: OWLClassExpression) -> None:
        self.__write(
            f"(define-primitive-concept {self.get_class_name(c)} {self.get_top_concept_name()})"
        )

    def write_data_property_declaration(self, dp: OWLDataPropertyExpression) -> None:
        self.write_functional_data_property_axiom(dp)
        self.__write(f"(range {self.get_data_property_name(dp)} *string*)")

    def write_object_property_declaration(
        self, op: OWLObjectPropertyExpression
    ) -> None:
        pass

    def write_concept_assertion_axiom(
        self, i: OWLIndividual, c: OWLClassExpression, d: float
    ) -> None:
        self.__write(
            f"(instance {self.get_individual_name(i)} {self.get_class_name(c)} {d})"
        )

    def write_object_property_assertion_axiom(
        self,
        i1: OWLIndividual,
        i2: OWLIndividual,
        p: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        self.__write(
            f"(related {self.get_individual_name(i1)} {self.get_individual_name(i2)} {self.get_object_property_name(p)} {d})"
        )

    def write_data_property_assertion_axiom(
        self,
        i1: OWLIndividual,
        i2: OWLIndividual,
        p: OWLDataPropertyExpression,
        d: float,
    ) -> None:
        datatype: OWLDatatype = i2.getDatatype()
        dp_name: str = self.get_data_property_name(p)
        if datatype is None:
            self.__write(
                f"(instance {self.get_individual_name(i1)} (= {dp_name} {i2.getLiteral()}) {d})"
            )
        else:
            datatype_name: str = self.get_short_name(datatype.asOWLDatatype())
            if datatype_name in self.fuzzy_datatypes:
                self.__write(
                    f"(instance {self.get_individual_name(i1)} (some {dp_name} {datatype_name}) {d})"
                )
            else:
                if self.__is_real_datatype(i2) or self.__is_integer_datatype(i2):
                    if dp_name not in self.numerical_datatypes:
                        self.numerical_datatypes.add(dp_name)
                        self.write_functional_data_property_axiom(p)
                        if self.__is_integer_datatype(i2):
                            self.__write(
                                f"(range {dp_name} *integer* {FuzzyOwl2ToFuzzyDL.INTEGER_MIN_VALUE} {FuzzyOwl2ToFuzzyDL.INTEGER_MAX_VALUE})"
                            )
                        else:
                            self.__write(
                                f"(range {dp_name} *real* {FuzzyOwl2ToFuzzyDL.DOUBLE_MIN_VALUE} {FuzzyOwl2ToFuzzyDL.DOUBLE_MAX_VALUE})"
                            )
                    value: typing.Any = None
                    if self.__is_real_datatype(i2):
                        value = float(i2.parseDouble())
                    else:
                        value = int(i2.parseInteger())
                    self.__write(
                        f"(instance {self.get_individual_name(i1)} (>= {dp_name} {value}) {d})"
                    )
                else:
                    if dp_name not in self.string_datatypes:
                        self.string_datatypes.add(dp_name)
                        self.write_data_property_declaration(p)
                    l: str = str(i2.getLiteral())
                    l: str = re.sub(r"\s", "_", l)
                    l: str = re.sub(r"[\)\(]", "--", l)
                    l: str = re.sub(r"\"", "'", l)
                    if l[0] in string.digits:
                        l = f"_{l}"
                    self.__write(
                        f"(instance {self.get_individual_name(i1)} (= {dp_name} {l}) {d})"
                    )

    def write_negative_object_property_assertion_axiom(
        self,
        i1: OWLIndividual,
        i2: OWLIndividual,
        p: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        Util.error(
            f"Negative object property assertion not supported -- NegativeObjectPropertyAssertion({p} {i1} {i2} {d})"
        )
        return None

    def write_negative_data_property_assertion_axiom(
        self,
        i1: OWLIndividual,
        i2: OWLIndividual,
        p: OWLDataPropertyExpression,
        d: float,
    ) -> None:
        Util.error(
            f"Negative data property assertion not supported -- NegativeDataPropertyAssertion({p} {i1} {i2} {d})"
        )
        return None

    def write_same_individual_axiom(self, ind_set: set[OWLIndividual]) -> None:
        Util.error(
            f"Same individual axiom not supported -- NegativeDataPropertyAssertion({self.__get_set_name(ind_set)})"
        )
        return None

    def write_different_individuals_axiom(self, ind_set: set[OWLIndividual]) -> None:
        Util.error(
            f"Different individual axiom not supported -- DifferentIndividuals({self.__get_set_name(ind_set)})"
        )
        return None

    def write_disjoint_classes_axiom(self, class_set: set[OWLClassExpression]) -> None:
        if len(class_set) <= 1:
            return
        self.__write(
            f"(disjoint {' '.join(self.get_short_name(c.asOWLClass()) for c in class_set)})"
        )

    def write_disjoint_union_axiom(self, class_set: set[OWLClassExpression]) -> None:
        if len(class_set) <= 1:
            return
        for c in class_set:
            if c.getClassExpressionType() != ClassExpressionType.OWL_CLASS:
                Util.error("Concept type not supported in disjoint union axiom")
        self.__write(
            f"(disjoint-union {' '.join(self.get_short_name(c.asOWLClass()) for c in class_set)})"
        )

    def write_subclass_of_axiom(
        self, subclass: OWLClassExpression, superclass: OWLClassExpression, d: float
    ) -> None:
        type: ClassExpressionType = subclass.getClassExpressionType()
        if type == ClassExpressionType.OWL_CLASS and d == 1:
            self.__write(
                f"(define-primitive-concept {self.get_short_name(subclass.asOWLClass())} {self.get_class_name(superclass)})"
            )
        else:
            self.__write(
                f"(implies {self.get_class_name(subclass)} {self.get_class_name(superclass)} {d})"
            )

    def write_equivalent_classes_axiom(
        self, class_set: set[OWLClassExpression]
    ) -> None:
        name: str = None
        left_class: OWLClassExpression = None
        for c in class_set:
            if c.getClassExpressionType() == ClassExpressionType.OWL_CLASS:
                name = self.get_short_name(c.asOWLClass())
                left_class = c
                break
        if name is None:
            self.__write(
                f"(equivalent-concepts {' '.join(self.get_class_name(c) for c in class_set)})"
            )
        else:
            for c in class_set:
                if c != left_class:
                    self.__write(f"(define-concept {name} {self.get_class_name(c)})")

    def write_sub_object_property_of_axiom(
        self,
        subproperty: OWLObjectPropertyExpression,
        superproperty: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        self.__write(
            f"(implies-role {self.get_object_property_name(subproperty)} {self.get_object_property_name(superproperty)} {d})"
        )

    def write_sub_data_property_of_axiom(
        self,
        subproperty: OWLDataPropertyExpression,
        superproperty: OWLDataPropertyExpression,
        d: float,
    ) -> None:
        self.__write(
            f"(implies-role {self.get_object_property_name(subproperty)} {self.get_object_property_name(superproperty)} {d})"
        )

    def write_sub_property_chain_of_axiom(
        self,
        chain: list[OWLObjectPropertyExpression],
        superproperty: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        Util.error(
            f"Subproperty chain axiom not supported -- SubObjectPropertyOf(ObjectPropertyChain({self.__get_set_name(chain)}) {superproperty} {d})"
        )

    def write_equivalent_object_properties_axiom(
        self, class_set: set[OWLObjectPropertyExpression]
    ) -> None:
        first: OWLObjectPropertyExpression = next(class_set)
        first_name: str = self.get_object_property_name(first)
        for property in class_set - set([first]):
            property_name: str = self.get_object_property_name(property)
            self.__write(f"(implies-role {first_name} {property_name})")
            self.__write(f"(implies-role {property_name} {first_name})")

    def write_equivalent_data_properties_axiom(
        self, class_set: set[OWLDataPropertyExpression]
    ) -> None:
        first: OWLDataPropertyExpression = next(class_set)
        first_name: str = self.get_object_property_name(first)
        for property in class_set - set([first]):
            property_name: str = self.get_object_property_name(property)
            self.__write(f"(implies-role {first_name} {property_name})")
            self.__write(f"(implies-role {property_name} {first_name})")

    def write_transitive_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        self.__write(f"(transitive {self.get_object_property_name(p)})")

    def write_symmetric_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        self.__write(f"(symmetric {self.get_object_property_name(p)})")

    def write_asymmetric_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        Util.error(
            f"Asymmetric object property axiom not supported -- AsymmetricObjectProperty({p})"
        )

    def write_reflexive_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        self.__write(f"(reflexive {self.get_object_property_name(p)})")

    def write_irreflexive_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        Util.error(
            f"Irreflexive object property axiom not supported -- IrreflexiveObjectProperty({p})"
        )

    def write_functional_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        name: str = self.get_object_property_name(p)
        if name not in self.processed_functional_object_properties:
            self.processed_functional_object_properties.add(name)
            self.__write(f"(functional {name})")

    def write_functional_data_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        name: str = self.get_data_property_name(p)
        if name not in self.processed_functional_data_properties:
            self.processed_functional_data_properties.add(name)
            self.__write(f"(functional {name})")

    def write_inverse_object_property_axiom(
        self, p1: OWLObjectPropertyExpression, p2: OWLObjectPropertyExpression
    ) -> None:
        self.__write(
            f"(inverse {self.get_object_property_name(p1)} {self.get_object_property_name(p2)})"
        )

    def write_inverse_functional_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        self.__write(f"(inverse-functional {self.get_object_property_name(p)})")

    def write_object_property_domain_axiom(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> None:
        self.__write(
            f"(domain {self.get_object_property_name(p)} {self.get_class_name(c)})"
        )

    def write_object_property_range_axiom(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> None:
        self.__write(
            f"(range {self.get_object_property_name(p)} {self.get_class_name(c)})"
        )

    def write_data_property_domain_axiom(
        self, p: OWLDataPropertyExpression, c: OWLClassExpression
    ) -> None:
        self.__write(
            f"(domain {self.get_data_property_name(p)} {self.get_class_name(c)})"
        )

    def write_data_property_range_axiom(
        self, p: OWLDataPropertyExpression, range: OWLDataRange
    ) -> None:
        range_str: str = None
        dp_name: str = self.get_data_property_name(p)
        type: DataRangeType = range.getDataRangeType()
        if type == DataRangeType.DATATYPE:
            datatype: OWLDatatype = range.asOWLDatatype()
            if datatype.isString() or str(range.toString()) in (
                "xsd:date",
                "xsd:dateTime",
                "xsd:anyURI",
            ):
                self.string_datatypes.add(dp_name)
                range_str = "*string*"
            elif datatype.isBoolean():
                self.boolean_datatypes.add(dp_name)
                range_str = "*boolean*"
        elif type == DataRangeType.DATA_INTERSECTION_OF:
            correctness: int = 0
            is_integer: int = 0
            min: float = 0.0
            max: float = 0.0
            data_range: set[OWLDataRange] = typing.cast(
                OWLDataIntersectionOf, range
            ).getOperands()
            if len(data_range) == 2:
                for dr in data_range:
                    if dr.getDataRangeType() == DataRangeType.DATATYPE_RESTRICTION:
                        restrictions: set[OWLFacetRestriction] = typing.cast(
                            OWLFacetRestriction, dr
                        ).getFacetRestrictions()
                        if len(restrictions) != 1:
                            continue
                        facet: OWLFacetRestriction = list(restrictions)[0]
                        val: str = str(facet.getFacetValue().getLiteral())
                        if facet.getFacetValue().isInteger():
                            is_integer += 1
                        k: float = float(val)
                        if facet.getFacet() == OWLFacet.MIN_INCLUSIVE:
                            min = k
                            correctness += 1
                        elif facet.getFacet() == OWLFacet.MIN_EXCLUSIVE:
                            if is_integer != 0:
                                min = k + 1
                            else:
                                min = k + FuzzyOwl2ToFuzzyDL.EPSILON
                            correctness += 1
                        elif facet.getFacet() == OWLFacet.MAX_INCLUSIVE:
                            max = k
                            correctness += 1
                        elif facet.getFacet() == OWLFacet.MAX_EXCLUSIVE:
                            if is_integer != 0:
                                min = k - 1
                            else:
                                min = k - FuzzyOwl2ToFuzzyDL.EPSILON
                            correctness += 1
            if correctness == 2:
                if is_integer == 2:
                    range_str = f"*integer* {min} {max}"
                else:
                    range_str = f"*real* {min} {max}"
                self.numerical_datatypes.add(dp_name)
            else:
                Util.error(
                    f"Data property range axiom with range {range} not supported -- DataPropertyRange({p} {range})"
                )
        if range_str is not None:
            self.write_functional_data_property_axiom(p)
            self.__write(f"(range {dp_name} {range_str})")
        else:
            if str(type.toString()) == "DATA_ONE_OF":
                Util.error(
                    f"Data one of range axiom not supported -- DataPropertyRange({p} {range})"
                )
            else:
                range_type: OWLDatatype = range.asOWLDatatype()
                if self.__is_real_datatype(range_type):
                    self.write_functional_data_property_axiom(p)
                    self.__write(
                        f"(range {dp_name} *real* {FuzzyOwl2ToFuzzyDL.DOUBLE_MIN_VALUE} {FuzzyOwl2ToFuzzyDL.DOUBLE_MAX_VALUE})"
                    )
                    self.numerical_datatypes.add(dp_name)
                elif self.__is_integer_datatype(range_type):
                    self.write_functional_data_property_axiom(p)
                    facets: float = self.__get_facets(str(range_type.toString()))
                    self.__write(f"(range {dp_name} *integer* {facets[0]} {facets[1]})")
                    self.numerical_datatypes.add(dp_name)
                else:
                    Util.error(
                        f"Data property range axiom with range {range} not supported -- DataPropertyRange({p} {range})"
                    )

    def write_disjoint_object_properties_axiom(
        self, class_set: set[OWLObjectPropertyExpression]
    ) -> None:
        Util.error(
            f"Disjoint object properties axiom not supported -- DisjointObjectProperties({self.__get_set_name(class_set)})"
        )

    def write_disjoint_data_properties_axiom(
        self, class_set: set[OWLDataPropertyExpression]
    ) -> None:
        Util.error(
            f"Disjoint data properties axiom not supported -- DisjointDataProperties({self.__get_set_name(class_set)})"
        )

    def write_triangular_modifier_definition(
        self, name: str, mod: TriangularModifier
    ) -> None:
        self.__write(f"(define-modifier {name} {mod})")

    def write_linear_modifier_definition(self, name: str, mod: LinearModifier) -> None:
        self.__write(f"(define-modifier {name} {mod})")

    def write_left_shoulder_function_definition(
        self, name: str, dat: LeftShoulderFunction
    ) -> None:
        self.__write(f"(define-fuzzy-concept {name} {dat})")

    def write_right_shoulder_function_definition(
        self, name: str, dat: RightShoulderFunction
    ) -> None:
        self.__write(f"(define-fuzzy-concept {name} {dat})")

    def write_linear_function_definition(self, name: str, dat: LinearFunction) -> None:
        self.__write(f"(define-fuzzy-concept {name} {dat})")

    def write_triangular_function_definition(
        self, name: str, dat: TriangularFunction
    ) -> None:
        self.__write(f"(define-fuzzy-concept {name} {dat})")

    def write_trapezoidal_function_definition(
        self, name: str, dat: TrapezoidalFunction
    ) -> None:
        self.__write(f"(define-fuzzy-concept {name} {dat})")

    def write_modified_function_definition(
        self, name: str, dat: ModifiedFunction
    ) -> None:
        self.__write(f"(define-concept {name} {dat})")

    def write_modified_property_definition(
        self, name: str, dat: ModifiedProperty
    ) -> None:
        Util.error(
            f"Modified property not supported -- EquivalentObjectProperties({name} <{dat.get_fuzzy_modifier()} {dat.get_property()}>)"
        )

    def write_modified_concept_definition(
        self, name: str, dat: ModifiedConcept
    ) -> None:
        self.__write(f"(define-concept {name} {dat})")

    def write_fuzzy_nominal_concept_definition(
        self, name: str, dat: FuzzyNominalConcept
    ) -> None:
        Util.error(
            f"Fuzzy nominal not supported -- EquivalentConcepts({name} OneOf({dat}))"
        )

    def write_weighted_concept_definition(self, name: str, c: WeightedConcept) -> None:
        self.__write(f"(define-concept {name} {c})")

    def write_weighted_max_concept_definition(
        self, name: str, c: WeightedMaxConcept
    ) -> None:
        self.__write(f"(define-concept {name} {c})")

    def write_weighted_min_concept_definition(
        self, name: str, c: WeightedMinConcept
    ) -> None:
        self.__write(f"(define-concept {name} {c})")

    def write_weighted_sum_concept_definition(
        self, name: str, c: WeightedSumConcept
    ) -> None:
        self.__write(f"(define-concept {name} {c})")

    def write_weighted_sum_zero_concept_definition(
        self, name: str, c: WeightedSumZeroConcept
    ) -> None:
        self.__write(f"(define-concept {name} {c})")

    def write_owa_concept_definition(self, name: str, c: OwaConcept) -> None:
        self.__write(f"(define-concept {name} {c})")

    def write_choquet_concept_definition(self, name: str, c: ChoquetConcept) -> None:
        self.__write(f"(define-concept {name} {c})")

    def write_sugeno_concept_definition(self, name: str, c: SugenoConcept) -> None:
        self.__write(f"(define-concept {name} {c})")

    def write_quasi_sugeno_concept_definition(
        self, name: str, c: QsugenoConcept
    ) -> None:
        self.__write(f"(define-concept {name} {c})")

    def write_qowa_concept_definition(self, name: str, c: QowaConcept) -> None:
        self.__write(f"(define-concept {name} {c})")
