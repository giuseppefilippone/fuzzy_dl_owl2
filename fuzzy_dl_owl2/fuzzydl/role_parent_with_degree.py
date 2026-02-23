class RoleParentWithDegree:
    """
    This class models a weighted hierarchical relationship between a role and its parent, capturing the extent to which the parent role is included. It stores a string identifier for the parent role alongside a floating-point degree value, which usually represents a probability or strength of inclusion within the range of 0 to 1. Users can instantiate this object with the parent name and degree, and subsequently retrieve these values via the getter methods to support complex role inheritance logic.

    :param parent: The name of the parent role.
    :type parent: str
    :param degree: Inclusion degree of the parent role, ranging from 0 to 1.
    :type degree: float
    """


    def __init__(self, parent: str, degree: float) -> None:
        """
        Initializes a new instance by associating a parent entity with a specific degree value. The constructor accepts a string identifier for the parent and a floating-point number for the degree, assigning them directly to the corresponding instance attributes. Since no validation logic is applied, the attributes store the inputs exactly as provided, allowing for any string or float value to be set.

        :param parent: The string identifier or name of the parent entity.
        :type parent: str
        :param degree: The degree value associated with the instance.
        :type degree: float
        """

        self.parent: str = parent
        self.degree: float = degree

    def get_degree(self) -> float:
        """
        Retrieves the current degree value associated with the instance. This method serves as an accessor for the `degree` attribute, returning the stored numeric value without modifying the object's internal state. It is typically used to inspect the specific weight or metric assigned to this role.

        :return: The degree value associated with the object.

        :rtype: float
        """

        return self.degree

    def get_parent(self) -> str:
        """
        Retrieves the parent identifier associated with the current role instance. This method returns the string value stored in the `parent` attribute, representing the hierarchical relationship or predecessor of the current role. It is a read-only operation that does not alter the object's state.

        :return: The string representing the parent of the object.

        :rtype: str
        """

        return self.parent
