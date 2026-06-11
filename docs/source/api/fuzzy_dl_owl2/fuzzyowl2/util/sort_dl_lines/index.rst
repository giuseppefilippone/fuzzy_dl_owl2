fuzzy_dl_owl2.fuzzyowl2.util.sort_dl_lines
==========================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.util.sort_dl_lines



.. ── LLM-GENERATED DESCRIPTION START ──

Sorts fuzzy-DL statements according to a specific syntax hierarchy derived from the official language documentation.


Description
-----------


The software defines a comprehensive list of regular expressions that correspond to the specific sequence of commands presented in the fuzzy-DL reference manual, ensuring that generated or processed code adheres to this canonical structure. By matching input statements against these compiled patterns, the logic assigns a numerical rank to each line, effectively classifying commands like concept definitions, role properties, and queries into their correct positions. Once ranked, the statements are sorted primarily by this rank and secondarily by their content, with the added capability to insert a separator string between distinct groups of command types. Unrecognized statements that do not match any defined pattern are automatically relegated to the end of the output to maintain stability without disrupting the known order.

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

   Finds the index of the first regex in :data:`FUZZYDL_PDF_ORDER_RE` that
   matches *text*. If no entry matches, returns a large number (``10**9``)
   so the item sorts at the end.

   :param text: The fuzzy-DL statement to classify.
   :type text: str

   :return: The PDF-order index, or ``10**9`` if unrecognised.

   :rtype: int


.. py:function:: sort_by_fuzzydl_pdf_order(values: collections.abc.Iterable[str], *, group_separator: str = '') -> list[str]

   Sorts fuzzy-DL statements by PDF order index, groups equal-index items,
   and inserts *group_separator* after each group. Unknown statements are
   placed at the end.

   :param values: The fuzzy-DL statements to sort.
   :type values: Iterable[str]
   :param group_separator: String inserted after each group of equal-index items.
   :type group_separator: str

   :return: The sorted statements with group separators inserted.

   :rtype: list[str]


.. py:data:: FUZZYDL_PDF_ORDER
   :type:  list[str]
   :value: ['^\\s*\\(\\s*define-fuzzy-logic\\b', '^\\s*\\(\\s*define-truth-constant\\b',...


.. py:data:: FUZZYDL_PDF_ORDER_RE
   :type:  list[re.Pattern[str]]
