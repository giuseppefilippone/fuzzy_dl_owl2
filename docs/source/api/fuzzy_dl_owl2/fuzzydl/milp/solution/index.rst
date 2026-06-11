fuzzy_dl_owl2.fuzzydl.milp.solution
===================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.milp.solution



.. ── LLM-GENERATED DESCRIPTION START ──

A data container encapsulates the outcome of a query on a fuzzy knowledge base, distinguishing between a numerical degree of satisfaction and the logical consistency status of the base.


Description
-----------


The software defines a structure to represent the results of queries executed against a fuzzy knowledge base, specifically handling the dual nature of outcomes where the base might be consistent or inconsistent. When the knowledge base is consistent, the object stores a numerical value representing the degree of satisfaction for the query, whereas an inconsistent state is flagged explicitly to indicate logical failure. To support detailed analysis, the implementation maintains a collection of variable bindings that map specific names to their calculated values, allowing users to inspect the internal state of the solution. Type safety and initialization flexibility are achieved through method overloading, ensuring that the object can be constructed either with a boolean status or a floating-point result while enforcing strict input validation. Furthermore, the design includes standard object representations and hashing capabilities to facilitate debugging and usage within collection data structures.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.solution.Solution


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_milp_solution_Solution.png
       :alt: UML Class Diagram for Solution
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **Solution**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_milp_solution_Solution.pdf
       :alt: UML Class Diagram for Solution
       :align: center
       :width: 11.5cm
       :class: uml-diagram

       UML Class Diagram for **Solution**

.. py:class:: Solution(consistent: bool)
              Solution(sol: float)

   This class encapsulates the outcome of a query performed on a fuzzy knowledge base, distinguishing between a numerical degree of satisfaction and the consistency status of the base itself. When initialized with a floating-point number, it represents a valid query result where the knowledge base is consistent, storing the satisfaction value and allowing the retrieval of specific variable bindings. Alternatively, it can be instantiated with a boolean flag to explicitly represent an inconsistent knowledge base, in which case the satisfaction value is disregarded. Users can access the consistency status, the numerical solution, and any associated variable values through dedicated accessor methods, while the string representation provides a human-readable summary of the result.

   :param CONSISTENT_KB: Constant indicating a consistent fuzzy Knowledge Base.
   :type CONSISTENT_KB: bool
   :param INCONSISTENT_KB: Constant flag indicating an inconsistent fuzzy Knowledge Base, used to initialize a solution object.
   :type INCONSISTENT_KB: bool

   :raises ValueError: Raised if the argument provided to the constructor is neither a boolean nor a numeric type.


   .. py:method:: __hash__() -> int

      Calculates the hash value for the instance by hashing its string representation, enabling the object to be used as a key in dictionaries or as an element in sets. This implementation relies on the `__str__` method to determine the object's identity for hashing purposes. It is important to note that if the object is mutable and its string representation changes after it has been added to a hash-based collection, the hash value will change, potentially causing the object to become lost or inaccessible within that collection.

      :return: An integer hash value derived from the string representation of the object.

      :rtype: int



   .. py:method:: __repr__() -> str

      Returns the official string representation of the object, which is primarily intended for debugging and developer feedback. This implementation delegates directly to the informal string conversion logic, meaning the output is identical to the result of calling `str()` on the instance. Consequently, the returned string may not strictly adhere to the convention of being a valid Python expression that can be used to recreate the object.

      :return: The string representation of the object.

      :rtype: str



   .. py:method:: __solution_init_1(consistent: bool) -> None

      Initializes the core state attributes for a solution instance, setting the numerical solution value (`sol`) to a default float of 0.0 and assigning the provided boolean consistency status to the `consistent` attribute. Additionally, it creates an empty dictionary to store variable values (`showed_variables`). This method effectively resets or establishes the initial state of these specific instance variables, overwriting any pre-existing data.

      :param consistent: Indicates whether the fuzzy knowledge base is consistent.
      :type consistent: bool



   .. py:method:: __solution_init_2(sol: float) -> None

      Initializes the internal state of the solution object by setting the numerical solution value, establishing the consistency of the fuzzy knowledge base, and preparing a container for displayed variables. It assigns the provided numerical value to the solution attribute, defaults the consistency flag to true, and creates an empty dictionary to track the values of variables that have been shown. This method serves as a secondary initialization routine to reset or configure the object's state before further operations.

      :param sol: Numerical value of the solution.
      :type sol: float



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the solution object, which varies based on the consistency of the underlying knowledge base. If the solution is consistent, the method returns the string representation of the solution itself; otherwise, it returns a message indicating that the knowledge base is inconsistent.

      :return: Returns the string representation of the solution if the knowledge base is consistent, or 'Inconsistent KB' otherwise.

      :rtype: str



   .. py:method:: add_showed_variable(var_name: str, value: float) -> None

      Updates the internal collection of variables designated for display by associating a specific name with a floating-point value. This method modifies the instance's `showed_variables` dictionary in place, adding a new entry if the name does not exist or overwriting the existing value if it does. It is typically used to record metrics or parameters that need to be tracked or visualized later in the solution process.

      :param var_name: The name of the showed variable to set.
      :type var_name: str
      :param value: Numeric content to assign to the showed variable.
      :type value: float



   .. py:method:: get_showed_variables() -> dict[str, float]

      Returns a dictionary containing the values of variables that were highlighted or determined during the query resolution process. This method is intended to be used after a query has been successfully solved over a consistent Knowledge Base. The keys of the dictionary are variable names, and the values are their corresponding floating-point representations. Note that this method returns a direct reference to the internal dictionary, so modifying the returned object will affect the state of the Solution instance.

      :return: A dictionary mapping variable names to their float values, representing the variables resulting from a solved query over a consistent knowledge base.

      :rtype: dict[str, float]



   .. py:method:: get_solution() -> Union[bool, float]

      Retrieves the solution stored within the instance, which represents the outcome of a query over a consistent knowledge base. The returned value can be either a boolean, indicating satisfiability or truth, or a float, representing a numerical metric such as a probability or cost. This method acts as a simple accessor and does not perform any computation or modify the object's state.

      :return: The solution to the query, returned as either a boolean (True/False) or a float (e.g., a probability or confidence score).

      :rtype: typing.Union[bool, float]



   .. py:method:: is_consistent_kb() -> bool

      Returns a boolean flag indicating the consistency status of the original Knowledge Base (KB). This method acts as a direct accessor to the internal `consistent` attribute, reflecting whether the KB was found to be logically sound during prior processing. It does not perform any new computations or modify the object's state.

      :return: True if the original Knowledge Base is consistent, False otherwise.

      :rtype: bool



   .. py:attribute:: CONSISTENT_KB
      :type:  bool
      :value: True



   .. py:attribute:: INCONSISTENT_KB
      :type:  bool
      :value: False


