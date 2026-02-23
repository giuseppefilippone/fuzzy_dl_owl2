API Reference
=============

This page contains auto-generated API reference documentation [#f1]_.


.. ── LLM-GENERATED DESCRIPTION START ──

A hybrid reasoning and translation framework that bridges Fuzzy Description Logic with OWL2 ontologies using tableau-based algorithms and Mixed-Integer Linear Programming.


Description
-----------


Software within this collection provides a dual-layered architecture that facilitates both advanced reasoning under uncertainty and interoperability between fuzzy logic systems and semantic web standards. At the reasoning core, a hybrid engine integrates tableau-based logical inference with Mixed-Integer Linear Programming to determine the satisfiability and truth degrees of complex assertions, effectively separating the management of ontology states from the mathematical solving of optimization problems. Complementing the inference capabilities, a translation framework parses OWL2 ontologies annotated with fuzzy semantics, transforming them into structured object models that encapsulate mathematical membership functions and fuzzy operators for downstream processing. By modularizing components such as lexical analysis, constraint evaluation, and data serialization, the system supports diverse tasks like classification, subsumption checking, and instance retrieval while ensuring that complex logical constructs are accurately mapped between textual definitions and standard XML formats.


Sub-packages
------------


* ``fuzzy_dl_owl2.fuzzydl`` — A fuzzy description logic reasoning engine that combines tableau-based algorithms with Mixed-Integer Linear Programming to determine the satisfiability and truth degrees of uncertain assertions.
* ``fuzzy_dl_owl2.fuzzyowl2`` — A translation framework that converts OWL2 ontologies annotated with fuzzy logic semantics into a Fuzzy Description Logic representation suitable for reasoning engines.

.. ── LLM-GENERATED DESCRIPTION END ──

.. toctree::
   :titlesonly:

   /api/fuzzy_dl_owl2/index

.. [#f1] Created with `sphinx-autoapi <https://github.com/readthedocs/sphinx-autoapi>`_