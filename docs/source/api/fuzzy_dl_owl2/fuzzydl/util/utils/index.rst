fuzzy_dl_owl2.fuzzydl.util.utils
================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.util.utils


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

   Decorator to wrap all methods of a class using debugging_wrapper.


.. py:function:: debugging_wrapper(cls, func)

   Debugging wrapper that prints before and after the method call.


.. py:function:: recursion_unlimited(func: Callable)

.. py:data:: FULL_CLASS_DEBUG_PRINT
   :type:  bool
   :value: False


