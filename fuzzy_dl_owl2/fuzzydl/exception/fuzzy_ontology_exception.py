class FuzzyOntologyException(Exception):

    """This custom exception class is designed to handle errors specific to the fuzzy description logic framework. It is raised when issues arise during the manipulation of concepts, such as invalid concept definitions or the incorrect application of modifiers. By extending the standard Exception class, it allows developers to catch and manage domain-specific errors distinctly from general Python exceptions. To use it, instantiate the class with a descriptive string message that details the specific error encountered."""


    def __init__(self, message: str) -> None:
        """
        Initializes the exception instance with a descriptive error message provided by the caller. This method accepts a single string argument which is forwarded to the superclass constructor, ensuring that the exception behaves consistently with standard Python error handling mechanisms. By capturing the message, the exception allows for detailed logging or debugging of issues related to fuzzy ontology operations.

        :param message: A human-readable description of the error or condition.
        :type message: str
        """

        super().__init__(message)
