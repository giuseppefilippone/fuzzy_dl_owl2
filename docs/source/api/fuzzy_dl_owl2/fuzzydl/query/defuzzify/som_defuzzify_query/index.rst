fuzzy_dl_owl2.fuzzydl.query.defuzzify.som_defuzzify_query
=========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.defuzzify.som_defuzzify_query



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized query implementation applies the Smallest of Maxima strategy to convert fuzzy logic values into crisp numerical outputs.


Description
-----------


By identifying domain values that correspond to the highest degree of membership for a specific individual within a given concept, the logic selects the smallest value among those maxima. Extending a base defuzzification handler allows the component to inherit standard initialization parameters, such as the target concept, individual instance, and feature name, while defining unique behavior for the optimization process. The objective function is constructed to minimize a specific variable, ensuring that the mathematical solver identifies the lower bound of the maximized membership set.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.defuzzify.som_defuzzify_query.SomDefuzzifyQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_defuzzify_som_defuzzify_query_SomDefuzzifyQuery.png
       :alt: UML Class Diagram for SomDefuzzifyQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **SomDefuzzifyQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_defuzzify_som_defuzzify_query_SomDefuzzifyQuery.pdf
       :alt: UML Class Diagram for SomDefuzzifyQuery
       :align: center
       :width: 12.4cm
       :class: uml-diagram

       UML Class Diagram for **SomDefuzzifyQuery**

.. py:class:: SomDefuzzifyQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, f_name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query.DefuzzifyQuery`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.defuzzify.som_defuzzify_query.SomDefuzzifyQuery
      :parts: 1
      :private-bases:


   This class implements the Smallest of Maxima (SOM) defuzzification strategy, a method used to convert fuzzy logic values into crisp, numerical outputs. It operates by identifying the domain values that correspond to the highest degree of membership for a specific individual within a given concept and selecting the smallest among those maxima. The query is constructed using a target concept, an individual instance, and a feature name, which define the scope of the fuzzy evaluation. As a subclass of `DefuzzifyQuery`, it provides a specific implementation for resolving feature values based on the SOM algorithm within a larger fuzzy logic framework.


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the defuzzification query, specifically formatted to describe a "Smallest of the maxima" operation. The string dynamically includes the feature name and instance identifier stored in the object, providing context for the specific calculation being represented. This method is primarily used for logging or display purposes, outputting a descriptive label that concludes with an equals sign.

      :return: A string representation describing the smallest of the maxima defuzzification for the specific feature and instance.

      :rtype: str



   .. py:method:: get_obj_expression(q: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression

      Constructs a linear expression representing the provided variable with a coefficient of 1.0. The method encapsulates the variable within a Term object assigned a unit weight and wraps it in an Expression structure, effectively creating a mathematical representation of the variable itself. This function is stateless and produces no side effects on the instance or the input variable, though it assumes the input is a valid Variable object to prevent errors during Term instantiation.

      :param q: The variable used to construct the objective expression.
      :type q: Variable

      :return: An Expression object representing the variable `q` with a coefficient of 1.0.

      :rtype: Expression


