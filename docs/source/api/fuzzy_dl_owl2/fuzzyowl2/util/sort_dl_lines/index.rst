fuzzy_dl_owl2.fuzzyowl2.util.sort_dl_lines
==========================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.util.sort_dl_lines



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a sorting mechanism for fuzzyDL statements that arranges them according to the specific syntax order presented in the official PDF documentation.


Description
-----------


The software relies on a comprehensive list of regular expressions that mirror the sequential appearance of commands in the fuzzyDL reference manual, ensuring that generated or processed code adheres to a standardized visual structure. By matching input strings against these compiled patterns, the logic assigns a specific rank to each statement, allowing for a primary sort based on documentation order and a secondary sort based on the string content itself. Once sorted, the results are grouped by their assigned rank, and a customizable separator is inserted between distinct groups to visually distinguish different categories of fuzzyDL commands. Statements that do not match any known pattern are assigned a high priority value, effectively pushing them to the end of the output while maintaining the overall organization of recognized elements.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.util.sort_dl_lines.FUZZYDL_PDF_ORDER
   fuzzy_dl_owl2.fuzzyowl2.util.sort_dl_lines.FUZZYDL_PDF_ORDER_RE


Functions
---------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.util.sort_dl_lines.find_fuzzydl_pdf_order_index
   fuzzy_dl_owl2.fuzzyowl2.util.sort_dl_lines.sort_by_fuzzydl_pdf_order


Module Contents
---------------

.. py:function:: find_fuzzydl_pdf_order_index(text: str) -> int

   Find the index of the first regex in FUZZYDL_PDF_ORDER that matches s.
   If no entry matches, return a large number so the item sorts at the end.


.. py:function:: sort_by_fuzzydl_pdf_order(values: collections.abc.Iterable[str], *, group_separator: str = '') -> list[str]

   Sort fuzzyDL statements by PDF order index, group equal-index items,
   and insert `group_separator` after each group.

   Unknown statements are placed at the end.


.. py:data:: FUZZYDL_PDF_ORDER
   :type:  list[str]
   :value: ['^\\s*\\(\\s*define-fuzzy-logic\\b', '^\\s*\\(\\s*define-truth-constant\\b',...


.. py:data:: FUZZYDL_PDF_ORDER_RE
   :type:  list[re.Pattern[str]]
