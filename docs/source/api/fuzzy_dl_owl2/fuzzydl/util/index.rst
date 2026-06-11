fuzzy_dl_owl2.fuzzydl.util
==========================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_util.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.util
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.util**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_util.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.util
       :align: center
       :width: 11.6cm
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.util**

.. py:module:: fuzzy_dl_owl2.fuzzydl.util



.. ── LLM-GENERATED DESCRIPTION START ──

Foundational infrastructure supporting a fuzzy description logic reasoning engine by centralizing configuration management, defining core operational constants, and providing cross-cutting utilities for logging, mathematics, and runtime instrumentation.


Description
-----------


The software establishes a robust environment for fuzzy logic processing by first loading and normalizing system parameters from external files or environment variables, which subsequently drives global numerical limits and solver capabilities. A comprehensive taxonomy of enumerations and type aliases defines the logical vocabulary, including specific t-norms, aggregation methods, and Mixed-Integer Linear Programming solver backends, ensuring that parsing and execution strategies remain consistent across the application. Cross-cutting concerns are managed through a static utility class that handles precise mathematical operations and timestamped logging, while high-level decorators facilitate deep recursion and method tracing for debugging purposes. By integrating these components, the system ensures that numerical precision, optimization levels, and diagnostic visibility are uniformly applied throughout the reasoning process.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.util.config_reader``] — A centralized configuration manager that loads and applies settings for a fuzzy reasoning engine from INI or environment files.
* [``fuzzy_dl_owl2.fuzzydl.util.constants``] — A collection of enumerations, type aliases, and utility functions that define the core vocabulary, operational strategies, and configuration parameters for a fuzzy description logic reasoning engine.
* [``fuzzy_dl_owl2.fuzzydl.util.util``] — Centralizes logging infrastructure and provides static helper methods for mathematical operations and data manipulation within the fuzzy description logic reasoner.
* [``fuzzy_dl_owl2.fuzzydl.util.utils``] — A collection of utility decorators designed to facilitate debugging through method tracing and to handle deep recursion by dynamically adjusting system limits.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/util/config_reader/index
   /api/fuzzy_dl_owl2/fuzzydl/util/constants/index
   /api/fuzzy_dl_owl2/fuzzydl/util/util/index
   /api/fuzzy_dl_owl2/fuzzydl/util/utils/index

