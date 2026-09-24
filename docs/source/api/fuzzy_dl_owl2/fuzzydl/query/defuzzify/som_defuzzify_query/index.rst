fuzzy_dl_owl2.fuzzydl.query.defuzzify.som_defuzzify_query
=========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.defuzzify.som_defuzzify_query





.. ── LLM-GENERATED DESCRIPTION START ──

Defines a defuzzification query that converts a fuzzy membership degree into a single crisp number using the Smallest of Maxima (SOM) strategy, which selects the smallest domain value at which an individual's membership in a concept reaches its peak.


Description
-----------


Within the fuzzy description logic framework, defuzzification is the step that translates graded membership into a concrete numeric output, and the SOM strategy accomplishes this by locating every domain point at which an individual's degree of membership in a concept is maximal and returning the smallest of those points. The ``SomDefuzzifyQuery`` class specialises the shared ``DefuzzifyQuery`` machinery for this particular strategy: it delegates storage of the concept, individual, and feature name to the superclass and contributes only the pieces that make SOM distinct from sibling strategies such as mean or largest of maxima. The most important of these pieces is the objective expression handed to the underlying MILP solver, which is nothing more than the feature variable itself with a unit coefficient, so the optimisation directly drives that variable and, under minimisation, settles on the smallest domain point compatible with the maximal-membership constraints built by the surrounding solver pipeline. Because the objective is so simple, nearly all of the strategy-specific reasoning lives in the constraint generation elsewhere in the framework, keeping the subclass minimal and uniform with its alternatives. A human-readable string representation names the strategy, the feature, and the instance, making the query easy to trace in solver logs and debugging output.

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
       :width: 11.2cm
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

