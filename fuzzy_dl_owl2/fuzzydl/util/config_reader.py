from __future__ import annotations

import configparser
import math

from fuzzy_dl_owl2.fuzzydl.util import constants


class ConfigReader:
    # Anywhere pairwise blocking applied. false disables anywhere double blocking; true enables anywher edouble blocking.
    ANYWHERE_DOUBLE_BLOCKING: bool = True
    # Anywhere simple blocking applied. false disables anywhere simple blocking; true enables anywhere simple blocking.
    ANYWHERE_SIMPLE_BLOCKING: bool = True
    # Debugging mode
    DEBUG_PRINT: bool = True
    # Precision of the reasoner
    EPSILON: float = 0.001
    # Maximum number of new individuals that will be created
    MAX_INDIVIDUALS: int = -1
    # Number of digits of precision
    NUMBER_DIGITS: int = 2
    # Level of the optimizations applied. 0 disables optimizations; a positive value enables optimizations.
    OPTIMIZATIONS: int = 1
    # Rule acyclic TBox optimization applied
    RULE_ACYCLIC_TBOXES: bool = True
    # XML OWL 2 annotation label used to create and parse Fuzzy OWL 2 ontologies
    OWL_ANNOTATION_LABEL: str = "fuzzyLabel"
    # MILP Solver provider used by the reasoner
    MILP_PROVIDER: constants.MILPProvider = constants.MILPProvider.GUROBI

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
            ConfigReader.MILP_PROVIDER = constants.MILPProvider(
                config.get("DEFAULT", "milpProvider").lower()
            )
            ConfigReader.NUMBER_DIGITS = int(
                round(abs(math.log10(ConfigReader.EPSILON) - 1.0))
            )
            if ConfigReader.MILP_PROVIDER in [
                constants.MILPProvider.MIP,
                constants.MILPProvider.PULP,
            ]:
                constants.MAXVAL = (1 << 31) - 1
                constants.MAXVAL2 = constants.MAXVAL * 2
            elif ConfigReader.MILP_PROVIDER in [
                constants.MILPProvider.PULP_GLPK,
                constants.MILPProvider.PULP_HIGHS,
                constants.MILPProvider.PULP_CPLEX,
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
