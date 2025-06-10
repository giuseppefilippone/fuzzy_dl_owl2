fuzzy_dl_owl2.fuzzydl.milp.show_variables_helper
================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.milp.show_variables_helper


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.show_variables_helper.ShowVariablesHelper


Module Contents
---------------

.. py:class:: ShowVariablesHelper

   .. py:method:: add_abstract_filler_to_show(role_name: str) -> None
                  add_abstract_filler_to_show(role_name: str, ind_name: str) -> None

      Shows the membership degree to some atomic concepts of the fillers of an abstract role.



   .. py:method:: add_concept_to_show(conc_name: str) -> None

      Show membership degree of every instance of an atomic concept.



   .. py:method:: add_concrete_filler_to_show(f_name: str) -> None
                  add_concrete_filler_to_show(f_name: str, ind_name: str) -> None
                  add_concrete_filler_to_show(f_name: str, ind_name: str, ar: list[fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept]) -> None

      Shows the value of the fillers of a concrete feature.



   .. py:method:: add_individual_to_show(ind_name: str) -> None

      Shows the value of an individual to every atomic concept.



   .. py:method:: add_variable(var: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, name_to_show: str) -> None

      Add a variable to shown, showing it with a given name.

      :param var: A variable.
      :type var: Variable
      :param name_to_show: Name of the variable when shown.
      :type name_to_show: str



   .. py:method:: clone() -> Self


   .. py:method:: get_labels(var_name: str) -> list[fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept]

      Gets the fuzzy concrete concepts marked to be shown for a variable.



   .. py:method:: get_name(var: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> str

      Gets the name of a variable.



   .. py:method:: get_variables() -> list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]

      Gets the variables to be shown.



   .. py:method:: show_abstract_role_fillers(role_name: str, ind_name: str) -> bool

      Returns whether a given individuals is marked for showing every filler of an abstract role.

      :param role_name: Name of the abstract role.
      :type role_name: str
      :param ind_name: Name of the individual.
      :type ind_name: str



   .. py:method:: show_concepts(concept_name: str) -> bool

      Returns whether an atomic concept is marked to show the membership degree of every individual.

      :param concept_name: Name of atomic concept.
      :type concept_name: str

      :returns: true if the concept is marked to be shown; false otherwise.
      :rtype: bool



   .. py:method:: show_concrete_fillers(f_name: str, ind_name: str) -> bool

      Returns whether a given individuals is marked for showing every filler of a concrete feature.

      :param f_name: Name of the concrete feature.
      :type f_name: str
      :param ind_name: Name of the individual.
      :type ind_name: str



   .. py:method:: show_individuals(ind_name: str) -> bool

      Checks whether an individual is marked to be shown or not.



   .. py:method:: show_variable(var: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> bool

      Checks whether the variable exists or not.



   .. py:attribute:: abstract_fillers
      :type:  dict[str, set[str]]


   .. py:attribute:: concepts
      :type:  set[str]


   .. py:attribute:: concrete_fillers
      :type:  dict[str, set[str]]


   .. py:attribute:: global_abstract_fillers
      :type:  set[str]


   .. py:attribute:: global_concrete_fillers
      :type:  set[str]


   .. py:attribute:: individuals
      :type:  set[str]


   .. py:attribute:: labels_for_fillers
      :type:  dict[str, list[fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept]]


   .. py:attribute:: variables
      :type:  dict[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, str]


