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

Implements fuzzy description logic restrictions that enforce constraints on roles and concepts using specific membership degrees.


Description
-----------


Logic constraints within a fuzzy framework are modeled by combining roles, concepts, and degree thresholds to define specific relationships. A universal restriction ensures that for all entities connected via a given role, they belong to a specified concept with a certainty meeting a lower bound degree. Another type of constraint enforces that a specific role must be associated with a particular individual, using a fuzzy degree to represent the strength of this association. These components utilize a common base structure to manage attributes like role names and degrees while translating logical assertions into formatted string expressions suitable for integration into broader reasoning tasks.


Modules
-------


* ``fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction`` — A fuzzy description logic restriction that enforces a specific value for a given role, constrained by a degree of membership.
* ``fuzzy_dl_owl2.fuzzydl.restriction.restriction`` — A class representing a universal restriction that combines a role, a concept, and a degree threshold within a fuzzy logic framework.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/restriction/has_value_restriction/index
   /api/fuzzy_dl_owl2/fuzzydl/restriction/restriction/index

