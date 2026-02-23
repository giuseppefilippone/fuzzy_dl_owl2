from __future__ import annotations

import configparser
import math

from fuzzy_dl_owl2.fuzzydl.util import constants


class ConfigReader:
    """
    A centralized configuration manager for a reasoning engine, defining default parameters that control precision, optimization levels, blocking strategies, and the selection of the Mixed-Integer Linear Programming (MILP) solver. It allows users to customize the reasoner's behavior by loading settings from a configuration file and overriding specific values via command-line arguments. When parameters are loaded, the manager automatically adjusts internal precision calculations and updates global constants within the application to match the capabilities of the selected solver provider.

    :param ANYWHERE_DOUBLE_BLOCKING: Determines whether the anywhere double blocking optimization is applied.
    :type ANYWHERE_DOUBLE_BLOCKING: bool
    :param ANYWHERE_SIMPLE_BLOCKING: Determines whether anywhere simple blocking is applied during reasoning.
    :type ANYWHERE_SIMPLE_BLOCKING: bool
    :param DEBUG_PRINT: Flag to enable or disable the printing of debug messages to the console.
    :type DEBUG_PRINT: bool
    :param EPSILON: Precision threshold defining the minimum degree of satisfaction required for a concept to be considered satisfied by an individual.
    :type EPSILON: float
    :param MAX_INDIVIDUALS: Defines the maximum number of new individuals that can be generated during reasoning. A negative value disables this limit, allowing unlimited creation.
    :type MAX_INDIVIDUALS: int
    :param NUMBER_DIGITS: Number of digits of precision, computed from the epsilon value to define the decimal places required for the reasoner's operations.
    :type NUMBER_DIGITS: int
    :param OPTIMIZATIONS: Level of optimizations applied. A value of 0 disables optimizations, while a positive value enables them. Default is 1.
    :type OPTIMIZATIONS: int
    :param RULE_ACYCLIC_TBOXES: Enables the rule acyclic TBox optimization.
    :type RULE_ACYCLIC_TBOXES: bool
    :param OWL_ANNOTATION_LABEL: The XML annotation label used to identify fuzzy logic constructs when creating or parsing Fuzzy OWL 2 ontologies.
    :type OWL_ANNOTATION_LABEL: str
    :param MILP_PROVIDER: Specifies the Mixed-Integer Linear Programming (MILP) solver backend used by the reasoner for optimization tasks, influencing internal numerical limits based on the selected provider.
    :type MILP_PROVIDER: constants.MILPProvider
    """


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
        """
        Reads configuration settings from the specified file and applies overrides from the provided argument list, which is interpreted as sequential key-value pairs. This method updates class-level attributes of `ConfigReader` and modifies global constants within the application's `constants` module based on the loaded settings, such as the MILP provider and epsilon value. It also calculates derived values like `NUMBER_DIGITS` and prints a debug message if enabled. The provided argument list must contain an even number of elements to form valid key-value pairs; otherwise, a generic exception is triggered. Errors during file reading or parsing are caught and printed to standard output without halting execution, potentially leaving the configuration in a partially updated state.

        :param config_file: Filesystem path to the configuration file containing default parameters.
        :type config_file: str
        :param args: A list of strings representing key-value pairs to override configuration settings, interpreted as alternating keys and values.
        :type args: list[str]
        """

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
