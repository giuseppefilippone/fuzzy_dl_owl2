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

__all__ = [
    "reset_timers",
    "get_timers",
    "get_cumulative_timers",
    "get_timer",
    "set_timer",
    "get_cumulative_timer",
    "set_cumulative_timer",
    "print_timers",
    "print_cumulative_timers",
    "class_timer",
    "singleton",
    "_TIMERS",
    "_TIMERS_CACHE",
    "_CUMULATIVE_TIMERS"
]

_TIMERS_CACHE: dict[str, bool] = dict()
_TIMERS: dict[str, int] = dict()
_CUMULATIVE_TIMERS: dict[str, int] = dict()


def reset_timers() -> None:
    global _TIMERS
    global _TIMERS_CACHE
    global _CUMULATIVE_TIMERS

    _TIMERS.clear()
    _TIMERS_CACHE.clear()
    _CUMULATIVE_TIMERS.clear()


def get_timers() -> dict[str, int]:
    return _TIMERS


def get_cumulative_timers() -> dict[str, int]:
    return _CUMULATIVE_TIMERS


def get_timer(key: str) -> int:
    return _TIMERS.get(key, None)


def get_cumulative_timer(key: str) -> int:
    return _CUMULATIVE_TIMERS.get(key, None)


def set_cumulative_timer(key: str, value: int) -> None:
    global _CUMULATIVE_TIMERS
    _CUMULATIVE_TIMERS[key] = _CUMULATIVE_TIMERS.get(key, 0) + value


def set_timer(key: str, value: int) -> None:
    global _TIMERS
    _TIMERS[key] = max(_TIMERS.get(key, 0), value)
    set_cumulative_timer(key, value)


def _format_time(t: int):
    return datetime.timedelta(microseconds=t / 1000)


def print_timers(delta: float | None = 1e-2) -> None:
    delta_ns: int = int(delta * 1e9) if delta is not None else None
    for func in get_timers():
        curr_time: int = get_timer(func)
        if delta is not None and curr_time < delta_ns:
            continue
        print(f"Max exec time of {func}: {_format_time(curr_time)}")


def print_cumulative_timers(delta: float | None = 1e-2) -> None:
    delta_ns: int = int(delta * 1e9) if delta is not None else None
    for func in get_cumulative_timers():
        curr_time: int = get_cumulative_timer(func)
        if delta is not None and curr_time < delta_ns:
            continue
        print(f"Cumulative exec time of {func}: {_format_time(curr_time)}")


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


def func_timer(func: typing.Callable, cls: typing.Type = None):
    global _TIMERS_CACHE

    module: types.ModuleType = inspect.getmodule(func)
    key: str = (
        f"{module.__name__}:{func.__name__}"
        if cls is None
        else f"{module.__name__}.{cls.__name__}:{func.__name__}"
    )

    _TIMERS_CACHE[key] = False

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # in case of recursive call to the same function, then do not update timer
        if _TIMERS_CACHE.get(key, False):
            return func(*args, **kwargs)

        _TIMERS_CACHE[key] = True
        start_time: int = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time: int = time.perf_counter_ns()
        _TIMERS_CACHE[key] = False

        elapsed_time_ns: int = end_time - start_time
        set_timer(key, elapsed_time_ns)

        return result

    return wrapper


def class_timer(
    get_private: bool = False,
    functions: list[str] | None = None,
    include_init: bool = False,
):
    functions: list[str] = functions or []

    def timer(cls: typing.Type):
        for attr_name, attr_value in cls.__dict__.items():
            if not callable(attr_value):
                continue
            if not get_private and attr_name.startswith("_"):
                continue
            if (
                len(functions) > 0
                and attr_name.replace(f"_{cls.__name__}", "") not in functions
            ):
                continue
            if not include_init and "__init__" in attr_name:
                continue
            setattr(cls, attr_name, func_timer(attr_value, cls=cls))
        return cls

    return timer


class ClassVisitor(ast.NodeVisitor):
    def __init__(self):
        self.inner_classes = []

    def visit_ClassDef(self, node: ast.ClassDef) -> typing.Any:
        self.inner_classes.append(node.name)
        return super().generic_visit(node)


def get_class(main_module: str, classname: str) -> typing.Any:
    for dirpath, _, files in os.walk(main_module):
        for filename in files:
            if (
                filename.endswith("__init__.py")
                or "old_" in filename
                or not filename.endswith(".py")
            ):
                continue
            filepath: str = os.path.join(dirpath, filename)
            package: str = filepath.replace(".py", "").replace("/", ".")
            with open(filepath, "r") as file:
                tree = ast.parse(file.read())
                vis = ClassVisitor()
                vis.visit(tree)
                if classname in vis.inner_classes:
                    if package in sys.modules:
                        return getattr(sys.modules[package], classname)
                    spec = importlib.util.find_spec(package)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    return getattr(module, classname)
    return None


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance
