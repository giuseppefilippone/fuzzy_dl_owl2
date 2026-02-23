import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class SigmaConcept(Concept):
    """
    This class models a sigma-count construct within fuzzy description logic, defining a concept that is satisfied based on the cardinality of related individuals. Specifically, it evaluates whether the number of individuals reachable via a specific role that also belong to a given concept falls within a fuzzy concrete domain relative to a specified set of reference individuals. To utilize this class, instantiate it by providing a role string, a target concept, a list of individual objects, and a fuzzy concrete concept. The object automatically generates a string representation for its name and provides methods to access its components, clone itself deeply, and participate in logical operations such as negation, conjunction, and disjunction.

    :param concept: The concept C that related individuals must be instances of to be counted in the sigma-count.
    :type concept: Concept
    :param role: The binary relation used in the sigma-count expression to identify the connections between individuals.
    :type role: str
    :param individuals: The list of individuals constituting the set {a1, a2, ..., an} used as the reference context for evaluating the sigma-count concept.
    :type individuals: list[Individual]
    :param concrete_concept: The fuzzy concrete concept used to evaluate the sigma-count of related individuals.
    :type concrete_concept: FuzzyConcreteConcept
    :param name: Computed string representation of the sigma-count concept, automatically generated during initialization.
    :type name: str
    """


    def __init__(
        self,
        concept: Concept,
        role: str,
        individuals: list[Individual],
        concrete_concept: FuzzyConcreteConcept,
    ) -> None:
        """
        Initializes a SigmaConcept instance, representing a specialized concept defined by a specific role applied to a set of individuals within a fuzzy logic framework. The constructor requires a general Concept object, a string defining the role, a list of Individual entities, and a FuzzyConcreteConcept that provides the concrete fuzzy definition. It configures the instance by calling the superclass initializer with the SIGMA_CONCEPT type, storing the provided arguments as attributes, and automatically deriving the instance's name based on the input parameters.

        :param concept: The underlying concept entity or definition that this object encapsulates.
        :type concept: Concept
        :param role: The string identifier for the role or relationship associated with the concept.
        :type role: str
        :param individuals: A list of individual entities associated with the concept.
        :type individuals: list[Individual]
        :param concrete_concept: The fuzzy concrete concept instance defining the specific characteristics or membership logic for this sigma concept.
        :type concrete_concept: FuzzyConcreteConcept
        """

        super().__init__(ConceptType.SIGMA_CONCEPT, "")
        self.concept: Concept = concept
        self.role: str = role
        self.individuals: list[Individual] = individuals
        self.concrete_concept: FuzzyConcreteConcept = concrete_concept
        self.name: str = self.compute_name()

    def get_individuals(self) -> list[Individual]:
        """
        Returns the list of `Individual` entities currently associated with this `SigmaConcept` instance. This method provides direct access to the underlying list attribute, allowing callers to inspect the collection. Note that because the reference is returned directly, any modifications made to the list (such as adding or removing elements) will immediately affect the internal state of the `SigmaConcept` object.

        :return: The list of Individual objects associated with this instance.

        :rtype: list[Individual]
        """

        return self.individuals

    def get_concept(self) -> Concept:
        """
        Retrieves the underlying `Concept` instance associated with this `SigmaConcept` object. This method acts as a simple accessor, returning the value stored in the `concept` attribute without modifying the state of the `SigmaConcept` instance. Note that because it returns a direct reference to the internal object, any mutations made to the returned `Concept` will be reflected in the original instance.

        :return: The `Concept` object associated with this instance.

        :rtype: Concept
        """

        return self.concept

    def get_role(self) -> str:
        """
        Retrieves the role associated with the SigmaConcept instance. This accessor method returns the value of the internal `role` attribute without modifying the object's state. The method assumes the attribute has been initialized; otherwise, an AttributeError will be raised.

        :return: The role associated with the instance.

        :rtype: str
        """

        return self.role

    def get_fuzzy_concept(self) -> FuzzyConcreteConcept:
        """
        Retrieves the fuzzy concrete concept representation associated with this instance. This method acts as a simple accessor, returning the object stored in the `concrete_concept` attribute. It performs no computation or modification of state during the retrieval process.

        :return: The FuzzyConcreteConcept instance stored in the concrete_concept attribute.

        :rtype: FuzzyConcreteConcept
        """

        return self.concrete_concept

    def clone(self) -> typing.Self:
        """
        Creates and returns a deep copy of the current `SigmaConcept` instance. To ensure the new object is independent of the original, the method recursively clones the `concept`, `concrete_concept`, and every element within the `individuals` list. The `role` attribute is passed by reference to the new instance. This operation does not modify the original object.

        :return: A new instance of the class that is a copy of the current object, with nested concepts, individuals, and concrete concepts also cloned.

        :rtype: typing.Self
        """

        return SigmaConcept(
            self.concept.clone(),
            self.role,
            [i.clone() for i in self.individuals],
            self.concrete_concept.clone(),
        )

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Computes the set of atomic concepts associated with this SigmaConcept. In this specific implementation, the method returns an empty set, indicating that the concept does not decompose into atomic constituents or serving as a default stub for subclasses. The operation is side-effect free and generates a new set instance upon each call.

        :return: A set of atomic concepts.

        :rtype: set[Concept]
        """

        return set()

    def get_roles(self) -> set[str]:
        """
        Retrieves the set of role identifiers associated with the concept instance. The current implementation returns an empty set, serving as a default behavior for subclasses or instances where no specific roles are defined. This method has no side effects and returns a new set object on every call.

        :return: A set of strings representing the roles.

        :rtype: set[str]
        """

        return set()

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Returns the current instance unchanged, acting as an identity function within the replacement operation. Although the method signature implies a substitution of concept `a` with concept `c`, the implementation indicates that `SigmaConcept` is treated as an atomic or terminal entity that does not contain sub-components subject to this transformation. As a result, the method has no side effects and returns the original object regardless of the arguments provided.

        :param a: The concept to be replaced.
        :type a: Concept
        :param c: The concept to replace the original concept with.
        :type c: Concept

        :return: Returns the current instance.

        :rtype: Concept
        """

        return self

    def compute_name(self) -> str | None:
        """
        Constructs and returns a string representation of the sigma concept using a specific parenthesized syntax. The format follows the pattern `(sigma-count role concept {individuals} concrete_concept)`, where the list of individuals is converted to strings, joined by spaces, and enclosed in curly braces. This method relies on the current values of the `role`, `concept`, `individuals`, and `concrete_concept` attributes without modifying them, resulting in a deterministic string output based on the object's state. While the type hint indicates a potential return of `None`, the implementation consistently returns a formatted string, which may include literal "None" text if the underlying attributes are unset.

        :return: A formatted string representing the sigma-count, constructed from the role, concept, individuals, and concrete concept.

        :rtype: str | None
        """

        return f"(sigma-count {self.role} {self.concept} {{{' '.join(map(str, self.individuals))}}} {self.concrete_concept})"

    def __neg__(self) -> Concept:
        """
        Implements the unary negation operator to return the logical negation of the current concept. This allows the use of the minus sign (`-`) to invert the meaning of a `SigmaConcept`, resulting in a new `Concept` that represents the logical NOT operation applied to the original instance. The method delegates the actual construction of the negated concept to the `OperatorConcept.not_` factory method.

        :return: A new Concept representing the logical negation of the current instance.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise AND operation (`&`) for the `SigmaConcept` instance, allowing it to be combined with another instance of the same type. This method delegates the logic to `OperatorConcept.and_`, passing the current object and the provided value to compute the result. The operation returns a new instance representing the conjunction of the two concepts, leaving the original operands unmodified.

        :param value: The right-hand operand for the AND operation.
        :type value: typing.Self

        :return: A new instance representing the result of the AND operation between this object and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operator (`|`) to combine the current concept with another instance of the same type. This method delegates the logic to `OperatorConcept.or_`, effectively creating a new concept that represents the logical disjunction or union of the two operands. It ensures type consistency by returning an instance of the same class as the inputs.

        :param value: The right-hand operand to combine with the current instance using the OR operation.
        :type value: typing.Self

        :return: The result of the OR operation between the current instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Returns an integer hash value for the instance based on its string representation, enabling the object to be used as a dictionary key or stored in a set. The implementation delegates the hashing logic to the built-in `hash` function applied to the result of `str(self)`, which implies that the object should be treated as immutable or that its string representation must remain constant to maintain consistent behavior within hash-based collections.

        :return: An integer hash value based on the string representation of the object.

        :rtype: int
        """

        return hash(str(self))
