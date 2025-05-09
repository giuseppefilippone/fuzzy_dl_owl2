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
    @staticmethod
    def info(message: str) -> None:
        logger.info(message)

    @staticmethod
    def warning(message: str) -> None:
        logger.warning(message)

    @staticmethod
    def debug(message: str) -> None:
        if ConfigReader.DEBUG_PRINT:
            logger.debug(message)

    @staticmethod
    def error(message: str) -> None:
        logger.error(message)
        raise FuzzyOntologyException(message)

    @staticmethod
    def has_integer_value(d: float) -> bool:
        return d.is_integer()

    @staticmethod
    def round(x: float) -> float:
        decimal = Decimal(str(x))
        return float(
            decimal.quantize(
                Decimal("0." + "0" * ConfigReader.NUMBER_DIGITS), rounding=ROUND_HALF_UP
            )
        )

    @staticmethod
    def order(v: list[typing.Any]) -> None:
        v.sort(key=lambda x: str(x))

    @staticmethod
    def log2(n: float) -> int:
        return int(math.ceil(math.log2(n)))
