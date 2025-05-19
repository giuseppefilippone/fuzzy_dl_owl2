from __future__ import annotations

import configparser
import math


class ConfigReader:
    ANYWHERE_DOUBLE_BLOCKING: bool = True
    ANYWHERE_SIMPLE_BLOCKING: bool = True
    RELAX_MILP: bool = False
    DEBUG_PRINT: bool = True
    EPSILON: float = 0.001
    MAX_INDIVIDUALS: int = -1
    NUMBER_DIGITS: int = 2
    OPTIMIZATIONS: int = 1
    RULE_ACYCLIC_TBOXES: bool = True

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

            ConfigReader.RELAX_MILP = config.getboolean("DEFAULT", "relaxMilp")
            ConfigReader.DEBUG_PRINT = config.getboolean("DEFAULT", "debugPrint")
            ConfigReader.EPSILON = config.getfloat("DEFAULT", "epsilon")
            ConfigReader.MAX_INDIVIDUALS = config.getint("DEFAULT", "maxIndividuals")
            ConfigReader.NUMBER_DIGITS = int(
                round(abs(math.log10(ConfigReader.EPSILON) - 1.0))
            )

            if ConfigReader.DEBUG_PRINT:
                print(f"Debugging mode = {ConfigReader.DEBUG_PRINT}")

        except FileNotFoundError:
            print(f"Error: File {config_file} not found.")
        except Exception as e:
            print(f"Error: {e}.")
