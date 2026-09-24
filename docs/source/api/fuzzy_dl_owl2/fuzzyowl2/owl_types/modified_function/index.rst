fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_function
===================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_function





.. ── LLM-GENERATED DESCRIPTION START ──

Defines a ``ModifiedFunction`` fuzzy datatype that pairs a linguistic modifier with a base datatype to express hedged fuzzy concepts such as "very tall" within the FuzzyOWL2 framework.


Description
-----------


In fuzzy ontology modelling, linguistic hedges like "very" or "somewhat" reshape the membership function of an underlying fuzzy concept, and capturing that pairing is the sole purpose here: the modifier's name and the identifier of the datatype it alters are stored as the object's entire state. Because the class derives from ``FuzzyDatatype``, an instance can be treated polymorphically anywhere the framework expects a generic fuzzy datatype, while still carrying the extra modifier information that distinguishes it from plain datatypes. Both values are held in private attributes and exposed only through getter methods, leaving the object effectively immutable after construction and consistent with the encapsulation conventions used throughout the surrounding owl_types package. The constructor performs no validation — whatever is passed in is stored as-is — so semantic correctness is deferred to the layers that actually interpret the ontology. A string representation formatted as ``modified(modifier, datatype)`` rounds out the behaviour, making instances easy to print, log, or embed in textual output while keeping the modifier–datatype relationship immediately visible.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_function.ModifiedFunction


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_modified_function_ModifiedFunction.png
       :alt: UML Class Diagram for ModifiedFunction
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ModifiedFunction**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_modified_function_ModifiedFunction.pdf
       :alt: UML Class Diagram for ModifiedFunction
       :align: center
       :width: 7.2cm
       :class: uml-diagram

       UML Class Diagram for **ModifiedFunction**

.. py:class:: ModifiedFunction(mod: str, d: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype.FuzzyDatatype`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_function.ModifiedFunction
      :parts: 1
      :private-bases:


   This class models a modified function within the FuzzyOWL2 framework, representing a fuzzy datatype that has been transformed by a specific linguistic modifier. It extends the base fuzzy datatype functionality by associating a standard datatype with a modifier string, allowing for the representation of nuanced fuzzy concepts where a base property is altered by terms such as "very" or "somewhat." To utilize this class, instantiate it with the desired modifier and the name of the target datatype; the resulting object provides access to these components through getter methods and generates a string representation formatted as a parenthesized pair.

   :param _mod: The fuzzy modifier or linguistic hedge applied to the underlying datatype.
   :type _mod: str
   :param _d: The name of the datatype to which the fuzzy modifier is applied.
   :type _d: str


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the object, formatted as a parenthesized tuple containing the internal modifier and data attributes separated by a space. This method is invoked implicitly by the `str()` built-in function and the `print` statement, providing a concise summary of the object's state without modifying it. The output depends entirely on the string conversion of the underlying `_mod` and `_d` attributes, meaning any exceptions raised during their stringification will propagate to this call.

      :return: A string representation of the object, formatted as 'modified(_mod, _d)'.

      :rtype: str



   .. py:method:: get_d() -> str

      Retrieves the value of the internal attribute `_d` stored within the instance. This method serves as an accessor to expose the encapsulated data without modifying the object's state. It returns the value as a string, though an `AttributeError` will be raised if the attribute has not been initialized.

      :return: The value of the _d attribute.

      :rtype: str



   .. py:method:: get_mod() -> str

      Retrieves the value of the internal `_mod` attribute, which represents the modification context or module name associated with the function instance. This method serves as a simple accessor, returning the stored string without modifying the object's state. If the underlying attribute has not been initialized, an `AttributeError` will be raised.

      :return: The current value of the `_mod` attribute.

      :rtype: str



   .. py:attribute:: _d
      :type:  str


   .. py:attribute:: _mod
      :type:  str
