from __future__ import annotations

import configparser
import math
import os

from dotenv import dotenv_values, find_dotenv, load_dotenv

from fuzzy_dl_owl2.fuzzydl.util import constants


class ConfigReader:
    """
    A centralized configuration manager for a reasoning engine, defining default parameters that control precision, optimization levels, blocking strategies, and the selection of the Mixed-Integer Linear Programming (MILP) solver. It allows users to customize the reasoner's behavior by loading settings from a configuration file (INI) or, when that file is missing or unspecified, from a ``.env`` file located in the current working directory. Specific values can be overridden via command-line arguments. When parameters are loaded, the manager automatically adjusts internal precision calculations and updates global constants within the application to match the capabilities of the selected solver provider.

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
    DEBUG_PRINT: bool = False
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
    def _read_ini(config_file: str) -> dict[str, str]:
        """
        Reads an INI-style configuration file and returns the key/value pairs of its ``DEFAULT`` section as a plain dictionary. Parsing is delegated to :class:`configparser.ConfigParser`; if the file cannot be found or read, a ``FileNotFoundError`` is raised rather than silently returning an empty mapping.

        :param config_file: Path to the INI configuration file to read.
        :type config_file: str

        :raises FileNotFoundError: if the configuration file does not exist or cannot be read.

        :return: The ``DEFAULT`` section entries as a ``{key: value}`` mapping.

        :rtype: dict[str, str]
        """

        config = configparser.ConfigParser()
        read_files = config.read(config_file)
        if not read_files:
            raise FileNotFoundError(f"Config file not found: {config_file}")
        return {k: v for k, v in config["DEFAULT"].items()}

    @staticmethod
    def _read_env() -> dict[str, str] | None:
        """
        Loads the default ``.env`` discovered by python-dotenv.

        python-dotenv's default ``find_dotenv()`` walks up from the *caller's
        file* (``config_reader.py``), not from the current working directory,
        so a ``.env`` placed in the user's working directory was previously
        invisible. Pass ``usecwd=True`` so discovery starts at ``os.getcwd()``
        and walks up from there.

        :return: The file-only key/value mapping, or ``None`` when no ``.env``
            file is discovered.

        :rtype: dict[str, str] | None
        """
        dotenv_path = find_dotenv(usecwd=True)
        if not dotenv_path or not load_dotenv(dotenv_path, override=True):
            return None
        return {k: v for k, v in dotenv_values(dotenv_path).items() if v is not None}

    @staticmethod
    def load_parameters(config_file: str | None, **kwargs: list[str]) -> None:
        """
        Loads configuration settings and applies overrides from the provided argument list.

        When ``config_file`` is ``None`` or points to a non-existent path, the loader falls
        back to a ``.env`` file located in the current working directory (``./.env``). The
        ``.env`` file uses the standard ``KEY=VALUE`` format; keys are matched against the
        INI configuration keys in a case- and underscore-insensitive way, so either
        ``DEBUG_PRINT=True`` or ``debugPrint=True`` is accepted.

        Overrides are supplied as keyword arguments and applied on top of the values read
        from the INI/``.env`` source before case- and underscore-insensitive normalisation.

        :param config_file: Filesystem path to the INI configuration file. If ``None`` or
            missing, ``./.env`` is used as a fallback.
        :type config_file: str | None
        :param kwargs: A dictionary of key-value pairs to override configuration settings.
        :type kwargs: dict[str, typing.Any]

        :raises FileNotFoundError: if ``config_file`` is ``None`` or missing and no ``.env``
            file can be discovered by python-dotenv.
        """

        if config_file is not None and os.path.isfile(config_file):
            settings = ConfigReader._read_ini(config_file)
        else:
            settings = ConfigReader._read_env()
            if settings is None:
                raise FileNotFoundError(
                    f"No configuration source found: config_file={config_file!r}, "
                    "no .env discovered by python-dotenv"
                )

        # kwargs are optional key/value override pairs.
        for key, value in kwargs.items():
            settings[key] = value

        # Match keys case- and underscore-insensitively so INI keys
        # (``milpProvider``) and ``.env`` keys (``MILP_PROVIDER``) both resolve.
        settings = {k.replace("_", "").lower(): v for k, v in settings.items()}

        # Apply settings with appropriate type conversions and defaults.
        debug_print = settings.get("debugprint", ConfigReader.DEBUG_PRINT)
        ConfigReader.DEBUG_PRINT = (
            debug_print
            if isinstance(debug_print, bool)
            else str(debug_print).strip().lower() in ("1", "true", "yes", "on")
        )
        ConfigReader.EPSILON = float(settings.get("epsilon", ConfigReader.EPSILON))
        ConfigReader.MAX_INDIVIDUALS = int(
            settings.get("maxindividuals", ConfigReader.MAX_INDIVIDUALS)
        )
        ConfigReader.OWL_ANNOTATION_LABEL = settings.get(
            "owlannotationlabel", ConfigReader.OWL_ANNOTATION_LABEL
        )
        ConfigReader.MILP_PROVIDER = constants.MILPProvider(
            str(
                settings.get("milpprovider", ConfigReader.MILP_PROVIDER.name)
            ).lower()
        )

        # Compute the number of digits of precision based on the epsilon value and set global constants based on the selected MILP provider.
        ConfigReader.NUMBER_DIGITS = int(
            round(abs(math.log10(ConfigReader.EPSILON) - 1.0))
        )

        # Set global constants based on the selected MILP provider, adjusting MAXVAL accordingly to ensure compatibility with the solver's capabilities.
        if ConfigReader.MILP_PROVIDER in (
            constants.MILPProvider.MIP,
            constants.MILPProvider.PULP,
        ):
            constants.MAXVAL = (1 << 31) - 1
        elif ConfigReader.MILP_PROVIDER in (
            constants.MILPProvider.PULP_GLPK,
            constants.MILPProvider.PULP_CPLEX,
            constants.MILPProvider.PULP_HIGHS,
        ):
            constants.MAXVAL = (1 << 28) - 1
        constants.MAXVAL2 = constants.MAXVAL * 2

        if ConfigReader.DEBUG_PRINT:
            print(f"Debugging mode = {ConfigReader.DEBUG_PRINT}")
