fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception
===============================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception





.. ── LLM-GENERATED DESCRIPTION START ──

A custom exception that signals logical inconsistencies detected in fuzzy ontologies, such as contradictory concept definitions or unsatisfiable concepts.


Description
-----------


**InconsistentOntologyException** extends Python's built-in ``Exception`` to provide a dedicated error type for a fuzzy description logic framework, allowing reasoning and ontology-management code to distinguish genuine logical conflicts from ordinary runtime failures. Because it carries a single human-readable message that is forwarded directly to the superclass constructor, the exception integrates seamlessly with standard Python error handling, appearing correctly in tracebacks, logging output, and ``except`` clauses. Raising a specialised type rather than a generic ``Exception`` lets callers catch ontology inconsistencies selectively, so they can respond to logical problems — for example, by aborting a reasoning task or reporting a diagnostic — without masking unrelated bugs. The minimal, message-only design keeps the class lightweight while still giving developers the contextual detail needed to pinpoint the exact source of an inconsistency during debugging.

.. ── LLM-GENERATED DESCRIPTION END ──

Exceptions
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception.InconsistentOntologyException


Module Contents
---------------

.. py:exception:: InconsistentOntologyException(message: str)

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception.InconsistentOntologyException
      :parts: 1
      :private-bases:


   This exception is raised when an inconsistency is detected within a fuzzy ontology, particularly within the context of a fuzzy description logic framework. It serves to signal errors related to contradictory concept definitions, unsatisfiable concepts, or other logical conflicts that arise during the manipulation of concepts. Users can instantiate this class with a descriptive string message to provide context about the specific inconsistency encountered, enabling precise error handling and debugging in ontology management systems.
