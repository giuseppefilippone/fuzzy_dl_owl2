fuzzy_dl_owl2.fuzzyowl2.parser
==============================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzyowl2_parser.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzyowl2.parser
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzyowl2.parser**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzyowl2_parser.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzyowl2.parser
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzyowl2.parser**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.parser



.. ── LLM-GENERATED DESCRIPTION START ──

Specialized XML parsing logic transforms FuzzyOWL2 annotations into corresponding Python data structures for fuzzy logic concepts, datatypes, and properties.


Description
-----------


Deserialization of FuzzyOWL2 XML data occurs by interpreting specific tags and attributes to instantiate a wide range of fuzzy logic objects, including concept definitions, fuzzy datatypes, and property modifiers. The implementation utilizes ``defusedxml`` to safely parse input strings, dispatching to specific constructors based on the ``fuzzyType`` annotation found within the XML structure. Complex constructs such as weighted concepts, aggregation operators like OWA or Sugeno integrals, and various membership functions are mapped to their respective Python representations to support the underlying fuzzy description logic. Furthermore, the software integrates configuration management to load runtime parameters and provides robust error handling to ensure that parsing failures or missing configuration files do not cause unexpected termination.


Modules
-------


* [``fuzzy_dl_owl2.fuzzyowl2.parser.owl2_xml_parser``] — Specialized XML parsing logic transforms FuzzyOWL2 annotations into corresponding Python data structures for fuzzy logic concepts, datatypes, and properties.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzyowl2/parser/owl2_xml_parser/index

