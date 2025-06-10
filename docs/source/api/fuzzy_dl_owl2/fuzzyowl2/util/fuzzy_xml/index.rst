fuzzy_dl_owl2.fuzzyowl2.util.fuzzy_xml
======================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.util.fuzzy_xml


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.util.fuzzy_xml.FuzzyXML


Module Contents
---------------

.. py:class:: FuzzyXML

   Bases: :py:obj:`object`


   .. py:method:: build_concept_xml(concept_type: str, attrib: dict[str, str] = dict()) -> xml.etree.ElementTree.Element
      :staticmethod:



   .. py:method:: build_datatype_xml(datatype_type: str, attrib: dict[str, str] = dict()) -> xml.etree.ElementTree.Element
      :staticmethod:



   .. py:method:: build_degree_xml(value: Union[int, float], attrib: dict[str, str] = dict()) -> xml.etree.ElementTree.Element
      :staticmethod:



   .. py:method:: build_logic_xml(logic: str, attrib: dict[str, str] = dict()) -> xml.etree.ElementTree.Element
      :staticmethod:



   .. py:method:: build_main_xml(fuzzy_type: str) -> xml.etree.ElementTree.Element
      :staticmethod:



   .. py:method:: build_modifier_xml(modifier_type: str, attrib: dict[str, str] = dict()) -> xml.etree.ElementTree.Element
      :staticmethod:



   .. py:method:: build_names_xml(concepts: list[pyowl2.abstracts.class_expression.OWLClassExpression]) -> xml.etree.ElementTree.Element
      :staticmethod:



   .. py:method:: build_weights_xml(weights: list[float]) -> xml.etree.ElementTree.Element
      :staticmethod:



   .. py:method:: to_str(element: xml.etree.ElementTree.Element) -> str
      :staticmethod:



