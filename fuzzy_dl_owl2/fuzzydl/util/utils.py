import functools
import inspect
import sys
import types
import typing

from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.util import Util

FULL_CLASS_DEBUG_PRINT: bool = False


def debugging_wrapper(cls, func):
    """
    Debugging wrapper that prints before and after the method call.
    """

    is_static: bool = False
    try:
        is_static = isinstance(inspect.getattr_static(cls, func.__name__), staticmethod)
    except:
        pass

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        Util.debug(
            f"\t\t\t>>>>Entering {cls.__name__}:{func.__name__} with args={args if is_static else args[1:]}, kwargs={kwargs}"
        )
        result = func(*args, **kwargs)
        Util.debug(
            f"\t\t\t<<<<Leaving {cls.__name__}:{func.__name__} returned {result}"
        )
        return result

    return wrapped


def class_debugging():
    """
    Decorator to wrap all methods of a class using debugging_wrapper.
    """

    def class_decorator(cls):
        if FULL_CLASS_DEBUG_PRINT:
            for attr_name in dir(cls):
                attr = getattr(cls, attr_name)
                # Only wrap instance methods
                if isinstance(attr, types.FunctionType):
                    # Wrap the method
                    wrapped_method = debugging_wrapper(cls, attr)
                    setattr(cls, attr_name, wrapped_method)
        return cls

    return class_decorator


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
