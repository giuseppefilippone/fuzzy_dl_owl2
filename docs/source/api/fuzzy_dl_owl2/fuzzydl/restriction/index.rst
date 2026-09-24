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

A small set of value objects that model role restrictions in a fuzzy description logic, binding a role to either a target concept or a specific named individual together with a minimum degree of truth.


Description
-----------


Two restriction forms are supported: the universal construct, the fuzzy analogue of ∀R.C, which requires every individual reachable through a role to belong to a given concept with at least the stored degree, and the has-value construct, which pins a role to one concrete named individual under the same kind of degree lower bound. Both are deliberately minimal data carriers — they hold a role name, a filler, and a ``Degree`` threshold as plain attributes, expose them through trivial getters, and duplicate cheaply via a shallow-copy clone that shares its concept and degree references — so all substantive behaviour is inherited from a shared base abstraction, which the has-value case specialises by substituting the individual's name in place of a concept filler. A key architectural decision is the uniform textual encoding: restrictions render in the Lisp-like concrete syntax consumed by the fuzzydl reasoner, with universal restrictions printed as ``(all role concept)`` (optionally suffixed with ``>= degree`` to make the membership bound explicit) and has-value restrictions deliberately formatted as negated existentials, ``(not (b-some role individual))``, which allows the reasoner to normalise and reason about every restriction through the same quantified-expression machinery rather than maintaining a dedicated code path for nominal fillers. The result is a lightweight, data-oriented layer that cleanly separates the syntactic modelling of fuzzy restrictions from the reasoning engine that consumes them.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction``] — Defines a fuzzy description-logic restriction that ties a role to one specific named individual, requiring the association to hold with at least a given degree of truth.
* [``fuzzy_dl_owl2.fuzzydl.restriction.restriction``] — A lightweight value object that models a universal role restriction in a fuzzy description logic, storing a role name, a target concept, and the minimum membership degree that the restriction imposes.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/restriction/has_value_restriction/index
   /api/fuzzy_dl_owl2/fuzzydl/restriction/restriction/index