fuzzy_dl_owl2.fuzzydl.util.config_reader
========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.util.config_reader



.. ── LLM-GENERATED DESCRIPTION START ──

Centralizes configuration management for a fuzzy description logic reasoning engine by loading parameters from files and command-line arguments to control precision, optimization strategies, and solver selection.


Description
-----------


The software defines a set of default parameters that govern the operational behavior of a reasoning engine, including numerical precision thresholds, optimization levels, and specific blocking strategies used during inference. It provides a mechanism to ingest settings from an external configuration file while simultaneously supporting overrides via a list of command-line arguments, ensuring flexibility for different execution environments. Upon loading these parameters, the logic automatically derives secondary values, such as the number of precision digits based on the epsilon threshold, and dynamically adjusts global numerical limits within the application to match the capabilities of the selected Mixed-Integer Linear Programming (MILP) solver. Error handling is implemented to catch and report issues during file parsing or type conversion without crashing the application, allowing the reasoning process to proceed with default or partially loaded settings.

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
       :width: 10.8cm
       :class: uml-diagram

       UML Class Diagram for **ConfigReader**

.. py:class:: ConfigReader

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


   .. py:method:: load_parameters(config_file: str, args: list[str]) -> None
      :staticmethod:


      Reads configuration settings from the specified file and applies overrides from the provided argument list, which is interpreted as sequential key-value pairs. This method updates class-level attributes of `ConfigReader` and modifies global constants within the application's `constants` module based on the loaded settings, such as the MILP provider and epsilon value. It also calculates derived values like `NUMBER_DIGITS` and prints a debug message if enabled. The provided argument list must contain an even number of elements to form valid key-value pairs; otherwise, a generic exception is triggered. Errors during file reading or parsing are caught and printed to standard output without halting execution, potentially leaving the configuration in a partially updated state.

      :param config_file: Filesystem path to the configuration file containing default parameters.
      :type config_file: str
      :param args: A list of strings representing key-value pairs to override configuration settings, interpreted as alternating keys and values.
      :type args: list[str]



   .. py:attribute:: ANYWHERE_DOUBLE_BLOCKING
      :type:  bool
      :value: True



   .. py:attribute:: ANYWHERE_SIMPLE_BLOCKING
      :type:  bool
      :value: True



   .. py:attribute:: DEBUG_PRINT
      :type:  bool
      :value: True



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


