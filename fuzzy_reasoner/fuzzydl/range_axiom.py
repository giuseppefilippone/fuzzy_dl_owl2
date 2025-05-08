from fuzzy_reasoner.fuzzydl.concept.concept import Concept


class RangeAxiom:
    def __init__(self, role: str, concept: Concept) -> None:
        self.role: str = role
        self.concept: Concept = concept
