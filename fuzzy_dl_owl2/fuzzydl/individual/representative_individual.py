from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number import (
        TriangularFuzzyNumber,
    )
    from fuzzy_dl_owl2.fuzzydl.individual.created_individual import CreatedIndividual
    from fuzzy_dl_owl2.fuzzydl.util.constants import RepresentativeIndividualType


class RepresentativeIndividual:
    """
    This class serves as a concrete proxy for a collection of individuals that satisfy a specific fuzzy condition relative to a threshold. It encapsulates the logic required to define a set of entities based on a `TriangularFuzzyNumber` applied to a specific feature, determining membership through a comparison type (such as greater than or less than). By associating a specific `CreatedIndividual` with this fuzzy constraint, the object models the relationship between an individual and the abstract group it represents or belongs to. This structure is primarily used to represent degrees of satisfaction within a fuzzy logic framework, enabling the system to handle uncertainty and partial truths in feature evaluation.

    :param f_name: The name of the feature for which this individual acts as a filler.
    :type f_name: str
    :param type: The classification of the representative individual, defining the specific criteria or nature of the set it represents.
    :type type: RepresentativeIndividualType
    :param f: Fuzzy number representing the degree of satisfaction of the concept by the individual.
    :type f: TriangularFuzzyNumber
    :param ind: The concrete individual entity referenced by this representative instance.
    :type ind: CreatedIndividual
    """


    def __init__(
        self,
        c_type: RepresentativeIndividualType,
        f_name: str,
        f: TriangularFuzzyNumber,
        ind: CreatedIndividual,
    ) -> None:
        # Name of the feature for which the individual is a filler.
        """
        Initializes a RepresentativeIndividual instance by associating a specific feature name with a fuzzy value and a reference individual. The constructor accepts a type classification, the name of the feature being represented, a TriangularFuzzyNumber quantifying the value, and a CreatedIndividual object serving as the reference. These parameters are stored directly as instance attributes for subsequent access.

        :param c_type: The representative type of the individual.
        :type c_type: RepresentativeIndividualType
        :param f_name: Name of the feature for which the individual acts as a filler.
        :type f_name: str
        :param f: The triangular fuzzy number representing the value of the feature.
        :type f: TriangularFuzzyNumber
        :param ind: The reference individual object.
        :type ind: CreatedIndividual
        """

        self.f_name: str = f_name
        # Type of the individual
        self.type: RepresentativeIndividualType = c_type
        # Fuzzy number
        self.f: TriangularFuzzyNumber = f
        # Reference individual
        self.ind: CreatedIndividual = ind

    def get_type(self) -> RepresentativeIndividualType:
        """
        Returns the classification type associated with this representative individual instance. This method serves as a getter for the internal `type` attribute, providing access to the specific `RepresentativeIndividualType` that defines the individual's category. The operation is read-only and does not modify the state of the object.

        :return: The type of the representative individual.

        :rtype: RepresentativeIndividualType
        """

        return self.type

    def get_feature_name(self) -> str:
        """
        Retrieves the name of the feature represented by this instance. This method serves as a simple getter for the internal `f_name` attribute, returning its current value. It performs no computation or modification of the object's state.

        :return: The name of the feature.

        :rtype: str
        """

        return self.f_name

    def get_fuzzy_number(self) -> TriangularFuzzyNumber:
        """
        Retrieves the triangular fuzzy number associated with this representative individual. This method serves as a direct accessor for the internal attribute representing the individual's value, returning the specific `TriangularFuzzyNumber` instance stored within the object. Because it returns a reference to the internal object rather than a copy, any modifications made to the returned fuzzy number will directly alter the state of this individual. If the internal attribute has not been initialized prior to calling this method, an `AttributeError` will be raised.

        :return: The TriangularFuzzyNumber instance stored in the object.

        :rtype: TriangularFuzzyNumber
        """

        return self.f

    def get_individual(self) -> CreatedIndividual:
        """
        Retrieves the `CreatedIndividual` instance currently associated with this `RepresentativeIndividual`. This method serves as an accessor for the internal `ind` attribute, returning the stored object directly. Since it returns a reference to the internal state, any modifications made to the returned object will be reflected in the `RepresentativeIndividual` instance.

        :return: The CreatedIndividual instance associated with this object.

        :rtype: CreatedIndividual
        """

        return self.ind
