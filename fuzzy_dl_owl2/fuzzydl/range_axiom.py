from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept


class RangeAxiom:
    """
    This class represents a logical constraint used to define the permissible types of individuals that can be the target of a specific relationship or role. It enforces the rule that any individual related through the specified role must be an instance of the provided concept. To utilize this constraint, an instance is created by passing the role's identifier as a string and the corresponding concept object.

    :param role: The name of the role for which the range axiom is defined.
    :type role: str
    :param concept: The concept defining the range of the role, representing the set of individuals that can be related through it.
    :type concept: Concept
    """


    def __init__(self, role: str, concept: Concept) -> None:
        """
        Initializes a new instance representing a range axiom, which defines the permissible types or concepts that a specific role can take as its value. The constructor accepts a string identifying the role and a Concept object representing the range constraint, storing them as instance attributes. This setup allows the axiom to be used for validation or reasoning regarding the properties of entities within the system.

        :param role: The specific function or capacity that the associated concept fulfills.
        :type role: str
        :param concept: The Concept instance to be associated with the object.
        :type concept: Concept
        """

        self.role: str = role
        self.concept: Concept = concept
