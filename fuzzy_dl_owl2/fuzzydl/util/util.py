from __future__ import annotations

import datetime
import logging
import math
import os
import typing
from decimal import ROUND_HALF_UP, Decimal

from fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception import (
    FuzzyOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader

TODAY: datetime.datetime = datetime.datetime.today()
LOG_DIR: str = os.path.join(
    ".", "logs", "reasoner", str(TODAY.year), str(TODAY.month), str(TODAY.day)
)
FILENAME: str = (
    f"fuzzydl_{str(TODAY.hour).zfill(2)}-{str(TODAY.minute).zfill(2)}-{str(TODAY.second).zfill(2)}.log"
)

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, FILENAME),
    filemode="w",
    level=logging.INFO if not ConfigReader.DEBUG_PRINT else logging.DEBUG,
    format="%(asctime)s - %(levelname)s -- %(message)s",
)


class Util:
    """
    This class serves as a centralized utility namespace for the reasoner, providing static methods for logging and common data manipulations. It wraps standard logging operations, allowing for conditional debug output based on configuration settings and automatically raising a specific exception when an error is logged. Beyond logging, it offers mathematical helpers such as rounding numbers with configurable precision and half-up rounding rules, checking for integer values in floats, calculating the ceiling of the base-2 logarithm, and sorting lists in-place based on string conversion.

    :raises FuzzyOntologyException: Raised by the `Util.error` method to indicate a critical error or failure condition within the fuzzy ontology reasoner.
    """


    @staticmethod
    def info(message: str) -> None:
        """
        Logs a message at the INFO level using the underlying logger instance. This static method accepts a string argument and passes it directly to the logging system, typically used to confirm that the program is functioning as expected. It produces no return value, and the actual handling of the message—such as writing to a file or standard output—depends on the specific configuration of the logger. Note that if the logging threshold is set above the INFO level, this message will be ignored.

        :param message: The text content to log at the INFO level.
        :type message: str
        """

        logger.info(message)

    @staticmethod
    def warning(message: str) -> None:
        """
        Logs a message with a severity level of WARNING using the configured logger instance. This static method serves as a convenience wrapper that forwards the provided string directly to the logging infrastructure. While the method itself returns no value, it triggers side effects such as writing to standard output or a log file, depending on the logger's configuration. If the logging system is disabled or configured to suppress warning-level events, calling this method will result in no action.

        :param message: The text content of the warning to be logged.
        :type message: str
        """

        logger.warning(message)

    @staticmethod
    def debug(message: str) -> None:
        """
        Conditionally logs a message at the debug level based on the application's configuration settings. This method checks the `DEBUG_PRINT` flag from the `ConfigReader` to determine whether debug output is currently enabled. If the flag is set to true, the provided message string is passed to the underlying logger; otherwise, the call is a no-op and the message is silently discarded. This provides a centralized mechanism for controlling debug verbosity without modifying individual logging calls throughout the codebase.

        :param message: The message content to be logged at the debug level.
        :type message: str
        """

        if ConfigReader.DEBUG_PRINT:
            logger.debug(message)

    @staticmethod
    def error(message: str) -> None:
        """
        Logs the specified error message to the application's logger and subsequently raises a `FuzzyOntologyException` containing that message. This utility function ensures that critical errors are both recorded for debugging purposes and propagated up the call stack to halt execution. As the method always raises an exception, it never returns normally.

        :param message: The error message to be logged and included in the raised exception.
        :type message: str

        :raises FuzzyOntologyException: Raised to signal a general error or failure condition within the fuzzy ontology context, carrying the provided descriptive message.
        """

        logger.error(message)
        raise FuzzyOntologyException(message)

    @staticmethod
    def has_integer_value(d: float) -> bool:
        """
        Determines whether the provided floating-point number represents an integer value, effectively checking for the absence of a fractional component. This static utility method returns `True` if the input is equivalent to an integer (e.g., 5.0 or -2.0) and `False` otherwise (e.g., 5.1). It correctly handles special floating-point cases such as infinity and NaN by returning `False`, and it performs no side effects on the input data.

        :param d: 
        :type d: float

        :return: True if the float represents an integer value, False otherwise.

        :rtype: bool
        """

        return d.is_integer()

    @staticmethod
    def round(x: float) -> float:
        """
        Rounds a floating-point number to a specific precision defined by the `ConfigReader.NUMBER_DIGITS` configuration, utilizing the `Decimal` module to avoid binary floating-point representation errors. Unlike Python's built-in `round` function, this method employs "round half up" logic, meaning values exactly halfway between two rounding points are rounded away from zero. The input is converted to a string prior to decimal conversion to ensure accuracy, and the final result is returned as a standard float.

        :param x: The floating-point value to be rounded to the configured number of decimal places.
        :type x: float

        :return: The input value rounded to the configured number of decimal places using round-half-up rounding.

        :rtype: float
        """

        decimal = Decimal(str(x))
        return float(
            decimal.quantize(
                Decimal("0." + "0" * ConfigReader.NUMBER_DIGITS), rounding=ROUND_HALF_UP
            )
        )

    @staticmethod
    def order(v: list[typing.Any]) -> None:
        """
        Sorts the input list in-place using the string representation of each element as the sorting key. This approach ensures that heterogeneous lists containing mixed types can be ordered, though the resulting sequence follows lexicographical rules rather than numerical or type-specific logic. The method modifies the list directly and returns None, meaning the original reference is updated without creating a new list.

        :param v: List to be sorted in-place based on the string representation of its elements.
        :type v: list[typing.Any]
        """

        v.sort(key=lambda x: str(x))

    @staticmethod
    def log2(n: float) -> int:
        """
        Calculates the ceiling of the base-2 logarithm of a given number, returning the smallest integer $k$ such that $2^k$ is greater than or equal to the input. This is useful for determining the necessary bit-width or the next power of two for a given size. The function accepts a float and returns an integer, but it will raise a ValueError if the input is less than or equal to zero. This is a static method with no side effects.

        :param n: The positive number for which the ceiling of the base-2 logarithm is computed.
        :type n: float

        :return: The smallest integer greater than or equal to the base-2 logarithm of n.

        :rtype: int
        """

        return int(math.ceil(math.log2(n)))
