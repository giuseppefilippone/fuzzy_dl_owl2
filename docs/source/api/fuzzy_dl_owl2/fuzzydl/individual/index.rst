fuzzy_dl_owl2.fuzzydl.individual
================================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_individual.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.individual
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.individual**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_individual.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.individual
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.individual**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.individual



.. ── LLM-GENERATED DESCRIPTION START ──

An entity management system for fuzzy description logic reasoning that supports hierarchical tracking, state cloning, and fuzzy constraint evaluation.


Description
-----------


The architecture centers on defining and manipulating instances within a knowledge base, ranging from core entities that manage concept assertions and role relations to dynamically generated nodes used in completion forests. To support tableau-based reasoning algorithms, the system implements deep cloning capabilities that allow the exploration of logical branches without mutating original data, while blocking mechanisms prevent infinite loops by tracking redundant expansions. Fuzzy logic constraints are handled through proxy structures that link concrete entities to abstract groups defined by triangular fuzzy numbers, enabling the quantification of partial truths and degrees of satisfaction. Together, these components enforce strict identity rules and optimize memory usage by pruning unnecessary relations, ensuring efficient inference within complex reasoning frameworks.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.individual.created_individual``] — A class representing dynamically generated nodes within a completion forest for tableau-based reasoning, incorporating hierarchical tracking, blocking mechanisms, and state cloning capabilities.
* [``fuzzy_dl_owl2.fuzzydl.individual.individual``] — Defines a core entity class representing a specific instance within a fuzzy description logic knowledge base, managing concept assertions, role relations, and restrictions during reasoning processes.
* [``fuzzy_dl_owl2.fuzzydl.individual.representative_individual``] — A concrete proxy that models a collection of individuals satisfying a specific fuzzy condition relative to a threshold by associating a feature with a triangular fuzzy number.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/individual/created_individual/index
   /api/fuzzy_dl_owl2/fuzzydl/individual/individual/index
   /api/fuzzy_dl_owl2/fuzzydl/individual/representative_individual/index

