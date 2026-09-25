fuzzy_dl_owl2.fuzzydl.query.all_instances_query
===============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.all_instances_query



.. ── LLM-GENERATED DESCRIPTION START ──

A fuzzy description-logic query that finds every individual in a knowledge base belonging to a given abstract concept and reports the minimum degree to which each one satisfies it.


Description
-----------


``AllInstancesQuery`` extends the reasoner's generic query abstraction to answer questions of the form *which individuals are instances of concept C, and to what degree*. Because the underlying logic is fuzzy, membership is not binary: a degree of satisfaction is computed for every individual, and both the matching individuals and their degrees are stored on the query object and exposed through simple accessors so callers can inspect the results after solving. The constructor guards against misuse by rejecting concrete (data-range) concepts, since degrees of membership are only meaningful for abstract concepts, and it prepares a human-readable name that is progressively filled with the answers and later doubles as the query's string representation.

Two alternative solving strategies are offered. The straightforward one iterates over the knowledge base's individuals — skipping those that were dynamically created during reasoning — and delegates to a ``MinInstanceQuery`` for each, accumulating the resulting degree whenever the answer is consistent and aborting the loop as soon as an inconsistency surfaces. The second, more sophisticated strategy encodes the entire problem as a single mixed-integer linear program: it clones the knowledge base so the original remains untouched, introduces one semi-continuous variable per individual, adds assertions that tie each variable to the individual's membership in the concept, and maximises the sum of those variables in a single optimisation pass, afterwards mapping the variable values back to degrees. Both strategies first verify ABox consistency and return a dedicated inconsistent-knowledge-base solution rather than raising an exception, keeping error signalling uniform with the rest of the reasoning framework; during the optimisation step, MILP output flags are temporarily silenced and restored afterwards so solver logs stay clean without permanently altering global helper state.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.all_instances_query.AllInstancesQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_all_instances_query_AllInstancesQuery.png
       :alt: UML Class Diagram for AllInstancesQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **AllInstancesQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_all_instances_query_AllInstancesQuery.pdf
       :alt: UML Class Diagram for AllInstancesQuery
       :align: center
       :width: 8.9cm
       :class: uml-diagram

       UML Class Diagram for **AllInstancesQuery**

.. py:class:: AllInstancesQuery(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.all_instances_query.AllInstancesQuery
      :parts: 1
      :private-bases:


   This class represents a query designed to retrieve all individuals from a knowledge base that are instances of a specified concept, along with their respective degrees of membership. It supports fuzzy logic by determining the minimum degree to which each individual satisfies the concept, rather than relying on binary classification. To use this class, instantiate it with a target `Concept` object—ensuring the concept is not concrete—and invoke the `solve` method with a `KnowledgeBase` to perform the retrieval. The results can be accessed via the `get_individuals` and `get_degrees` methods, which return the list of matching entities and their calculated membership values.

   :param conc: The concept defining the criteria for retrieving instances and calculating membership degrees.
   :type conc: typing.Any
   :param degrees: Stores the membership degrees corresponding to the retrieved individuals, indicating the extent to which each satisfies the concept.
   :type degrees: list[float]
   :param individuals: The list of individuals from the knowledge base that are evaluated for membership in the concept.
   :type individuals: list[Individual]
   :param name: A string representation of the query that stores the formatted results, including individuals and their degrees, or an error message upon execution.
   :type name: typing.Any


   .. py:method:: __str__() -> str

      Returns the informal string representation of the query object, which is utilized by the built-in `str()` function and `print()` calls. This implementation simply delegates to the instance's `name` attribute, ensuring that the object is represented by its identifying name in user-facing contexts. Since it relies on the `name` attribute, it assumes that the attribute is defined and holds a value suitable for string representation.

      :return: The string representation of the object, which is its name.

      :rtype: str



   .. py:method:: get_degrees() -> list[float]

      Retrieves the collection of degree values stored within the query instance. This accessor returns the reference to the internal `degrees` attribute, which is a list of floating-point numbers. Note that because the list object is returned directly, modifications to the returned list will affect the internal state of the query object.

      :return: A list of floating-point numbers representing the degree values.

      :rtype: list[float]



   .. py:method:: get_individuals() -> list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]

      Retrieves the list of `Individual` objects stored in the `individuals` attribute of the query instance. This method serves as a direct accessor and does not modify the object's state or perform any calculations. Because it returns a reference to the internal list, any in-place modifications made to the returned list will be reflected in the query object's internal state.

      :return: The list of individuals stored in the instance.

      :rtype: list[Individual]



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the query for execution by performing necessary setup operations using the provided `KnowledgeBase`. This method typically involves validating the query parameters, resolving internal references, or optimizing the retrieval strategy based on the schema or data available in the knowledge base. It modifies the internal state of the query object in place and does not return a value.

      :param kb: The knowledge base object to be preprocessed or prepared for subsequent operations.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Executes the query to identify all individuals within the Knowledge Base that are instances of the specified concept. It begins by validating the consistency of the ABox, returning a specific solution if the ontology is found to be inconsistent. The method iterates through the individuals in the knowledge base, ignoring any that are dynamically created, and performs a minimum instance query for each to determine the degree of membership. As consistent results are found, they are appended to the internal list of degrees and formatted into the query's name string. If an inconsistency arises during the iteration, the loop terminates immediately, and the inconsistent solution is returned.

      :param kb: The knowledge base containing the ontology and individuals to be queried and solved.
      :type kb: KnowledgeBase

      :return: A Solution object representing the result of the operation. If the Knowledge Base is inconsistent, the solution indicates this error state; otherwise, it contains the result of the minimum instance query for the last individual processed.

      :rtype: Solution



   .. py:method:: solve_new(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Implements a specific algorithm to retrieve instances of the target concept by calculating the degree of membership for each individual in the provided knowledge base. The method operates on a clone of the input knowledge base to preserve the original state, first checking for consistency; if the ABox is inconsistent, it returns a solution indicating an inconsistent knowledge base. For each individual, excluding those that are dynamically created, it introduces a new semi-continuous variable into the MILP model and adds assertions that link the individual's relationship to the concept with this variable. It then constructs an objective function to maximize the sum of these variables and performs an optimization. As a side effect of this process, the method updates the instance's internal state by populating `self.degrees` with the calculated membership values and `self.name` with a descriptive string of the results, while temporarily toggling MILP helper flags for the optimization step.

      :param kb: The knowledge base containing the ontology and individuals to be analyzed. It is cloned internally to ensure the original object remains unmodified during the solving process.
      :type kb: KnowledgeBase

      :return: A Solution object containing the optimization results, including the degrees of membership for individuals regarding the target concept, or indicating an inconsistent knowledge base.

      :rtype: Solution



   .. py:attribute:: conc


   .. py:attribute:: degrees
      :type:  list[float]
      :value: []



   .. py:attribute:: individuals
      :type:  list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]
      :value: []



   .. py:attribute:: name
      :value: 'Instances of Uninferable?'


