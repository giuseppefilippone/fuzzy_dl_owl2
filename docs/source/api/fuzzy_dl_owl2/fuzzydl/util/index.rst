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
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.util**

.. py:module:: fuzzy_dl_owl2.fuzzydl.util



.. ── LLM-GENERATED DESCRIPTION START ──

Foundational infrastructure for a fuzzy description logic reasoning engine that centralizes configuration management, logging, debugging instrumentation, and mathematical utilities.


Description
-----------


Operational parameters and type safety are established through a centralized configuration system that loads settings from external files and command-line arguments while defining enumerations for solvers, logical operators, and domain-specific vocabulary. Runtime behavior is monitored via a persistent logging framework that organizes output by date and supports dynamic verbosity, complemented by decorators that enable method tracing and automatic recursion limit adjustments to handle complex computations. To ensure numerical accuracy within the reasoning engine, static helper methods provide precise decimal-based rounding and mathematical operations, while global constants align application limits with the constraints of selected Mixed-Integer Linear Programming solvers.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.util.config_reader``] — A centralized configuration manager for a fuzzy description logic reasoning engine that loads parameters from files and command-line arguments to control precision, optimization strategies, and solver selection.
* [``fuzzy_dl_owl2.fuzzydl.util.constants``] — A central configuration module that defines enumerations, type aliases, and global constants for a fuzzy description logic reasoning system.
* [``fuzzy_dl_owl2.fuzzydl.util.util``] — A centralized utility module that configures application logging and provides static helper methods for mathematical operations, data manipulation, and error handling within the fuzzy ontology reasoner.
* [``fuzzy_dl_owl2.fuzzydl.util.utils``] — Utility decorators are provided to facilitate debugging through method tracing and to manage deep recursion by dynamically adjusting system limits.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/util/config_reader/index
   /api/fuzzy_dl_owl2/fuzzydl/util/constants/index
   /api/fuzzy_dl_owl2/fuzzydl/util/util/index
   /api/fuzzy_dl_owl2/fuzzydl/util/utils/index

