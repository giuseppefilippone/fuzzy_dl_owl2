from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept


class DomainAxiom:
    """
    This class encapsulates a logical constraint that defines the domain of a specific role within an ontology or knowledge graph. It asserts that any individual acting as the subject of the specified role must be an instance of the provided concept. By associating a role identifier with a concept definition, it serves to enforce type consistency and restrict the range of valid subjects for a given relationship.

    :param role: The name of the role for which the domain is defined.
    :type role: str
    :param concept: The concept defining the domain of the role.
    :type concept: Concept
    """


    def __init__(self, role: str, concept: Concept) -> None:
        """
        Initializes a new instance representing a domain restriction for a specific role within an ontology or logical framework. The constructor accepts a string identifying the role and a Concept object defining the domain to which the role applies. Upon instantiation, these values are directly assigned to the instance attributes `self.role` and `self.concept` for subsequent access and manipulation. No validation or transformation is performed on the inputs during initialization, meaning the instance relies on the caller to provide valid references to a role identifier and a Concept object.

        :param role: The specific function, persona, or capacity assigned to the instance.
        :type role: str
        :param concept: 
        :type concept: Concept
        """

        self.role: str = role
        self.concept: Concept = concept
