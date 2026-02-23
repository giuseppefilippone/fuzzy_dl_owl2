class InconsistentOntologyException(Exception):

    """This exception is raised when an inconsistency is detected within a fuzzy ontology, particularly within the context of a fuzzy description logic framework. It serves to signal errors related to contradictory concept definitions, unsatisfiable concepts, or other logical conflicts that arise during the manipulation of concepts. Users can instantiate this class with a descriptive string message to provide context about the specific inconsistency encountered, enabling precise error handling and debugging in ontology management systems."""


    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the exception to signal that an inconsistency has been detected within an ontology. The constructor accepts a single string argument that provides a detailed description of the specific logical conflict or error encountered. By passing this message to the superclass initializer, the method ensures that the exception integrates seamlessly with Python's standard error handling mechanisms.

        :param message: A description of the error explaining why the exception was raised.
        :type message: str
        """

        super().__init__(message)
