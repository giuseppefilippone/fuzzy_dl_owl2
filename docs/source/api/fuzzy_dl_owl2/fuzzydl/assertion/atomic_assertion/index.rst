fuzzy_dl_owl2.fuzzydl.assertion.atomic_assertion
================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.assertion.atomic_assertion



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a data structure for representing atomic assertions within a fuzzy description logic system by associating a concept with a minimum membership degree.


Description
-----------


Software components within a fuzzy description logic system rely on this structure to model fundamental constraints where a specific concept must satisfy a minimum membership threshold. By associating a *Concept* instance with a *Degree* object, the implementation encapsulates the logical relationship between an entity and its required truth value. Accessor methods are provided to retrieve the concept's identifier and the specific degree value, enabling the evaluation of logical rules or constraints. Additionally, a string representation is generated to visualize the assertion in a human-readable format, displaying the concept and the associated degree enclosed in angle brackets.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.assertion.atomic_assertion.AtomicAssertion


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_assertion_atomic_assertion_AtomicAssertion.png
       :alt: UML Class Diagram for AtomicAssertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **AtomicAssertion**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_assertion_atomic_assertion_AtomicAssertion.pdf
       :alt: UML Class Diagram for AtomicAssertion
       :align: center
       :width: 9.2cm
       :class: uml-diagram

       UML Class Diagram for **AtomicAssertion**

.. py:class:: AtomicAssertion(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree)

   This class models a fundamental logical constraint within a fuzzy logic framework, specifically asserting that a specific atomic concept must meet or exceed a defined threshold of membership. It encapsulates a relationship between a concept and a degree, representing the condition where the concept's membership is greater than or equal to the specified value. To utilize this class, instantiate it with a `Concept` object representing the subject and a `Degree` object representing the required lower bound. The object stores these components and provides methods to retrieve the concept's name and the specific degree value, as well as a string representation of the assertion.

   :param c: The atomic concept whose membership degree is evaluated against the assertion's lower bound.
   :type c: Concept
   :param degree: The lower bound degree threshold that the atomic concept's membership must meet or exceed for the assertion to be satisfied.
   :type degree: Degree


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the assertion, formatted with angle brackets that enclose the values of the 'c' and 'degree' attributes. This method is designed for display and logging purposes, providing a concise snapshot of the object's current state without causing any side effects.

      :return: A string representation of the object, displaying the values of `c` and `degree` enclosed in angle brackets.

      :rtype: str



   .. py:method:: get_concept_name() -> str

      Retrieves the name of the concept associated with this atomic assertion by accessing the internal attribute `c` and converting it to a string. This method ensures that the concept identifier is returned as a string, regardless of the original type of the stored attribute. It is a read-only operation that does not modify the state of the object.

      :return: The concept name as a string.

      :rtype: str



   .. py:method:: get_degree() -> fuzzy_dl_owl2.fuzzydl.degree.degree.Degree

      Retrieves the degree value associated with this atomic assertion. This method acts as a simple accessor for the internal `degree` attribute, returning the stored instance of the `Degree` type. As it only reads an existing attribute, the operation has no side effects and does not alter the state of the object.

      :return: The degree associated with the object.

      :rtype: Degree



   .. py:attribute:: c
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: degree
      :type:  fuzzy_dl_owl2.fuzzydl.degree.degree.Degree

