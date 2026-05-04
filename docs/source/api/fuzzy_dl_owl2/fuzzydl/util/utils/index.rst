fuzzy_dl_owl2.fuzzydl.util.utils
================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.util.utils



.. ── LLM-GENERATED DESCRIPTION START ──

Utility decorators are provided to facilitate debugging through method tracing and to manage deep recursion by dynamically adjusting system limits.


Description
-----------


The debugging infrastructure includes a wrapper that logs method entry and exit details, such as arguments and return values, while intelligently distinguishing between static and instance methods to ensure accurate context reporting. A class-level decorator automates this instrumentation by iterating through class attributes and applying the wrapper to all functions, controlled by a global flag that enables or disables the verbose logging. Furthermore, a recursion handling mechanism intercepts stack overflow errors to progressively double the recursion limit until the operation succeeds, thereby preventing premature termination of complex logical computations while restoring the original limit upon completion.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.util.utils.FULL_CLASS_DEBUG_PRINT


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


.. py:function:: debugging_wrapper(cls, func)

   This function creates a debugging wrapper for a class method, logging the entry and exit of the method call. It prints a formatted message before execution that includes the class and method names, along with the arguments passed to the function; notably, it excludes the first argument (typically `self` or `cls`) unless the method is detected as a static method. After the method completes, it logs a message containing the return value. The wrapper uses `functools.wraps` to preserve the original function's metadata and relies on the `Util.debug` utility for output.

   :param cls: The class containing the method being wrapped, used to access the class name and check if the method is static.
   :type cls: typing.Any
   :param func: The method or function to be wrapped with debug logging.
   :type func: typing.Any


.. py:function:: recursion_unlimited(func: Callable)

   This decorator wraps a callable to automatically handle `RecursionError` exceptions by dynamically increasing the system recursion limit. Upon invocation, the wrapper attempts to execute the function; if a recursion depth error occurs, the limit is doubled and the execution is retried repeatedly until the function succeeds. The decorator modifies the global recursion limit during execution but ensures it is restored to its original value upon completion. Note that this mechanism does not prevent infinite recursion and may lead to high memory consumption or segmentation faults if the recursion depth is excessive.

   :param func: The callable to be wrapped that may raise a RecursionError; the wrapper will dynamically increase the recursion limit until the function succeeds.
   :type func: typing.Callable


.. py:data:: FULL_CLASS_DEBUG_PRINT
   :type:  bool
   :value: False

