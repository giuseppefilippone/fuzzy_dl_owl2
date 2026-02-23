import typing

from fuzzy_dl_owl2.fuzzydl.concept.all_some_concept import AllSomeConcept
from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_concept_interface import (
    HasRoleConceptInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class ApproximationConcept(Concept, HasRoleConceptInterface):
    """
    This class models logical constructs that constrain individuals based on the properties of their related entities through a specific role, effectively representing various forms of quantification within a description logic framework. It encapsulates lower approximations (universal quantification), upper approximations (existential quantification), and their tight or loose nested variants, which define conditions such as "all related individuals must satisfy C" or "there exists a related individual satisfying C." Instead of direct instantiation, users should utilize the provided static factory methods—such as `lower_approx` or `upper_approx`—to construct these concepts by specifying a role name and a target concept. The class provides functionality to transform these approximations into standard "all" and "some" quantifier structures, supports logical negation by inverting the approximation type, and integrates seamlessly with the broader concept hierarchy for operations like conjunction, disjunction, and string representation.

    :param INVERSE_APPROXIMATION: Maps each approximation type to its inverse counterpart, used to determine the resulting type when negating a concept.
    :type INVERSE_APPROXIMATION: dict[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
    :param name: The string representation of the concept, formatted as (type role concept) (e.g., "(la r C)").
    :type name: typing.Any

    :raises ValueError: Raised when the provided concept type is not one of the valid approximation types (LOWER_APPROX, TIGHT_LOWER_APPROX, LOOSE_LOWER_APPROX, UPPER_APPROX, TIGHT_UPPER_APPROX, or LOOSE_UPPER_APPROX).
    """

    INVERSE_APPROXIMATION: dict[ConceptType, ConceptType] = {
        k: v
        for k, v in zip(
            [
                ConceptType.LOWER_APPROX,
                ConceptType.TIGHT_LOWER_APPROX,
                ConceptType.LOOSE_LOWER_APPROX,
                ConceptType.UPPER_APPROX,
                ConceptType.TIGHT_UPPER_APPROX,
                ConceptType.LOOSE_UPPER_APPROX,
            ],
            [
                ConceptType.UPPER_APPROX,
                ConceptType.TIGHT_UPPER_APPROX,
                ConceptType.LOOSE_UPPER_APPROX,
                ConceptType.LOWER_APPROX,
                ConceptType.TIGHT_LOWER_APPROX,
                ConceptType.LOOSE_LOWER_APPROX,
            ],
        )
    }

    def __init__(self, c_type: ConceptType, role: str, c: Concept) -> None:
        """
        Initializes an instance representing an approximation of a given concept, configured by a specific role and approximation type. This constructor validates that the provided concept type corresponds to a valid approximation strategy—such as lower or upper approximations, optionally qualified as tight or loose—and will raise an assertion error if an invalid type is supplied. It delegates initialization to the base `Concept` class and the `HasRoleConceptInterface` mixin to establish the core type and the role-based relationship to the target concept. Finally, it automatically computes and assigns a descriptive name to the instance based on its configuration.

        :param c_type: The specific type of approximation concept, restricted to lower or upper approximation variants (including tight and loose modifiers).
        :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
        :param role: The string identifier representing the specific role or relationship this concept fulfills.
        :type role: str
        :param c: The underlying concept instance to which the approximation and role apply.
        :type c: Concept
        """

        Concept.__init__(self, c_type)
        HasRoleConceptInterface.__init__(self, role, c)

        assert c_type in (
            ConceptType.LOWER_APPROX,
            ConceptType.TIGHT_LOWER_APPROX,
            ConceptType.LOOSE_LOWER_APPROX,
            ConceptType.UPPER_APPROX,
            ConceptType.TIGHT_UPPER_APPROX,
            ConceptType.LOOSE_UPPER_APPROX,
        )

        self.name = self.compute_name()

    @staticmethod
    def lower_approx(role: str, c: Concept) -> typing.Self:
        """
        This static method acts as a factory to construct a new instance of `ApproximationConcept` representing a lower approximation. It accepts a string defining the role and a base `Concept` object, initializing the new concept with the type `ConceptType.LOWER_APPROX`. The method returns the newly created object without modifying the input arguments.

        :param role: The string identifier representing the specific role or attribute associated with the lower approximation.
        :type role: str
        :param c: The concept to be approximated.
        :type c: Concept

        :return: A new instance representing the lower approximation of the specified concept for the given role.

        :rtype: typing.Self
        """

        return ApproximationConcept(ConceptType.LOWER_APPROX, role, c)

    @staticmethod
    def loose_lower_approx(role: str, c: Concept) -> typing.Self:
        """
        Constructs a new instance of `ApproximationConcept` representing a loose lower approximation of a given concept. This static factory method accepts a string defining the role and a `Concept` object, initializing the new entity with the specific type identifier `LOOSE_LOWER_APPROX`. The method delegates directly to the class constructor, meaning any exceptions raised during instantiation will propagate to the caller, and it does not modify the input arguments or maintain internal state between calls.

        :param role: The identifier of the role for which the approximation is defined.
        :type role: str
        :param c: The concept for which the loose lower approximation is defined.
        :type c: Concept

        :return: An instance representing a loose lower approximation concept initialized with the provided role and concept.

        :rtype: typing.Self
        """

        return ApproximationConcept(ConceptType.LOOSE_LOWER_APPROX, role, c)

    @staticmethod
    def tight_lower_approx(role: str, c: Concept) -> typing.Self:
        """
        Creates and returns an instance of `ApproximationConcept` configured as a tight lower approximation. This static factory method initializes the object with the specific type `ConceptType.TIGHT_LOWER_APPROX`, associating it with the provided role string and the source concept. It abstracts the instantiation process, allowing callers to create this specific approximation variant without needing to handle the underlying type enumeration directly.

        :param role: The specific role or relation used to define the tight lower approximation of the concept.
        :type role: str
        :param c: The concept to be approximated.
        :type c: Concept

        :return: An ApproximationConcept instance representing the tight lower approximation of the provided concept.

        :rtype: typing.Self
        """

        return ApproximationConcept(ConceptType.TIGHT_LOWER_APPROX, role, c)

    @staticmethod
    def upper_approx(role: str, c: Concept) -> typing.Self:
        """
        Creates an instance of `ApproximationConcept` representing an upper approximation for a given concept and role. This static factory method wraps the class constructor, explicitly setting the concept type to `ConceptType.UPPER_APPROX` while passing through the provided role string and the base concept object. It does not modify the input arguments and relies on the underlying class constructor for validation of the provided parameters.

        :param role: The identifier for the role or attribute under which the upper approximation is calculated.
        :type role: str
        :param c: The concept to be approximated.
        :type c: Concept

        :return: Returns an ApproximationConcept representing the upper approximation of the provided concept for the specified role.

        :rtype: typing.Self
        """

        return ApproximationConcept(ConceptType.UPPER_APPROX, role, c)

    @staticmethod
    def loose_upper_approx(role: str, c: Concept) -> typing.Self:
        """
        Constructs a new `ApproximationConcept` instance representing a loose upper approximation. This static method serves as a factory that accepts a role identifier and a base `Concept` object, initializing the new instance with the specific type `LOOSE_UPPER_APPROX`. It delegates the actual instantiation to the class constructor, ensuring the resulting object is correctly typed and associated with the provided role and concept.

        :param role: The name of the role or relation used to compute the loose upper approximation.
        :type role: str
        :param c: The base concept for which the loose upper approximation is constructed.
        :type c: Concept

        :return: An instance representing the loose upper approximation of the provided concept for the specified role.

        :rtype: typing.Self
        """

        return ApproximationConcept(ConceptType.LOOSE_UPPER_APPROX, role, c)

    @staticmethod
    def tight_upper_approx(role: str, c: Concept) -> typing.Self:
        """
        Creates and returns an `ApproximationConcept` instance configured as a tight upper approximation. This static factory method initializes the object with the specific type `ConceptType.TIGHT_UPPER_APPROX`, associating it with the provided role string and the source concept. It acts as a convenience wrapper for the class constructor, ensuring the correct approximation type is applied without requiring the caller to specify the enum value directly.

        :param role: The relation or attribute used to compute the tight upper approximation.
        :type role: str
        :param c: The concept to be approximated.
        :type c: Concept

        :return: Returns an instance representing the tight upper approximation of the provided concept for the specified role.

        :rtype: typing.Self
        """

        return ApproximationConcept(ConceptType.TIGHT_UPPER_APPROX, role, c)

    def to_all_some_concept(self) -> AllSomeConcept:
        """
        Converts the current approximation instance into an equivalent representation using the `AllSomeConcept` class based on the specific approximation type. The mapping logic translates lower approximations to universal quantification and upper approximations to existential quantification, with tight and loose variations handled by nesting these quantifiers appropriately using the instance's role and current concept. If the approximation type is not recognized, a `ValueError` is raised.

        :raises ValueError: Raised if `self.type` does not match any of the expected approximation types.

        :return: The AllSomeConcept equivalent of the current approximation type, constructed using the role and current concept.

        :rtype: AllSomeConcept
        """

        if self.type == ConceptType.LOWER_APPROX:
            return AllSomeConcept.all(self.role, self.curr_concept)
        if self.type == ConceptType.TIGHT_LOWER_APPROX:
            return AllSomeConcept.all(
                self.role, AllSomeConcept.all(self.role, self.curr_concept)
            )
        if self.type == ConceptType.LOOSE_LOWER_APPROX:
            return AllSomeConcept.some(
                self.role, AllSomeConcept.all(self.role, self.curr_concept)
            )
        if self.type == ConceptType.UPPER_APPROX:
            return AllSomeConcept.some(self.role, self.curr_concept)
        if self.type == ConceptType.TIGHT_UPPER_APPROX:
            return AllSomeConcept.all(
                self.role, AllSomeConcept.some(self.role, self.curr_concept)
            )
        if self.type == ConceptType.LOOSE_UPPER_APPROX:
            return AllSomeConcept.some(
                self.role, AllSomeConcept.some(self.role, self.curr_concept)
            )
        raise ValueError

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of `ApproximationConcept` that duplicates the state of the current object. The clone is initialized with the same `type`, `role`, and `curr_concept` values as the original. This method does not modify the original object or its attributes.

        :return: A new instance of the class that is a copy of the current object, initialized with the same type, role, and current concept.

        :rtype: typing.Self
        """

        return ApproximationConcept(self.type, self.role, self.curr_concept)

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Replaces occurrences of a specific concept `a` with the provided concept `c` within the current structure. This method recursively applies the replacement operation to the underlying concept (`self.curr_concept`). If the replacement concept `c` is an instance of `ApproximationConcept`, the resulting structure is reconstructed using the specific approximation type (e.g., lower, upper, loose, or tight) defined by `c`, while preserving the current role. The method returns a new `Concept` instance without modifying the original.

        :param a: The concept to be replaced within the underlying concept structure.
        :type a: Concept
        :param c: The concept to replace `a` with. If `c` is an ApproximationConcept, the resulting concept inherits its approximation type.
        :type c: Concept

        :return: A new Concept resulting from replacing sub-concept a with c. If c is an ApproximationConcept, returns a new ApproximationConcept of the same type as c, preserving the current role and wrapping the recursively modified inner concept.

        :rtype: Concept
        """

        if isinstance(c, ApproximationConcept):
            c_type: ConceptType = c.type
            if c_type == ConceptType.LOWER_APPROX:
                return ApproximationConcept.lower_approx(
                    self.role, self.curr_concept.replace(a, c)
                )
            elif c_type == ConceptType.LOOSE_LOWER_APPROX:
                return ApproximationConcept.loose_lower_approx(
                    self.role, self.curr_concept.replace(a, c)
                )
            elif c_type == ConceptType.TIGHT_LOWER_APPROX:
                return ApproximationConcept.tight_lower_approx(
                    self.role, self.curr_concept.replace(a, c)
                )
            elif c_type == ConceptType.UPPER_APPROX:
                return ApproximationConcept.upper_approx(
                    self.role, self.curr_concept.replace(a, c)
                )
            elif c_type == ConceptType.LOOSE_UPPER_APPROX:
                return ApproximationConcept.loose_upper_approx(
                    self.role, self.curr_concept.replace(a, c)
                )
            elif c_type == ConceptType.TIGHT_UPPER_APPROX:
                return ApproximationConcept.tight_upper_approx(
                    self.role, self.curr_concept.replace(a, c)
                )

    def compute_name(self) -> typing.Optional[str]:
        """
        Generates a standardized string identifier for the approximation concept based on its type, role, and current concept value. The method maps the internal concept type to a specific abbreviation—such as 'la' for lower approximation or 'ua' for upper approximation—and formats these components into a parenthesized string. If the concept type is not recognized among the defined approximation categories, the method raises a ValueError.

        :raises ValueError: Raised when `self.type` does not correspond to a recognized or supported concept type.

        :return: A string representing the concept name in the format '(type_abbreviation role curr_concept)'.

        :rtype: typing.Optional[str]
        """

        if self.type == ConceptType.LOWER_APPROX:
            return f"(la {self.role} {self.curr_concept})"
        elif self.type == ConceptType.LOOSE_UPPER_APPROX:
            return f"(lua {self.role} {self.curr_concept})"
        elif self.type == ConceptType.LOOSE_LOWER_APPROX:
            return f"(lla {self.role} {self.curr_concept})"
        elif self.type == ConceptType.UPPER_APPROX:
            return f"(ua {self.role} {self.curr_concept})"
        elif self.type == ConceptType.TIGHT_UPPER_APPROX:
            return f"(tua {self.role} {self.curr_concept})"
        elif self.type == ConceptType.TIGHT_LOWER_APPROX:
            return f"(tla {self.role} {self.curr_concept})"
        raise ValueError

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Calculates the set of atomic concepts derived from the underlying concept stored in `curr_concept`. The method acts as a wrapper, forwarding the request directly to the `compute_atomic_concepts` method of the `curr_concept` attribute and returning the resulting set. It assumes that `curr_concept` is properly initialized and implements the corresponding computation logic.

        :return: A set of atomic concepts representing the base-level constituents of the current concept.

        :rtype: set[Concept]
        """

        return self.curr_concept.compute_atomic_concepts()

    def get_roles(self) -> set[str]:
        """
        Retrieves a comprehensive set of role identifiers associated with the current object and its underlying concept. This method aggregates the specific role defined on the instance with the roles returned by the `curr_concept` object's `get_roles` method, performing a set union to ensure uniqueness. The operation is read-only and does not modify the state of the object or its dependencies.

        :return: A set of strings representing the union of the object's role and the roles associated with the current concept.

        :rtype: set[str]
        """

        return set([self.role]) | self.curr_concept.get_roles()

    def __neg__(self) -> Concept:
        """
        Returns a new ApproximationConcept representing the negation of the current instance. This operation creates a new object where the approximation type is inverted using the INVERSE_APPROXIMATION mapping, the role remains unchanged, and the underlying curr_concept is negated. The method does not modify the original object in place, but it assumes the current type exists in the inversion mapping and that curr_concept supports the unary minus operation.

        :return: Returns a new `Concept` representing the negation of the current concept, inverting both the approximation type and the underlying value.

        :rtype: Concept
        """

        return ApproximationConcept(
            ApproximationConcept.INVERSE_APPROXIMATION[self.type],
            self.role,
            -self.curr_concept,
        )

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise AND operation (`&`) for the approximation concept, combining the current instance with another instance of the same type. This method delegates the core logic to `OperatorConcept.and_`, which handles the specific rules for calculating the conjunction or intersection of the two values. The operation returns a new instance of `ApproximationConcept` representing the result, leaving the original operands unmodified.

        :param value: The other instance to perform the AND operation with.
        :type value: typing.Self

        :return: The result of the logical AND operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operator (`|`) to combine the current approximation concept with another value of the same type. This method delegates the logic to the `OperatorConcept.or_` static method, which performs the specific calculation required to merge the two concepts. It returns a new instance representing the result of the operation, ensuring that the original objects remain unmodified.

        :param value: The right-hand operand for the OR operation.
        :type value: typing.Self

        :return: Returns a new instance representing the logical OR of this concept and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Computes the integer hash value for the object by delegating to the hash of its string representation. This enables the instance to be used as a key in dictionaries or as an element in sets, assuming the object is immutable or its string representation does not change. The specific hash value is determined by the `__str__` method, so any modifications to the object that alter its string output will result in a different hash, potentially affecting its behavior in hash-based collections.

        :return: An integer hash value computed from the object's string representation.

        :rtype: int
        """

        return hash(str(self))


LowerApprox = ApproximationConcept.lower_approx
LooseLowerApprox = ApproximationConcept.loose_lower_approx
TightLowerApprox = ApproximationConcept.tight_lower_approx
UpperApprox = ApproximationConcept.upper_approx
LooseUpperApprox = ApproximationConcept.loose_upper_approx
TightUpperApprox = ApproximationConcept.tight_upper_approx
