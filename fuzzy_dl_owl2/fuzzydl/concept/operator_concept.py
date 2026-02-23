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
    """
    This class serves as a representation of logical operators—specifically conjunctions, disjunctions, and negations—within a fuzzy description logic system. It extends the base `Concept` class to support the construction and manipulation of complex logical expressions using various fuzzy logic semantics, such as classical, Lukasiewicz, and Zadeh (Goedel). Users can create operator concepts through static factory methods like `and_`, `or_`, and `not_`, which dynamically determine the specific operator type based on the global knowledge base semantics or allow for explicit selection of fuzzy variants. Beyond construction, the class offers a suite of methods for logical simplification and normalization, including the application of De Morgan's laws, reduction of double negations, distribution of operators, and conversion to Conjunctive or Disjunctive Normal Forms (CNF/DNF). It also integrates with quantifier logic by merging `AllSomeConcept` instances and supports operator overloading for `&`, `|`, and unary `-` to enable syntactically natural logical operations.

    :param AND_OPERATORS: Concept types identifying conjunction operators for classical, Lukasiewicz, and Goedel fuzzy logic semantics.
    :type AND_OPERATORS: list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
    :param OR_OPERATORS: A list of ConceptType values representing all supported disjunction operators, covering classical, Gödel, and Łukasiewicz semantics.
    :type OR_OPERATORS: list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
    :param BINARY_OPERATORS: A list of concept types representing all binary logical operators, encompassing both conjunction and disjunction variants.
    :type BINARY_OPERATORS: list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
    :param COMPLEMENT_LAW_OPERATORS: Operators for which the complement law holds, allowing the simplification of expressions containing a concept and its negation.
    :type COMPLEMENT_LAW_OPERATORS: list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
    :param DISTRIBUTIVE_OPERATORS: A list of operator types that satisfy distributive laws, comprising classical and Goedel conjunctions and disjunctions.
    :type DISTRIBUTIVE_OPERATORS: list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
    :param ABSORPTION_OPERATORS: A list of operator types (AND, OR, and their Gödel variants) for which absorption laws apply, used during logical simplification.
    :type ABSORPTION_OPERATORS: list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
    :param ALL_OPERATORS: A list of all valid operator concept types, including binary conjunctions and disjunctions across various fuzzy logic semantics, as well as the complement operator.
    :type ALL_OPERATORS: list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
    :param OPERATORS: Maps each binary operator type to its logical dual (e.g., AND to OR), used for applying De Morgan's laws and distribution.
    :type OPERATORS: dict[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
    :param type: The specific logical operator and fuzzy semantics (e.g., AND, OR, COMPLEMENT, or their variants) defining the concept's behavior in logical operations, simplifications, and string representation.
    :type type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
    :param name: Computed string representation of the operator concept, automatically generated based on the operator type and its operands.
    :type name: typing.Any

    :raises NotImplementedError: Raised when attempting to negate an operator concept whose type is not one of the recognized logical operators (AND, OR, COMPLEMENT, or their fuzzy variants).
    """

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
        """
        Initializes an OperatorConcept instance with a specific type and a collection of child concepts. The provided type is validated against the class's defined set of valid operators to ensure it is supported. This method sets up the object by invoking the initialization logic of the parent Concept class and the HasConceptsInterface, and finally derives the instance's name from the provided configuration.

        :param c_type: The specific operator type for the concept. Must be a valid member of OperatorConcept.ALL_OPERATORS.
        :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
        :param concepts: An iterable of Concept objects to be associated with this operator, typically serving as its operands or children.
        :type concepts: typing.Iterable[Concept]
        """

        Concept.__init__(self, c_type, None)
        HasConceptsInterface.__init__(self, concepts)

        assert c_type in OperatorConcept.ALL_OPERATORS, f"Type {c_type} is not valid."

        self.type: ConceptType = c_type
        self.name = self.compute_name()

    @property
    def concepts(self) -> list[Concept]:
        """
        Updates the collection of concepts associated with the operator by accepting an iterable of Concept objects. The provided iterable is converted to a list and stored internally, ensuring that the underlying data structure is mutable and indexable. As a side effect of this assignment, the operator's name is automatically recalculated to reflect the new set of concepts.

        :param value: The collection of Concept objects to assign to the instance, replacing the current concepts and triggering a name update.
        :type value: typing.Iterable[Concept]
        """

        return self._concepts

    @concepts.setter
    def concepts(self, value: typing.Iterable[Concept]) -> None:
        self._concepts = list(value)
        self.name = self.compute_name()

    def clone(self) -> Concept:
        """
        Generates a shallow copy of the current `OperatorConcept` instance, preserving its type and associated concepts. The returned object is a new instance containing a shallow copy of the original's concept list, ensuring that structural modifications to the list do not affect the source object. However, because the copy is shallow, any mutable objects referenced within the concepts list remain shared between the original and the clone.

        :return: A new Concept instance that is a copy of the current object.

        :rtype: Concept
        """

        return OperatorConcept(
            self.type,
            [c for c in self.concepts],
        )

    @staticmethod
    def __op(c_type: ConceptType, concepts: typing.Iterable[Concept]) -> Concept:
        """
        Constructs a `Concept` representing the specified logical operation applied to the provided iterable of concepts, performing normalization to ensure a canonical form. If the operation type is not a complement and only a single concept is provided, the method returns that concept directly rather than wrapping it. For binary operators, the method recursively flattens the structure by merging any nested operators of the same type into the current list of arguments. The final list of concepts is sorted before being encapsulated in a new `OperatorConcept` instance, and an assertion error is raised if the input iterable is empty.

        :param c_type: The type of the operator concept to create, determining how the input concepts are combined or flattened.
        :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
        :param concepts: The concepts to be combined into the resulting operator concept. The iterable is flattened to merge nested concepts of the same type and sorted before construction.
        :type concepts: typing.Iterable[Concept]

        :return: A normalized `Concept` representing the logical operation defined by `c_type` applied to `concepts`, where nested operators of the same type are flattened and the resulting concepts are sorted.

        :rtype: Concept
        """

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
        """
        Creates a new `Concept` representing the logical conjunction of the provided input concepts. The specific semantic interpretation of the conjunction is determined by the global `KNOWLEDGE_BASE_SEMANTICS` setting. If the semantics are set to `CLASSICAL`, it returns a concept in classical Conjunctive Normal Form. For `LUKASIEWICZ` semantics, it applies Lukasiewicz fuzzy logic, and for `ZADEH` semantics, it applies Goedel fuzzy logic. This method acts as a factory for `OperatorConcept` instances, adapting the underlying operator based on the current configuration.

        :param concepts: The Concept instances to be combined using logical conjunction.
        :type concepts: Concept

        :return: A Concept representing the logical conjunction of the input concepts, calculated according to the active knowledge base semantics.

        :rtype: Concept
        """

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
        """
        Constructs a logical conjunction using Gödel logic semantics from a variable number of input concepts. This static method instantiates an `OperatorConcept` representing the AND operation and immediately normalizes the result into Conjunctive Normal Form (CNF) before returning it. The behavior ensures that the resulting structure is flattened and standardized according to the framework's logic rules, regardless of the complexity or quantity of the input concepts.

        :param concepts: The Concept instances to be combined using the Gödel AND operator.
        :type concepts: Concept

        :return: A Concept representing the Gödel logic conjunction of the input concepts, converted to Conjunctive Normal Form (CNF).

        :rtype: Concept
        """

        return OperatorConcept.__op(ConceptType.GOEDEL_AND, concepts).goedel_cnf()

    @staticmethod
    def lukasiewicz_and(*concepts: Concept) -> Concept:
        """
        Creates a new Concept representing the Łukasiewicz logical conjunction of the provided input concepts. This static method instantiates an operator node of type LUKASIEWICZ_AND and immediately converts the resulting structure into Conjunctive Normal Form (CNF) to standardize its representation. It accepts a variable number of Concept arguments, returning a single Concept that encapsulates the combined logic in its normalized form.

        :param concepts: The concepts to be combined using the Łukasiewicz AND operation.
        :type concepts: Concept

        :return: A Concept representing the Łukasiewicz logical conjunction of the provided concepts.

        :rtype: Concept
        """

        return OperatorConcept.__op(
            ConceptType.LUKASIEWICZ_AND, concepts
        ).lukasiewicz_cnf()

    @staticmethod
    def or_(*concepts: Concept) -> Concept:
        """
        Constructs a new Concept representing the logical disjunction of the provided input concepts. The specific logic applied depends on the global `constants.KNOWLEDGE_BASE_SEMANTICS` setting, supporting Classical, Lukasiewicz, and Zadeh (Gödel) semantics. The resulting operator concept is transformed into Conjunctive Normal Form (CNF) using the method corresponding to the active logic before being returned. This method relies on external configuration state to determine its behavior.

        :param concepts: A variable number of Concept instances to be combined via logical disjunction.
        :type concepts: Concept

        :return: A Concept representing the logical disjunction of the input concepts, calculated according to the current knowledge base semantics.

        :rtype: Concept
        """

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
        """
        Constructs a logical concept representing the Gödelian disjunction (OR) of the provided input concepts. This static method accepts a variable number of Concept instances and generates an `OperatorConcept` defined by the `GOEDEL_OR` type. Crucially, the resulting concept is immediately transformed into Conjunctive Normal Form (CNF) before being returned, which standardizes the structure for subsequent logical operations. The method expects at least one operand; providing zero arguments may lead to unexpected behavior or errors depending on the internal implementation of the operator factory.

        :param concepts: One or more Concept instances to be combined using the Gödel OR operation.
        :type concepts: Concept

        :return: A Concept representing the Gödel OR of the input concepts, converted to Conjunctive Normal Form (CNF).

        :rtype: Concept
        """

        return OperatorConcept.__op(ConceptType.GOEDEL_OR, concepts).goedel_cnf()

    @staticmethod
    def lukasiewicz_or(*concepts: Concept) -> Concept:
        """
        Computes the Łukasiewicz disjunction (bounded sum) for a variable number of input concepts. This method constructs an operator node representing the logical operation and immediately normalizes the result into Conjunctive Normal Form (CNF) specific to the Łukasiewicz logic system. It returns a new `Concept` instance representing this normalized logical expression without modifying the original input concepts.

        :param concepts: Variable number of concepts to be combined using the Łukasiewicz OR logic.
        :type concepts: Concept

        :return: A Concept representing the Łukasiewicz disjunction of the provided concepts, converted to Conjunctive Normal Form.

        :rtype: Concept
        """

        return OperatorConcept.__op(
            ConceptType.LUKASIEWICZ_OR, concepts
        ).lukasiewicz_cnf()

    @staticmethod
    def not_(concept: Concept) -> Concept:
        """
        Computes the logical complement of the provided concept, performing immediate simplifications where possible. If the input concept represents the universal set (Top), the method returns the empty set (Bottom), and vice versa. In cases of double negation, where the input is already a complement operator, the method unwraps and returns the original inner concept. For all other inputs, it constructs and returns a new complement operator node wrapping the provided concept.

        :param concept: The concept to apply logical negation to.
        :type concept: Concept

        :return: The logical complement of the input concept, handling double negation and specific truth values.

        :rtype: Concept
        """

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
        """
        Determines whether the provided concept type represents a logical OR operation by verifying its membership in the class-level collection of OR operators. This static method returns `True` if the input type is found within `OperatorConcept.OR_OPERATORS` and `False` otherwise, serving as a type-checking utility without causing any side effects.

        :param c_type: The concept type to check if it represents an OR operator.
        :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType

        :return: True if the concept type is an OR operator, False otherwise.

        :rtype: bool
        """

        return c_type in OperatorConcept.OR_OPERATORS

    @staticmethod
    def is_and(c_type: ConceptType) -> bool:
        """
        Determines whether the provided concept type represents a logical AND operation by verifying its presence in the class's collection of AND operators. This method returns `True` if the input matches one of the defined AND operator types, and `False` otherwise. It performs a read-only check without modifying any state, and it safely returns `False` for any input type that is not explicitly listed as an AND operator.

        :param c_type: The concept type to verify if it represents an AND operator.
        :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType

        :return: True if the provided concept type is an AND operator, False otherwise.

        :rtype: bool
        """

        return c_type in OperatorConcept.AND_OPERATORS

    @staticmethod
    def is_not_type(op: Concept, c_type: ConceptType) -> bool:
        """
        Determines whether a given concept represents a logical negation of a specific concept type. The method first verifies that the input `op` is an instance of `OperatorConcept` and that its type is `COMPLEMENT`. If these structural conditions are not met, the function returns `False`. Otherwise, it checks if the type of the first nested concept within the operator matches the provided `c_type` argument and returns the result of that comparison.

        :param op: The concept to check, which should represent a logical complement (negation) of the specified type.
        :type op: Concept
        :param c_type: The specific type to match against the operand of the complement operator.
        :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType

        :return: True if the provided concept is a complement operator acting on a concept of the specified type, otherwise False.

        :rtype: bool
        """

        if not isinstance(op, OperatorConcept):
            return False
        if op.type != ConceptType.COMPLEMENT:
            return False
        return op.concepts[0].type == c_type

    @staticmethod
    def is_not_fuzzy_number(op: Concept) -> bool:
        """
        Determines whether the provided concept is not classified as a fuzzy number. This static method serves as a specific type guard, verifying that the input concept does not correspond to the `FUZZY_NUMBER` category within the system's type hierarchy. It returns `True` if the concept is of any other type, and `False` if it is specifically identified as a fuzzy number.

        :param op: The concept to verify is not a fuzzy number.
        :type op: Concept

        :return: True if the provided concept is not a fuzzy number, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.FUZZY_NUMBER)

    @staticmethod
    def is_not_concrete(op: Concept) -> bool:
        """
        Determines whether the provided `Concept` instance is not classified as a concrete type. This static method acts as a specific predicate that delegates to the underlying `is_not_type` utility, passing the `ConceptType.CONCRETE` enum value to perform the check. It returns `True` if the concept is abstract, undefined, or any other non-concrete type, and `False` only if the concept is explicitly concrete.

        :param op: The concept to check for non-concreteness.
        :type op: Concept

        :return: True if the concept is not concrete, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.CONCRETE)

    @staticmethod
    def is_not_has_value(op: Concept) -> bool:
        """
        Determines whether the provided concept is not of the `HAS_VALUE` type. This static method acts as a specific predicate, delegating to the underlying type-checking logic to verify the concept's classification. It returns `True` if the concept's type differs from `HAS_VALUE`, and `False` otherwise, without modifying the input object.

        :param op: The concept to verify is not of type HAS_VALUE.
        :type op: Concept

        :return: True if the concept is not of type HAS_VALUE, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.HAS_VALUE)

    @staticmethod
    def is_not_goedel_implies(op: Concept) -> bool:
        """
        Determines whether the provided concept is not a Gödel implication operator. This static method checks the type of the input concept against the `ConceptType.GOEDEL_IMPLIES` enumeration value. It returns `True` if the concept's type does not match the Gödel implication type, and `False` if it does. The function performs a read-only check and does not modify the state of the input concept.

        :param op: The concept to verify is not a Gödel implication.
        :type op: Concept

        :return: True if the concept is not a Gödel implies operator, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.GOEDEL_IMPLIES)

    @staticmethod
    def is_not_at_most_value(op: Concept) -> bool:
        """
        Determines whether the provided concept is not of the AT_MOST_VALUE type. This static method evaluates the input concept and returns True if its type differs from AT_MOST_VALUE, effectively filtering out concepts that represent this specific constraint. The check is performed by delegating to the is_not_type method, ensuring consistent type validation logic without modifying the input object.

        :param op:
        :type op: Concept

        :return: True if the provided concept is not of type AT_MOST_VALUE, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.AT_MOST_VALUE)

    @staticmethod
    def is_not_at_least_value(op: Concept) -> bool:
        """
        Determines whether the provided `Concept` object does not represent an "at least value" operator. This static method acts as a specific type guard by delegating the type comparison to the `is_not_type` method, passing `ConceptType.AT_LEAST_VALUE` as the target type to exclude. It returns `True` if the concept's type differs from the specified value, and `False` if it matches.

        :param op: The concept instance to verify is not of type AT_LEAST_VALUE.
        :type op: Concept

        :return: True if the provided concept is not of type AT_LEAST_VALUE, otherwise False.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.AT_LEAST_VALUE)

    @staticmethod
    def is_not_exact_value(op: Concept) -> bool:
        """
        Determines whether the provided concept does not represent an exact value. This method serves as a specific type guard, checking if the concept's type differs from `ConceptType.EXACT_VALUE` by delegating to the generic `is_not_type` method. It returns `True` for concepts that are operators, variables, or other non-literal entities, and `False` only if the concept is explicitly classified as an exact value. The operation is read-only and does not modify the input object.

        :param op: The concept to verify is not an exact value.
        :type op: Concept

        :return: True if the concept is not an exact value, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.EXACT_VALUE)

    @staticmethod
    def is_not_weighted(op: Concept) -> bool:
        """
        Determines whether the provided operator concept is not classified as a weighted operator. This static method acts as a specific predicate that checks if the concept's type differs from `ConceptType.WEIGHTED`. It delegates the actual type verification to the `is_not_type` method, returning `True` if the concept is not weighted and `False` otherwise.

        :param op: The concept to verify is not of type WEIGHTED.
        :type op: Concept

        :return: True if the concept is not weighted, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.WEIGHTED)

    @staticmethod
    def is_not_weighted_min(op: Concept) -> bool:
        """
        Determines whether the provided operator concept is not classified as a weighted minimum. This static method evaluates the type of the input concept and returns True if it does not correspond to the weighted minimum operator type (`ConceptType.W_MIN`). The function performs a read-only check and does not modify the state of the input object.

        :param op: The concept to verify is not a weighted minimum operator.
        :type op: Concept

        :return: True if the concept is not a weighted minimum operator, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.W_MIN)

    @staticmethod
    def is_not_weighted_max(op: Concept) -> bool:
        """
        Determines whether the provided operator concept is not a weighted maximum operator. This static method checks the concept's type against `ConceptType.W_MAX` and returns `True` if they do not match, indicating that the concept represents a different kind of operation. The function performs a read-only check and does not modify the input object.

        :param op: The concept to verify is not a weighted maximum operator.
        :type op: Concept

        :return: True if the provided concept is not a weighted maximum operator, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.W_MAX)

    @staticmethod
    def is_not_weighted_sum(op: Concept) -> bool:
        """
        Determines whether the provided concept is not a weighted sum operation. This static method serves as a specific type check, evaluating the input concept against the `ConceptType.W_SUM` identifier. It returns `True` if the concept is of any type other than a weighted sum, and `False` if it matches that specific classification.

        :param op: The concept to verify is not a weighted sum operation.
        :type op: Concept

        :return: True if the input concept is not a weighted sum operation, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.W_SUM)

    @staticmethod
    def is_not_weighted_sum_zero(op: Concept) -> bool:
        """
        Determines whether the provided `Concept` instance does not represent a weighted sum zero operation. This static method checks the type of the input concept against `ConceptType.W_SUM_ZERO` and returns `True` if the types do not match. It serves as a specific type guard to identify concepts that are not weighted sum zero, performing no modifications to the input object.

        :param op: The concept to verify is not of the weighted sum zero type.
        :type op: Concept

        :return: True if the concept is not a weighted sum zero, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.W_SUM_ZERO)

    @staticmethod
    def is_not_pos_threshold(op: Concept) -> bool:
        """
        Determines whether the provided concept is not classified as a positive threshold. This static method evaluates the input concept against the `POS_THRESHOLD` type definition, returning `True` if the concept differs from this specific type and `False` otherwise. It acts as a specific predicate wrapper, delegating the actual type comparison to the underlying `is_not_type` method. The function does not modify the input object and has no side effects.

        :param op: The concept to verify is not of type POS_THRESHOLD.
        :type op: Concept

        :return: True if the concept is not of type POS_THRESHOLD, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.POS_THRESHOLD)

    @staticmethod
    def is_not_neg_threshold(op: Concept) -> bool:
        """
        Determines whether the provided concept is not classified as a negative threshold. This method acts as a specific type guard, returning True if the concept's type differs from `ConceptType.NEG_THRESHOLD`. It performs a read-only check without modifying the input object or any external state.

        :param op: The concept to check against the NEG_THRESHOLD type.
        :type op: Concept

        :return: True if the concept is not a negative threshold, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.NEG_THRESHOLD)

    @staticmethod
    def is_not_ext_pos_threshold(op: Concept) -> bool:
        """
        Determines whether the provided concept is not of the external positive threshold type. This static method acts as a specific type check, returning `True` if the concept's type differs from `ConceptType.EXT_POS_THRESHOLD` and `False` if it matches. It delegates the actual comparison logic to the `is_not_type` method.

        :param op: The concept to verify is not of type EXT_POS_THRESHOLD.
        :type op: Concept

        :return: True if the provided concept is not an external positive threshold, otherwise False.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.EXT_POS_THRESHOLD)

    @staticmethod
    def is_not_ext_neg_threshold(op: Concept) -> bool:
        """
        Determines whether the provided concept is not classified as an external negative threshold. This static method acts as a specific type guard, delegating to the general type-checking logic to verify that the concept's type does not match `ConceptType.EXT_NEG_THRESHOLD`. It returns `True` if the concept is of any other type, and `False` only if the concept is explicitly identified as an external negative threshold.

        :param op: The concept to verify is not of type EXT_NEG_THRESHOLD.
        :type op: Concept

        :return: True if the concept is not of type EXT_NEG_THRESHOLD, otherwise False.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.EXT_NEG_THRESHOLD)

    @staticmethod
    def is_not_concrete(op: Concept) -> bool:
        return OperatorConcept.is_not_type(op, ConceptType.CONCRETE)

    @staticmethod
    def is_not_modified(op: Concept) -> bool:
        """
        Checks if the specified concept is not of the modified type. This static method evaluates the input concept and returns `True` if its type is not `ConceptType.MODIFIED`, effectively determining that the concept has not been modified. It performs a read-only check without altering the state of the concept.

        :param op: The concept to check against the MODIFIED type.
        :type op: Concept

        :return: True if the concept is not of type MODIFIED, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.MODIFIED)

    @staticmethod
    def is_not_owa(op: Concept) -> bool:
        """
        Determines whether the provided concept is not an Ordered Weighted Averaging (OWA) operator. This static method acts as a specific type guard, delegating to the generic `is_not_type` method to verify that the concept's type does not match `ConceptType.OWA`. It returns `True` if the concept is of a different type, and `False` if it is identified as an OWA operator. The operation is read-only and does not modify the input object.

        :param op: The concept to verify is not of type OWA.
        :type op: Concept

        :return: True if the provided concept is not an OWA operator, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.OWA)

    @staticmethod
    def is_not_qowa(op: Concept) -> bool:
        """
        Determines whether the provided concept is not a Quantified Open World Assumption (QOWA) operator. This static method acts as a specific type guard, delegating the verification logic to the underlying `is_not_type` method with the `QUANTIFIED_OWA` classification. It returns a boolean value indicating that the concept does not belong to the QOWA category, facilitating type filtering within the broader operator concept hierarchy. The function performs a pure check without modifying the input concept.

        :param op: The concept to verify is not of type QUANTIFIED_OWA.
        :type op: Concept

        :return: True if the concept is not a Quantified OWA, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.QUANTIFIED_OWA)

    @staticmethod
    def is_not_choquet(op: Concept) -> bool:
        """
        Determines whether the provided concept is not a Choquet integral operator. This static method evaluates the input object to verify that its type does not correspond to `ConceptType.CHOQUET_INTEGRAL`. It returns `True` if the concept is of a different type, and `False` if it is identified as a Choquet integral.

        :param op: The concept to check against the Choquet integral type.
        :type op: Concept

        :return: True if the concept is not a Choquet integral, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.CHOQUET_INTEGRAL)

    @staticmethod
    def is_not_sugeno(op: Concept) -> bool:
        """
        Determines whether the provided operator concept is not a Sugeno integral. This static method acts as a specific predicate that delegates to the generic type-checking logic, verifying that the concept's type attribute does not correspond to the Sugeno integral category. It returns `True` if the concept is of a different type, and `False` if it is identified as a Sugeno integral.

        :param op: The concept to verify is not a Sugeno integral.
        :type op: Concept

        :return: True if the provided concept is not a Sugeno integral, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.SUGENO_INTEGRAL)

    @staticmethod
    def is_not_quasi_sugeno(op: Concept) -> bool:
        """
        Determines whether the provided operator concept is not a Quasi-Sugeno integral. This static method accepts a Concept object and returns True if the concept's type does not match the Quasi-Sugeno Integral classification. It functions as a specific type-checking utility that delegates the underlying comparison logic to the `is_not_type` method.

        :param op: The concept to check against the Quasi-Sugeno integral type.
        :type op: Concept

        :return: True if the provided concept is not a Quasi-Sugeno integral, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.QUASI_SUGENO_INTEGRAL)

    @staticmethod
    def is_not_self(op: Concept) -> bool:
        """
        Determines whether the provided concept is not classified as a "self" concept. This method acts as a specific type check, delegating to the general type verification logic to ensure the concept's type does not match `ConceptType.SELF`. It returns a boolean result without modifying the input object or causing side effects.

        :param op: The concept to check against the SELF type.
        :type op: Concept

        :return: True if the provided concept is not of type SELF, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.SELF)

    @staticmethod
    def is_not_zadeh_implies(op: Concept) -> bool:
        """
        Determines whether the provided concept is not specifically a Zadeh implication operator. This static method evaluates the input concept and returns true if its type differs from the Zadeh implies definition, and false otherwise. It serves as a type guard within the `OperatorConcept` module, relying on the underlying `is_not_type` utility to perform the actual comparison against the `ZADEH_IMPLIES` enum value. The operation is read-only and does not modify the input concept.

        :param op: The concept to evaluate.
        :type op: Concept

        :return: True if the given concept is not a Zadeh implication operator, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.ZADEH_IMPLIES)

    @staticmethod
    def is_not_sigma_concept(op: Concept) -> bool:
        """
        Determines whether the provided concept is not a sigma concept. This static method accepts a `Concept` object and returns `True` if the concept's type does not match `ConceptType.SIGMA_CONCEPT`, returning `False` otherwise. It relies on the `is_not_type` helper method to perform the underlying type verification.

        :param op: The concept to check.
        :type op: Concept

        :return: True if the concept is not a sigma concept, False otherwise.

        :rtype: bool
        """

        return OperatorConcept.is_not_type(op, ConceptType.SIGMA_CONCEPT)

    def is_concrete(self) -> bool:
        """
        Determines whether the operator concept is considered concrete based on its internal state and type. The method returns True if the concept is identified as not being a concrete type or not being a fuzzy number. If the concept is flagged as not modified, the concrete status is determined by recursively calling this method on the first concept in the `concepts` list. In all other scenarios, the method returns False.

        :return: True if the concept is not a concrete concept or not a fuzzy number. If the concept is not modified, returns the concreteness of the first concept. Returns False for modified concepts that are both concrete concepts and fuzzy numbers.

        :rtype: bool
        """

        if OperatorConcept.is_not_concrete(self) or OperatorConcept.is_not_fuzzy_number(
            self
        ):
            return True
        if OperatorConcept.is_not_modified(self):
            return self.concepts[0].is_concrete()
        return False

    def is_atomic(self) -> bool:
        """
        Determines whether the operator is considered atomic, meaning it cannot be decomposed into simpler sub-operators. This implementation returns False by default, indicating that the operator is a composite structure rather than a primitive building block. Subclasses representing fundamental or indivisible operations are expected to override this method to return True. The function performs no side effects and is primarily used to distinguish between complex operators and their atomic counterparts during analysis or traversal.

        :return: True if the object is atomic, False otherwise.

        :rtype: bool
        """

        return False

    def is_complemented_atomic(self) -> bool:
        """
        Determines whether the current concept represents a complement operation applied to a single atomic concept. This method returns true only if the concept's type is identified as a complement and its immediate child concept is considered atomic according to the child's own definition. The operation assumes the internal list of concepts is non-empty and does not modify the object's state.

        :return: True if this concept is a complement of an atomic concept, False otherwise.

        :rtype: bool
        """

        return self.type == ConceptType.COMPLEMENT and (
            self.concepts[0].is_atomic()
            # or self.concepts[0].type
            # in (ConceptType.MODIFIED, ConceptType.FUZZY_NUMBER, ConceptType.CONCRETE)
        )

    def get_atom(self) -> typing.Optional[typing.Self]:
        """
        Retrieves the underlying atomic concept if the current instance represents a complement operation. When the concept type is `ConceptType.COMPLEMENT`, this method returns the first element from the internal `concepts` collection. For any other concept type, it returns `None`, indicating that no specific atom is associated with this instance.

        :return: Returns the first concept if the instance type is COMPLEMENT, or None otherwise.

        :rtype: typing.Optional[typing.Self]
        """

        return self.concepts[0] if self.type == ConceptType.COMPLEMENT else None

    def get_atoms(self) -> list[typing.Self]:
        """
        Recursively traverses the concept structure to return a list of all atomic concepts that constitute this concept. If the current concept is a complement of an atomic concept, it returns a list containing itself; if it is a complement of a complex concept, it returns the atoms of the inner concept. For other concept types, it aggregates the atomic results from all child concepts into a single list. This method effectively flattens the concept tree to its base elements, handling negation by looking through the complement operator to the underlying structure.

        :return: A list of the atomic concepts that constitute this concept.

        :rtype: list[typing.Self]
        """

        if self.type == ConceptType.COMPLEMENT:
            if self.is_complemented_atomic():
                return [self]
            else:
                return self.concepts[0].get_atoms()
        else:
            return list.extend(*[c.get_atoms() for c in self.concepts])

    def is_simplified(self) -> bool:
        """
        Determines whether the current logical formula node is considered simplified based on the types of its immediate children. The method returns true if the node is a negated atomic proposition or if none of its direct child concepts share the same operator type as the current node. This logic effectively verifies that the formula is flattened at this level, ensuring that operators are not nested within other operators of the same type (e.g., an AND operation directly containing another AND operation).

        :return: True if the formula is a negated atomic proposition or if the current logical operator is not nested within itself (i.e., the structure is flat at the current level).

        :rtype: bool
        """

        if self.is_complemented_atomic():
            return True
        return all(c.type != self.type for c in self.concepts)

    def de_morgan(self) -> typing.Self:
        """
        Recursively applies De Morgan's laws to the logical expression tree represented by this concept. The method first normalizes all child concepts by invoking `de_morgan` on them. If the current node is a negation of a binary operator (such as AND or OR), it performs a structural transformation: the operator is inverted (swapping AND with OR) and the negation is pushed down to the operands, resulting in a new `OperatorConcept` instance. If the current node does not match the pattern for De Morgan's laws, the method returns the current instance with its updated children.

        :return: Returns the concept after recursively applying De Morgan's laws to push negations inward.

        :rtype: typing.Self
        """

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
        """
        Recursively traverses and simplifies the logical expression tree represented by the concept by applying reduction rules to its children. For complement operations, it resolves negations of absolute truth values, converting negated Top concepts to Bottom and vice versa. For binary operators, it performs algebraic simplification: conjunctions reduce to Bottom if they contain a Bottom operand or a contradiction (A and not A) under classical logic, while disjunctions reduce to Top if they contain a Top operand or a tautology (A or not A). Additionally, the method removes identity elements (Top from conjunctions, Bottom from disjunctions) and eliminates redundant operands through deduplication for operators supporting absorption. The operation modifies the concept's internal state in place and returns the simplified instance.

        :return: Returns a simplified version of the concept by recursively applying logical reduction rules to resolve identities, annihilators, and contradictions involving Top and Bottom concepts.

        :rtype: typing.Self
        """

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
        """
        Recursively simplifies the logical structure by eliminating double negations, applying the equivalence ~(~A) = A. The method first processes all child concepts to ensure the entire subtree is reduced. If the current concept is a negation and its immediate child is also a negation, the method returns the grandchild concept, effectively canceling out both operators. If no double negation is found at the current level, the method returns the current instance with its updated children.

        :return: Returns the concept after recursively eliminating double negations.

        :rtype: typing.Self
        """

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
        """
        Recursively distributes the specified operator type over its dual operator within the logical expression tree represented by this concept. The method traverses the structure bottom-up, applying distribution rules if the current node's type matches `c_type` and it contains children of the dual operator type; for instance, distributing AND over OR transforms `A & (B | C)` into `(A & B) | (A & C)`. If the concept is a Complement, the operation is delegated to its single child, while non-distributive operators are left untouched. This process modifies the concept's internal list of children in place but returns the resulting concept, which may be a new instance if the root node is restructured during distribution.

        :param c_type: The operator type to distribute over its dual (e.g., AND over OR) to expand the expression.
        :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType

        :return: Returns the concept after recursively distributing the specified operator type over its structure.

        :rtype: typing.Self
        """

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
        """
        Recursively simplifies the logical structure of the operator concept by applying Boolean algebra reduction rules, including idempotency, domination, complement, and identity laws. The method traverses the tree of child concepts to reduce them first, then removes duplicate operands for operators that support idempotency. It checks for domination conditions, returning the top truth value if the operator is OR and contains top, or the bottom truth value if the operator is AND and contains bottom. Furthermore, it evaluates complement laws to detect contradictions or tautologies where a concept appears alongside its negation. Identity elements that do not trigger short-circuiting are removed, and the method returns the reconstructed, normalized concept, or the original instance if it is an atomic complement.

        :param is_type: A callable function passed recursively to child concepts to assist in type identification or classification during the reduction process.
        :type is_type: typing.Callable

        :return: The simplified concept resulting from recursively applying idempotency, absorption, and complement laws to the operator's children.

        :rtype: typing.Self
        """

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
        """
        Recursively simplifies the logical structure by consolidating quantifiers based on the operator type. First, it applies the reduction process to all child concepts to ensure the tree is normalized from the bottom up. If the current node represents a conjunction (AND or Goedel AND), the method merges multiple universal quantifiers (ALL) sharing the same role into a single quantifier whose restriction is the conjunction of the original restrictions, while filtering out trivial existential quantifiers (SOME). Conversely, if the node represents a disjunction (OR or Goedel OR), it merges multiple existential quantifiers (SOME) sharing the same role into a single quantifier whose restriction is the disjunction of the original restrictions, leaving universal quantifiers unchanged. The method modifies the list of child concepts in place and returns the resulting concept structure, or returns the instance itself if the operator type does not support quantifier reduction.

        :return: Returns a new concept with reduced quantifiers by merging 'ALL' concepts under conjunctions and 'SOME' concepts under disjunctions that share the same role.

        :rtype: typing.Self
        """

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
        """
        Converts the concept into a normal form determined by the `is_type` predicate, which selects the primary binary operator for distribution. The method repeatedly applies a suite of logical transformations—such as De Morgan's laws, double negation elimination, distribution, idempotency reduction, truth value reduction, and quantifier reduction—until the expression stabilizes and no further simplifications are possible. This operation modifies the instance in place and returns the updated object.

        :param is_type: A predicate function used to identify the specific binary operator type (e.g., conjunction or disjunction) that defines the target normal form structure.
        :type is_type: typing.Callable

        :return: Returns the current instance after iteratively applying logical equivalences and reductions to achieve a simplified normal form.

        :rtype: typing.Self
        """

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
        """
        Retrieves the clauses associated with the operator concept. When the concept type is COMPLEMENT, the method returns a singleton list containing the current instance. For any other concept type, it returns the list of child concepts managed by the operator. Note that the `is_type` argument is currently ignored by the logic.

        :param is_type: A callable predicate used to filter or identify concepts based on their type.
        :type is_type: typing.Callable

        :return: A list of Concept objects. If the concept type is COMPLEMENT, returns a list containing the current concept; otherwise, returns the list of associated sub-concepts.

        :rtype: list[Concept]
        """

        if self.type == ConceptType.COMPLEMENT:
            return [self]
        return self.concepts

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Recursively replaces occurrences of concept `a` with concept `c` within the structure of the current `OperatorConcept` and transforms the current node into the type of `c`. The method first traverses all child concepts to perform the replacement. If `c` is a logical operator such as AND, OR, or their fuzzy logic variants (Gödel, Łukasiewicz), the method returns a new `OperatorConcept` of that specific type containing the updated children. If `c` is a COMPLEMENT, the method checks if the current concept's first child matches `a`; if so, it returns the negation of `c`, otherwise it returns the current concept unchanged without modifying its children. If `c` is an atomic concept or an unsupported type, the method implicitly returns `None`.

        :param a: The concept to be replaced.
        :type a: Concept
        :param c: The concept to substitute in place of `a`. Its type determines the operator type of the resulting concept structure.
        :type c: Concept

        :return: A new Concept where all occurrences of `a` are recursively replaced by `c`, with the operator type of the resulting concept determined by the type of `c`.

        :rtype: Concept
        """

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
        """
        Generates a string representation of the logical operator concept based on its specific type and the list of constituent concepts. The method joins the string values of the underlying concepts and formats them within parentheses, prefixed by a label corresponding to the logic operation, such as 'and', 'or', or 'not', including specific variants for Gödel and Łukasiewicz logics. If the concept type does not match any of the defined operators, the method returns None. This function performs a read-only operation and does not modify the object's state.

        :return: A string representation of the concept formatted according to its logical type, or None if the type is not recognized.

        :rtype: typing.Optional[str]
        """

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
        """
        Computes and returns the set of atomic concepts that constitute this operator concept by recursively aggregating the atomic concepts of its immediate children. The method iterates through the collection of concepts associated with this operator, invoking their respective `compute_atomic_concepts` methods and merging the results into a unified set to ensure uniqueness. This process effectively flattens the conceptual hierarchy, returning the base-level concepts found at the leaves of the structure. If the operator contains no child concepts, an empty set is returned. The operation does not modify the state of the current instance or its children.

        :return: A set containing the union of atomic concepts derived from the object's internal concepts.

        :rtype: set[Concept]
        """

        result: set[Concept] = set()
        for c in self.concepts:
            result.update(c.compute_atomic_concepts())
        return result

    def get_roles(self) -> set[str]:
        """
        Aggregates and returns a unique set of role strings from all underlying concepts associated with this operator. This method iterates through the internal collection of concepts, retrieves the roles for each, and combines them into a single set to eliminate duplicates. The operation is non-destructive and returns an empty set if the operator contains no constituent concepts.

        :return: A set of unique role strings aggregated from all associated concepts.

        :rtype: set[str]
        """

        return set().union(*[c.get_roles() for c in self.concepts])

    def __neg__(self) -> Concept:
        """
        Computes the logical negation of the operator concept by applying De Morgan's laws. This process recursively negates all child concepts and inverts the logical operator type, transforming conjunctions (AND) into disjunctions (OR) and vice versa. The implementation supports standard logical operators alongside specific fuzzy logic variants, such as Gödel and Łukasiewicz. When applied to a COMPLEMENT operator, the method effectively resolves a double negation by returning the inner child concept. If the concept's operator type is unsupported, the method raises a NotImplementedError.

        :raises NotImplementedError: Raised if negation is not defined for the current concept type.

        :return: Returns the logical negation of the concept, applying De Morgan's laws to distribute the negation over the underlying operator and resolving double negations.

        :rtype: Concept
        """

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
        """
        Implements the bitwise AND operation (`&`) to combine the current `OperatorConcept` instance with another instance of the same type. The behavior varies based on the type of the current instance: if it represents an AND operation, the method merges the new value directly; if it represents an OR operation, it retrieves the specific operator logic to combine the operands. For any other type, the method defaults to creating a new AND operation that includes both the current instance and the provided value, returning the resulting `OperatorConcept`.

        :param value: The right-hand operand to combine with the current instance using the AND operator.
        :type value: typing.Self

        :return: A new instance representing the logical AND of the current concept and the provided value.

        :rtype: typing.Self
        """

        if OperatorConcept.is_and(self.type):
            return OperatorConcept.__op(self.type, [self, value])
        elif OperatorConcept.is_or(self.type):
            return OperatorConcept.__op(
                OperatorConcept.OPERATORS[self.type], [self, value]
            )
        return OperatorConcept.and_([self, value])

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operation (`|`) to combine the current `OperatorConcept` with another instance of the same type. The behavior varies based on the internal type of the current concept: if it is already an OR operation, the value is merged using the existing type; if it is an AND operation, a specific operator logic is retrieved and applied; otherwise, a standard OR relationship is established between the two concepts. This method returns a new `OperatorConcept` representing the resulting logical expression without modifying the original instances.

        :param value: The right-hand operand to combine with the current instance using the OR operator.
        :type value: typing.Self

        :return: A new instance representing the result of the OR operation between the current instance and the provided value.

        :rtype: typing.Self
        """

        if OperatorConcept.is_or(self.type):
            return OperatorConcept.__op(self.type, [self, value])
        elif OperatorConcept.is_and(self.type):
            return OperatorConcept.__op(
                OperatorConcept.OPERATORS[self.type], [self, value]
            )
        return OperatorConcept.or_([self, value])

    def __eq__(self, value: typing.Self) -> bool:
        """
        Determines equality by verifying that the provided value is an instance of the same class and that its string representation matches that of the current instance. This comparison relies entirely on the output of the string conversion method, meaning two distinct objects are considered equal if they produce identical strings. Comparisons against objects of different types will result in a value of False.

        :param value: The object to compare against the current instance, where equality is determined by comparing the string representations.
        :type value: typing.Self

        :return: True if the provided value is an instance of OperatorConcept and its string representation matches that of this instance; otherwise, False.

        :rtype: bool
        """

        return isinstance(value, OperatorConcept) and str(self) == str(value)

    def __ne__(self, value: typing.Self) -> bool:
        """
        Determines whether the current instance is not equal to the provided value by negating the result of the equality comparison. This method delegates the logic to the `__eq__` implementation, meaning its behavior, including any raised exceptions or handling of incompatible types, is defined by that method. If the equality check returns the `NotImplemented` singleton, this implementation will treat it as a falsy value, resulting in a return value of `True`.

        :param value: The object to compare against the current instance.
        :type value: typing.Self

        :return: True if the instance is not equal to the provided value, False otherwise.

        :rtype: bool
        """

        return not (self == value)

    def __hash__(self) -> int:
        """
        Computes the hash value for the instance, enabling its use as a key in dictionaries or as an element in sets. The implementation derives the hash from the string representation of the object, ensuring that instances with identical string representations produce the same hash code. This method delegates the calculation to the built-in hash function applied to the result of the object's string conversion.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

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
