from __future__ import annotations

import typing

import trycast

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface import (
    HasWeightedConceptsInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class SugenoIntegral(Concept, HasWeightedConceptsInterface):
    """This class models a Sugeno integral, a fuzzy aggregation operator used to combine a collection of sub-concepts based on a corresponding set of weights. It serves as a composite concept within a logical framework, allowing for the representation of complex, weighted decision structures. To utilize this class, instantiate it with a list of floating-point weights and a list of `Concept` objects, ensuring that the number of weights exactly matches the number of concepts; a mismatch will trigger an error during initialization. Once created, the instance supports operations such as cloning, replacing specific sub-concepts, and recursively retrieving atomic concepts or roles, while also providing a string representation of the integral formula."""


    @typing.overload
    def __init__(self) -> None: ...

    @typing.overload
    def __init__(
        self, weights: typing.Optional[list[float]], concepts: list[Concept]
    ) -> None: ...

    def __init__(self, *args) -> None:
        """
        Initializes the SugenoIntegral object, supporting two distinct modes of instantiation depending on the arguments provided. When invoked without arguments, the method performs a default initialization routine. Conversely, when supplied with exactly two arguments, it expects an optional list of floating-point values and a list of Concept objects, validating their types before configuring the instance with these specific data points.

        :param args: Variable positional arguments determining the initialization mode. If omitted, default initialization is used. If provided, exactly two arguments are required: an optional list of floats and a list of Concepts.
        :type args: typing.Any
        """

        assert len(args) in [0, 2]
        if len(args) == 0:
            self.__sugeno_init_1()
        else:
            trycast.checkcast(typing.Optional[list[float]], args[0])
            trycast.checkcast(list[Concept], args[1])
            self.__sugeno_init_2(*args)

    def __sugeno_init_1(self) -> None:
        """Initializes the SugenoIntegral instance by delegating to the constructors of its parent classes to establish the object's core identity and capabilities. Specifically, it registers the instance as a Concept of type SUGENO_INTEGRAL and initializes the HasWeightedConceptsInterface with a null weight set and an empty list of concepts, thereby preparing the object for subsequent data population or resetting it to a default state."""

        Concept.__init__(self, ConceptType.SUGENO_INTEGRAL)
        HasWeightedConceptsInterface.__init__(self, None, [])

    def __sugeno_init_2(
        self, weights: typing.Optional[list[float]], concepts: list[Concept]
    ) -> None:
        """
        This internal initialization method configures a Sugeno Integral instance by establishing its inheritance chain and validating the relationship between weights and concepts. It initializes the `Concept` base class with the specific `SUGENO_INTEGRAL` type and invokes the `HasWeightedConceptsInterface` to handle the weighted concepts logic. If weights are provided, the method performs a strict validation to ensure the count of weights matches the count of concepts, raising an error if they differ, and subsequently computes the instance's name. In the absence of provided weights, the method initializes the weights attribute as an empty list.

        :param weights: Optional list of numerical weights corresponding to the concepts. If provided, the length must match the number of concepts.
        :type weights: typing.Optional[list[float]]
        :param concepts: A list of concepts that constitute the Sugeno integral. The number of concepts must match the number of provided weights.
        :type concepts: list[Concept]
        """

        Concept.__init__(self, ConceptType.SUGENO_INTEGRAL)
        HasWeightedConceptsInterface.__init__(self, weights, concepts)

        if weights is not None:
            if len(weights) != len(concepts):
                Util.error(
                    "Error: The number of weights and the number of concepts should be the same"
                )
            self.name = self.compute_name()
        else:
            self.weights: list[float] = []

    def clone(self) -> typing.Self:
        """
        Generates a distinct copy of the current instance, preserving the state of the fuzzy integral's parameters. The method constructs a new object using shallow copies of the internal weights and concepts lists, thereby decoupling the clone's data structure from the original. This ensures that subsequent modifications to the weights or concepts of the returned object will not impact the source instance, providing a safe way to manipulate or store the current configuration.

        :return: A new instance of the class with the same weights and concepts as the current object.

        :rtype: typing.Self
        """

        return SugenoIntegral(self.weights[:], [c for c in self.concepts])

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Retrieves the complete set of atomic concepts associated with the current instance by aggregating results from its constituent concepts. It iterates over the collection of concepts stored in the `concepts` attribute, invoking the `compute_atomic_concepts` method on each individual element to extract their fundamental components. The resulting atomic concepts are collected into a unified set to ensure uniqueness, effectively flattening the hierarchy of concepts. This method does not modify the state of the instance or its contained concepts, and it returns an empty set if the internal collection of concepts is empty.

        :return: A set containing the union of all atomic concepts derived from the object's concepts.

        :rtype: set[Concept]
        """

        concept_list: set[Concept] = set()
        for c in self.concepts:
            concept_list.update(c.compute_atomic_concepts())
        return concept_list

    def get_roles(self) -> set[str]:
        """
        Retrieves the union of all role identifiers defined across the concepts associated with this SugenoIntegral instance. It iterates through the internal collection of concepts, invoking the `get_roles` method on each to gather their specific roles, and aggregates them into a single set to ensure uniqueness. This method does not modify the internal state of the instance or its concepts, and it returns an empty set if no concepts are present.

        :return: A set of unique role strings aggregated from all associated concepts.

        :rtype: set[str]
        """

        role_list: set[str] = set()
        for c in self.concepts:
            role_list.update(c.get_roles())
        return role_list

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Replaces all occurrences of a specific concept within the integral's underlying concepts with another concept. It constructs a new SugenoIntegral instance using the original weights and the transformed list of concepts, where each constituent concept has undergone the replacement. The method returns the logical negation of this newly constructed integral without modifying the original instance.

        :param a: The concept to be replaced within the integral's components.
        :type a: Concept
        :param c: The concept to substitute for `a`.
        :type c: Concept

        :return: Returns a new Concept representing the negation of the Sugeno Integral resulting from replacing concept 'a' with concept 'c' in the internal concepts.

        :rtype: Concept
        """

        return -SugenoIntegral(self.weights, [ci.replace(a, c) for ci in self.concepts])

    def compute_name(self) -> str:
        """
        Constructs a standardized string identifier for the current instance by formatting the object's weights and concepts into a specific parenthetical syntax. The resulting string follows an S-expression-like structure, explicitly labeling the operation as "sugeno" and listing the weights and concepts as space-separated sequences within nested parentheses. This method is a pure function of the instance's state, causing no side effects, and handles non-string elements within the weights or concepts lists by implicitly converting them to strings.

        :return: A string representation of the Sugeno model, formatted with its weights and concepts.

        :rtype: str
        """

        return f"(sugeno ({' '.join(map(str, self.weights))}) ({' '.join(map(str, self.concepts))}))"

    def __neg__(self) -> Concept:
        """
        Implements the unary negation operator, allowing the Sugeno integral instance to be inverted using the minus sign. This method returns a new Concept object representing the logical negation or complement of the current instance. The operation is performed by delegating to the static `OperatorConcept.not_` method, ensuring consistent handling of logical complement across the module.

        :return: The logical negation of the current concept.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Computes the logical conjunction of the current instance with another Sugeno integral using the bitwise AND operator. This operation combines the two integrals according to the logic defined in `OperatorConcept`, typically representing an intersection or a specific fuzzy logic t-norm, and returns a new `SugenoIntegral` instance without modifying the original operands. The method relies on the `OperatorConcept.and_` helper to perform the actual calculation, ensuring that the behavior is consistent with the module's operator handling framework.

        :param value: The right-hand operand to perform the AND operation with.
        :type value: typing.Self

        :return: The result of the AND operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operation for the Sugeno integral, enabling the use of the `|` operator to combine the current instance with another Sugeno integral. This method delegates the underlying logic to the `OperatorConcept.or_` function, which performs the specific algebraic or logical combination defined by the concept. It returns a new instance of the SugenoIntegral representing the result, leaving the original operands unchanged and ensuring no side effects occur on the input objects.

        :param value: Another instance of the same class to perform the OR operation with.
        :type value: typing.Self

        :return: The result of the OR operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Calculates a hash code for the current instance to support its use in hash-based collections like dictionaries and sets. This method derives the hash value by converting the object to its string representation and hashing that string. Because the hash depends on the string output, any changes to the object's state that affect its string representation will alter its hash value, which may lead to unexpected behavior if the object is used as a dictionary key after modification.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))
