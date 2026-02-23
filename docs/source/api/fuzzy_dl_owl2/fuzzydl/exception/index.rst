fuzzy_dl_owl2.fuzzydl.exception
===============================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_exception.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.exception
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.exception**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_exception.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.exception
       :align: center
       :width: 7.6cm
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.exception**

.. py:module:: fuzzy_dl_owl2.fuzzydl.exception



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized exception hierarchy for handling errors and logical inconsistencies within fuzzy description logic frameworks.


Description
-----------


Custom error types are defined to distinguish between general framework issues, such as invalid concept definitions, and specific logical conflicts like contradictory or unsatisfiable concepts. By extending the standard Python ``Exception`` class, these classes integrate seamlessly with native error handling workflows while enabling developers to implement granular control flow and debugging strategies. The architecture focuses on providing context-specific error messages that help identify the root cause of failures during ontology manipulation. This separation of concerns ensures that applications can manage domain-specific failures distinctly from generic runtime errors, leading to more robust and maintainable code.


Modules
-------


* ``fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception`` — A custom exception class designed to handle errors specific to the fuzzy description logic framework.
* ``fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception`` — A custom exception class designed to signal logical inconsistencies within fuzzy ontologies.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/exception/fuzzy_ontology_exception/index
   /api/fuzzy_dl_owl2/fuzzydl/exception/inconsistent_ontology_exception/index

