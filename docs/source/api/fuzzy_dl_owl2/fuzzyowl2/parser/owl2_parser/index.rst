fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser
==========================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser.FuzzyOwl2Parser


Module Contents
---------------

.. py:class:: FuzzyOwl2Parser

   Bases: :py:obj:`object`


   .. py:method:: get_grammatics() -> pyparsing.ParserElement
      :staticmethod:


      This function generate the grammatics to parse the predicate wih formula "formula".

      :param formula:
      :type formula: = The predicate formula used for the parsing.

      :rtype: The parsed result given by pyparsing.



   .. py:method:: load_config(*args) -> None
      :staticmethod:



   .. py:method:: main(annotation: str, *args) -> tuple[fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase, list[fuzzy_dl_owl2.fuzzydl.query.query.Query]]
      :staticmethod:



   .. py:method:: parse_string(instring: str, parse_all: bool = False, *, parseAll: bool = False) -> pyparsing.ParseResults
      :staticmethod:



