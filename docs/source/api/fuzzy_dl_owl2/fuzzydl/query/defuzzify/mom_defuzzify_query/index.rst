fuzzy_dl_owl2.fuzzydl.query.defuzzify.mom_defuzzify_query
=========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.defuzzify.mom_defuzzify_query



.. ── LLM-GENERATED DESCRIPTION START ──

Implements the Mean of Maxima defuzzification strategy to calculate a crisp feature value for an individual within a fuzzy ontology.


Description
-----------


The process begins by determining the maximum degree of membership the individual has to a specified concept, effectively identifying the height of the fuzzy set. Once this peak degree is established, the system constrains the problem to the region where this maximum membership holds and performs optimization to locate the minimum and maximum boundaries of the target feature within that plateau. The final crisp result is computed as the arithmetic mean of these two boundary values, providing a representative value for the feature. This method integrates with mixed-integer linear programming solvers to navigate the feasible region and handles potential inconsistencies or missing data by returning specific error states or warnings.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.defuzzify.mom_defuzzify_query.MomDefuzzifyQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_defuzzify_mom_defuzzify_query_MomDefuzzifyQuery.png
       :alt: UML Class Diagram for MomDefuzzifyQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **MomDefuzzifyQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_defuzzify_mom_defuzzify_query_MomDefuzzifyQuery.pdf
       :alt: UML Class Diagram for MomDefuzzifyQuery
       :align: center
       :width: 12.4cm
       :class: uml-diagram

       UML Class Diagram for **MomDefuzzifyQuery**

.. py:class:: MomDefuzzifyQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, feature_name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query.DefuzzifyQuery`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.defuzzify.mom_defuzzify_query.MomDefuzzifyQuery
      :parts: 1
      :private-bases:


   This class implements a defuzzification strategy that calculates the crisp value of a specific feature for an individual based on the "middle of maxima" principle within a fuzzy ontology framework. To determine the result, it first establishes the maximum degree of membership the individual has to a given concept. It then performs optimization to find the smallest and largest feature values that satisfy this maximum membership degree, effectively identifying the boundaries of the membership plateau. The final output is the arithmetic mean of these two boundary values. Users should instantiate this class with a target concept, an individual, and a feature name, then invoke the solve method with a knowledge base to retrieve the calculated solution.


   .. py:method:: __str__() -> str

      Provides a human-readable string representation of the Middle of Maxima (MoM) defuzzification query object. The returned string formats a description that includes the specific feature name and instance identifier associated with the query, ending with an equals sign to facilitate the display of the resulting value. This method relies on the existence of the `f_name` and `a` attributes; accessing this string representation will raise an AttributeError if these attributes are not defined on the instance.

      :return: Returns a string describing the middle of the maxima defuzzification calculation for the specific feature and instance.

      :rtype: str



   .. py:method:: get_obj_expression(variable: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression

      Returns a placeholder objective expression for the provided variable. This method is currently not utilized within the defuzzification logic and serves as a stub implementation. It constructs and returns an Expression object containing a single Term with a coefficient of -1.0, regardless of the input variable's state.

      :param variable: The variable object to be used in constructing the expression.
      :type variable: Variable

      :return: An Expression object representing the negative of the provided variable.

      :rtype: Expression



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the internal state of the query object for the Mean of Maxima (MoM) defuzzification process by interacting with the provided KnowledgeBase. This method retrieves and validates the configuration of the target output variable, ensuring that the necessary fuzzy sets and universe of discourse are available for calculation. As a side effect, it updates the instance attributes to store intermediate results or references required for the subsequent defuzzification step, potentially raising an error if the specified variable cannot be found in the KnowledgeBase or is improperly configured.

      :param kb: The knowledge base object to be preprocessed.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Executes a Mean of Maxima (MOM) defuzzification strategy to derive a crisp numerical value from a fuzzy knowledge base. The method begins by solving the ABox of the input knowledge base and determining the maximum degree of membership for the target concept and individual via a max-satisfiability query. It then creates a modified clone of the knowledge base where the individual is asserted to possess the concept at this maximum degree, subsequently identifying the MILP variable associated with the specified role relation. The solution is calculated by optimizing this variable to find both the minimum and maximum values within the feasible region and returning their average. Edge cases include returning an inconsistent solution if the ontology cannot be solved or if optimization fails, and returning None with a warning if the required role relations or variables are absent. The method has side effects of solving the ABox of the input knowledge base and printing warnings or stack traces to standard output upon encountering errors.

      :param kb: The input knowledge base containing the ontology, individuals, and assertions used to perform the reasoning and optimization tasks.
      :type kb: KnowledgeBase

      :return: A Solution object containing the calculated numeric value (Mean of Maximums) derived from fuzzy logic optimization, or None if defuzzification fails. The Solution may also indicate an inconsistent knowledge base.

      :rtype: Solution


