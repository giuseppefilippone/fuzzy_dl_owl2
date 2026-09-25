fuzzy_dl_owl2.fuzzydl.util.utils
================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.util.utils



.. ── LLM-GENERATED DESCRIPTION START ──

A small collection of decorators that add opt-in call tracing to classes and let deeply recursive functions transparently raise the interpreter's recursion limit until they complete.


Description
-----------


Tracing support centres on a wrapper that, whenever a global debug-print configuration flag is enabled, logs the class and method name together with the arguments on entry and the return value on exit, while ``functools.wraps`` keeps the original metadata intact and the return value passes through unchanged. The wrapper inspects the owning class to detect static methods, so the implicit first argument is only omitted from the log for ordinary bound methods rather than stripped indiscriminately. A companion decorator factory builds on this by instrumenting whole classes at once: when a global boolean switch is turned on, it walks the class's attributes and replaces every plain function with its traced counterpart, whereas with the switch off the class is returned completely unmodified, so normal behaviour and performance are unaffected.

A separate decorator addresses the very deep recursion that the fuzzy description-logic algorithms can naturally produce: it catches ``RecursionError``, doubles the system recursion limit, and retries the call repeatedly until it succeeds, restoring the original limit in a ``finally`` block regardless of the outcome. Because the retry loop cannot distinguish legitimately deep recursion from infinite recursion, the limit is only allowed to grow up to a hard cap of 2^20, beyond which the error is re-raised to bound memory consumption and avoid crashing the interpreter. All diagnostic output from both mechanisms is funnelled through a shared debug utility, keeping log formatting consistent and making the reasoning process observable during development without changing program semantics.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.util.utils.FULL_CLASS_DEBUG_PRINT
   fuzzy_dl_owl2.fuzzydl.util.utils.RECURSION_LIMIT_CAP


Functions
---------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.util.utils.class_debugging
   fuzzy_dl_owl2.fuzzydl.util.utils.debugging_wrapper
   fuzzy_dl_owl2.fuzzydl.util.utils.recursion_unlimited


Module Contents
---------------

.. py:function:: class_debugging()

   This function serves as a decorator factory that generates a class-level decorator to instrument all instance methods with debugging capabilities. When applied to a class, it checks the global `FULL_CLASS_DEBUG_PRINT` flag; if this flag is true, the decorator iterates over the class's attributes to identify functions and replaces them with wrapped versions using `debugging_wrapper`. This mechanism enables automatic logging or tracing of method execution across the entire class, contingent on the global configuration state.

   :return: A class decorator that optionally instruments the methods of the class it is applied to.

   :rtype: typing.Callable


.. py:function:: debugging_wrapper(cls, func)

   This function creates a debugging wrapper for a class method, logging the entry and exit of the method call. It prints a formatted message before execution that includes the class and method names, along with the arguments passed to the function; notably, it excludes the first argument (typically `self` or `cls`) unless the method is detected as a static method. After the method completes, it logs a message containing the return value. The wrapper uses `functools.wraps` to preserve the original function's metadata and relies on the `Util.debug` utility for output.

   :param cls: The class containing the method being wrapped, used to access the class name and check if the method is static.
   :type cls: typing.Any
   :param func: The method or function to be wrapped with debug logging.
   :type func: typing.Any

   :return: The wrapped function, which logs entry/exit around ``func`` and returns its result unchanged.

   :rtype: typing.Callable


.. py:function:: recursion_unlimited(func: Callable)

   This decorator wraps a callable to automatically handle `RecursionError` exceptions by dynamically increasing the system recursion limit. Upon invocation, the wrapper attempts to execute the function; if a recursion depth error occurs, the limit is doubled and the execution is retried repeatedly until the function succeeds. The decorator modifies the global recursion limit during execution but ensures it is restored to its original value upon completion. Note that this mechanism does not prevent infinite recursion and may lead to high memory consumption or segmentation faults if the recursion depth is excessive.

   :param func: The callable to be wrapped that may raise a RecursionError; the wrapper will dynamically increase the recursion limit until the function succeeds.
   :type func: typing.Callable

   :return: The wrapped callable, which retries ``func`` while raising the recursion limit and always restores the original limit afterwards.

   :rtype: typing.Callable


.. py:data:: FULL_CLASS_DEBUG_PRINT
   :type:  bool
   :value: False


.. py:data:: RECURSION_LIMIT_CAP
   :type:  int
   :value: 1048576

