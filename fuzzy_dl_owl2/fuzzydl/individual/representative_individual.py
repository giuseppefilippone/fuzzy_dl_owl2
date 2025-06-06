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
    New concrete individual being a representative of a set of individuals.
    Given an individual p and a fuzzy number F, a representative individual is the set of individuals that are greater or equal (or less or equal) than F. Then, p is related to the representative individual in some way.
    """

    def __init__(
        self,
        c_type: RepresentativeIndividualType,
        f_name: str,
        f: TriangularFuzzyNumber,
        ind: CreatedIndividual,
    ) -> None:
        # Name of the feature for which the individual is a filler.
        self.f_name: str = f_name
        # Type of the individual
        self.type: RepresentativeIndividualType = c_type
        # Fuzzy number
        self.f: TriangularFuzzyNumber = f
        # Reference individual
        self.ind: CreatedIndividual = ind

    def get_type(self) -> RepresentativeIndividualType:
        return self.type

    def get_feature_name(self) -> str:
        return self.f_name

    def get_fuzzy_number(self) -> TriangularFuzzyNumber:
        return self.f

    def get_individual(self) -> CreatedIndividual:
        return self.ind
