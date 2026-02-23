from __future__ import annotations

import os
import traceback
import typing
from xml.etree import ElementTree

from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.util import Util
from fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept import ChoquetConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.owl_types.crisp_function import CrispFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype import FuzzyDatatype
from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier import FuzzyModifier
from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_nominal_concept import FuzzyNominalConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.left_shoulder_function import (
    LeftShoulderFunction,
)
from fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function import LinearFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier import LinearModifier
from fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_concept import ModifiedConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property import ModifiedProperty
from fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept import OwaConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.property_definition import PropertyDefinition
from fuzzy_dl_owl2.fuzzyowl2.owl_types.qowa_concept import QowaConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept import QsugenoConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.right_shoulder_function import (
    RightShoulderFunction,
)
from fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept import SugenoConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.trapezoidal_function import TrapezoidalFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_function import TriangularFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_modifer import TriangularModifier
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_concept import WeightedConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_max_concept import WeightedMaxConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_min_concept import WeightedMinConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_concept import WeightedSumConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_zero_concept import (
    WeightedSumZeroConcept,
)
from fuzzy_dl_owl2.fuzzyowl2.util.constants import FuzzyOWL2Keyword
from fuzzy_dl_owl2.fuzzyowl2.util.fuzzy_xml import FuzzyXML


class FuzzyOwl2XMLParser(object):
    """
    This class serves as a specialized parser for converting FuzzyOWL2 XML annotations into corresponding Python data structures. It interprets XML strings to instantiate a variety of objects representing fuzzy logic elements, including concept definitions (such as weighted or modified concepts), fuzzy datatypes (like triangular or trapezoidal functions), and property definitions. The parsing logic relies on inspecting specific XML attributes to determine the correct object type to construct. Additionally, the class provides functionality to load configuration parameters from an external file and includes error handling mechanisms to manage parsing or file access issues gracefully.

    :raises ValueError: Raised when the parsed XML string contains an unsupported, unrecognized, or missing annotation type that does not correspond to any of the defined FuzzyOWL2 elements (Concept, Datatype, Modifier, Axiom, Ontology, or Role).
    """


    @staticmethod
    def get_caseless_attrib(attrib: dict[str, str], key: str) -> typing.Optional[str]:
        """
        This static method retrieves a value from a dictionary of attributes by performing a case-insensitive lookup on the provided key. It scans the dictionary for keys that match the target key when both are converted to lowercase, returning the value associated with the first such match found. If no matching key exists, the method returns None. Note that if the input dictionary contains multiple keys that differ only by case, the value returned corresponds to the first match encountered during iteration, which depends on the dictionary's insertion order.

        :param attrib: A dictionary containing the attributes to search.
        :type attrib: dict[str, str]
        :param key: The name of the attribute to retrieve, matched case-insensitively.
        :type key: str

        :return: The value of the attribute if a case-insensitive match is found, otherwise None.

        :rtype: typing.Optional[str]
        """

        keys = [k for k in attrib if k.lower() == key.lower()]
        return attrib.get(keys[0]) if len(keys) > 0 else None

    @staticmethod
    def parse_string(
        instring: str,
    ) -> typing.Union[
        ConceptDefinition, FuzzyDatatype, PropertyDefinition, FuzzyModifier, float, str
    ]:
        """
        Parses a string containing FuzzyOWL2 XML and constructs the corresponding Python representation based on the structure and attributes of the XML. The method inspects the root element's type annotation to dispatch the parsing logic to specific handlers for concepts, datatypes, modifiers, axioms, ontology settings, or roles. Depending on the content, it returns specialized objects such as `ModifiedConcept`, `TriangularFunction`, or `LinearModifier`, or primitive values like floats for axiom degrees and strings for logic types. During execution, the method logs the XML structure for debugging purposes. It raises an `AssertionError` if the root element does not match the expected FuzzyOWL2 tag and a `ValueError` if the fuzzy type is unsupported.

        :param instring: A string containing the FuzzyOWL2 XML data to be parsed.
        :type instring: str

        :raises ValueError: Raised if the input XML string does not specify a valid or supported FuzzyOWL2 annotation type.

        :return: Returns a Python object representing the parsed FuzzyOWL2 element. The specific type is determined by the XML's `fuzzyType` attribute and may be a `ConceptDefinition`, `FuzzyDatatype`, `PropertyDefinition`, `FuzzyModifier`, a `float` (for axiom degrees), or a `str` (for ontology logic).

        :rtype: typing.Union[ConceptDefinition, FuzzyDatatype, PropertyDefinition, FuzzyModifier, float, str]
        """

        root: ElementTree.Element = ElementTree.fromstring(instring)
        Util.debug(f"XML PARSER -> {FuzzyXML.to_str(root)}")
        assert root.tag == FuzzyOWL2Keyword.FUZZY_OWL_2

        annotation_type: str = root.attrib.get(
            FuzzyOWL2Keyword.FUZZY_TYPE.get_str_value()
        )
        if annotation_type == FuzzyOWL2Keyword.CONCEPT:
            child = root.find(FuzzyOWL2Keyword.CONCEPT.get_tag_name())
            concept_type = child.attrib.get(FuzzyOWL2Keyword.TYPE.get_str_value())
            if concept_type == FuzzyOWL2Keyword.MODIFIED:
                return ModifiedConcept(
                    child.attrib.get(FuzzyOWL2Keyword.MODIFIER.get_str_value()),
                    child.attrib.get(FuzzyOWL2Keyword.BASE.get_str_value()),
                )
            elif concept_type == FuzzyOWL2Keyword.WEIGHTED:
                return WeightedConcept(
                    float(
                        child.attrib.get(FuzzyOWL2Keyword.DEGREE_VALUE.get_str_value())
                    ),
                    child.attrib.get(FuzzyOWL2Keyword.BASE.get_str_value()),
                )
            elif concept_type in (
                FuzzyOWL2Keyword.WEIGHTED_MINIMUM,
                FuzzyOWL2Keyword.WEIGHTED_MAXIMUM,
                FuzzyOWL2Keyword.WEIGHTED_SUM,
                FuzzyOWL2Keyword.WEIGHTED_SUMZERO,
            ):
                wc: list[WeightedConcept] = [
                    WeightedConcept(
                        float(
                            inner_child.attrib.get(
                                FuzzyOWL2Keyword.DEGREE_VALUE.get_str_value()
                            )
                        ),
                        inner_child.attrib.get(FuzzyOWL2Keyword.BASE.get_str_value()),
                    )
                    for inner_child in child
                    if inner_child.tag == FuzzyOWL2Keyword.CONCEPT.get_tag_name()
                    and inner_child.attrib.get(FuzzyOWL2Keyword.TYPE.get_str_value())
                    == FuzzyOWL2Keyword.WEIGHTED
                ]
                if concept_type == FuzzyOWL2Keyword.WEIGHTED_MAXIMUM:
                    return WeightedMaxConcept(wc)
                elif concept_type == FuzzyOWL2Keyword.WEIGHTED_MINIMUM:
                    return WeightedMinConcept(wc)
                elif concept_type == FuzzyOWL2Keyword.WEIGHTED_SUM:
                    return WeightedSumConcept(wc)
                elif concept_type == FuzzyOWL2Keyword.WEIGHTED_SUMZERO:
                    return WeightedSumZeroConcept(wc)
            elif concept_type in (
                FuzzyOWL2Keyword.OWA,
                FuzzyOWL2Keyword.CHOQUET,
                FuzzyOWL2Keyword.SUGENO,
                FuzzyOWL2Keyword.QUASI_SUGENO,
            ):
                weights: list[float] = [
                    float(weight.text)
                    for weight in child.find(
                        FuzzyOWL2Keyword.WEIGHTS.get_tag_name()
                    ).findall(FuzzyOWL2Keyword.WEIGHT.get_tag_name())
                ]
                concepts: list[str] = [
                    name.text
                    for name in child.find(
                        FuzzyOWL2Keyword.CONCEPT_NAMES.get_tag_name()
                    ).findall(FuzzyOWL2Keyword.NAME.get_tag_name())
                ]
                if concept_type == FuzzyOWL2Keyword.OWA:
                    return OwaConcept(weights, concepts)
                elif concept_type == FuzzyOWL2Keyword.CHOQUET:
                    return ChoquetConcept(weights, concepts)
                elif concept_type == FuzzyOWL2Keyword.SUGENO:
                    return SugenoConcept(weights, concepts)
                elif concept_type == FuzzyOWL2Keyword.QUASI_SUGENO:
                    return QsugenoConcept(weights, concepts)
            elif concept_type == FuzzyOWL2Keyword.Q_OWA:
                quantifier = child.attrib.get(
                    FuzzyOWL2Keyword.QUANTIFIER.get_str_value()
                )
                concepts: list[str] = [
                    name.text
                    for name in child.find(
                        FuzzyOWL2Keyword.CONCEPT_NAMES.get_tag_name()
                    ).findall(FuzzyOWL2Keyword.NAME.get_tag_name())
                ]
                return QowaConcept(quantifier, concepts)
            elif concept_type == FuzzyOWL2Keyword.NOMINAL:
                return FuzzyNominalConcept(
                    float(
                        child.attrib.get(FuzzyOWL2Keyword.DEGREE_VALUE.get_str_value())
                    ),
                    child.attrib.get(FuzzyOWL2Keyword.INDIVIDUAL.get_str_value()),
                )
        elif annotation_type == FuzzyOWL2Keyword.DATATYPE:
            child = root.find(FuzzyOWL2Keyword.DATATYPE.get_tag_name())
            datatype_type = child.attrib.get(FuzzyOWL2Keyword.TYPE.get_str_value())

            if datatype_type == FuzzyOWL2Keyword.CRISP:
                return CrispFunction(
                    float(child.attrib.get(FuzzyOWL2Keyword.A.get_str_value())),
                    float(child.attrib.get(FuzzyOWL2Keyword.B.get_str_value())),
                )
            elif datatype_type == FuzzyOWL2Keyword.LEFT_SHOULDER:
                return LeftShoulderFunction(
                    float(child.attrib.get(FuzzyOWL2Keyword.A.get_str_value())),
                    float(child.attrib.get(FuzzyOWL2Keyword.B.get_str_value())),
                )
            elif datatype_type == FuzzyOWL2Keyword.RIGHT_SHOULDER:
                return RightShoulderFunction(
                    float(child.attrib.get(FuzzyOWL2Keyword.A.get_str_value())),
                    float(child.attrib.get(FuzzyOWL2Keyword.B.get_str_value())),
                )
            elif datatype_type == FuzzyOWL2Keyword.LINEAR:
                return LinearFunction(
                    float(child.attrib.get(FuzzyOWL2Keyword.A.get_str_value())),
                    float(child.attrib.get(FuzzyOWL2Keyword.B.get_str_value())),
                )
            elif datatype_type == FuzzyOWL2Keyword.TRIANGULAR:
                return TriangularFunction(
                    float(child.attrib.get(FuzzyOWL2Keyword.A.get_str_value())),
                    float(child.attrib.get(FuzzyOWL2Keyword.B.get_str_value())),
                    float(child.attrib.get(FuzzyOWL2Keyword.C.get_str_value())),
                )
            elif datatype_type == FuzzyOWL2Keyword.TRAPEZOIDAL:
                return TrapezoidalFunction(
                    float(child.attrib.get(FuzzyOWL2Keyword.A.get_str_value())),
                    float(child.attrib.get(FuzzyOWL2Keyword.B.get_str_value())),
                    float(child.attrib.get(FuzzyOWL2Keyword.C.get_str_value())),
                    float(child.attrib.get(FuzzyOWL2Keyword.D.get_str_value())),
                )
        elif annotation_type == FuzzyOWL2Keyword.MODIFIER:
            child = root.find(FuzzyOWL2Keyword.MODIFIER.get_tag_name())
            mod_type = child.attrib.get(FuzzyOWL2Keyword.TYPE.get_str_value())
            if mod_type == FuzzyOWL2Keyword.LINEAR:
                return LinearModifier(
                    float(child.attrib.get(FuzzyOWL2Keyword.C.get_str_value())),
                )
            elif mod_type == FuzzyOWL2Keyword.TRIANGULAR:
                return TriangularModifier(
                    float(child.attrib.get(FuzzyOWL2Keyword.A.get_str_value())),
                    float(child.attrib.get(FuzzyOWL2Keyword.B.get_str_value())),
                    float(child.attrib.get(FuzzyOWL2Keyword.C.get_str_value())),
                )
        elif annotation_type == FuzzyOWL2Keyword.AXIOM:
            child = root.find(FuzzyOWL2Keyword.DEGREE_DEF.get_tag_name())
            return float(
                child.attrib.get(FuzzyOWL2Keyword.DEGREE_VALUE.get_str_value())
            )
        elif annotation_type == FuzzyOWL2Keyword.ONTOLOGY:
            child = root.find(FuzzyOWL2Keyword.FUZZY_LOGIC.get_tag_name())
            return child.attrib.get(FuzzyOWL2Keyword.LOGIC.get_str_value())
        elif annotation_type == FuzzyOWL2Keyword.ROLE:
            child = root.find(FuzzyOWL2Keyword.ROLE.get_tag_name())
            assert (
                child.attrib.get(FuzzyOWL2Keyword.TYPE.get_str_value())
                == FuzzyOWL2Keyword.MODIFIED
            )
            return ModifiedProperty(
                child.attrib.get(FuzzyOWL2Keyword.MODIFIER.get_str_value()),
                child.attrib.get(FuzzyOWL2Keyword.BASE.get_str_value()),
            )
        else:
            raise ValueError

    @staticmethod
    def load_config(*args) -> None:
        """
        This static method loads configuration parameters by reading a "CONFIG.ini" file located in the current working directory. It acts as a wrapper that forwards any provided arguments to the underlying `ConfigReader.load_parameters` method to facilitate the parsing and application of settings. The operation modifies the global or class-level configuration state but does not return a value. Note that this method relies on the specific execution context, as it will fail to locate the configuration file if the current working directory does not contain "CONFIG.ini".

        :param args: Additional arguments passed directly to the underlying configuration loader.
        :type args: typing.Any
        """

        ConfigReader.load_parameters(os.path.join(os.getcwd(), "CONFIG.ini"), args)

    @staticmethod
    def main(
        annotation: str, *args
    ) -> typing.Union[
        ConceptDefinition, FuzzyDatatype, PropertyDefinition, FuzzyModifier, float, str
    ]:
        """
        This static method serves as the primary entry point for parsing FuzzyOWL2 XML strings into structured Python objects. It initializes the parser's configuration using the provided arguments before processing the input annotation, ensuring that necessary settings are loaded prior to parsing. The method returns a parsed entity, which may be a ConceptDefinition, FuzzyDatatype, PropertyDefinition, FuzzyModifier, or a primitive value, depending on the content of the XML. In the event of a missing configuration file or a general parsing exception, the method logs the error and traceback details to the standard error output and returns None implicitly, allowing the program to handle failures gracefully without crashing.

        :param annotation: The FuzzyOWL2 XML string to be parsed.
        :type annotation: str
        :param args: Variable length argument list passed to the configuration loader, typically starting with the path to the configuration file.
        :type args: typing.Any

        :return: The parsed representation of the FuzzyOWL2 XML annotation, which may be a ConceptDefinition, FuzzyDatatype, PropertyDefinition, FuzzyModifier, float, or str depending on the input content. Returns None if parsing or configuration fails.

        :rtype: typing.Union[ConceptDefinition, FuzzyDatatype, PropertyDefinition, FuzzyModifier, float, str]
        """

        try:
            FuzzyOwl2XMLParser.load_config(*args)
            return FuzzyOwl2XMLParser.parse_string(annotation)
        except FileNotFoundError as e:
            Util.error(f"Error: File {args[0]} not found.")
        except Exception as e:
            Util.error(e)
            Util.error(traceback.format_exc())
