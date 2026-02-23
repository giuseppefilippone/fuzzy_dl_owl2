import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_concept_interface import (
    HasRoleConceptInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.truth_concept import TruthConcept
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class AllSomeConcept(Concept, HasRoleConceptInterface):
    """
    Represents quantified role restrictions, specifically universal ("all") and existential ("some") restrictions, within a description logic framework. It defines conditions that an individual must satisfy regarding its relationships: for a universal restriction, every individual connected via a specific role must belong to a target concept, while for an existential restriction, at least one such connected individual must belong to the target concept. Instances are best created using the static factory methods `all` and `some`, which apply logical optimizations—such as reducing `(all r TOP)` to `TOP`—before construction. The object supports standard concept operations including negation, which inverts the quantifier type and negates the nested concept, as well as cloning and sub-concept replacement.

    :param _name: Computed string representation of the concept, formatted as "(all r C)" or "(some r C)".
    :type _name: str
    """

    def __init__(self, role: str, c: Concept, c_type: ConceptType) -> None:
        """
        Initializes a specialized concept that applies a universal or existential quantifier to a target concept within a specific role. The constructor accepts a role string, a child Concept, and a ConceptType, asserting that the type is strictly limited to either ALL or SOME. It performs initialization for both the base Concept class and the HasRoleConceptInterface mixin before calculating and assigning the internal name of the concept.

        :param role: The name or identifier of the role associated with the concept.
        :type role: str
        :param c: The concept that fills the role.
        :type c: Concept
        :param c_type: The type of concept quantification, restricted to either ConceptType.ALL or ConceptType.SOME.
        :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
        """

        Concept.__init__(self, c_type)
        HasRoleConceptInterface.__init__(self, role, c)

        assert c_type in (ConceptType.ALL, ConceptType.SOME)
        self._name: str = self.compute_name()

    @staticmethod
    def new(c_type: ConceptType, role: str, concept: Concept) -> typing.Self:
        """
        Acts as a factory method for instantiating `AllSomeConcept` objects based on a specified concept type, role, and nested concept. When optimizations are enabled via the configuration, the method applies logical simplifications: if the type is `SOME` and the nested concept is `BOTTOM`, it returns the global bottom concept; conversely, if the type is `ALL` and the nested concept is `TOP`, it returns the global top concept. If these optimization conditions are not met, the method constructs and returns a new `AllSomeConcept` instance initialized with the provided arguments.

        :param c_type: Specifies the type of concept to instantiate, determining whether it represents a universal (ALL) or existential (SOME) quantification.
        :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
        :param role: The role or property name used to define the concept restriction.
        :type role: str
        :param concept: The concept instance to be wrapped or restricted.
        :type concept: Concept

        :return: Returns a new instance representing the specified restriction. If optimizations are enabled and the result is trivial (e.g., `SOME` of `BOTTOM` or `ALL` of `TOP`), returns the corresponding `TruthConcept` singleton.

        :rtype: typing.Self
        """

        if c_type == ConceptType.SOME:
            if ConfigReader.OPTIMIZATIONS != 0 and concept.type == ConceptType.BOTTOM:
                return TruthConcept.get_bottom()
        else:
            if ConfigReader.OPTIMIZATIONS != 0 and concept.type == ConceptType.TOP:
                return TruthConcept.get_top()
        return AllSomeConcept(role, concept, c_type)

    @staticmethod
    def all(role: str, concept: Concept) -> typing.Self:
        """
        Constructs a new `AllSomeConcept` instance representing a universal quantification over the provided concept. This static factory method accepts a role string and a `Concept` object, initializing the instance with the specific type `ConceptType.ALL`. It serves as a convenience wrapper around the internal `new` method to simplify the creation of "all" relationships within the module.

        :param role: The name of the role or property defining the universal restriction.
        :type role: str
        :param concept: The concept defining the range of the universal restriction.
        :type concept: Concept

        :return: Returns a new instance representing a universal quantification over the specified role and concept.

        :rtype: typing.Self
        """

        return AllSomeConcept.new(ConceptType.ALL, role, concept)

    @staticmethod
    def some(role: str, concept: Concept) -> typing.Self:
        """
        Constructs a new instance of the class representing a specific type of concept relationship defined by the `SOME` type identifier. This static factory method accepts a string defining the role and a `Concept` object, delegating the actual instantiation logic to the underlying `new` method. It serves as a semantic convenience for creating objects that represent partial or existential quantification within the broader concept system.

        :param role: The name or identifier of the property or relation involved in the existential restriction.
        :type role: str
        :param concept: The concept to be represented as a 'some' concept.
        :type concept: Concept

        :return: A new instance of the class representing a "some" concept relationship initialized with the provided role and concept.

        :rtype: typing.Self
        """

        return AllSomeConcept.new(ConceptType.SOME, role, concept)

    def clone(self) -> typing.Self:
        """
        Creates and returns a distinct copy of the current `AllSomeConcept` instance. This method generates the new object by passing the current object's `type`, `role`, and `curr_concept` attributes to the class constructor. The original object remains unmodified by this operation, although the clone will reference the same underlying attribute values as the source.

        :return: A new instance of the class with the same type, role, and current concept as the current object.

        :rtype: typing.Self
        """

        return AllSomeConcept.new(self.type, self.role, self.curr_concept)

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Creates and returns a new `AllSomeConcept` instance where all occurrences of the specified concept `a` within the underlying `curr_concept` are replaced by concept `c`. The `type` and `role` attributes of the original instance are preserved in the resulting object. This method does not modify the current instance in place, ensuring immutability.

        :param a: The concept to be replaced.
        :type a: Concept
        :param c: The concept to substitute in place of `a`.
        :type c: Concept

        :return: Returns a new concept where all occurrences of concept `a` are replaced by concept `c`.

        :rtype: Concept
        """

        return AllSomeConcept.new(self.type, self.role, self.curr_concept.replace(a, c))

    def get_atoms(self) -> list[typing.Self]:
        """
        Retrieves the fundamental atomic elements associated with the current concept by delegating the call to the `get_atoms` method of the internal `curr_concept` attribute. The returned list contains instances of the class, representing the indivisible components that constitute the concept's structure. This method acts as a pass-through wrapper without modifying the state of the object, though it may raise an error if the underlying `curr_concept` is not initialized.

        :return: A list of instances of this class representing the atomic components of the current concept.

        :rtype: list[typing.Self]
        """

        return self.curr_concept.get_atoms()

    def is_complemented_atomic(self) -> bool:
        """
        Determines if the current concept represents a complemented atomic concept, which is the negation of a primitive class. Because this class models a complex restriction involving quantifiers rather than a simple negation, it cannot satisfy this condition. The method always returns False and has no side effects.

        :return: True if the object is complemented atomic, False otherwise.

        :rtype: bool
        """

        return False

    def compute_name(self) -> str:
        """
        Generates a string representation of the concept based on its quantifier type, formatting the output to include the role and current concept within parentheses. If the concept type is defined as 'ALL', the resulting string uses the 'all' quantifier; otherwise, it defaults to the 'some' quantifier. This method does not modify the object's state and relies on the string representations of the associated role and concept attributes.

        :return: A string representation of the concept, formatted as '(all role concept)' or '(some role concept)' based on the concept type.

        :rtype: str
        """

        if self.type == ConceptType.ALL:
            return f"(all {self.role} {self.curr_concept})"
        else:
            return f"(some {self.role} {self.curr_concept})"

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Calculates and returns the set of atomic concepts by delegating the computation to the concept object stored in the `curr_concept` attribute. This method serves as a wrapper that forwards the request, allowing the underlying concept to determine its own atomic constituents. The result is a set containing the fundamental concepts that compose the current structure, and the operation relies entirely on the implementation of the delegated method within the referenced concept.

        :return: A set of atomic concepts that constitute the current concept.

        :rtype: set[Concept]
        """

        return self.curr_concept.compute_atomic_concepts()

    def get_roles(self) -> set[str]:
        """
        Returns a comprehensive set of role identifiers associated with the current instance and its related concept. The method constructs a set containing the instance's own `role` attribute and merges it with the roles retrieved from the `curr_concept` attribute via a recursive call to `get_roles`. This ensures that the returned collection includes both the local role and any roles inherited or defined by the linked concept object.

        :return: A set of role strings representing the union of the instance's role and the roles of the current concept.

        :rtype: set[str]
        """

        return set([self.role]) | self.curr_concept.get_roles()

    def __neg__(self) -> Concept:
        """
        Implements the unary negation operator for the concept, returning a new instance that represents the logical inverse. The method swaps the quantifier type between 'ALL' and 'SOME', retains the current role, and recursively negates the inner concept. This operation is side-effect free, leaving the original object unchanged.

        :return: The logical negation of the concept, with the quantifier type toggled between ALL and SOME and the underlying concept negated.

        :rtype: Concept
        """

        return AllSomeConcept.new(
            ConceptType.ALL if self.type == ConceptType.SOME else ConceptType.SOME,
            self.role,
            -self.curr_concept,
        )

    def __hash__(self) -> int:
        """
        Returns an integer hash value for the instance based on its string representation, enabling the object to be used as a dictionary key or stored in a set. The implementation delegates to the built-in `hash` function applied to `str(self)`, meaning the hash value is intrinsically linked to the output of the object's string conversion. Consequently, if the object is mutable and its string representation changes, the hash value will also change, which violates the immutability requirement for objects used in hash-based collections and may lead to unpredictable behavior.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))


# class AllConcept(AllSomeConcept):
#     def __call__(self, *args) -> typing.Self:
#         return AllSomeConcept.all(args)


# class SomeConcept(AllSomeConcept):
#     def __call__(self, *args) -> typing.Self:
#         return AllSomeConcept.some(args)


All = AllSomeConcept.all
Some = AllSomeConcept.some
