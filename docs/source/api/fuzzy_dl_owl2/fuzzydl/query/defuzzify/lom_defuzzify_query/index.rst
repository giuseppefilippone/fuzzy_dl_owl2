fuzzy_dl_owl2.fuzzydl.query.defuzzify.lom_defuzzify_query
=========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.defuzzify.lom_defuzzify_query



.. ── LLM-GENERATED DESCRIPTION START ──

Implements the Largest of Maxima defuzzification strategy to derive crisp numerical values from fuzzy membership functions by maximizing the target variable in an optimization context.


Description
-----------


The Largest of Maxima (LOM) approach is utilized to resolve fuzzy values into precise numbers by identifying the highest point within the plateau of maximum membership degrees. By extending the base defuzzification logic, the implementation accepts a specific concept, an individual entity, and a feature name to define the scope of the calculation. To facilitate this within a mixed-integer linear programming environment, the logic constructs an objective expression that mathematically represents the negation of the target variable. This formulation allows the underlying optimization solver to effectively maximize the variable value, thereby satisfying the criteria for selecting the largest maximum during the defuzzification process.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.defuzzify.lom_defuzzify_query.LomDefuzzifyQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_defuzzify_lom_defuzzify_query_LomDefuzzifyQuery.png
       :alt: UML Class Diagram for LomDefuzzifyQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **LomDefuzzifyQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_defuzzify_lom_defuzzify_query_LomDefuzzifyQuery.pdf
       :alt: UML Class Diagram for LomDefuzzifyQuery
       :align: center
       :width: 12.4cm
       :class: uml-diagram

       UML Class Diagram for **LomDefuzzifyQuery**

.. py:class:: LomDefuzzifyQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, feature_name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query.DefuzzifyQuery`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.defuzzify.lom_defuzzify_query.LomDefuzzifyQuery
      :parts: 1
      :private-bases:


   Represents a query that performs defuzzification using the Largest of Maxima (LOM) method to convert a fuzzy membership value into a crisp number. This approach is specifically designed to select the highest numerical value within the plateau where the degree of membership is maximized for a given feature. To use this class, instantiate it with a `Concept` providing the context, an `Individual` representing the entity being analyzed, and a string specifying the `feature_name` to be defuzzified. It functions within a broader fuzzy logic framework by generating objective expressions that facilitate the calculation of the desired crisp value.


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the defuzzification query, formatted to describe the specific operation being performed. The output identifies the method as "Largest of the maxima defuzzification" and incorporates the name of the feature and the instance identifier stored within the object. The resulting string is constructed as a prefix ending with an equals sign, suitable for logging or displaying the query context before the final result.

      :return: A string describing the largest of the maxima defuzzification for the specific feature and instance.

      :rtype: str



   .. py:method:: get_obj_expression(variable: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression

      Constructs an objective expression representing the negative of the specified variable by creating a Term with a coefficient of -1.0 associated with that variable and wrapping it within an Expression object. This is typically utilized within optimization contexts to formulate a minimization objective for the given variable. The method is stateless and does not modify the input variable or the instance's internal state.

      :param variable: The variable for which to generate the objective expression.
      :type variable: Variable

      :return: An Expression representing the negative of the specified variable.

      :rtype: Expression


