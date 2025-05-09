import ast
import datetime
import functools
import importlib
import importlib.util
import inspect
import os
import sys
import time
import types
import typing

from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.util import Util

def recursion_unlimited(func: typing.Callable):
    module: types.ModuleType = inspect.getmodule(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        orig_n: int = sys.getrecursionlimit()
        while True:
            try:
                result = func(*args, **kwargs)
                break
            except RecursionError:
                # since self.proposition is too long, change the recursion limit
                n: int = sys.getrecursionlimit() * 2
                sys.setrecursionlimit(n)
                if ConfigReader.DEBUG_PRINT:
                    Util.debug(
                        f"Updating recursion limit for {module.__name__}:{func.__name__}() to {n}"
                    )
        # reset recursion limit to its original value
        sys.setrecursionlimit(orig_n)
        return result

    return wrapper