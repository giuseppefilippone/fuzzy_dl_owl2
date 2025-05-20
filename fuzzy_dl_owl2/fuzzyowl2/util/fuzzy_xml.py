from __future__ import annotations

import re
import typing
from xml.dom import minidom
from xml.etree.ElementTree import Element, tostring

from fuzzy_dl_owl2.fuzzyowl2.util.constants import FuzzyOWL2Keyword
from pyowl2.abstracts.class_expression import OWLClassExpression


class FuzzyXML(object):

    @staticmethod
    def build_main_xml(fuzzy_type: str) -> Element:
        return Element(
            FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value(),
            attrib={FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value(): fuzzy_type},
        )

    @staticmethod
    def build_logic_xml(logic: str, attrib: dict[str, str] = dict()) -> Element:
        full_attrib = {FuzzyOWL2Keyword.LOGIC.get_str_value(): logic}
        if attrib:
            full_attrib.update(attrib)
        return Element(
            FuzzyOWL2Keyword.FUZZY_LOGIC.get_tag_name(),
            attrib=full_attrib,
        )

    @staticmethod
    def build_datatype_xml(
        datatype_type: str, attrib: dict[str, str] = dict()
    ) -> Element:
        full_attrib = {FuzzyOWL2Keyword.TYPE.get_str_value(): datatype_type}
        if attrib:
            full_attrib.update(attrib)
        return Element(
            FuzzyOWL2Keyword.DATATYPE.get_tag_name(),
            attrib=full_attrib,
        )

    @staticmethod
    def build_modifier_xml(
        modifier_type: str, attrib: dict[str, str] = dict()
    ) -> Element:
        full_attrib = {FuzzyOWL2Keyword.TYPE.get_str_value(): modifier_type}
        if attrib:
            full_attrib.update(attrib)
        return Element(
            FuzzyOWL2Keyword.MODIFIER.get_tag_name(),
            attrib=full_attrib,
        )

    @staticmethod
    def build_degree_xml(
        value: typing.Union[int, float], attrib: dict[str, str] = dict()
    ) -> Element:
        full_attrib = {FuzzyOWL2Keyword.DEGREE_VALUE.get_str_value(): str(value)}
        if attrib:
            full_attrib.update(attrib)
        return Element(
            FuzzyOWL2Keyword.DEGREE_DEF.get_tag_name(),
            attrib=full_attrib,
        )

    @staticmethod
    def build_concept_xml(
        concept_type: str, attrib: dict[str, str] = dict()
    ) -> Element:
        full_attrib = {FuzzyOWL2Keyword.TYPE.get_str_value(): concept_type}
        if attrib:
            full_attrib.update(attrib)
        return Element(
            FuzzyOWL2Keyword.CONCEPT.get_tag_name(),
            attrib=full_attrib,
        )

    @staticmethod
    def build_weights_xml(weights: list[float]) -> Element:
        element = Element(FuzzyOWL2Keyword.WEIGHTS.get_tag_name())
        for w in weights:
            curr = Element(FuzzyOWL2Keyword.WEIGHT.get_tag_name())
            curr.text = str(w)
            element.append(curr)
        return element

    @staticmethod
    def build_names_xml(concepts: list[OWLClassExpression]) -> Element:
        element = Element(FuzzyOWL2Keyword.CONCEPT_NAMES.get_tag_name())
        for c in concepts:
            curr = Element(FuzzyOWL2Keyword.NAME.get_tag_name())
            curr.text = str(c)
            element.append(curr)
        return element

    @staticmethod
    def to_str(element: Element) -> str:
        return re.sub(
            "\n+",
            "\n",
            "\n".join(
                minidom.parseString(tostring(element, encoding="unicode", method="xml"))
                .toprettyxml()
                .split("\n")[1:]
            ),
        )
