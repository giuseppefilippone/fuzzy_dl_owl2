from __future__ import annotations

import re
import typing
from xml.dom import minidom
from xml.etree.ElementTree import Element, tostring

from fuzzy_dl_owl2.fuzzyowl2.util.constants import FuzzyOWL2Keyword
from pyowl2.abstracts.class_expression import OWLClassExpression


class FuzzyXML(object):
    """This utility class acts as a builder for XML elements conforming to the FuzzyOWL2 ontology specification. It provides a suite of static methods for constructing specific XML nodes, including definitions for fuzzy logics, datatypes, modifiers, truth degrees, concepts, weights, and concept names. By abstracting the underlying tag names and attribute structures, it facilitates the programmatic generation of complex fuzzy ontology documents. The class also includes a serialization helper to convert constructed XML elements into formatted, human-readable strings for debugging or output purposes."""


    @staticmethod
    def build_main_xml(fuzzy_type: str) -> Element:
        """
        Constructs the root XML element for a FuzzyOWL2 ontology document, serving as the entry point for building the ontology structure. This static method creates an `Element` with a tag name corresponding to the FuzzyOWL2 standard and assigns the provided `fuzzy_type` string (e.g., "fuzzyDL" or "fuzzyOWL2") to a specific attribute to denote the dialect. The function acts as a pure factory method with no side effects, returning a new XML node without validating the content of the input string.

        :param fuzzy_type: The specific dialect or variant of the fuzzy ontology (e.g., "fuzzyDL", "fuzzyOWL2").
        :type fuzzy_type: str

        :return: The root XML element for the FuzzyOWL2 ontology, initialized with the specified fuzzy type attribute.

        :rtype: Element
        """

        return Element(
            FuzzyOWL2Keyword.FUZZY_OWL_2.get_str_value(),
            attrib={FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value(): fuzzy_type},
        )

    @staticmethod
    def build_logic_xml(logic: str, attrib: dict[str, str] = dict()) -> Element:
        """
        Constructs an XML element representing a specific fuzzy logic definition, typically used within Fuzzy OWL 2 ontology structures. The method assigns the provided logic type string, such as 'Lukasiewicz' or 'Zadeh', to the standard logic attribute key defined by the underlying ontology keywords. If an optional dictionary of additional attributes is supplied, its contents are merged into the element's attributes, allowing for custom metadata or potentially overriding the default logic attribute if a conflicting key is provided. The function returns the newly created `Element` object and does not perform any I/O operations or modify global state.

        :param logic: The specific fuzzy logic type to define, such as "Lukasiewicz" or "Zadeh".
        :type logic: str
        :param attrib: Optional mapping of additional XML attributes to include in the generated element.
        :type attrib: dict[str, str]

        :return: An XML element representing the fuzzy logic definition, configured with the specified logic type and any additional attributes.

        :rtype: Element
        """

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
        """
        This static method constructs an XML element representing a datatype definition, formatted according to the specific ontology keywords used by the class. It initializes the element with a tag corresponding to a datatype and sets the primary type attribute using the provided `datatype_type` string. Any additional attributes supplied in the optional dictionary are merged into the element's properties, with user-provided values taking precedence in case of key conflicts, before returning the fully configured `Element` object.

        :param datatype_type: The specific data type identifier (e.g., "integer", "float") to be assigned to the type attribute of the XML element.
        :type datatype_type: str
        :param attrib: Additional XML attributes to include in the element, merged with the standard type attribute.
        :type attrib: dict[str, str]

        :return: An XML element representing a datatype definition, configured with the provided type and optional attributes.

        :rtype: Element
        """

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
        """
        Constructs an XML element representing a modifier definition, tagged according to the FuzzyOWL2 vocabulary. The method automatically assigns the mandatory 'type' attribute using the provided `modifier_type` argument, ensuring the element identifies the specific kind of modifier. Any additional attributes supplied via the `attrib` dictionary are merged into the element's properties, potentially overwriting default values if keys conflict, to allow for extended configuration.

        :param modifier_type: The specific classification of the modifier (e.g., "linear", "triangular").
        :type modifier_type: str
        :param attrib: Optional dictionary of additional XML attributes to include in the modifier element.
        :type attrib: dict[str, str]

        :return: An XML `Element` representing the modifier definition, containing the specified type and any additional attributes.

        :rtype: Element
        """

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
        """
        Constructs an XML element representing a degree definition, typically used for defining membership degrees or truth values in Fuzzy OWL 2 ontologies. The method accepts a numeric value, which is converted to a string and assigned to a specific attribute key determined by the FuzzyOWL2Keyword standard. It also allows for an optional dictionary of additional attributes to be merged into the element; if the provided dictionary contains a key identical to the degree value attribute, the user-provided value will override the automatically generated one. The function returns a new XML Element object without modifying the input arguments.

        :param value: 
        :type value: typing.Union[int, float]
        :param attrib: Optional dictionary of additional XML attributes to merge into the degree definition element.
        :type attrib: dict[str, str]

        :return: An XML element representing a degree definition, containing the provided value as an attribute along with any additional specified attributes.

        :rtype: Element
        """

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
        """
        Creates an XML element representing a concept definition, specifically designed for use within Fuzzy OWL 2 structures. The generated element is tagged according to the concept keyword and automatically includes a 'type' attribute derived from the input string. While the method accepts an optional dictionary of additional attributes to append to the element, any keys in this dictionary that conflict with the default 'type' attribute will override the initial value, allowing for manual control over the final attribute set.

        :param concept_type: The classification of the concept (e.g., "fuzzy" or "crisp"), which is assigned to the element's type attribute.
        :type concept_type: str
        :param attrib: Optional dictionary of additional XML attributes to include in the concept element.
        :type attrib: dict[str, str]

        :return: An XML `Element` representing a concept definition, including the specified type and any additional attributes.

        :rtype: Element
        """

        full_attrib = {FuzzyOWL2Keyword.TYPE.get_str_value(): concept_type}
        if attrib:
            full_attrib.update(attrib)
        return Element(
            FuzzyOWL2Keyword.CONCEPT.get_tag_name(),
            attrib=full_attrib,
        )

    @staticmethod
    def build_weights_xml(weights: list[float]) -> Element:
        """
        Constructs an XML hierarchy representing a sequence of weights for use in fuzzy logic definitions. The method instantiates a root element to encapsulate the collection and iterates over the provided list of floating-point values, creating a distinct child element for each. Every weight is converted to a string and embedded within its corresponding tag. If the input list is empty, the method returns a root element with no children. This function does not modify the input list and relies on `FuzzyOWL2Keyword` to determine the appropriate tag names for the generated elements.

        :param weights: A sequence of numerical values to be serialized as individual weight elements within the XML structure.
        :type weights: list[float]

        :return: The root XML element representing the weights definition, containing child elements for each provided float value.

        :rtype: Element
        """

        element = Element(FuzzyOWL2Keyword.WEIGHTS.get_tag_name())
        for w in weights:
            curr = Element(FuzzyOWL2Keyword.WEIGHT.get_tag_name())
            curr.text = str(w)
            element.append(curr)
        return element

    @staticmethod
    def build_names_xml(concepts: list[OWLClassExpression]) -> Element:
        """
        Constructs an XML hierarchy representing a collection of concept names derived from a list of OWL class expressions. The method initializes a parent element corresponding to concept names and iterates over the provided list to generate individual child elements for each concept. Each child element's text content is populated by converting the corresponding class expression to its string representation. If the input list is empty, the method returns an empty parent element. This operation does not modify the input list or the class expressions themselves.

        :param concepts: The OWL class expressions to be serialized as XML name elements.
        :type concepts: list[OWLClassExpression]

        :return: An XML element representing the concept names container, with child elements corresponding to each concept in the input list.

        :rtype: Element
        """

        element = Element(FuzzyOWL2Keyword.CONCEPT_NAMES.get_tag_name())
        for c in concepts:
            curr = Element(FuzzyOWL2Keyword.NAME.get_tag_name())
            curr.text = str(c)
            element.append(curr)
        return element

    @staticmethod
    def to_str(element: Element) -> str:
        """
        Converts the provided XML element into a formatted, human-readable string representation. This static method serializes the element using standard XML methods and applies indentation via minidom to produce a clean structure. The resulting Unicode string excludes the XML declaration header and has any consecutive newline characters collapsed into a single line break to ensure compact formatting. This process does not modify the original element.

        :param element: The XML element to be converted to a string.
        :type element: Element

        :return: A pretty-printed string representation of the XML element, excluding the XML declaration header.

        :rtype: str
        """

        return re.sub(
            "\n+",
            "\n",
            "\n".join(
                minidom.parseString(tostring(element, encoding="unicode", method="xml"))
                .toprettyxml()
                .split("\n")[1:]
            ),
        )
