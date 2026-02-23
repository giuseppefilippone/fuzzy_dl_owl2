fuzzy_dl_owl2.fuzzydl.relation
==============================

.. py:module:: fuzzy_dl_owl2.fuzzydl.relation



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a data structure for representing fuzzy role assertions that link two individuals through a named relationship constrained by a lower bound degree.


Description
-----------


The software models a specific type of logical assertion used in fuzzy description logics, where a relationship exists between a subject and an object entity. It encapsulates the properties of this connection, including the name of the role, the two distinct individuals involved, and a degree value that acts as a lower bound for the truth of the assertion. Design choices include allowing the modification of the participating individuals after instantiation, which provides flexibility for dynamic updates within a larger reasoning system. String representations are provided to visualize the relationship both with and without the degree constraint, facilitating debugging and logging. The implementation also supports cloning to create independent copies of the assertion, ensuring that modifications to a copy do not affect the original instance.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.relation.Relation


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_relation_Relation.png
       :alt: UML Class Diagram for Relation
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **Relation**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_relation_Relation.pdf
       :alt: UML Class Diagram for Relation
       :align: center
       :width: 14.8cm
       :class: uml-diagram

       UML Class Diagram for **Relation**

.. py:class:: Relation(role_name: str, ind1: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, ind2: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree)

   This class models a role assertion connecting a subject individual to an object individual via a specific role, constrained by a lower bound degree. It serves as a container for the relationship's properties, storing the role name, the two involved individuals, and the minimum degree required for the assertion to hold. Users can instantiate this object to define such relationships, modify the subject or object individuals after creation, and retrieve string representations that include or exclude the degree constraint. Additionally, the class supports cloning to create independent copies of the assertion.

   :param role_name: The name identifying the specific role or relationship type asserted between the subject and object individuals.
   :type role_name: str
   :param ind_a: The subject individual of the role assertion.
   :type ind_a: Individual
   :param ind_b: The object individual of the role assertion.
   :type ind_b: Individual
   :param degree: The lower bound value for the role assertion.
   :type degree: Degree


   .. py:method:: __repr__() -> str

      Returns the official string representation of the instance by delegating to the object's informal string conversion method. This ensures that the output displayed in interactive sessions or logs is identical to the result of calling `str()` on the object. Since it relies on the underlying string conversion logic, any exceptions raised during that process will propagate through this method.

      :return: The string representation of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the relation, formatted as 'name >= degree'. The name component is retrieved by calling `get_name_without_degree`, while the degree component is taken directly from the object's degree attribute. This method is automatically invoked by the `str()` built-in function and the `print` statement to provide a concise summary of the relation's constraint.

      :return: A string representation of the object in the format "name >= degree".

      :rtype: str



   .. py:method:: clone() -> Self

      Creates and returns a distinct copy of the current Relation instance. This method instantiates a new Relation object using the current values of role_name, ind_a, ind_b, and degree, ensuring that the original object remains unmodified. The returned object is a separate entity, though it shares the same attribute values as the source at the moment of cloning.

      :return: A new instance of the class with identical attributes to the current object.

      :rtype: typing.Self



   .. py:method:: get_degree() -> fuzzy_dl_owl2.fuzzydl.degree.degree.Degree

      Retrieves the degree associated with this relation instance. This method serves as an accessor for the internal `degree` attribute, returning the stored `Degree` object. It performs no modifications to the object's state and has no side effects.

      :return: The degree associated with the instance.

      :rtype: Degree



   .. py:method:: get_name_without_degree() -> str

      Generates a human-readable string representation of the relation that omits any degree or lower bound information. The returned string is formatted as '(individual_a, individual_b): role_name', incorporating the identifiers of the two entities involved and the name of the role connecting them. This method performs no modifications to the object's state and relies on the existence of the `ind_a`, `ind_b`, and `role_name` attributes.

      :return: A string representation of the role assertion formatted as "(individual_a, individual_b): role_name", excluding the lower bound.

      :rtype: str



   .. py:method:: get_object_individual() -> fuzzy_dl_owl2.fuzzydl.individual.individual.Individual

      Returns the `Individual` instance that serves as the object of this relation. This method retrieves the target entity involved in the binary link, corresponding to the internal attribute `ind_b`. The operation is read-only and does not modify the state of the relation or the returned individual.

      :return: The Individual instance stored in the object.

      :rtype: Individual



   .. py:method:: get_role_name() -> str

      Retrieves the name of the role associated with this relation instance. This method provides read access to the internal `role_name` attribute, which typically identifies the specific function or label of the entity within the relationship. It performs no modification of the object's state and will return the exact string value stored, or raise an `AttributeError` if the attribute has not been initialized.

      :return: The name of the role.

      :rtype: str



   .. py:method:: get_subject_individual() -> fuzzy_dl_owl2.fuzzydl.individual.individual.Individual

      Retrieves the individual entity that serves as the subject of this relation. This method returns the internal attribute `ind_a`, representing the source node or the first participant in the relationship. Since it returns a direct reference to the stored object, any modifications made to the returned instance will be reflected within the relation, and the method may raise an AttributeError if the relation has not been properly initialized.

      :return: The Individual object representing the subject.

      :rtype: Individual



   .. py:method:: set_object_individual(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual) -> None

      Updates the object of the relation by assigning the provided Individual instance to the internal attribute `ind_b`. This operation mutates the state of the Relation object, replacing any existing object individual with the new value. The method returns None and does not enforce type constraints at runtime, assuming the provided argument adheres to the Individual type hint.

      :param ind:
      :type ind: Individual



   .. py:method:: set_subject_individual(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual) -> None

      Assigns the provided `Individual` instance as the subject of the relation by updating the internal attribute `ind_a`. This method modifies the state of the object in place, overwriting any existing subject reference without performing additional validation or side effects on the input object. The operation returns `None`.

      :param ind: The individual to be assigned as the subject.
      :type ind: Individual



   .. py:attribute:: degree
      :type:  fuzzy_dl_owl2.fuzzydl.degree.degree.Degree


   .. py:attribute:: ind_a
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: ind_b
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: role_name
      :type:  str

