fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction
=======================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a fuzzy logic restriction that associates a specific role with a particular individual, constrained by a lower bound degree.


Description
-----------


Designed to operate within the framework of fuzzy description logics, the implementation handles constraints where a property or role is strictly associated with a specific entity. By inheriting from a base restriction class, it manages the storage of the role identifier and a fuzzy degree object, which quantifies the certainty or lower bound of the logical assertion. The logic encapsulates the relationship between a role and an individual, ensuring that the constraint can be evaluated or represented within the broader system. When generating a textual representation of the logical structure, the software formats the output as a negated existential quantification, specifically using a syntax that involves the role and individual names to define the constraint.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction.HasValueRestriction


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_restriction_has_value_restriction_HasValueRestriction.png
       :alt: UML Class Diagram for HasValueRestriction
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **HasValueRestriction**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_restriction_has_value_restriction_HasValueRestriction.pdf
       :alt: UML Class Diagram for HasValueRestriction
       :align: center
       :width: 13.4cm
       :class: uml-diagram

       UML Class Diagram for **HasValueRestriction**

.. py:class:: HasValueRestriction(role_name: str, individual: str, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.restriction.restriction.Restriction`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction.HasValueRestriction
      :parts: 1
      :private-bases:


   This class models a universal restriction that links a specific role to a particular individual, constrained by a lower bound degree. It is designed to represent logical constraints where a role must be associated with a specific entity, often within the context of fuzzy description logics. To use this class, instantiate it with a string representing the role name, a string for the individual name, and a `Degree` object that defines the lower bound. The class allows retrieval of the individual name via the `get_individual` method and offers a string representation of the restriction's logical structure—specifically a negated existential quantification—through the `get_name_without_degree` method.

   :param ind_name: The name of the individual involved in the restriction.
   :type ind_name: str


   .. py:method:: get_individual() -> str

      Returns the specific individual name associated with the restriction instance. This method acts as a getter for the internal `ind_name` attribute, providing access to the identifier of the entity being restricted. Since it simply returns the stored value, it does not modify the object's state or have side effects, though the returned value depends entirely on how the instance was initialized or modified prior to this call.

      :return: The name of the individual.

      :rtype: str



   .. py:method:: get_name_without_degree() -> str

      Generates a string representation of the restriction formatted as a negated existential assertion. It constructs this string using the instance's role name and individual name to produce a logical expression equivalent to stating that the specified role does not have the specified individual as a value. The returned string follows the specific syntax '(not (b-some ...))', which is used to define the constraint in the underlying system.

      :return: Returns a string formatted as a negated 'b-some' expression involving the role and individual.

      :rtype: str



   .. py:attribute:: ind_name
      :type:  str

