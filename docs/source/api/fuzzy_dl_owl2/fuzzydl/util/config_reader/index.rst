fuzzy_dl_owl2.fuzzydl.util.config_reader
========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.util.config_reader





.. ── LLM-GENERATED DESCRIPTION START ──

A centralized configuration manager for a fuzzy description-logic reasoner that loads runtime parameters from an INI file or a *.env* fallback, applies caller-supplied overrides, and keeps global solver constants aligned with the capabilities of the selected MILP backend.


Description
-----------


*ConfigReader* acts as the single source of truth for the reasoner's operational settings, storing them as class-level attributes so that any part of the application can consult or update them without object instantiation. The defaults govern blocking and TBox optimizations, debug output, the epsilon precision threshold, a cap on how many fresh individuals may be generated during reasoning, the optimization level, the XML annotation label used when creating and parsing Fuzzy OWL 2 ontologies, and the Mixed-Integer Linear Programming solver backend, which defaults to GUROBI. Configuration is ingested through *load_parameters*, which reads the DEFAULT section of an INI file when a valid path is supplied and otherwise falls back to a *.env* file discovered by python-dotenv; discovery deliberately starts from the current working directory rather than the library's own location, since dotenv's default search would otherwise miss a *.env* placed by the end user. If neither source can be found, a *FileNotFoundError* is raised rather than silently proceeding with defaults.

Keyword-argument overrides are merged on top of the loaded values, and all keys are normalized to be case- and underscore-insensitive so that camelCase INI keys such as *milpProvider* and SCREAMING_SNAKE *.env* keys such as *MILP_PROVIDER* resolve to the same setting. Raw strings are then coerced to their proper types, with booleans accepting forms like *1*, *true*, *yes*, and *on*, and the solver name being validated through the *MILPProvider* enum so that invalid backends fail immediately.

Two side effects tie the loaded configuration to the rest of the reasoning engine. First, the number of precision digits is derived from the epsilon value via a logarithm, so tightening epsilon automatically increases the decimal precision used throughout the reasoner. Second, global constants are updated with a Big-M value matched to the chosen solver's numeric limits — smaller ranges for the PuLP-based MIP, GLPK, CPLEX, and HiGHS backends, and a much larger one for GUROBI — while the provider-derived default is remembered separately so that per-knowledge-base adaptation can later cap it. An explicit *maxVal* setting overrides the provider default (with *auto* or an empty value meaning "keep the default"), and a doubled companion constant is kept in sync for use by the optimization routines elsewhere in the system.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.util.config_reader.ConfigReader


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_config_reader_ConfigReader.png
       :alt: UML Class Diagram for ConfigReader
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ConfigReader**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_config_reader_ConfigReader.pdf
       :alt: UML Class Diagram for ConfigReader
       :align: center
       :width: 9.7cm
       :class: uml-diagram

       UML Class Diagram for **ConfigReader**

.. py:class:: ConfigReader

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


   .. py:method:: _read_env() -> dict[str, str] | None
      :staticmethod:


      Loads the default ``.env`` discovered by python-dotenv.

      python-dotenv's default ``find_dotenv()`` walks up from the *caller's
      file* (``config_reader.py``), not from the current working directory,
      so a ``.env`` placed in the user's working directory was previously
      invisible. Pass ``usecwd=True`` so discovery starts at ``os.getcwd()``
      and walks up from there.

      :return: The file-only key/value mapping, or ``None`` when no ``.env``
          file is discovered.

      :rtype: dict[str, str] | None



   .. py:method:: _read_ini(config_file: str) -> dict[str, str]
      :staticmethod:


      Reads an INI-style configuration file and returns the key/value pairs of its ``DEFAULT`` section as a plain dictionary. Parsing is delegated to :class:`configparser.ConfigParser`; if the file cannot be found or read, a ``FileNotFoundError`` is raised rather than silently returning an empty mapping.

      :param config_file: Path to the INI configuration file to read.
      :type config_file: str

      :raises FileNotFoundError: if the configuration file does not exist or cannot be read.

      :return: The ``DEFAULT`` section entries as a ``{key: value}`` mapping.

      :rtype: dict[str, str]



   .. py:method:: load_parameters(config_file: str | None, **kwargs: list[str]) -> None
      :staticmethod:


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



   .. py:attribute:: ANYWHERE_DOUBLE_BLOCKING
      :type:  bool
      :value: True



   .. py:attribute:: ANYWHERE_SIMPLE_BLOCKING
      :type:  bool
      :value: True



   .. py:attribute:: DEBUG_PRINT
      :type:  bool
      :value: False



   .. py:attribute:: EPSILON
      :type:  float
      :value: 0.001



   .. py:attribute:: MAXVAL
      :type:  float | None
      :value: None



   .. py:attribute:: MAX_INDIVIDUALS
      :type:  int
      :value: -1



   .. py:attribute:: MILP_PROVIDER
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.MILPProvider


   .. py:attribute:: NUMBER_DIGITS
      :type:  int
      :value: 2



   .. py:attribute:: OPTIMIZATIONS
      :type:  int
      :value: 1



   .. py:attribute:: OWL_ANNOTATION_LABEL
      :type:  str
      :value: 'fuzzyLabel'



   .. py:attribute:: RULE_ACYCLIC_TBOXES
      :type:  bool
      :value: True

