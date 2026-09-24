fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception
========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception





.. ── LLM-GENERATED DESCRIPTION START ──

A domain-specific exception for reporting errors that arise during fuzzy ontology and fuzzy description logic operations, such as invalid concept definitions or the incorrect application of fuzzy modifiers.


Description
-----------


``FuzzyOntologyException`` extends Python's built-in ``Exception`` to give the fuzzy description logic framework a dedicated error channel that can be caught independently of generic language-level exceptions. Callers raise it with a single human-readable message string, which the constructor forwards unchanged to the superclass so that the exception behaves exactly like any standard Python error in tracebacks, logging output, and ``except`` clauses. The design is deliberately minimal — no additional state or behaviour is layered on top of the base class — because the value lies purely in the distinct type, which allows client code to isolate and handle ontology-related failures without accidentally masking unrelated bugs. The result is error handling across the wider fuzzydl system that is both precise and easy to reason about, since a malformed concept expression or a misused modifier can be distinguished at the ``except`` level from any other kind of runtime problem.

.. ── LLM-GENERATED DESCRIPTION END ──

Exceptions
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception.FuzzyOntologyException


Module Contents
---------------

.. py:exception:: FuzzyOntologyException(message: str)

   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception.FuzzyOntologyException
      :parts: 1
      :private-bases:


   This custom exception class is designed to handle errors specific to the fuzzy description logic framework. It is raised when issues arise during the manipulation of concepts, such as invalid concept definitions or the incorrect application of modifiers. By extending the standard Exception class, it allows developers to catch and manage domain-specific errors distinctly from general Python exceptions. To use it, instantiate the class with a descriptive string message that details the specific error encountered.
