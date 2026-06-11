fuzzy_dl_owl2.fuzzydl.util.config_reader
========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.util.config_reader



.. ── LLM-GENERATED DESCRIPTION START ──

A centralized configuration manager that loads and applies settings for a fuzzy reasoning engine from INI or environment files.


Description
-----------


The software establishes a set of default parameters governing the behavior of a fuzzy reasoning engine, including precision thresholds, optimization levels, and blocking strategies. It provides a flexible loading mechanism that prioritizes a specified INI configuration file but falls back to a ``.env`` file located in the current working directory if the primary source is unavailable. Input values are normalized to handle case and underscore variations, ensuring compatibility between different configuration formats, while specific overrides can be applied directly to the loaded settings. Once the parameters are loaded, the system automatically derives internal precision metrics and adjusts global numerical limits within the application to match the specific capabilities of the chosen Mixed-Integer Linear Programming solver.

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


