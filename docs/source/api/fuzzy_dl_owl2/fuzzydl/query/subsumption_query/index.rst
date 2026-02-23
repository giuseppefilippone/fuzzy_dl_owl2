fuzzy_dl_owl2.fuzzydl.query.subsumption_query
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.subsumption_query



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class defines the structure for evaluating fuzzy subsumption relationships between two concepts.


Description
-----------


Designed to operate within a fuzzy description logic framework, the software establishes a foundational structure for determining the degree to which one concept is subsumed by another. By accepting a pair of concepts and a specific fuzzy implication operator, it prepares the necessary context for evaluating logical relationships where validity is measured on a spectrum rather than as a binary state. A critical design aspect involves strict validation during initialization to ensure that both the subsumed and the subsumer are abstract concepts, as concrete concepts are incompatible with this type of hierarchical query. Once validated, the components are stored alongside a placeholder for the objective expression, allowing concrete subclasses to perform the actual mathematical formulation of the subsumption degree.

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

