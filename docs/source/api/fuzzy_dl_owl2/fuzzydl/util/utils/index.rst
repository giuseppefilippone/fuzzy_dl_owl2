fuzzy_dl_owl2.fuzzydl.util.utils
================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.util.utils



.. ── LLM-GENERATED DESCRIPTION START ──

Utility decorators provide debugging instrumentation and automatic recursion limit adjustment for Python classes and functions.


Description
-----------


A debugging mechanism wraps methods to log entry and exit details, including arguments and return values, while intelligently distinguishing between static and instance methods to format output correctly. This instrumentation is applied via a class-level decorator that conditionally activates based on a global flag, allowing developers to trace execution flow across entire classes without modifying individual method definitions. Furthermore, a recursion management decorator intercepts stack overflow errors by dynamically increasing the system recursion limit and retrying execution until success, ensuring that deep recursive algorithms can run to completion while preserving the original system limits afterward.

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

