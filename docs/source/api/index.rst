API Reference
=============

This page contains auto-generated API reference documentation [#f1]_.


.. ── LLM-GENERATED DESCRIPTION START ──

A comprehensive framework for reasoning over fuzzy ontologies that translates OWL2 annotations into a Fuzzy Description Logic engine powered by Mixed-Integer Linear Programming.


Description
-----------


Software bridges standard semantic web technologies with fuzzy logic by providing a translation layer that converts OWL2 ontologies annotated with fuzzy semantics into a format suitable for specialized reasoning. Input processing involves parsing XML and grammar-based strings to extract complex fuzzy constructs like triangular functions and aggregation operators, transforming them into a structured type system that represents the domain logic. Once translated, the core reasoning engine manages a central knowledge base containing concepts, individuals, and axioms, utilizing Mixed-Integer Linear Programming solvers to perform mathematical optimization for inference tasks such as concept satisfiability and instance checking. Foundational utilities support the entire workflow by handling configuration, logging, and XML generation, ensuring that the interoperability between the OWL2 representation and the internal fuzzy logic solver remains robust and compliant with specification standards.


Sub-packages
------------


* [``fuzzy_dl_owl2.fuzzydl``] — Implements a fuzzy description logic reasoning engine that manages knowledge bases, processes axioms and concepts, and performs inference using Mixed-Integer Linear Programming solvers.
* [``fuzzy_dl_owl2.fuzzyowl2``] — A translation framework that converts OWL2 ontologies annotated with fuzzy logic into the specific syntax required by Fuzzy Description Logic reasoners.

.. ── LLM-GENERATED DESCRIPTION END ──

.. toctree::
   :titlesonly:

   /api/fuzzy_dl_owl2/index

.. [#f1] Created with `sphinx-autoapi <https://github.com/readthedocs/sphinx-autoapi>`_