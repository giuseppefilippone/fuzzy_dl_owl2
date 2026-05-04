fuzzy_dl_owl2.fuzzydl.restriction
=================================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_restriction.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.restriction
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.restriction**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_restriction.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.restriction
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.restriction**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.restriction



.. ── LLM-GENERATED DESCRIPTION START ──

Implements fuzzy logic restrictions within a description logic framework to model constraints involving roles, concepts, and individuals.


Description
-----------


Designed to operate within fuzzy description logics, the software provides mechanisms to define and manage logical constraints that enforce specific membership degrees or certainty levels. The architecture relies on inheritance to handle different types of restrictions, including those that associate a specific role with an individual and those that enforce universal quantification across a role and concept combination. By storing core components such as role identifiers, target concepts, individuals, and fuzzy degree objects, the system ensures that logical assertions can be evaluated, copied, and represented textually according to formal syntax rules. These implementations collectively support the representation of complex logical relationships, allowing for the precise definition of conditions where entities must satisfy specific criteria with a defined degree of truth.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction``] — Defines a fuzzy logic restriction that associates a specific role with a particular individual, constrained by a lower bound degree.
* [``fuzzy_dl_owl2.fuzzydl.restriction.restriction``] — A universal restriction in a fuzzy description logic system that enforces a minimum membership degree for a specific role and concept combination.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/restriction/has_value_restriction/index
   /api/fuzzy_dl_owl2/fuzzydl/restriction/restriction/index

