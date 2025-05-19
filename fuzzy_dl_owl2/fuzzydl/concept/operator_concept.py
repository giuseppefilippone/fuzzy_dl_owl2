import typing
from functools import partial

from fuzzy_dl_owl2.fuzzydl.concept.all_some_concept import AllSomeConcept
from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface import (
    HasConceptsInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.truth_concept import TruthConcept
from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType, FuzzyLogic


class OperatorConcept(Concept, HasConceptsInterface):
    AND_OPERATORS: list[ConceptType] = [
        ConceptType.AND,
        ConceptType.GOEDEL_AND,
        ConceptType.LUKASIEWICZ_AND,
    ]

    OR_OPERATORS: list[ConceptType] = [
        ConceptType.OR,
        ConceptType.GOEDEL_OR,
        ConceptType.LUKASIEWICZ_OR,
    ]

    BINARY_OPERATORS: list[ConceptType] = AND_OPERATORS + OR_OPERATORS

    COMPLEMENT_LAW_OPERATORS: list[ConceptType] = [
        ConceptType.AND,
        ConceptType.LUKASIEWICZ_AND,
        ConceptType.OR,
        ConceptType.LUKASIEWICZ_OR,
    ]

    DISTRIBUTIVE_OPERATORS: list[ConceptType] = [
        ConceptType.AND,
        ConceptType.OR,
        ConceptType.GOEDEL_AND,
        ConceptType.GOEDEL_OR,
    ]

    ABSORPTION_OPERATORS: list[ConceptType] = DISTRIBUTIVE_OPERATORS

    ALL_OPERATORS: list[ConceptType] = BINARY_OPERATORS + [ConceptType.COMPLEMENT]

    OPERATORS: dict[ConceptType, ConceptType] = {
        k: v for k, v in zip(AND_OPERATORS + OR_OPERATORS, OR_OPERATORS + AND_OPERATORS)
    }

    def __init__(self, c_type: ConceptType, concepts: typing.Iterable[Concept]) -> None:
        Concept.__init__(self, c_type, None)
        HasConceptsInterface.__init__(self, concepts)

        assert c_type in OperatorConcept.ALL_OPERATORS, f"Type {c_type} is not valid."

        self.type: ConceptType = c_type
        self.name = self.compute_name()

    @property
    def concepts(self) -> list[Concept]:
        return self._concepts

    @concepts.setter
    def concepts(self, value: typing.Iterable[Concept]) -> None:
        self._concepts = list(value)
        self.name = self.compute_name()

    def clone(self) -> Concept:
        return OperatorConcept(
            self.type,
            [c for c in self.concepts],
        )

    @staticmethod
    def __op(c_type: ConceptType, concepts: typing.Iterable[Concept]) -> Concept:
        assert len(concepts) > 0, "You must have at least one argument"
        if c_type != ConceptType.COMPLEMENT and len(concepts) == 1:
            return concepts[0]
        concepts: list[Concept] = list(concepts)
        if c_type in OperatorConcept.BINARY_OPERATORS:
            changes: bool = True
            while changes:
                i: int = 0
                changes = False
                while len(concepts) > 0 and i < len(concepts):
                    c: Concept = concepts[i]
                    if c.type == c_type:
                        concepts.extend(typing.cast(OperatorConcept, c).concepts)
                        concepts.pop(i)
                        changes = True
                    else:
                        i += 1
        return OperatorConcept(c_type, sorted(concepts))

    @staticmethod
    def and_(*concepts: Concept) -> Concept:
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL:
            return OperatorConcept.__op(ConceptType.AND, concepts).classic_cnf()
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
            return OperatorConcept.__op(
                ConceptType.LUKASIEWICZ_AND, concepts
            ).lukasiewicz_cnf()
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.ZADEH:
            return OperatorConcept.__op(ConceptType.GOEDEL_AND, concepts).goedel_cnf()

    @staticmethod
    def goedel_and(*concepts: Concept) -> Concept:
        return OperatorConcept.__op(ConceptType.GOEDEL_AND, concepts).goedel_cnf()

    @staticmethod
    def lukasiewicz_and(*concepts: Concept) -> Concept:
        return OperatorConcept.__op(
            ConceptType.LUKASIEWICZ_AND, concepts
        ).lukasiewicz_cnf()

    @staticmethod
    def or_(*concepts: Concept) -> Concept:
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL:
            return OperatorConcept.__op(ConceptType.OR, concepts).classic_cnf()
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
            return OperatorConcept.__op(
                ConceptType.LUKASIEWICZ_OR, concepts
            ).lukasiewicz_cnf()
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.ZADEH:
            return OperatorConcept.__op(ConceptType.GOEDEL_OR, concepts).goedel_cnf()

    @staticmethod
    def goedel_or(*concepts: Concept) -> Concept:
        return OperatorConcept.__op(ConceptType.GOEDEL_OR, concepts).goedel_cnf()

    @staticmethod
    def lukasiewicz_or(*concepts: Concept) -> Concept:
        return OperatorConcept.__op(
            ConceptType.LUKASIEWICZ_OR, concepts
        ).lukasiewicz_cnf()

    @staticmethod
    def not_(concept: Concept) -> Concept:
        if concept.type == ConceptType.TOP:
            return TruthConcept.get_bottom()
        if concept.type == ConceptType.BOTTOM:
            return TruthConcept.get_top()
        if concept.type != ConceptType.COMPLEMENT:
            return OperatorConcept(ConceptType.COMPLEMENT, [concept])
        else:
            return typing.cast(OperatorConcept, concept).concepts[0]

    @staticmethod
    def is_or(c_type: ConceptType) -> bool:
        return c_type in OperatorConcept.OR_OPERATORS

    @staticmethod
    def is_and(c_type: ConceptType) -> bool:
        return c_type in OperatorConcept.AND_OPERATORS

    @staticmethod
    def is_not_type(op: Concept, c_type: ConceptType) -> bool:
        if not isinstance(op, OperatorConcept):
            return False
        if op.type != ConceptType.COMPLEMENT:
            return False
        return op.concepts[0].type == c_type

    @staticmethod
    def is_not_fuzzy_number(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.FUZZY_NUMBER)

    @staticmethod
    def is_not_concrete(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.CONCRETE)

    @staticmethod
    def is_not_has_value(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.HAS_VALUE)

    @staticmethod
    def is_not_goedel_implies(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.GOEDEL_IMPLIES)

    @staticmethod
    def is_not_at_most_value(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.AT_MOST_VALUE)

    @staticmethod
    def is_not_at_least_value(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.AT_LEAST_VALUE)

    @staticmethod
    def is_not_exact_value(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.EXACT_VALUE)

    @staticmethod
    def is_not_weighted(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.WEIGHTED)

    @staticmethod
    def is_not_weighted_min(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.W_MIN)

    @staticmethod
    def is_not_weighted_max(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.W_MAX)

    @staticmethod
    def is_not_weighted_sum(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.W_SUM)

    @staticmethod
    def is_not_weighted_sum_zero(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.W_SUM_ZERO)

    @staticmethod
    def is_not_pos_threshold(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.POS_THRESHOLD)

    @staticmethod
    def is_not_neg_threshold(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.NEG_THRESHOLD)

    @staticmethod
    def is_not_ext_pos_threshold(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.EXT_POS_THRESHOLD)

    @staticmethod
    def is_not_ext_neg_threshold(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.EXT_NEG_THRESHOLD)

    @staticmethod
    def is_not_concrete(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.CONCRETE)

    @staticmethod
    def is_not_modified(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.MODIFIED)

    @staticmethod
    def is_not_owa(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.OWA)

    @staticmethod
    def is_not_qowa(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.QUANTIFIED_OWA)

    @staticmethod
    def is_not_choquet(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.CHOQUET_INTEGRAL)

    @staticmethod
    def is_not_sugeno(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.SUGENO_INTEGRAL)

    @staticmethod
    def is_not_quasi_sugeno(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.QUASI_SUGENO_INTEGRAL)

    @staticmethod
    def is_not_self(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.SELF)

    @staticmethod
    def is_not_zadeh_implies(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.ZADEH_IMPLIES)

    def is_concrete(self) -> bool:
        if OperatorConcept.is_not_concrete(self) or OperatorConcept.is_not_fuzzy_number(
            self
        ):
            return True
        if OperatorConcept.is_not_modified(self):
            return self.concepts[0].is_concrete()
        return False

    def is_atomic(self) -> bool:
        return False

    def is_complemented_atomic(self) -> bool:
        return self.type == ConceptType.COMPLEMENT and (
            self.concepts[0].is_atomic()
            # or self.concepts[0].type
            # in (ConceptType.MODIFIED, ConceptType.FUZZY_NUMBER, ConceptType.CONCRETE)
        )

    def get_atom(self) -> typing.Optional[typing.Self]:
        return self.concepts[0] if self.type == ConceptType.COMPLEMENT else None

    def get_atoms(self) -> list[typing.Self]:
        if self.type == ConceptType.COMPLEMENT:
            if self.is_complemented_atomic():
                return [self]
            else:
                return self.concepts[0].get_atoms()
        else:
            return list.extend(*[c.get_atoms() for c in self.concepts])

    def is_simplified(self) -> bool:
        """
        This function check if current formula is simplified, i.e., if:
            - The only negated elements are literal of kind (~ A), where A is an AtomicProposition
            - The OR operator is between:
                - Two literals => A | B
                - One literal and a AND => A | (B & C) - (A & B) | C
                - Two (or more) OR => (A & B) | (C & D) | (E & F)
            - The AND operator is between:
                - Two literals => A & B
                - One literal and a OR => A & (B | C) - (A | B) & C
                - Two (or more) AND => (A | B) & (C | D) & (E | F)
            - The only operators are AND, OR and NOT
        """
        if self.is_complemented_atomic():
            return True
        return all(c.type != self.type for c in self.concepts)

    def de_morgan(self) -> typing.Self:
        self.concepts: Concept = [c.de_morgan() for c in self._concepts]
        if (
            self.type == ConceptType.COMPLEMENT
            and isinstance(self.concepts[0], OperatorConcept)
            and self.concepts[0].type in OperatorConcept.BINARY_OPERATORS
        ):
            # ~(A & B) = (~A | ~B)
            # ~(A | B) = (~A & ~B)
            op: ConceptType = OperatorConcept.OPERATORS[self.concepts[0].type]
            concepts: list[Concept] = [
                (-c).de_morgan()
                for c in typing.cast(OperatorConcept, self.concepts[0]).concepts
            ]
            return OperatorConcept(op, concepts).de_morgan()
        return self

    def reduce_truth_values(self) -> typing.Self:
        self.concepts: list[Concept] = [c.reduce_truth_values() for c in self._concepts]
        if self.type == ConceptType.COMPLEMENT and self.concepts[0].type in (
            ConceptType.TOP,
            ConceptType.BOTTOM,
        ):
            """
            ~ ⊤ = ⊥
            ~ ⊥ = ⊤
            """
            return -self.concepts[0]
        elif self.type in OperatorConcept.BINARY_OPERATORS:
            """
            ⊤ & ⊤ = ⊤
            ⊤ & A = A & ⊤ = A

            ⊥ & ⊤ = ⊥
            ⊥ & A = A & ⊥ = ⊥

            A & ~A = ⊥
            A & A = A

            ⊥ | ⊥ = ⊥
            ⊥ | A = A | ⊥ = A

            ⊤ | ⊥ = ⊤
            ⊤ | A = A | ⊤ = ⊤

            A | ~A = ⊤
            A | A = A
            """
            if OperatorConcept.is_and(self.type):
                if (
                    ConceptType.BOTTOM in [c.type for c in self.concepts]
                    or any(-c in self.concepts for c in self.concepts)
                    and constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
                ):
                    return TruthConcept.get_bottom()
                if self.type in OperatorConcept.ABSORPTION_OPERATORS:
                    self.concepts = sorted(set(self.concepts))
                self.concepts = [c for c in self.concepts if c.type != ConceptType.TOP]
            elif OperatorConcept.is_or(self.type):
                if (
                    ConceptType.TOP in [c.type for c in self.concepts]
                    or any(-c in self.concepts for c in self.concepts)
                    and constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
                ):
                    return TruthConcept.get_top()
                if self.type in OperatorConcept.ABSORPTION_OPERATORS:
                    self.concepts = sorted(set(self.concepts))
                self.concepts = [
                    c for c in self.concepts if c.type != ConceptType.BOTTOM
                ]
        return self

    def reduce_double_negation(self) -> typing.Self:
        self.concepts: list[Concept] = [
            c.reduce_double_negation() for c in self._concepts
        ]
        # ~(~A) = A
        if self.type == ConceptType.COMPLEMENT:
            if (
                isinstance(self.concepts[0], OperatorConcept)
                and self.concepts[0].type == ConceptType.COMPLEMENT
            ):
                return self.concepts[0].concepts[0].reduce_double_negation()
        return self

    def distribute(self, c_type: ConceptType) -> typing.Self:
        if self.type == ConceptType.COMPLEMENT:
            self.concepts: list[Concept] = [self._concepts[0].distribute(c_type)]
            return self

        if self.type not in OperatorConcept.DISTRIBUTIVE_OPERATORS:
            return self

        outer_operator = partial(OperatorConcept.__op, c_type)
        inner_operator = partial(
            OperatorConcept.__op, OperatorConcept.OPERATORS[c_type]
        )

        self.concepts: list[Concept] = [c.distribute(c_type) for c in self._concepts]
        if self.type == c_type:
            #   A & (B | C) = (A & B) | (A & C), where A is literal of DNF clause (A = A_1 & A_2 & ... & A_n)
            #   (A | B) & (C | D) = ((A | B) & C) | ((A | B) & D)
            #   A | (B & C) = (A | B) & (A | C), where A is literal of CNF clause (A = A_1 | A_2 | ... | A_n)
            #   (A & B) | (C & D) = (A & B | C) & (A & B | D)
            #   (A | B) & C = (A & C) | (B & C), where C is literal of DNF clause (C = C_1 & C_2 & ... & C_n)
            #   (A & B) | C = (A | C) & (B | C), where C is literal of CNF clause (C = C_1 | C_2 | ... | C_n)
            c1: list[OperatorConcept] = [
                c for c in self.concepts if c.type == OperatorConcept.OPERATORS[c_type]
            ]
            c2: list[Concept] = [
                c for c in self.concepts if c.type != OperatorConcept.OPERATORS[c_type]
            ]
            if len(c1) > 0:
                return inner_operator(
                    [outer_operator(c2 + [c]) for ci in c1 for c in ci.concepts]
                )
        return self

    def reduce_idempotency(self, is_type: typing.Callable) -> typing.Self:
        self.concepts: list[Concept] = [
            c.reduce_idempotency(is_type) for c in self._concepts
        ]
        if self.is_complemented_atomic():
            return self
        if self.type in OperatorConcept.ABSORPTION_OPERATORS:
            self.concepts = sorted(set(self.concepts))
        if TruthConcept.get_top() in self.concepts and OperatorConcept.is_or(self.type):
            return TruthConcept.get_top()
        elif TruthConcept.get_bottom() in self.concepts and OperatorConcept.is_and(
            self.type
        ):
            return TruthConcept.get_bottom()
        if (
            self.type
            in OperatorConcept.COMPLEMENT_LAW_OPERATORS
            # or constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
            # and (OperatorConcept.is_and(self.type) or OperatorConcept.is_or(self.type))
        ):
            if any(-c in self.concepts for c in self.concepts):
                return (
                    TruthConcept.get_top()
                    if OperatorConcept.is_or(self.type)
                    else TruthConcept.get_bottom()
                )
        self.concepts: list[Concept] = sorted(
            [
                a
                for a in self.concepts
                if a not in [TruthConcept.get_bottom(), TruthConcept.get_top()]
            ]
        )
        # if len(self.concepts) == 1:
        #     return self.concepts[0]
        return OperatorConcept.__op(self.type, self.concepts)

    def reduce_quantifiers(self) -> typing.Self:
        self.concepts: list[Concept] = [c.reduce_quantifiers() for c in self._concepts]
        remaining_concepts: list[Concept] = []
        all_groups: dict[str, list[Concept]] = dict()
        some_groups: dict[str, list[Concept]] = dict()
        all_reduced_concepts: list[Concept] = []
        some_reduced_concepts: list[Concept] = []
        for c in self.concepts:
            if c.type not in (ConceptType.ALL, ConceptType.SOME):
                remaining_concepts.append(c)
                continue
            c: AllSomeConcept = typing.cast(AllSomeConcept, c)
            if c.type == ConceptType.ALL:
                all_groups[c.role] = all_groups.get(c.role, []) + [c]
            else:
                some_groups[c.role] = some_groups.get(c.role, []) + [c]
        if (
            self.type in (ConceptType.AND, ConceptType.GOEDEL_AND)
            or constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
            and OperatorConcept.is_and(self.type)
        ):
            if (
                constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
                and OperatorConcept.is_and(self.type)
            ):
                and_: typing.Callable = OperatorConcept.and_
            else:
                and_: typing.Callable = OperatorConcept.goedel_and
            for role in all_groups:
                curr_concepts: list[AllSomeConcept] = all_groups[role]
                if len(curr_concepts) == 1:
                    remaining_concepts.extend(curr_concepts)
                    continue
                all_reduced_concepts.append(
                    AllSomeConcept.all(
                        role, and_(*[c.curr_concept for c in curr_concepts])
                    )
                )
            for role in some_groups:
                curr_concepts: list[AllSomeConcept] = some_groups[role]
                if len(curr_concepts) == 1:
                    remaining_concepts.extend(curr_concepts)
                    continue
                some_reduced_concepts.extend(
                    [
                        AllSomeConcept.some(role, c.curr_concept)
                        for c in curr_concepts
                        if c.curr_concept.type != ConceptType.TOP
                    ]
                )
            return OperatorConcept.__op(
                self.type,
                remaining_concepts + all_reduced_concepts + some_reduced_concepts,
            )

        if self.type not in (ConceptType.OR, ConceptType.GOEDEL_OR) and (
            constants.KNOWLEDGE_BASE_SEMANTICS != FuzzyLogic.CLASSICAL
            or not OperatorConcept.is_or(self.type)
        ):
            return self
        if (
            constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
            and OperatorConcept.is_or(self.type)
        ):
            or_: typing.Callable = OperatorConcept.or_
        else:
            or_: typing.Callable = OperatorConcept.goedel_or

        for role in all_groups:
            remaining_concepts.extend(all_groups[role])

        some_reduced_concepts = []
        for role in some_groups:
            curr_concepts: list[AllSomeConcept] = some_groups[role]
            if len(curr_concepts) == 1:
                remaining_concepts.extend(curr_concepts)
                continue
            some_reduced_concepts.append(
                AllSomeConcept.some(role, or_(*[c.curr_concept for c in curr_concepts]))
            )

        return OperatorConcept.__op(
            self.type,
            remaining_concepts + all_reduced_concepts + some_reduced_concepts,
        )

    def normal_form(self, is_type: typing.Callable) -> typing.Self:
        c_type: ConceptType = next(
            filter(
                is_type,
                OperatorConcept.BINARY_OPERATORS,
            )
        )
        while True:
            self: Concept = self.de_morgan()
            self: Concept = self.reduce_double_negation()
            self: Concept = self.distribute(c_type)
            self: Concept = self.reduce_idempotency(is_type)
            self: Concept = self.reduce_truth_values()
            self: Concept = self.reduce_quantifiers()
            if self.is_simplified():
                break
        return self

    def get_clauses(self, is_type: typing.Callable) -> list[Concept]:
        if self.type == ConceptType.COMPLEMENT:
            return [self]
        return self.concepts

    def replace(self, a: Concept, c: Concept) -> Concept:
        c_type: ConceptType = c.type
        replaced_concepts: list[Concept] = [ci.replace(a, c) for ci in self.concepts]
        if c_type == ConceptType.AND:
            return OperatorConcept.and_(replaced_concepts)
        elif c_type == ConceptType.GOEDEL_AND:
            return OperatorConcept.goedel_and(replaced_concepts)
        elif c_type == ConceptType.LUKASIEWICZ_AND:
            return OperatorConcept.lukasiewicz_and(replaced_concepts)
        if c_type == ConceptType.OR:
            return OperatorConcept.or_(replaced_concepts)
        elif c_type == ConceptType.GOEDEL_AND:
            return OperatorConcept.goedel_or(replaced_concepts)
        elif c_type == ConceptType.LUKASIEWICZ_AND:
            return OperatorConcept.lukasiewicz_or(replaced_concepts)
        elif c_type == ConceptType.COMPLEMENT:
            if self.concepts[0] == a:
                return -c
            return self

    def compute_name(self) -> typing.Optional[str]:
        concepts: str = " ".join(map(str, self.concepts))
        if self.type == ConceptType.AND:
            return f"(and {concepts})"
        elif self.type == ConceptType.GOEDEL_AND:
            return f"(g-and {concepts})"
        elif self.type == ConceptType.LUKASIEWICZ_AND:
            return f"(l-and {concepts})"
        elif self.type == ConceptType.OR:
            return f"(or {concepts})"
        elif self.type == ConceptType.GOEDEL_OR:
            return f"(g-or {concepts})"
        elif self.type == ConceptType.LUKASIEWICZ_OR:
            return f"(l-or {concepts})"
        elif self.type == ConceptType.COMPLEMENT:
            return f"(not {concepts})"

    def compute_atomic_concepts(self) -> set[Concept]:
        result: set[Concept] = set()
        for c in self.concepts:
            result.update(c.compute_atomic_concepts())
        return result

    def get_roles(self) -> set[str]:
        return set().union(*[c.get_roles() for c in self.concepts])

    def __neg__(self) -> Concept:
        concepts: list[Concept] = [-ci for ci in self.concepts]
        if self.type == ConceptType.AND:
            return OperatorConcept.or_(*concepts)
        elif self.type == ConceptType.GOEDEL_AND:
            return OperatorConcept.goedel_or(*concepts)
        elif self.type == ConceptType.LUKASIEWICZ_AND:
            return OperatorConcept.lukasiewicz_or(*concepts)
        elif self.type == ConceptType.OR:
            return OperatorConcept.and_(*concepts)
        elif self.type == ConceptType.GOEDEL_OR:
            return OperatorConcept.goedel_and(*concepts)
        elif self.type == ConceptType.LUKASIEWICZ_OR:
            return OperatorConcept.lukasiewicz_and(*concepts)
        elif self.type == ConceptType.COMPLEMENT:
            return self.concepts[0]
        raise NotImplementedError

    def __and__(self, value: typing.Self) -> typing.Self:
        if OperatorConcept.is_and(self.type):
            return OperatorConcept.__op(self.type, [self, value])
        elif OperatorConcept.is_or(self.type):
            return OperatorConcept.__op(
                OperatorConcept.OPERATORS[self.type], [self, value]
            )
        return OperatorConcept.and_([self, value])

    def __or__(self, value: typing.Self) -> typing.Self:
        if OperatorConcept.is_or(self.type):
            return OperatorConcept.__op(self.type, [self, value])
        elif OperatorConcept.is_and(self.type):
            return OperatorConcept.__op(
                OperatorConcept.OPERATORS[self.type], [self, value]
            )
        return OperatorConcept.or_([self, value])

    def __eq__(self, value: typing.Self) -> bool:
        return isinstance(value, OperatorConcept) and str(self) == str(value)

    def __ne__(self, value: typing.Self) -> bool:
        return not (self == value)

    def __hash__(self) -> int:
        return hash(str(self))


# class Not(OperatorConcept):
#     def __call__(self, *args) -> typing.Self:
#         return OperatorConcept.not_(args)


# class And(OperatorConcept):
#     def __call__(self, *args) -> typing.Self:
#         return OperatorConcept.and_(args)


# class GoedelAnd(OperatorConcept):
#     def __call__(self, *args) -> typing.Self:
#         return OperatorConcept.goedel_and(args)


# class LukasiewiczAnd(OperatorConcept):
#     def __call__(self, *args) -> typing.Self:
#         return OperatorConcept.lukasiewicz_and(args)


# class Or(OperatorConcept):
#     def __call__(self, *args) -> typing.Self:
#         return OperatorConcept.or_(args)


# class GoedelOr(OperatorConcept):
#     def __call__(self, *args) -> typing.Self:
#         return OperatorConcept.goedel_or(args)


# class LukasiewiczOr(OperatorConcept):
#     def __call__(self, *args) -> typing.Self:
#         return OperatorConcept.lukasiewicz_or(args)


Not = OperatorConcept.not_
And = OperatorConcept.and_
GoedelAnd = OperatorConcept.goedel_and
LukasiewiczAnd = OperatorConcept.lukasiewicz_and
Or = OperatorConcept.or_
GoedelOr = OperatorConcept.goedel_or
LukasiewiczOr = OperatorConcept.lukasiewicz_or
