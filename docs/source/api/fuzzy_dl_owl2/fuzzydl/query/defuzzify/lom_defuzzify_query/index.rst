fuzzy_dl_owl2.fuzzydl.query.defuzzify.lom_defuzzify_query
=========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.defuzzify.lom_defuzzify_query







.. ── LLM-GENERATED DESCRIPTION START ──

A defuzzification query that applies the Largest of Maxima (LOM) method, converting a fuzzy membership value into a crisp number by selecting the largest value at which the degree of membership is maximized.


Description
-----------


The central class, **LomDefuzzifyQuery**, specializes the shared defuzzification machinery for the Largest of Maxima strategy: when a fuzzy concept's membership function plateaus at its maximum degree over a range of values, LOM resolves the ambiguity by picking the highest value in that plateau rather than an arbitrary or central one. An instance is created from a fuzzy Concept providing the context, an Individual representing the entity under analysis, and the name of the feature to be defuzzified, with all common setup delegated to the parent DefuzzifyQuery so that behaviour remains consistent with the other defuzzification variants offered by the framework. The essential design decision lies in the objective expression handed to the underlying MILP solver: by negating the decision variable, the solver is driven to maximise the feature's value while the constraints generated elsewhere in the framework pin the membership degree to its maximum, which is precisely the condition that produces the largest of the maxima. A human-readable string representation is also provided, labelling the operation with the feature and instance names and ending in an equals sign, so that the computed crisp value can be appended directly for logging or display. In this way the class plugs into the broader fuzzy description-logic reasoning framework as one interchangeable strategy for answering queries of the form "what is the largest value at which a given individual maximally satisfies a concept on a given feature?"

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
