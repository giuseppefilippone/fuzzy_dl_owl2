fuzzy_dl_owl2.fuzzydl.query.classification_query
================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.classification_query



.. ── LLM-GENERATED DESCRIPTION START ──

Encapsulates the logic for executing a classification operation on a knowledge base within a query framework.


Description
-----------


Extending the base ``Query`` class, this component serves as a specialized command to initiate the classification process of a provided knowledge base. Unlike other query types that might require complex parameter resolution or validation steps beforehand, the implementation intentionally leaves the preprocessing phase empty, indicating that classification is a standalone operation dependent only on the current state of the knowledge base. During execution, the logic invokes the classification routine directly on the knowledge base object, handling potential runtime errors gracefully by catching exceptions and interpreting them as indicators of an inconsistent knowledge base rather than allowing the application to crash. Upon successful completion, a solution object with a perfect score is generated, while failures result in a specific error state solution, ensuring that the classification status is communicated clearly through the standard query interface.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.classification_query.ClassificationQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_classification_query_ClassificationQuery.png
       :alt: UML Class Diagram for ClassificationQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ClassificationQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_classification_query_ClassificationQuery.pdf
       :alt: UML Class Diagram for ClassificationQuery
       :align: center
       :width: 11.2cm
       :class: uml-diagram

       UML Class Diagram for **ClassificationQuery**

.. py:class:: ClassificationQuery

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.classification_query.ClassificationQuery
      :parts: 1
      :private-bases:


   This class defines a specific type of inquiry designed to trigger the classification of a knowledge base. It operates by invoking the classification method on the provided knowledge base object during the solve phase. If the classification completes without error, the query returns a successful solution with a score of 1.0; however, if the process raises an exception, it interprets this as an inconsistency within the knowledge base and returns the corresponding error state. Unlike other query types, this implementation does not require any preprocessing steps before execution.


   .. py:method:: __str__() -> str

      Returns the string representation of the `ClassificationQuery` object, specifically the constant prompt "Classify? <= ". This method is invoked when the object is converted to a string or printed, providing a standardized textual format that indicates the nature of the query. The output is static and does not depend on the internal state of the instance.

      :return: Returns the string representation of the object, specifically the prompt 'Classify? <= '.

      :rtype: str



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the current query instance for execution by resolving and validating its parameters against the provided KnowledgeBase. This method typically performs lookups to map external identifiers or labels to internal representations used by the system, ensuring that all constraints are valid within the context of the specific knowledge base. It operates by mutating the internal state of the query object rather than returning a new instance, potentially raising exceptions if the referenced classes or entities do not exist in the KnowledgeBase.

      :param kb: The knowledge base instance to be prepared or modified for subsequent operations.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Executes the classification process on the provided KnowledgeBase to determine a solution. This method invokes the classification logic of the knowledge base and returns a Solution object representing a successful outcome if no errors occur. Should an exception be raised during classification, the method logs the traceback and returns a Solution indicating that the knowledge base is inconsistent, thereby preventing the exception from propagating.

      :param kb: The knowledge base instance to be solved.
      :type kb: KnowledgeBase

      :return: A Solution object representing the outcome of the classification attempt. It indicates success with a value of 1.0 or failure due to an inconsistent knowledge base.

      :rtype: Solution


