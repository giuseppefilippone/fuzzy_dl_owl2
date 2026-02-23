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

A subsystem for managing individual entities within a fuzzy description logic ontology that supports tableau-based reasoning, hierarchical tracking, and fuzzy constraint evaluation.


Description
-----------


At the core, a foundational class encapsulates the state of specific instances by managing concept assertions, role relations, and constraints to serve as nodes within a knowledge graph. Extending this base structure, a specialized implementation handles dynamically generated nodes for tableau algorithms, incorporating mechanisms for lineage tracking, depth calculation, and blocking optimizations to prevent infinite expansion during inference. To support the non-deterministic nature of reasoning, the architecture employs deep cloning of internal states, enabling the preservation of snapshots for backtracking and branching scenarios while distinguishing between abstract nodes and concrete instances. Additionally, a proxy component models collections of entities satisfying fuzzy conditions by encapsulating triangular fuzzy numbers and thresholds, thereby integrating uncertainty and partial truth evaluation into the reasoning framework.


Modules
-------


* ``fuzzy_dl_owl2.fuzzydl.individual.created_individual`` — A class representing dynamically generated nodes within a completion forest for tableau-based reasoning, supporting hierarchical tracking, blocking mechanisms, and state cloning.
* ``fuzzy_dl_owl2.fuzzydl.individual.individual`` — Defines a base class representing an individual entity within a fuzzy description logic ontology, managing concept assertions, role relations, and restrictions during reasoning processes.
* ``fuzzy_dl_owl2.fuzzydl.individual.representative_individual`` — A proxy class representing a collection of individuals satisfying a fuzzy condition based on a specific feature and threshold.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/individual/created_individual/index
   /api/fuzzy_dl_owl2/fuzzydl/individual/individual/index
   /api/fuzzy_dl_owl2/fuzzydl/individual/representative_individual/index

