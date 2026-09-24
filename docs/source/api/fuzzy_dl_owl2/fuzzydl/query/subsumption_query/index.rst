fuzzy_dl_owl2.fuzzydl.query.subsumption_query
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.subsumption_query







.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class for fuzzy subsumption queries, capturing the pair of concepts whose containment relationship is to be evaluated along with the fuzzy implication operator used to grade it.


Description
-----------


Subsumption in fuzzy description logics is a matter of degree rather than a simple yes-or-no question, so a query must record not only the subsumed and subsumer concepts but also the specific fuzzy implication chosen to interpret the containment. **SubsumptionQuery** acts as the shared foundation for all such queries: it inherits from the generic ``Query`` abstraction and remains abstract itself, deliberately leaving the construction of the actual optimization problem to concrete subclasses. During construction it enforces a key semantic restriction — neither concept may be concrete, since subsumption is only well-defined between abstract concepts — and reports any violation through the central error-handling utility. Once validation passes, the two concepts, the implication operator type, and a placeholder for the objective expression are stored as instance state; that objective expression, initially unset, is expected to be populated by subclasses with a linear expression encoding the computed degree of subsumption within the mixed-integer linear programming framework that drives the reasoning engine.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.subsumption_query.SubsumptionQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_subsumption_query_SubsumptionQuery.png
       :alt: UML Class Diagram for SubsumptionQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **SubsumptionQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_subsumption_query_SubsumptionQuery.pdf
       :alt: UML Class Diagram for SubsumptionQuery
       :align: center
       :width: 14.1cm
       :class: uml-diagram

       UML Class Diagram for **SubsumptionQuery**

.. py:class:: SubsumptionQuery(c1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, s_type: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.subsumption_query.SubsumptionQuery
      :parts: 1
      :private-bases:


   This abstract base class provides a structured interface for performing subsumption queries, specifically designed to evaluate the degree to which one concept is subsumed by another using fuzzy logic implications. Upon initialization, it accepts a subsumed concept, a subsumer concept, and a logic operator type defining the specific implication method to be used. A critical validation step ensures that neither concept is concrete, as subsumption queries are restricted to abstract concepts. The class prepares an objective expression attribute to hold the calculated degree of subsumption, which is typically populated by concrete subclasses.

   :param c1: The concept being subsumed, which must not be a concrete concept.
   :type c1: Concept
   :param c2: The concept acting as the subsumer in the subsumption relationship.
   :type c2: Concept
   :param type: The fuzzy implication operator used to evaluate the subsumption relationship.
   :type type: LogicOperatorType
   :param obj_expr: The objective expression representing the degree of subsumption.
   :type obj_expr: Expression


   .. py:attribute:: c1
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: c2
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: obj_expr
      :type:  fuzzy_dl_owl2.fuzzydl.milp.expression.Expression
      :value: None



   .. py:attribute:: type
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType