fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query
=====================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query





.. ── LLM-GENERATED DESCRIPTION START ──

An abstract query class that converts a fuzzy membership degree into a crisp value for a named feature of an individual, by first computing the individual's maximal degree of membership in a concept and then optimizing a MILP objective built from the feature's associated variable.


Description
-----------


``DefuzzifyQuery`` provides the shared skeleton for defuzzification inside a fuzzy description-logic reasoner: given a concept, an individual, and a feature name, it determines the crisp value that best represents the individual's fuzzy membership. The design is deliberately split so that all heavy lifting — solving a maximum-satisfiability problem, asserting results, and running the optimization — lives in the base class, while subclasses only supply the abstract objective-expression hook that encodes a particular defuzzification strategy (for example, maximizing or minimizing the feature value). This keeps the surrounding machinery in one place and makes it trivial to add new strategies without duplicating the workflow.

Execution is carefully isolated: the original knowledge base is cloned before any work begins, so assertions and intermediate results never leak into the caller's ontology. During preprocessing, a maximum-satisfiability query establishes the best degree to which the individual belongs to the target concept; that degree is asserted back into the clone, the assertions are resolved, and the individual's role relations are then traversed to locate the target individual linked through the feature, from which the corresponding Mixed-Integer Linear Programming variable is retrieved to build the objective expression. The final optimization runs against the cloned knowledge base, and any negative result is normalized to its absolute value before being returned.

Robustness is handled at two levels: an inconsistent ontology is caught through a dedicated exception and reported as a solution flagged as inconsistent, and a failure to derive an objective expression produces a warning and a null answer rather than a crash. Verbose MILP logging is suppressed during setup and only re-enabled for the final optimization, keeping intermediate reasoning quiet while still exposing the details of the decisive solve.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query.DefuzzifyQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_defuzzify_defuzzify_query_DefuzzifyQuery.png
       :alt: UML Class Diagram for DefuzzifyQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **DefuzzifyQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_defuzzify_defuzzify_query_DefuzzifyQuery.pdf
       :alt: UML Class Diagram for DefuzzifyQuery
       :align: center
       :width: 12.4cm
       :class: uml-diagram

       UML Class Diagram for **DefuzzifyQuery**

.. py:class:: DefuzzifyQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, feature_name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query.DefuzzifyQuery
      :parts: 1
      :private-bases:


   This abstract class defines the structure for performing defuzzification, which involves converting a fuzzy membership degree into a crisp value for a specific individual and feature within a knowledge base. During execution, it first determines the maximum degree of membership for the individual to the given concept and asserts this value into a cloned version of the knowledge base. It then identifies the variable associated with the specified feature and optimizes an objective expression derived from that variable to produce the final result. Subclasses are required to implement the abstract method for generating the objective expression, allowing for different defuzzification strategies to be applied. The process relies on Mixed-Integer Linear Programming (MILP) and handles potential inconsistencies in the ontology gracefully.

   :param conc: The concept for which the defuzzification operation is performed.
   :type conc: Concept
   :param a: The individual entity for which the defuzzification query is being executed.
   :type a: Individual
   :param f_name: The name of the feature for which to perform defuzzification.
   :type f_name: str
   :param obj_expr: The objective expression used to optimize the solution, representing the degree of membership of the individual to the concept.
   :type obj_expr: Expression


   .. py:method:: get_obj_expression(variable: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression
      :abstractmethod:


      Retrieves the objective expression associated with the specified variable for the defuzzification process. This abstract method requires subclasses to implement the logic for constructing the expression, which typically represents the target function or calculation needed to resolve the fuzzy variable into a crisp value. The implementation determines how the variable's properties are translated into a formal expression used by the query engine.

      :param variable: The variable instance for which the corresponding object expression is to be retrieved.
      :type variable: Variable

      :return: The expression representing the object associated with the provided variable.

      :rtype: Expression



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the defuzzification query by solving a maximum satisfiability problem to determine the optimal degree for the conclusion associated with the current individual. If a consistent solution is found, the method updates the internal reference to the individual, asserts the calculated numeric degree back into the knowledge base, and resolves these assertions. Furthermore, it inspects the individual's role relations to identify a specific target individual, retrieving the corresponding MILP variable to construct and store an objective expression for later use.

      :param kb: The knowledge base instance used to solve queries, retrieve individuals, and manage assertions and MILP variables. This object is modified during the preprocessing step.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> Optional[fuzzy_dl_owl2.fuzzydl.milp.solution.Solution]

      Attempts to solve the defuzzification problem by first resolving the ABox of the provided Knowledge Base and then operating on a cloned instance to preserve the original state. The method applies preprocessing to the clone and, if an objective expression is defined, performs an optimization to find a solution. If the resulting solution value is negative, it is converted to its absolute value before being returned. If no objective expression is available, the method issues a warning and returns None. Furthermore, it handles inconsistent ontologies by catching the specific exception and returning a Solution object marked as inconsistent.

      :param kb: The knowledge base containing the ontology and ABox to be solved and optimized.
      :type kb: KnowledgeBase

      :return: A Solution object representing the optimization result, or None if the objective expression is missing or a defuzzification problem occurs. Returns a specific Solution indicating inconsistency if the ontology is inconsistent.

      :rtype: typing.Optional[Solution]



   .. py:attribute:: a
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: conc
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: f_name
      :type:  str


   .. py:attribute:: obj_expr
      :type:  fuzzy_dl_owl2.fuzzydl.milp.expression.Expression
      :value: None

