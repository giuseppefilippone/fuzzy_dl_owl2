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

A foundational infrastructure for a fuzzy description logic reasoning engine that centralizes configuration management, standardizes logical constants, and provides essential utilities for logging, debugging, and high-precision arithmetic.


Description
-----------


Operational parameters are centralized through a robust configuration system that ingests settings from files and command-line arguments to control precision thresholds, optimization strategies, and solver selection, while a separate repository defines enumerations for logic operators, concept types, and parsing keywords to ensure type safety and consistency. Supporting the reasoning process, a static utility namespace establishes a timestamped logging infrastructure and wraps standard operations to raise custom exceptions, alongside mathematical helpers that utilize decimal arithmetic for precise rounding and integer detection. To facilitate development and troubleshooting, instrumentation decorators automatically trace execution flow across classes and dynamically adjust system recursion limits to handle deep algorithms without manual intervention. Together, these components abstract the complexities of environment setup and execution control, allowing the core reasoning logic to focus on inference rather than system-level concerns.


Modules
-------


* ``fuzzy_dl_owl2.fuzzydl.util.config_reader`` — Centralizes configuration management for a fuzzy description logic reasoning engine by loading parameters from files and command-line arguments to control precision, optimization strategies, and solver selection.
* ``fuzzy_dl_owl2.fuzzydl.util.constants`` — A central configuration repository for a fuzzy description logic reasoning system that defines enumerations for logic operators, concept types, solver backends, and parsing keywords.
* ``fuzzy_dl_owl2.fuzzydl.util.util`` — A centralized utility namespace and logging infrastructure for the fuzzy ontology reasoner.
* ``fuzzy_dl_owl2.fuzzydl.util.utils`` — Utility decorators provide debugging instrumentation and automatic recursion limit adjustment for Python classes and functions.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/util/config_reader/index
   /api/fuzzy_dl_owl2/fuzzydl/util/constants/index
   /api/fuzzy_dl_owl2/fuzzydl/util/util/index
   /api/fuzzy_dl_owl2/fuzzydl/util/utils/index

