from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number import (
        TriangularFuzzyNumber,
    )
    from fuzzy_dl_owl2.fuzzydl.individual.created_individual import CreatedIndividual
    from fuzzy_dl_owl2.fuzzydl.util.constants import RepresentativeIndividualType


class RepresentativeIndividual:

    def __init__(
        self,
        c_type: RepresentativeIndividualType,
        f_name: str,
        f: TriangularFuzzyNumber,
        ind: CreatedIndividual,
    ) -> None:
        self.f_name: str = f_name
        self.type: RepresentativeIndividualType = c_type
        self.f: TriangularFuzzyNumber = f
        self.ind: CreatedIndividual = ind

    def get_type(self) -> RepresentativeIndividualType:
        return self.type

    def get_feature_name(self) -> str:
        return self.f_name

    def get_fuzzy_number(self) -> TriangularFuzzyNumber:
        return self.f

    def get_individual(self) -> CreatedIndividual:
        return self.ind
