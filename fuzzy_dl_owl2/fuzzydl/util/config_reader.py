from __future__ import annotations

import configparser
import enum
import math

from fuzzy_dl_owl2.fuzzydl.util import constants


class MILPProvider(enum.StrEnum):
    GUROBI = enum.auto()
    MIP = enum.auto()
    # SCIPY = enum.auto()
    PULP = enum.auto()
    PULP_GLPK = enum.auto()
    PULP_HIGHS = enum.auto()
    PULP_CPLEX = enum.auto()

    @staticmethod
    def from_str(value: str) -> MILPProvider:
        try:
            return MILPProvider(value.lower())
        except ValueError:
            raise ValueError(
                f"Invalid MILP provider: {value}. Valid options are: {list(MILPProvider)}"
            )


class ConfigReader:
    ANYWHERE_DOUBLE_BLOCKING: bool = True
    ANYWHERE_SIMPLE_BLOCKING: bool = True
    DEBUG_PRINT: bool = True
    EPSILON: float = 0.001
    MAX_INDIVIDUALS: int = -1
    NUMBER_DIGITS: int = 2
    OPTIMIZATIONS: int = 1
    RULE_ACYCLIC_TBOXES: bool = True
    OWL_ANNOTATION_LABEL: str = "fuzzyLabel"
    MILP_PROVIDER: MILPProvider = MILPProvider.GUROBI

    @staticmethod
    def load_parameters(config_file: str, args: list[str]) -> None:
        try:
            config = configparser.ConfigParser()
            config.read(config_file)

            if len(args) > 1:
                for i in range(0, len(args), 2):
                    config["DEFAULT"][args[i]] = args[i + 1]
            # else:
            #     config["DEFAULT"] = {
            #         "epsilon": ConfigReader.EPSILON,
            #         "debugPrint": ConfigReader.DEBUG_PRINT,
            #         "maxIndividuals": ConfigReader.MAX_INDIVIDUALS,
            #         "showVersion": ConfigReader.SHOW_VERSION,
            #         "author": False,
            #     }

            ConfigReader.DEBUG_PRINT = config.getboolean("DEFAULT", "debugPrint")
            ConfigReader.EPSILON = config.getfloat("DEFAULT", "epsilon")
            ConfigReader.MAX_INDIVIDUALS = config.getint("DEFAULT", "maxIndividuals")
            ConfigReader.OWL_ANNOTATION_LABEL = config.get(
                "DEFAULT", "owlAnnotationLabel"
            )
            ConfigReader.MILP_PROVIDER = MILPProvider(
                config.get("DEFAULT", "milpProvider").lower()
            )
            ConfigReader.NUMBER_DIGITS = int(
                round(abs(math.log10(ConfigReader.EPSILON) - 1.0))
            )
            if ConfigReader.MILP_PROVIDER in [
                MILPProvider.MIP,
                MILPProvider.PULP,
            ]:
                constants.MAXVAL = (1 << 31) - 1
                constants.MAXVAL2 = constants.MAXVAL * 2
            elif ConfigReader.MILP_PROVIDER in [
                MILPProvider.PULP_GLPK,
                MILPProvider.PULP_HIGHS,
                MILPProvider.PULP_CPLEX,
                # MILPProvider.SCIPY,
            ]:
                constants.MAXVAL = (1 << 28) - 1
                constants.MAXVAL2 = constants.MAXVAL * 2

            if ConfigReader.DEBUG_PRINT:
                print(f"Debugging mode = {ConfigReader.DEBUG_PRINT}")

        except FileNotFoundError:
            print(f"Error: File {config_file} not found.")
        except Exception as e:
            print(f"Error: {e}.")
