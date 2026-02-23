from __future__ import annotations

import copy
import typing
from abc import abstractmethod

from fuzzy_dl_owl2.fuzzydl.assertion.assertion import Assertion
from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number import (
    TriangularFuzzyNumber,
)
from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.relation import Relation
from fuzzy_dl_owl2.fuzzydl.restriction.restriction import Restriction
from fuzzy_dl_owl2.fuzzydl.util.constants import RepresentativeIndividualType


class Individual:
    """
    This entity serves as a fundamental node within a knowledge base or ontology, representing a specific instance that possesses various properties and relationships with other entities. It is designed to manage the state of concept assertions, role relations, and restrictions during reasoning processes, such as those found in description logic tableau algorithms. Users can initialize it with a unique name and subsequently populate it with concepts, define role connections, and apply specific constraints like concrete role restrictions or "not self" rules. The object also supports advanced operations like cloning its internal state for branching and pruning relations to blockable successors to optimize reasoning performance.

    :param DEFAULT_NAME: Default prefix used for generating names for new individuals.
    :type DEFAULT_NAME: str
    :param name: The unique identifier for the individual, used for equality comparison and string representation.
    :type name: str
    :param concrete_role_restrictions: Maps concrete role names to a list of assertions representing restrictions on the individual's concrete values.
    :type concrete_role_restrictions: dict[str, list[Assertion]]
    :param fillers_to_show: Maps role names to sets of individual names representing the fillers to be displayed for those roles.
    :type fillers_to_show: dict[str, set[str]]
    :param list_of_concepts: A set of concepts for which a concept assertion has been processed for the individual.
    :type list_of_concepts: set[Concept]
    :param nominal_list: A set of names of individuals that are in the nominal list, used to determine if the individual is indirectly blocked.
    :type nominal_list: set[str]
    :param not_self_roles: A set of role names for which the "not self" rule applies, preventing the individual from being a filler for itself.
    :type not_self_roles: set[str]
    :param role_relations: A dictionary mapping role names to lists of `Relation` objects representing the connections from this individual to other individuals.
    :type role_relations: dict[str, list[Relation]]
    :param role_restrictions: A mapping of role names to lists of restrictions defining constraints on the fillers of those roles for this individual.
    :type role_restrictions: dict[str, list[Restriction]]

    :raises InconsistentOntologyException: Raised when the individual is assigned a name that conflicts with an existing name, violating the unique name assumption and resulting in an inconsistent ontology.
    """


    # Default prefix for new individual names
    DEFAULT_NAME: str = "i"

    def __init__(self, name: str) -> None:
        """
        Constructs a new Individual entity identified by the provided name string. This method initializes the instance's core identifier and sets up the necessary internal state by creating empty collections for tracking various semantic properties. Specifically, it prepares dictionaries to manage concrete role restrictions, visible fillers, role relations, and role restrictions, alongside sets to store processed concepts, nominal identifiers, and roles requiring specific exclusion rules.

        :param name: The name or identifier for the instance.
        :type name: str
        """

        self.name: str = name
        # Concrete role restrictions
        self.concrete_role_restrictions: dict[str, list[Assertion]] = dict()
        # Fillers to show
        self.fillers_to_show: dict[str, set[str]] = dict()
        # List of concepts such that a concept assertion has been processed
        self.list_of_concepts: set[Concept] = set()
        # Indicates if the individual is indirectly blocked or not
        self.nominal_list: set[str] = set()
        # List of roles for which to apply the not self rule
        self.not_self_roles: set[str] = set()
        # Role relations
        self.role_relations: dict[str, list[Relation]] = dict()
        # Role restrictions
        self.role_restrictions: dict[str, list[Restriction]] = dict()

    def clone(self) -> typing.Self:
        """
        Creates and returns a distinct copy of the current `Individual` instance. The method instantiates a new object using the existing name and then delegates the transfer of internal state to the `clone_attributes` method, ensuring that the new instance replicates the original's configuration. This approach provides a controlled cloning mechanism, though the depth and behavior of the attribute copy depend entirely on the implementation of `clone_attributes`.

        :return: A new instance of the class initialized with the same name and attributes as the current object.

        :rtype: typing.Self
        """

        ind = Individual(self.name)
        self.clone_attributes(ind)
        return ind

    def clone_attributes(self, ind: typing.Self) -> None:
        """
        Copies the attributes of the current instance into the provided target `Individual` instance, effectively duplicating the source's state. The method employs different copying strategies depending on the attribute: it performs deep copies for `fillers_to_show`, `nominal_list`, and `not_self_roles`, creates new set instances for `list_of_concepts`, and reconstructs dictionaries for `role_restrictions` and `role_relations` while invoking the `clone` method on their contained elements. This ensures that mutable data structures are independent between the source and the target, preventing unintended side effects from shared references. Notably, the `representatives` attribute is explicitly skipped during this process. The operation modifies the target instance in place and does not return a value.

        :param ind: The destination instance of the same class to receive the cloned attributes of the current instance.
        :type ind: typing.Self
        """

        ind.concrete_role_restrictions = {
            k: [a for a in v] for k, v in self.concrete_role_restrictions.items()
        }
        ind.fillers_to_show = copy.deepcopy(self.fillers_to_show)
        ind.list_of_concepts = set([c for c in self.list_of_concepts])
        ind.nominal_list = copy.deepcopy(self.nominal_list)
        ind.not_self_roles = copy.deepcopy(self.not_self_roles)
        # ind.representatives = copy.deepcopy(self.representatives)
        ind.role_restrictions = {
            k: [r.clone() for r in v] for k, v in self.role_restrictions.items()
        }
        ind.role_relations = {
            k: [r.clone() for r in v] for k, v in self.role_relations.items()
        }

    def set_name(self, name: str) -> None:
        """
        Assigns the provided string value to the `name` attribute of the Individual instance, effectively updating the individual's identifier. This operation mutates the object's state in place, overwriting any previously stored name. While the signature expects a string, the implementation performs no type checking, so any object passed as `name` will be assigned to the attribute.

        :param name: The new name to assign to the instance.
        :type name: str
        """

        self.name = name

    def add_concrete_restriction(self, f_name: str, ass: Assertion) -> None:
        """
        Associates a concrete restriction assertion with a specific feature name for the individual by updating the internal `concrete_role_restrictions` dictionary. If the feature name already exists, the assertion is appended to the existing list of restrictions; otherwise, a new list is created containing the assertion. This operation modifies the state of the individual in place.

        :param f_name: The name of the concrete role or feature to which the restriction applies.
        :type f_name: str
        :param ass: The assertion representing the negated datatype restriction to be added.
        :type ass: Assertion
        """

        self.concrete_role_restrictions[f_name] = self.concrete_role_restrictions.get(
            f_name, []
        ) + [ass]

    @abstractmethod
    def get_representative_if_exists(
        self,
        type: RepresentativeIndividualType,
        f_name: str,
        f: TriangularFuzzyNumber,
    ):
        """
        Retrieves a representative individual matching the specified type, name, and triangular fuzzy number, if such a representative is currently associated with the instance. This method serves as a query operation that searches for an existing representative based on the provided criteria without modifying the state of the individual. If no matching representative is found, the method returns None. As an abstract method, it must be implemented by subclasses to define the specific logic for identifying and returning the appropriate representative entity.

        :param type: Specifies the category or classification of the representative individual to retrieve.
        :type type: RepresentativeIndividualType
        :param f_name: The name or identifier of the triangular fuzzy number.
        :type f_name: str
        :param f: The triangular fuzzy number for which the representative individual is being retrieved.
        :type f: TriangularFuzzyNumber
        """

        pass

    def add_concept(self, c: Concept) -> None:
        """
        Associates a specific `Concept` instance with this `Individual` by adding it to the internal collection of concepts. This method mutates the `Individual`'s state by inserting the provided object into `list_of_concepts`. Because the underlying storage mechanism behaves like a set, attempting to add a concept that is already present will not result in a duplicate entry or raise an error.

        :param c: The concept object to be added to the internal collection.
        :type c: Concept
        """

        self.list_of_concepts.add(c)

    def get_concepts(self) -> set[Concept]:
        """
        Retrieves the collection of concepts associated with this `Individual` instance. The method returns the internal set of `Concept` objects directly. Because a reference to the internal set is returned, any modifications made to the set by the caller will directly alter the state of the `Individual` object.

        :return: A set of concepts associated with this instance.

        :rtype: set[Concept]
        """

        return self.list_of_concepts

    def add_to_nominal_list(self, ind_name: str) -> None:
        """
        Appends the specified name to the internal registry of nominal identifiers maintained by the instance. This method mutates the object's state by inserting the provided string into the `nominal_list` attribute. Because the underlying collection behaves like a set, adding a name that already exists results in no change to the data structure.

        :param ind_name: The individual name to be added to the nominal list.
        :type ind_name: str
        """

        self.nominal_list.add(ind_name)

    def get_nominal_list(self) -> set[str]:
        """
        Retrieves the set of nominal values associated with this `Individual` instance. This method returns a direct reference to the internal `nominal_list` attribute, which contains string identifiers. Since the returned set is mutable, any modifications made to it by the caller will directly alter the internal state of the object.

        :return: The set of nominal values.

        :rtype: set[str]
        """

        return self.nominal_list

    def is_blockable(self) -> bool:
        """
        Determines whether the individual is eligible to be blocked. This implementation always returns False, indicating that the base `Individual` type does not support or permit blocking operations. The method is intended to be overridden by subclasses to provide specific logic for determining blockability based on the subclass's requirements.

        :return: True if the object can be blocked, False otherwise.

        :rtype: bool
        """

        return False

    def set_label(self, ind_name: str) -> None:
        """
        This method is intended to assign a new label to the individual, but it enforces a strict constraint that prevents this modification. Instead of updating the label, it raises an InconsistentOntologyException to signal that the individual cannot be associated with the specified name, as this would conflict with its existing identity or the ontology's consistency rules.

        :param ind_name: The intended name or label to assign to the individual.
        :type ind_name: str

        :raises InconsistentOntologyException: Raised when the provided name conflicts with the individual's existing name, as an individual cannot be associated with both names simultaneously.
        """

        raise InconsistentOntologyException(
            f"Individuals cannot have names {self.name} and {ind_name}"
        )

    def prune(self) -> None:
        """Clears all role relations associated with the current individual and recursively prunes any blockable successors. The method iterates through existing relations to identify connected individuals that are marked as blockable, storing them for subsequent processing. Once identified, the method resets the individual's `role_relations` to an empty dictionary, effectively disconnecting it from the graph. Finally, it invokes the `prune` method on each of the collected blockable individuals to propagate the cleanup operation. If the individual has no relations or none of its successors are blockable, the method simply clears the relations dictionary."""

        to_prune: list[Individual] = []
        for role in self.role_relations:
            # We remove all relations
            rels: list[Relation] = self.role_relations.get(role, [])
            for r in rels:
                obj: Individual = r.get_object_individual()
                if obj.is_blockable():
                    to_prune.append(obj)
        # We remove all relations
        self.role_relations = dict()
        # Prune blockable successors
        for i in to_prune:
            i.prune()

    def __eq__(self, value: typing.Self) -> bool:
        """
        Checks if the current `Individual` instance is equal to another instance by comparing their `name` attributes. This method overrides the default equality behavior to ensure that two objects are considered equivalent if they share the same name, regardless of other potential differences in state. It returns `True` if the names match and `False` otherwise.

        :param value: The object to compare against.
        :type value: typing.Self

        :return: True if the instance has the same name as the other instance, otherwise False.

        :rtype: bool
        """

        return self.name == value.name

    def __ne__(self, value: typing.Self) -> bool:
        """
        Checks whether the current instance is not equal to the provided value. This method implements the inequality operator by returning the logical negation of the equality comparison, effectively delegating the logic to the `__eq__` method. It ensures that if two objects are considered equal, they are not considered unequal, and vice versa, without causing any side effects.

        :param value: The object to compare against the current instance.
        :type value: typing.Self

        :return: True if the current instance is not equal to the provided value, False otherwise.

        :rtype: bool
        """

        return not (self == value)

    def __repr__(self) -> str:
        """
        Returns the official string representation of the instance by delegating to the object's informal string conversion method. This implementation ensures that the output generated by the built-in `repr()` function is identical to that produced by `str()`, providing a unified string format for the `Individual` object. Because it relies on the `__str__` method, any modifications to the informal string representation will automatically propagate to the formal representation, and any errors raised during string conversion will be passed through.

        :return: The string representation of the object, as produced by str().

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Returns the informal string representation of the Individual instance, which is invoked by the `str()` built-in function and print operations. This method simply returns the value of the instance's `name` attribute, providing a human-readable identifier for the object. It has no side effects, though it relies on the `name` attribute being present and accessible on the instance.

        :return: The string representation of the object, which is the value of the `name` attribute.

        :rtype: str
        """

        return self.name
