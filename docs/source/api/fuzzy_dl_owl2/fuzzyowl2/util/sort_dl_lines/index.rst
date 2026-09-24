fuzzy_dl_owl2.fuzzyowl2.util.sort_dl_lines
==========================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.util.sort_dl_lines





.. ── LLM-GENERATED DESCRIPTION START ──

A utility for reordering fuzzyDL knowledge-base statements so that they follow the page-by-page order in which the commands are documented in the fuzzyDL PDF manual.


Description
-----------


A canonical ordering table, **FUZZYDL_PDF_ORDER**, drives the whole process: it holds regular expressions that mirror the sequence of fuzzyDL commands as they appear in the manual's PDF, ordered first by page number and then top-to-bottom within each page. The patterns are deliberately anchored to parenthesized command keywords and compiled case-insensitively, with multiline and dot-all flags so that shape keywords such as *triangular* or *modified* can still be matched when they appear later in a multi-line statement. Anchoring is what keeps superficially similar commands from colliding — feature-level and role-level uses of *functional* occupy different positions in the table, and feature ranges are told apart from role ranges by looking for datatype markers like *integer* or *real*. One ambiguity is knowingly left unresolved: a bare ``(functional F)`` is syntactically indistinguishable from a role-level declaration unless the caller already knows whether the identifier names a feature or a role, so inputs mixing both require external preclassification.

Classification works by scanning the compiled patterns in order and returning the index of the first one that matches a given statement, with a large sentinel value (10**9) serving as the fallback so that anything unrecognised sorts at the very end. The sorting routine pairs every input line with its classification index, orders the pairs by index and then by the statement text itself — which keeps lines sharing a command type in a deterministic lexicographic order — and groups runs of equal-index statements, emitting each cluster followed by a configurable separator string (empty by default, typically a blank line). The resulting output reads like the manual's running example, with logically related commands clustered together and visually separated. Optional debug tracing, gated behind a global configuration flag, logs every regex match attempt along with the final index assigned to each line, which makes it much easier to diagnose why a particular statement landed in an unexpected position.

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