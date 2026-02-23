from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.degree.degree_numeric import DegreeNumeric
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class Assertion:
    """
    This class models a fuzzy logic constraint or statement, specifically an assertion that an individual belongs to a concept with a minimum degree of membership. It is defined by three components: an individual entity, a concept (or category), and a degree representing a lower bound threshold. The assertion is considered satisfied if the individual's actual membership in the concept meets or exceeds this threshold. Users can instantiate this class by providing an `Individual`, a `Concept`, and a `Degree`, and utilize methods to retrieve or modify these components, such as `get_concept` or `set_lower_limit`. Additionally, the class supports cloning and generates a string representation in the format 'individual:concept >= degree'. It is important to note that the equality comparison logic is non-standard; two assertions are considered equal if they share the same individual and concept, provided the numeric degree of the first is less than the degree of the second, in addition to standard string equality.

    :param individual: The subject of the assertion, corresponding to the individual $a$ in the expression $a:C \ge d$.
    :type individual: Individual
    :param concept: The concept representing the category or property that the individual is evaluated against in the assertion.
    :type concept: Concept
    :param degree: The lower bound threshold that the individual's membership degree in the concept must meet or exceed for the assertion to be satisfied.
    :type degree: Degree
    """

    def __init__(self, ind: Individual, c: Concept, d: Degree) -> None:
        """
        Constructs an instance representing a logical association between an `Individual` and a `Concept`, characterized by a specific `Degree`. The degree parameter serves as a lower bound for the assertion, defining the minimum strength of the relationship. This initializer assigns the provided arguments directly to the instance's attributes without performing validation or inducing side effects on the inputs.

        :param ind: The individual entity associated with this instance.
        :type ind: Individual
        :param c: The concept associated with the individual.
        :type c: Concept
        :param d: The lower bound degree value.
        :type d: Degree
        """

        self.individual: Individual = ind
        self.concept: Concept = c
        # Lower bound degree
        self.degree: Degree = d

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of the class that replicates the state of the current object. The new object is initialized with the same `individual`, `concept`, and `degree` attributes as the original. This method does not modify the existing object, but it performs a shallow copy, meaning that if the attributes are mutable objects, changes to them in the clone will affect the original instance.

        :return: A new instance of the class that is a copy of the current object, initialized with the same individual, concept, and degree.

        :rtype: typing.Self
        """

        return Assertion(self.individual, self.concept, self.degree)

    def get_type(self) -> ConceptType:
        """
        Retrieves the `ConceptType` of the underlying concept associated with this assertion. This method acts as a getter, returning the value of the `type` attribute found on the internal `concept` object. It performs no modifications to the instance state, though it relies on the `concept` attribute being properly initialized to avoid runtime errors.

        :return: The type of the concept associated with this instance.

        :rtype: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
        """

        return self.concept.type

    def get_lower_limit(self) -> Degree:
        """
        Retrieves the lower limit defined for this assertion, returning the value stored in the `degree` attribute. This method serves as a simple accessor to expose the minimum boundary or threshold associated with the assertion's logic. It does not modify the object's state and has no side effects, though it assumes the `degree` attribute has been properly initialized.

        :return: The Degree representing the lower limit.

        :rtype: Degree
        """

        return self.degree

    def get_concept(self) -> Concept:
        """
        Retrieves the `Concept` instance associated with this `Assertion`. This method serves as a straightforward accessor for the internal `concept` attribute, returning the stored value without modifying the object's state. The returned object represents the specific concept that this assertion is evaluating or referencing.

        :return: Returns the `Concept` instance associated with this object.

        :rtype: Concept
        """

        return self.concept

    def get_individual(self) -> Individual:
        """
        Returns the `Individual` entity associated with this assertion instance. This method provides direct access to the internal `individual` attribute, allowing the caller to inspect the specific subject or agent linked to the assertion. Because it returns a reference to the object rather than a copy, any modifications made to the returned `Individual` will be reflected in the original data held by the assertion. If the attribute has not been initialized, an `AttributeError` will be raised.

        :return: The Individual object associated with this instance.

        :rtype: Individual
        """

        return self.individual

    def set_individual(self, ind: Individual) -> None:
        """
        Associates the `Assertion` instance with a specific `Individual` by assigning the provided object to the `individual` attribute. This operation updates the internal state of the assertion and overwrites any existing reference to a previously set individual. The method performs no validation on the input type beyond standard assignment, relying on the caller to provide a compatible object.

        :param ind:
        :type ind: Individual
        """

        self.individual = ind

    def set_lower_limit(self, deg: Degree) -> None:
        """
        Updates the internal state of the assertion by assigning the provided `Degree` object to the `degree` attribute, effectively setting the lower limit for the assertion's scope or validity. This operation modifies the object in place and does not return a value. It is typically used to define the minimum degree threshold that the assertion will enforce.

        :param deg: The degree value to set as the lower limit.
        :type deg: Degree
        """

        self.degree = deg

    def get_name_without_degree(self) -> str:
        """
        Constructs a simplified string identifier for the assertion by combining the `individual` and `concept` attributes separated by a colon. This representation specifically excludes the degree component, offering a way to reference the core assertion logic independent of its associated weight or confidence level. The method assumes that the `individual` and `concept` attributes are present on the instance and can be converted to strings.

        :return: A string combining the individual and concept, separated by a colon.

        :rtype: str
        """

        return f"{self.individual}:{self.concept}"

    def equals(self, ass: typing.Self) -> bool:
        """
        Determines whether the current instance is equivalent to the provided `Assertion` object by performing a direct equality comparison. This method delegates to the underlying `__eq__` implementation, returning `True` if the two objects are considered equal and `False` otherwise. The operation does not modify the state of either instance.

        :param ass: The instance to compare against the current object.
        :type ass: typing.Self

        :return: True if the provided object is equal to this instance, False otherwise.

        :rtype: bool
        """

        return self == ass

    def __eq__(self, value: typing.Self) -> bool:
        """
        Determines whether the current instance is equal to another object based on specific criteria. Returns False immediately if the provided value is not an instance of Assertion. Equality is established if the string representations of both assertions are identical. Additionally, equality is considered true if both assertions share the same name (excluding degree), possess numeric lower limits, and the numerical value of the current assertion's lower limit is strictly less than that of the provided assertion. This method does not modify the state of either object.

        :param value: The object to compare against the current instance.
        :type value: typing.Self

        :return: True if the provided value is an Assertion instance considered equivalent to this one, determined by identical string representations or matching names with a numerically lower lower limit; False otherwise.

        :rtype: bool
        """

        if not isinstance(value, Assertion):
            return False

        same: bool = False
        if str(self) == str(value):
            same = True
        elif (
            self.get_name_without_degree() == value.get_name_without_degree()
            and isinstance(self.get_lower_limit(), DegreeNumeric)
            and isinstance(value.get_lower_limit(), DegreeNumeric)
            and typing.cast(DegreeNumeric, self.get_lower_limit()).get_numerical_value()
            < typing.cast(DegreeNumeric, value.get_lower_limit()).get_numerical_value()
        ):
            same = True
        return same

    def __ne__(self, value: typing.Self) -> bool:
        """
        Determines if the current instance is not equal to the specified value by evaluating the logical negation of the equality comparison. This method enables the use of the `!=` operator for `Assertion` objects, relying on the underlying `__eq__` implementation to handle the actual comparison logic. Consequently, any edge cases or type restrictions enforced by the equality check will apply here, and exceptions raised during equality comparison will propagate through this method.

        :param value: The object to compare against for inequality.
        :type value: typing.Self

        :return: True if the instance is not equal to the provided value, False otherwise.

        :rtype: bool
        """

        return not (self == value)

    def __repr__(self) -> str:
        """
        Returns the official string representation of the Assertion object. This method delegates the formatting logic directly to the `__str__` method, resulting in an output that is identical to the informal string conversion. It is designed to provide a developer-readable representation, typically used in debugging contexts or interactive sessions.

        :return: Returns the string representation of the object.

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the assertion, formatted as a comparison between the entity's name and its associated degree. The output follows the pattern "name >= degree", where the name is retrieved by stripping degree information from the full identifier. This method is intended for display purposes, such as logging or debugging, and does not modify the object's state.

        :return: A string representation of the object in the format "name >= degree".

        :rtype: str
        """

        return f"{self.get_name_without_degree()} >= {self.degree}"
