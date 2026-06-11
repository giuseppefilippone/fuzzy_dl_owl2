import functools
import inspect
import sys
import types
import typing

from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.util import Util

FULL_CLASS_DEBUG_PRINT: bool = False
RECURSION_LIMIT_CAP: int = 1 << 20


def debugging_wrapper(cls, func):
    """
    This function creates a debugging wrapper for a class method, logging the entry and exit of the method call. It prints a formatted message before execution that includes the class and method names, along with the arguments passed to the function; notably, it excludes the first argument (typically `self` or `cls`) unless the method is detected as a static method. After the method completes, it logs a message containing the return value. The wrapper uses `functools.wraps` to preserve the original function's metadata and relies on the `Util.debug` utility for output.

    :param cls: The class containing the method being wrapped, used to access the class name and check if the method is static.
    :type cls: typing.Any
    :param func: The method or function to be wrapped with debug logging.
    :type func: typing.Any

    :return: The wrapped function, which logs entry/exit around ``func`` and returns its result unchanged.

    :rtype: typing.Callable
    """


    is_static: bool = False
    try:
        is_static = isinstance(inspect.getattr_static(cls, func.__name__), staticmethod)
    except AttributeError:
        pass

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        """
        Wrapped version of the target method that logs its entry and exit when debugging is enabled. The positional arguments and keyword arguments are logged on entry (omitting the leading ``self``/``cls`` for non-static methods) and the return value is logged on exit, both gated by :attr:`ConfigReader.DEBUG_PRINT`. The original return value is passed through unchanged.

        :param args: Positional arguments forwarded verbatim to the wrapped method.
        :type args: typing.Any
        :param kwargs: Keyword arguments forwarded verbatim to the wrapped method.
        :type kwargs: typing.Any

        :return: Whatever the wrapped method returns.

        :rtype: typing.Any
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(
                f"\t\t\t>>>>Entering {cls.__name__}:{func.__name__} with args={args if is_static else args[1:]}, kwargs={kwargs}"
            )
        result = func(*args, **kwargs)
        if ConfigReader.DEBUG_PRINT:
            Util.debug(
                f"\t\t\t<<<<Leaving {cls.__name__}:{func.__name__} returned {result}"
            )
        return result

    return wrapped


def class_debugging():
    """
    This function serves as a decorator factory that generates a class-level decorator to instrument all instance methods with debugging capabilities. When applied to a class, it checks the global `FULL_CLASS_DEBUG_PRINT` flag; if this flag is true, the decorator iterates over the class's attributes to identify functions and replaces them with wrapped versions using `debugging_wrapper`. This mechanism enables automatic logging or tracing of method execution across the entire class, contingent on the global configuration state.

    :return: A class decorator that optionally instruments the methods of the class it is applied to.

    :rtype: typing.Callable
    """


    def class_decorator(cls):
        """
        Class decorator that, when ``FULL_CLASS_DEBUG_PRINT`` is enabled, wraps every plain function attribute of the class with :func:`debugging_wrapper` to trace method calls. When the flag is disabled the class is returned untouched. The class is always returned (mutated in place when wrapping occurs).

        :param cls: The class to instrument with debug wrappers.
        :type cls: typing.Any

        :return: The same class, with its methods optionally wrapped.

        :rtype: typing.Any
        """

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
    """
    This decorator wraps a callable to automatically handle `RecursionError` exceptions by dynamically increasing the system recursion limit. Upon invocation, the wrapper attempts to execute the function; if a recursion depth error occurs, the limit is doubled and the execution is retried repeatedly until the function succeeds. The decorator modifies the global recursion limit during execution but ensures it is restored to its original value upon completion. Note that this mechanism does not prevent infinite recursion and may lead to high memory consumption or segmentation faults if the recursion depth is excessive.

    :param func: The callable to be wrapped that may raise a RecursionError; the wrapper will dynamically increase the recursion limit until the function succeeds.
    :type func: typing.Callable

    :return: The wrapped callable, which retries ``func`` while raising the recursion limit and always restores the original limit afterwards.

    :rtype: typing.Callable
    """

    module: types.ModuleType = inspect.getmodule(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapped version of the target callable that retries on ``RecursionError`` by repeatedly doubling the interpreter's recursion limit until the call succeeds or the limit would exceed ``RECURSION_LIMIT_CAP``. The original recursion limit is always restored in a ``finally`` block once the call returns or finally fails.

        :param args: Positional arguments forwarded verbatim to the wrapped callable.
        :type args: typing.Any
        :param kwargs: Keyword arguments forwarded verbatim to the wrapped callable.
        :type kwargs: typing.Any

        :raises RecursionError: if doubling the recursion limit would exceed ``RECURSION_LIMIT_CAP``.

        :return: Whatever the wrapped callable returns.

        :rtype: typing.Any
        """

        orig_n: int = sys.getrecursionlimit()
        try:
            while True:
                try:
                    return func(*args, **kwargs)
                except RecursionError:
                    n: int = sys.getrecursionlimit() * 2
                    if n > RECURSION_LIMIT_CAP:
                        raise RecursionError(
                            f"{module.__name__}:{func.__name__} exceeded recursion cap of {RECURSION_LIMIT_CAP}"
                        )
                    sys.setrecursionlimit(n)
                    if ConfigReader.DEBUG_PRINT:
                        Util.debug(
                            f"Updating recursion limit for {module.__name__}:{func.__name__}() to {n}"
                        )
        finally:
            sys.setrecursionlimit(orig_n)

    return wrapper
