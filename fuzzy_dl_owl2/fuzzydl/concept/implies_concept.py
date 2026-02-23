import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface import (
    HasConceptsInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import (
    And,
    GoedelAnd,
    GoedelOr,
    LukasiewiczOr,
    Not,
    OperatorConcept,
    Or,
)
from fuzzy_dl_owl2.fuzzydl.concept.truth_concept import TruthConcept
from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType, FuzzyLogic
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class ImpliesConcept(Concept, HasConceptsInterface):
    """
    Represents a logical implication relationship between two concepts—an antecedent and a consequent—within a fuzzy description logic framework. It supports specific fuzzy semantics such as Zadeh and Goedel implications, while also providing static utility methods to compute Lukasiewicz and Kleene-Dienes implications that dynamically adapt based on whether the underlying logic is classical or fuzzy. The class manages the structural composition of the implication, enabling operations such as cloning, replacing sub-concepts, extracting atomic concepts and roles, and generating string representations for the logical expression.

    :param name: String representation of the implication, generated based on the operator type and the string representations of the antecedent and consequent concepts.
    :type name: str
    """


    def __init__(self, c_type: ConceptType, concepts: list[Concept]) -> None:
        """
        Initializes an implication concept representing a logical relationship between a list of child concepts using a specific fuzzy logic operator. The constructor validates that the provided concept type is strictly limited to either Zadeh or Gödel implication, raising an assertion error if any other type is supplied. It performs initialization for both the `Concept` and `HasConceptsInterface` base classes and automatically computes and assigns a descriptive name to the instance.

        :param c_type: The specific implication logic type, which must be either Zadeh or Gödel implication.
        :type c_type: ConceptType
        :param concepts: A list of Concept objects representing the operands of the implication.
        :type concepts: list[Concept]
        """

        Concept.__init__(self, c_type)
        HasConceptsInterface.__init__(self, concepts)

        assert c_type in (
            ConceptType.ZADEH_IMPLIES,
            ConceptType.GOEDEL_IMPLIES,
        )

        self.name: str = self.compute_name()

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of `ImpliesConcept` that is a shallow copy of the current object. The new instance preserves the original's type attribute and constructs a new list containing references to the original concepts. While the list container itself is distinct, modifications to mutable objects within the concepts list will be reflected in both the original and the clone.

        :return: A new instance of the class with the same type and a shallow copy of the concepts list.

        :rtype: typing.Self
        """

        return ImpliesConcept(self.type, [c for c in self.concepts])

    @staticmethod
    def lukasiewicz_implies(c1: Concept, c2: Concept) -> Concept:
        """
        Computes the logical implication of the first concept by the second concept ($c1 \to c2$) using Łukasiewicz logic semantics. The function optimizes the resulting expression by handling specific edge cases: if the antecedent is the top concept, the consequent is returned; if the consequent is the top concept or the antecedent is the bottom concept, the top concept is returned; and if the consequent is the bottom concept, the negation of the antecedent is returned. If the global knowledge base semantics are set to classical logic, the implication is resolved as a standard logical disjunction of the negated antecedent and the consequent; otherwise, it is represented as a Łukasiewicz disjunction.

        :param c1: The antecedent concept (the "if" part) in the logical implication.
        :type c1: Concept
        :param c2: The consequent concept in the logical implication.
        :type c2: Concept

        :return: A Concept representing the logical implication of c1 by c2, calculated using either classical material implication or Łukasiewicz implication depending on the current knowledge base semantics.

        :rtype: Concept
        """

        if c1.type == ConceptType.TOP:
            return c2
        if c2.type == ConceptType.TOP or c1.type == ConceptType.BOTTOM:
            return TruthConcept.get_top()
        if c2.type == ConceptType.BOTTOM:
            return -c1
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL:
            return Or(-c1, c2)
        return LukasiewiczOr(-c1, c2)

    @staticmethod
    def kleene_dienes_implies(c1: Concept, c2: Concept) -> Concept:
        """
        Computes the Kleene-Dienes implication between two concepts, representing the logical statement that the first concept implies the second. The method optimizes for boundary conditions by returning the consequent if the antecedent is Top, or returning Top if the antecedent is Bottom or the consequent is Top. For the general case, the implementation depends on the global knowledge base semantics: under Classical logic, it returns the standard disjunction of the negation of the first concept and the second concept, while in other contexts it utilizes the Gödel disjunction operator.

        :param c1: The antecedent concept of the implication.
        :type c1: Concept
        :param c2: The consequent concept in the implication operation.
        :type c2: Concept

        :return: A Concept representing the Kleene-Dienes implication of `c1` implies `c2`.

        :rtype: Concept
        """

        if c1.type == ConceptType.TOP:
            return c2
        if c2.type == ConceptType.TOP or c1.type == ConceptType.BOTTOM:
            return TruthConcept.get_top()
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL:
            return Or(-c1, c2)
        return GoedelOr(-c1, c2)

    @staticmethod
    def goedel_implies(c1: Concept, c2: Concept) -> Concept:
        """
        Computes the logical implication of `c1` implies `c2` according to Gödel logic semantics, with fallback to classical logic if specified by the global knowledge base settings. The function performs immediate simplification for boundary conditions: if the antecedent `c1` is the Top concept, the consequent `c2` is returned; if the consequent `c2` is Top or the antecedent is Bottom, the Top concept is returned. When operating under classical logic, the implication is resolved to the material implication `Or(-c1, c2)`. Additionally, if the antecedent is a Gödel disjunction, the method distributes the implication across the disjuncts, resulting in a conjunction of individual implications. If no simplifications apply, a new `ImpliesConcept` instance is created to represent the operation.

        :param c1: The antecedent concept (the premise) of the Gödel implication.
        :type c1: Concept
        :param c2: The consequent concept in the implication.
        :type c2: Concept

        :return: A Concept representing the Gödel implication of `c1` implies `c2`, potentially simplified based on the input types or logic semantics.

        :rtype: Concept
        """

        if c1.type == ConceptType.TOP:
            return c2
        if c2.type == ConceptType.TOP or c1.type == ConceptType.BOTTOM:
            return TruthConcept.get_top()
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL:
            return Or(-c1, c2)
        if c1.type == ConceptType.GOEDEL_OR:
            return GoedelAnd(
                [GoedelOr(ci, c2) for ci in typing.cast(OperatorConcept, c1).concepts]
            )
        return ImpliesConcept(ConceptType.GOEDEL_IMPLIES, [c1, c2])

    @staticmethod
    def zadeh_implies(c1: Concept, c2: Concept) -> Concept:
        """
        Generates a logical implication relationship between two concepts, `c1` and `c2`, utilizing Zadeh's implication logic or classical logic depending on the system configuration. If the global `KNOWLEDGE_BASE_SEMANTICS` constant is set to `FuzzyLogic.CLASSICAL`, the method simplifies the implication to the standard material implication form, returning a disjunction of the negation of `c1` and `c2`. In all other cases, it constructs and returns a specialized `ImpliesConcept` instance with the type `ZADEH_IMPLIES`, preserving the specific fuzzy logic semantics for the operands.

        :param c1: The antecedent concept for the implication operation.
        :type c1: Concept
        :param c2: The consequent concept in the implication.
        :type c2: Concept

        :return: A Concept representing the logical implication between `c1` and `c2`, calculated using either classical material implication or Zadeh's implication operator depending on the current knowledge base semantics.

        :rtype: Concept
        """

        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL:
            return Or(-c1, c2)
        return ImpliesConcept(ConceptType.ZADEH_IMPLIES, [c1, c2])

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Recursively replaces occurrences of concept `a` with concept `c` within the left and right operands of the current implication. The method traverses the sub-concepts to apply the replacement and returns a new concept without modifying the original. The structure of the returned concept depends on the type of `c`: it returns a new Goedel implication if `c` is a Goedel implication, or a negated Goedel implication if `c` is a negated Goedel implication. The method raises an error if the replacement concept `c` is not one of these two implication types.

        :param a: The concept to be replaced by `c`.
        :type a: Concept
        :param c: The concept to substitute in place of `a`.
        :type c: Concept

        :return: A new Concept where all occurrences of `a` have been replaced with `c`.

        :rtype: Concept
        """

        c_type: ConceptType = c.type
        if c_type == ConceptType.GOEDEL_IMPLIES:
            return ImpliesConcept.goedel_implies(
                self.concepts[0].replace(a, c), self.concepts[1].replace(a, c)
            )
        elif c_type == ConceptType.NOT_GOEDEL_IMPLIES:
            return Not(
                ImpliesConcept.goedel_implies(
                    self.concepts[0].replace(a, c), self.concepts[1].replace(a, c)
                )
            )
        Util.error(f"Error replacing in concept {self}")

    def compute_name(self) -> typing.Optional[str]:
        """
        Generates a string representation of the implication concept based on its specific type. If the type is identified as Gödel implication, the method returns a formatted string prefixed with 'g-implies' followed by the first two associated concepts. Similarly, for Zadeh implication, it returns a string prefixed with 'z-implies'. If the concept type does not match either of these defined categories, the method returns None.

        :return: A formatted string representing the concept name for supported implication types, or None if the concept type is not handled.

        :rtype: typing.Optional[str]
        """

        if self.type == ConceptType.GOEDEL_IMPLIES:
            return f"(g-implies {self.concepts[0]} {self.concepts[1]})"
        elif self.type == ConceptType.ZADEH_IMPLIES:
            return f"(z-implies {self.concepts[0]} {self.concepts[1]})"

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Computes the set of atomic concepts comprising this implication by recursively traversing its operands. It aggregates the atomic concepts from both the antecedent and consequent concepts into a single, deduplicated set. This method is a pure function with no side effects, as it only reads the structure of the concept hierarchy without modifying it; however, it may raise an error or enter infinite recursion if the underlying concept graph is malformed or contains cycles.

        :return: A set containing the union of atomic concepts derived from the object's two component concepts.

        :rtype: set[Concept]
        """

        result: set[Concept] = set()
        result.update(self.concepts[0].compute_atomic_concepts())
        result.update(self.concepts[1].compute_atomic_concepts())
        return result

    def get_roles(self) -> set[str]:
        """
        Retrieves the union of roles associated with the two underlying concepts contained within this implication. It aggregates the results of calling `get_roles` on the first and second concepts, returning a set of unique strings that represents all roles present in either component. This method is a read-only operation and does not alter the state of the object or its child concepts.

        :return: A set containing the union of roles from the first and second concepts.

        :rtype: set[str]
        """

        return self.concepts[0].get_roles() | self.concepts[1].get_roles()

    def __neg__(self) -> Concept:
        """
        Implements the unary negation operator for the implication concept, allowing the use of the minus sign to represent logical negation. This method returns a new `Concept` instance that wraps the current object within a `Not` construct, effectively representing the logical inverse of the implication. The operation is side-effect free, as it generates a new object rather than modifying the existing instance.

        :return: A new Concept representing the logical negation of the current concept.

        :rtype: Concept
        """

        return Not(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Overloads the bitwise AND operator (`&`) to perform a logical conjunction between the current instance and another concept. It accepts another instance of the same type and returns a new object representing the logical AND of the two operands. This enables the construction of compound logical expressions using standard Python syntax, leaving the original operands unchanged.

        :param value: The right-hand operand to combine with the current instance using a logical AND.
        :type value: typing.Self

        :return: Returns an object representing the result of the AND operation between the current instance and the provided value.

        :rtype: typing.Self
        """

        return And(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        This method implements the bitwise OR operator (`|`) to create a logical disjunction between the current instance and another value. It returns a new object representing the combination of the two operands, allowing for syntactic sugar when defining logical relationships. The operation does not modify the original instances but instead produces a new `Or` object that encapsulates both the current concept and the provided value.

        :param value: The right-hand operand to combine with the current instance using the OR operator.
        :type value: typing.Self

        :return: Returns a new object representing the logical OR of the current instance and the provided value.

        :rtype: typing.Self
        """

        return Or(self, value)

    def __hash__(self) -> int:
        """
        Calculates the hash value for the instance, enabling it to be used as a dictionary key or stored in a set. The hash is derived from the object's string representation, meaning that two objects with identical string outputs will produce the same hash. Because the hash depends on the result of `str(self)`, any changes to the object's state that modify its string representation will also change its hash value.

        :return: An integer hash value derived from the object's string representation.

        :rtype: int
        """

        return hash(str(self))

    def __eq__(self, value: typing.Self) -> bool:
        """
        Determines equality between the current instance and another object by verifying both type identity and string representation equivalence. The method returns true only if the provided value is an instance of `ImpliesConcept` and its string form exactly matches the string form of the current object. This comparison relies on the `__str__` implementation, meaning that objects are considered equal if they serialize to the same string, regardless of potential internal differences not reflected in that representation.

        :param value: The object to compare with the current instance.
        :type value: typing.Self

        :return: True if the provided value is an instance of ImpliesConcept and its string representation matches that of this object, otherwise False.

        :rtype: bool
        """

        return isinstance(value, ImpliesConcept) and str(self) == str(value)


# class ZadehImplies(ImpliesConcept):
#     def implies(self, c: Concept) -> typing.Self:
#         return ImpliesConcept.zadeh_implies(self, c)


# class GoedelImplies(ImpliesConcept):
#     def implies(self, c: Concept) -> typing.Self:
#         return ImpliesConcept.goedel_implies(self, c)


# class LukasiewiczImplies(ImpliesConcept):
#     def implies(self, c: Concept) -> typing.Self:
#         return ImpliesConcept.lukasiewicz_implies(self, c)


# class KleeneDienesImplies(ImpliesConcept):
#     def implies(self, c: Concept) -> typing.Self:
#         return ImpliesConcept.kleene_dienes_implies(self, c)

ZadehImplies = ImpliesConcept.zadeh_implies
GoedelImplies = ImpliesConcept.goedel_implies
LukasiewiczImplies = ImpliesConcept.lukasiewicz_implies
KleeneDienesImplies = ImpliesConcept.kleene_dienes_implies
