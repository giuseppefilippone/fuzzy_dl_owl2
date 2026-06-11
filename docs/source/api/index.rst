API Reference
=============

This page contains auto-generated API reference documentation [#f1]_.


.. ── LLM-GENERATED DESCRIPTION START ──

A comprehensive framework for fuzzy description logic reasoning and interoperability that bridges abstract fuzzy logic with concrete optimization models and semantic web standards.


Description
-----------


The core reasoning engine employs tableau-based algorithms to normalize terminologies and manage assertional data, translating complex logical axioms into Mixed-Integer Linear Programming constraints to determine truth degrees. Logical expressions are constructed through a composite object model that supports operator overloading and advanced aggregations like Choquet integrals and Ordered Weighted Averaging, enabling the representation of sophisticated uncertainty. To ensure seamless integration with semantic web technologies, a translation layer converts OWL2 ontologies annotated with fuzzy semantics into internal representations using an inheritance-based type system and specialized XML parsing logic. This architecture facilitates bidirectional data exchange, allowing the serialization of fuzzy knowledge bases into standard OWL2 structures via XML annotations while enforcing canonical hierarchies required by the target reasoning engine.


Sub-packages
------------


* [``fuzzy_dl_owl2.fuzzydl``] — A comprehensive fuzzy description logic reasoner that manages knowledge bases and performs automated reasoning by translating fuzzy axioms into Mixed-Integer Linear Programming constraints.
* [``fuzzy_dl_owl2.fuzzyowl2``] — A translation framework converts OWL2 ontologies annotated with fuzzy logic semantics into a Fuzzy Description Logic representation suitable for reasoning engines.

.. ── LLM-GENERATED DESCRIPTION END ──

.. toctree::
   :titlesonly:

   /api/fuzzy_dl_owl2/index

.. [#f1] Created with `sphinx-autoapi <https://github.com/readthedocs/sphinx-autoapi>`_