fuzzy_dl_owl2.fuzzydl.assertion
===============================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_assertion.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.assertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.assertion**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_assertion.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.assertion
       :align: center
       :width: 14.7cm
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.assertion**

.. py:module:: fuzzy_dl_owl2.fuzzydl.assertion



.. ── LLM-GENERATED DESCRIPTION START ──

A collection of data structures for modeling fuzzy logic constraints that associate individuals with concepts based on minimum membership degrees.


Description
-----------


These components facilitate the representation of fuzzy description logic constraints by defining relationships between entities, concepts, and specific truth values. The architecture encapsulates the expression :math:`a:C \ge d`, where a degree acts as a threshold that an individual's membership in a concept must meet or exceed. Functionality includes retrieving or modifying internal components, generating human-readable string representations, and cloning instances to create independent copies. A distinctive design feature involves custom equality logic that supports comparisons based on threshold dominance, allowing instances to be considered equal if they represent the same entity and concept but hold a numerically lower degree. By providing accessors for concept identifiers and degree values, the software enables the evaluation of logical rules within a broader system.


Modules
-------


* ``fuzzy_dl_owl2.fuzzydl.assertion.assertion`` — Models a fuzzy logic constraint stating that an individual belongs to a concept with a specific minimum degree of membership.
* ``fuzzy_dl_owl2.fuzzydl.assertion.atomic_assertion`` — Implements a data structure for representing atomic assertions within a fuzzy description logic system by associating a concept with a minimum membership degree.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/assertion/assertion/index
   /api/fuzzy_dl_owl2/fuzzydl/assertion/atomic_assertion/index

