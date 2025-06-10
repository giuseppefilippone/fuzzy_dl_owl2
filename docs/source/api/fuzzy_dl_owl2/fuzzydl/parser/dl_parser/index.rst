fuzzy_dl_owl2.fuzzydl.parser.dl_parser
======================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.parser.dl_parser


Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.dl_parser.FILENAME
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser.LOG_DIR
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser.TODAY


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.dl_parser.DLParser


Module Contents
---------------

.. py:class:: DLParser

   Bases: :py:obj:`object`


   .. py:method:: get_grammatics() -> pyparsing.ParserElement
      :staticmethod:


      This function generate the grammatics to parse the predicate wih formula "formula".

      :param formula:
      :type formula: = The predicate formula used for the parsing.

      :rtype: The parsed result given by pyparsing.



   .. py:method:: get_kb(*args) -> tuple[fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase, list[fuzzy_dl_owl2.fuzzydl.query.query.Query]]
      :staticmethod:



   .. py:method:: load_config(*args) -> None
      :staticmethod:



   .. py:method:: main(*args) -> None
      :staticmethod:



   .. py:method:: parse_string(instring: str) -> pyparsing.ParseResults
      :staticmethod:



   .. py:method:: parse_string_opt(filename: str) -> pyparsing.ParseResults
      :staticmethod:



   .. py:attribute:: kb
      :type:  fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase
      :value: None



   .. py:attribute:: queries_list
      :type:  list[fuzzy_dl_owl2.fuzzydl.query.query.Query]
      :value: []



.. py:data:: FILENAME
   :type:  str

.. py:data:: LOG_DIR
   :type:  str

.. py:data:: TODAY
   :type:  datetime.datetime

