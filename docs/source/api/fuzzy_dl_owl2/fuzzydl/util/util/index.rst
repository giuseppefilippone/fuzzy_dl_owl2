fuzzy_dl_owl2.fuzzydl.util.util
===============================

.. py:module:: fuzzy_dl_owl2.fuzzydl.util.util



.. ── LLM-GENERATED DESCRIPTION START ──

A centralized utility namespace and logging infrastructure for the fuzzy ontology reasoner.


Description
-----------


Execution begins by establishing a robust logging system that organizes output into timestamped directories and files, with the verbosity level dynamically controlled by configuration settings. The ``Util`` class serves as a static repository for common operations, wrapping standard logging calls to automatically raise custom exceptions upon encountering errors. Mathematical helpers are provided to ensure high precision by using decimal arithmetic for rounding operations, specifically adhering to a "round half up" strategy rather than default binary rounding. Further functionality includes utilities for detecting integer values within floating-point numbers, calculating the ceiling of base-2 logarithms, and in-place sorting of lists based on string conversion.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.util.util.FILENAME
   fuzzy_dl_owl2.fuzzydl.util.util.LOG_DIR
   fuzzy_dl_owl2.fuzzydl.util.util.TODAY
   fuzzy_dl_owl2.fuzzydl.util.util.logger


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.util.util.Util


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_util_Util.png
       :alt: UML Class Diagram for Util
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **Util**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_util_Util.pdf
       :alt: UML Class Diagram for Util
       :align: center
       :width: 7.1cm
       :class: uml-diagram

       UML Class Diagram for **Util**

.. py:class:: Util

   This class serves as a centralized utility namespace for the reasoner, providing static methods for logging and common data manipulations. It wraps standard logging operations, allowing for conditional debug output based on configuration settings and automatically raising a specific exception when an error is logged. Beyond logging, it offers mathematical helpers such as rounding numbers with configurable precision and half-up rounding rules, checking for integer values in floats, calculating the ceiling of the base-2 logarithm, and sorting lists in-place based on string conversion.

   :raises FuzzyOntologyException: Raised by the `Util.error` method to indicate a critical error or failure condition within the fuzzy ontology reasoner.


   .. py:method:: debug(message: str) -> None
      :staticmethod:


      Conditionally logs a message at the debug level based on the application's configuration settings. This method checks the `DEBUG_PRINT` flag from the `ConfigReader` to determine whether debug output is currently enabled. If the flag is set to true, the provided message string is passed to the underlying logger; otherwise, the call is a no-op and the message is silently discarded. This provides a centralized mechanism for controlling debug verbosity without modifying individual logging calls throughout the codebase.

      :param message: The message content to be logged at the debug level.
      :type message: str



   .. py:method:: error(message: str) -> None
      :staticmethod:


      Logs the specified error message to the application's logger and subsequently raises a `FuzzyOntologyException` containing that message. This utility function ensures that critical errors are both recorded for debugging purposes and propagated up the call stack to halt execution. As the method always raises an exception, it never returns normally.

      :param message: The error message to be logged and included in the raised exception.
      :type message: str

      :raises FuzzyOntologyException: Raised to signal a general error or failure condition within the fuzzy ontology context, carrying the provided descriptive message.



   .. py:method:: has_integer_value(d: float) -> bool
      :staticmethod:


      Determines whether the provided floating-point number represents an integer value, effectively checking for the absence of a fractional component. This static utility method returns `True` if the input is equivalent to an integer (e.g., 5.0 or -2.0) and `False` otherwise (e.g., 5.1). It correctly handles special floating-point cases such as infinity and NaN by returning `False`, and it performs no side effects on the input data.

      :param d:
      :type d: float

      :return: True if the float represents an integer value, False otherwise.

      :rtype: bool



   .. py:method:: info(message: str) -> None
      :staticmethod:


      Logs a message at the INFO level using the underlying logger instance. This static method accepts a string argument and passes it directly to the logging system, typically used to confirm that the program is functioning as expected. It produces no return value, and the actual handling of the message—such as writing to a file or standard output—depends on the specific configuration of the logger. Note that if the logging threshold is set above the INFO level, this message will be ignored.

      :param message: The text content to log at the INFO level.
      :type message: str



   .. py:method:: log2(n: float) -> int
      :staticmethod:


      Calculates the ceiling of the base-2 logarithm of a given number, returning the smallest integer $k$ such that $2^k$ is greater than or equal to the input. This is useful for determining the necessary bit-width or the next power of two for a given size. The function accepts a float and returns an integer, but it will raise a ValueError if the input is less than or equal to zero. This is a static method with no side effects.

      :param n: The positive number for which the ceiling of the base-2 logarithm is computed.
      :type n: float

      :return: The smallest integer greater than or equal to the base-2 logarithm of n.

      :rtype: int



   .. py:method:: order(v: list[Any]) -> None
      :staticmethod:


      Sorts the input list in-place using the string representation of each element as the sorting key. This approach ensures that heterogeneous lists containing mixed types can be ordered, though the resulting sequence follows lexicographical rules rather than numerical or type-specific logic. The method modifies the list directly and returns None, meaning the original reference is updated without creating a new list.

      :param v: List to be sorted in-place based on the string representation of its elements.
      :type v: list[typing.Any]



   .. py:method:: round(x: float) -> float
      :staticmethod:


      Rounds a floating-point number to a specific precision defined by the `ConfigReader.NUMBER_DIGITS` configuration, utilizing the `Decimal` module to avoid binary floating-point representation errors. Unlike Python's built-in `round` function, this method employs "round half up" logic, meaning values exactly halfway between two rounding points are rounded away from zero. The input is converted to a string prior to decimal conversion to ensure accuracy, and the final result is returned as a standard float.

      :param x: The floating-point value to be rounded to the configured number of decimal places.
      :type x: float

      :return: The input value rounded to the configured number of decimal places using round-half-up rounding.

      :rtype: float



   .. py:method:: warning(message: str) -> None
      :staticmethod:


      Logs a message with a severity level of WARNING using the configured logger instance. This static method serves as a convenience wrapper that forwards the provided string directly to the logging infrastructure. While the method itself returns no value, it triggers side effects such as writing to standard output or a log file, depending on the logger's configuration. If the logging system is disabled or configured to suppress warning-level events, calling this method will result in no action.

      :param message: The text content of the warning to be logged.
      :type message: str



.. py:data:: FILENAME
   :type:  str

.. py:data:: LOG_DIR
   :type:  str

.. py:data:: TODAY
   :type:  datetime.datetime

.. py:data:: logger
