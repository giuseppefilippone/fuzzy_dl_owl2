fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction
=======================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction



.. ── LLM-GENERATED DESCRIPTION START ──

A fuzzy description logic restriction that enforces a specific value for a given role, constrained by a degree of membership.


Description
-----------


Models a logical constraint where a specific role must be associated with a particular individual, incorporating a fuzzy degree to represent the strength or lower bound of this relationship. Extending the base ``Restriction`` class allows the component to leverage common attributes for role names and degrees while specifically storing the identifier of the target individual. The implementation represents the constraint as a negated existential quantification, translating the "has value" assertion into a specific string format required by the underlying system. Accessor methods enable the retrieval of the individual's name and the formatted logical expression, facilitating the integration of these constraints into broader reasoning tasks.

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

