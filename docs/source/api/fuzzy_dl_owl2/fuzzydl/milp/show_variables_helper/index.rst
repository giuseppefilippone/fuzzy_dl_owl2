fuzzy_dl_owl2.fuzzydl.milp.show_variables_helper
================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.milp.show_variables_helper



.. ── LLM-GENERATED DESCRIPTION START ──

A configuration manager that controls the visibility and display of elements within a fuzzy description logic ontology, including atomic concepts, individuals, abstract roles, and concrete features.


Description
-----------


The software acts as a centralized registry for determining which components of a fuzzy description logic ontology should be rendered or tracked during processing. It distinguishes between global visibility, where specific roles or features apply to every individual, and targeted visibility, which restricts display settings to a defined subset of individuals. By maintaining separate collections for atomic concepts, individuals, abstract roles, and concrete features, the system allows fine-grained control over the output of membership degrees and filler values. Furthermore, it integrates fuzzy logic by associating concrete feature fillers with linguistic labels and maps internal variable objects to human-readable strings for presentation. The design supports state cloning, enabling the preservation of specific display configurations without affecting the original state, which is crucial for iterative processing or branching logic within the MILP solver context.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.show_variables_helper.ShowVariablesHelper


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_milp_show_variables_helper_ShowVariablesHelper.png
       :alt: UML Class Diagram for ShowVariablesHelper
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ShowVariablesHelper**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_milp_show_variables_helper_ShowVariablesHelper.pdf
       :alt: UML Class Diagram for ShowVariablesHelper
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ShowVariablesHelper**

.. py:class:: ShowVariablesHelper

   This class serves as a configuration manager for determining which elements of a fuzzy description logic ontology should be displayed. It enables the selective tracking of atomic concepts, individuals, abstract roles, and concrete features, distinguishing between global visibility—applying to all entities—and specific visibility restricted to particular individuals. Additionally, it manages the mapping of internal variable objects to display names and handles the association of fuzzy linguistic labels with concrete feature fillers. Users can interact with this class to populate these sets, query visibility status, and clone the entire configuration state to preserve or branch the current display settings.

   :param abstract_fillers: Maps abstract role names to sets of specific individuals for which the role's fillers should be displayed.
   :type abstract_fillers: dict[str, set[str]]
   :param concepts: A set of atomic concept names for which the membership degree of every individual should be displayed.
   :type concepts: set[str]
   :param concrete_fillers: A dictionary mapping the name of a concrete feature to a set of individuals for which the filler of that feature should be displayed.
   :type concrete_fillers: dict[str, set[str]]
   :param global_abstract_fillers: Names of abstract roles for which to show fillers for every individual.
   :type global_abstract_fillers: set[str]
   :param global_concrete_fillers: A set of concrete feature names for which the fillers are to be shown for every individual.
   :type global_concrete_fillers: set[str]
   :param individuals: Names of individuals for which the membership degree to every atomic concept should be displayed.
   :type individuals: set[str]
   :param labels_for_fillers: Maps a variable name to a list of fuzzy concrete concepts representing the linguistic labels to be displayed for that variable.
   :type labels_for_fillers: dict[str, list[FuzzyConcreteConcept]]
   :param variables: Stores the variables to be displayed, mapping each variable object to its corresponding display name string.
   :type variables: dict[Variable, str]


   .. py:method:: __add_abstract_filler_to_show_1(role_name: str) -> None

      Registers the specified abstract role name within the global collection of abstract fillers intended for display. As a side effect, it removes the role from the local `abstract_fillers` mapping if it is currently present, effectively promoting the role to a global scope and ensuring it is handled by the global display logic rather than being treated as a specific, local filler.

      :param role_name: Name of the abstract role to be added to the global abstract fillers set.
      :type role_name: str



   .. py:method:: __add_abstract_filler_to_show_2(role_name: str, ind_name: str) -> None

      Registers an individual as a filler for a specific abstract role within the helper's internal state, provided the role is not globally defined. If the role name is not found in the `global_abstract_fillers` collection, the method adds the individual name to the set of fillers associated with that role in the `abstract_fillers` dictionary. This ensures that only non-global abstract roles are tracked for the specific individual, modifying the instance state directly without returning a value.

      :param role_name: The name of the abstract role to which the individual is being added as a filler.
      :type role_name: str
      :param ind_name: The name of the individual to be added as a filler for the abstract role.
      :type ind_name: str



   .. py:method:: __add_concrete_filler_to_show_1(f_name: str) -> None

      Adds the specified concrete feature name to the set of global concrete fillers, marking it for display in a global context. If the feature is currently present in the local concrete fillers collection, it is removed to ensure it is not tracked redundantly. This method modifies the internal state of the helper by promoting the feature from a local to a global scope.

      :param f_name: The name of the concrete feature to be displayed.
      :type f_name: str



   .. py:method:: __add_concrete_filler_to_show_2(f_name: str, ind_name: str) -> None

      Registers the specified individual as a concrete filler for the given feature within the helper's internal tracking structure. This operation is conditional; if the feature is already present in the global concrete fillers collection, the method returns immediately without making changes. Otherwise, the individual is added to the set of fillers associated with the feature name in the instance's concrete fillers dictionary.

      :param f_name: The name of the concrete feature to associate with the individual, provided it is not a global feature.
      :type f_name: str
      :param ind_name: The name of the individual to be added to the set of fillers associated with the concrete feature.
      :type ind_name: str



   .. py:method:: __add_concrete_filler_to_show_3(f_name: str, ind_name: str, ar: list[fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept]) -> None

      Registers a concrete feature of an individual for display and associates a list of fuzzy concrete concepts (linguistic labels) with it. The method first ensures the feature-individual pair is tracked by calling `add_concrete_filler_to_show`. It then retrieves any existing labels associated with the pair; if labels already exist, the provided list of concepts is appended to them, otherwise, the list is stored directly. This process updates the internal `labels_for_fillers` dictionary to aggregate membership degrees for visualization.

      :param f_name: The name of the concrete feature for which membership degrees are being displayed.
      :type f_name: str
      :param ind_name: The name of the individual entity that possesses the concrete feature, used to uniquely identify the specific feature instance.
      :type ind_name: str
      :param ar: List of fuzzy concrete concepts representing linguistic labels to be displayed for the feature filler.
      :type ar: list[FuzzyConcreteConcept]



   .. py:method:: add_abstract_filler_to_show(role_name: str) -> None
                  add_abstract_filler_to_show(role_name: str, ind_name: str) -> None

      Configures the display settings to show the membership degrees of atomic concepts associated with the fillers of a specified abstract role. This method serves as a dispatcher that validates input types and argument counts before delegating the logic to internal helper methods. It accepts either one or two string arguments, corresponding to different modes of specifying the abstract role and its fillers, and will raise an assertion error if the provided arguments are not strings or if the number of arguments is incorrect.

      :param args: One or two string arguments identifying the abstract role and optionally a specific filler or concept.
      :type args: typing.Any



   .. py:method:: add_concept_to_show(conc_name: str) -> None

      Registers an atomic concept name to the internal collection of variables to be displayed, ensuring that the membership degree for every instance of this concept is tracked. This method modifies the state of the helper by adding the specified string to the set of active concepts. It is idempotent, meaning that adding the same concept name multiple times will not alter the state beyond the first addition.

      :param conc_name: Name of the atomic concept to include in the display.
      :type conc_name: str



   .. py:method:: add_concrete_filler_to_show(f_name: str) -> None
                  add_concrete_filler_to_show(f_name: str, ind_name: str) -> None
                  add_concrete_filler_to_show(f_name: str, ind_name: str, ar: list[fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept]) -> None

      Registers a concrete feature's filler value for display, acting as a dispatcher that delegates to internal helper methods based on the number of arguments provided. The first argument must always be a string identifying the feature name. If only one argument is supplied, the method processes the feature using minimal context; if two arguments are supplied, the second must be a string representing a specific value or attribute; and if three arguments are supplied, the second must be a string and the third must be a list of `FuzzyConcreteConcept` objects to define the filler using fuzzy logic. The method raises an `AssertionError` if the argument count is not between one and three or if the types of the arguments do not conform to these specific patterns. This function modifies the internal state of the `ShowVariablesHelper` to include the specified filler in the display configuration but returns no value.

      :param args: Variable arguments defining the concrete feature, comprising a feature name (str), optionally a filler (str), and optionally a list of FuzzyConcreteConcepts.
      :type args: typing.Any



   .. py:method:: add_individual_to_show(ind_name: str) -> None

      Registers the specified individual name to be tracked or displayed by adding it to the internal collection of individuals. This method modifies the state of the helper object by inserting the name into the set. If the individual name is already present in the collection, the operation has no effect.

      :param ind_name: The name of the individual to be added to the display set.
      :type ind_name: str



   .. py:method:: add_variable(var: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, name_to_show: str) -> None

      Registers a specific `Variable` instance for display, associating it with a custom string label to be used when rendering or presenting the variable. This method updates the internal state of the helper by storing the mapping between the variable object and its designated display name. If the variable is already present in the collection, the existing display name will be overwritten with the new value, ensuring that the most recent label is retained.

      :param var: The variable object to be added for display.
      :type var: Variable
      :param name_to_show: The display name to use for the variable.
      :type name_to_show: str



   .. py:method:: clone() -> Self

      Creates and returns a deep copy of the current `ShowVariablesHelper` instance. This method ensures that the new instance is independent of the original by performing a deep copy on complex attributes such as `abstract_fillers`, `concepts`, `concrete_fillers`, `global_abstract_fillers`, `global_concrete_fillers`, and `individuals`. For `labels_for_fillers` and `variables`, it constructs new dictionary and list containers to isolate the structure, though the contained elements are copied by reference. The original object remains unmodified during this process.

      :return: A new instance that is a deep copy of the current object.

      :rtype: typing.Self



   .. py:method:: get_labels(var_name: str) -> list[fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept]

      Retrieves the list of fuzzy concrete concepts designated for display for a specific variable. It queries the internal mapping of variable names to their associated labels. If the provided variable name is not found in the mapping, the method returns an empty list rather than raising an exception.

      :param var_name: Identifier of the variable whose associated fuzzy concrete concepts are to be retrieved.
      :type var_name: str

      :return: A list of fuzzy concrete concepts marked to be shown for the specified variable. Returns an empty list if the variable has no associated labels.

      :rtype: list[FuzzyConcreteConcept]



   .. py:method:: get_name(var: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> str

      Retrieves the string name associated with a given `Variable` instance by querying the internal mapping of variables. This method serves as a read-only accessor to resolve variable objects to their string identifiers. If the specified variable is not present in the internal collection, the method returns `None`.

      :param var: The variable instance for which to retrieve the name.
      :type var: Variable

      :return: The string name associated with the specified variable.

      :rtype: str



   .. py:method:: get_variables() -> list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]

      Returns a list of variables currently managed by the helper for display purposes. This method retrieves the keys from the internal `variables` mapping and returns them as a new list, ensuring that modifications to the returned collection do not affect the helper's internal state. If no variables are stored, an empty list is returned.

      :return: A list of the variable keys intended for display.

      :rtype: list[Variable]



   .. py:method:: show_abstract_role_fillers(role_name: str, ind_name: str) -> bool

      Determines whether the fillers of a specified abstract role should be displayed for a given individual. The method first checks if the role is globally enabled for display; if so, it returns true regardless of the individual. If the role is not global, it verifies whether the specific individual is explicitly listed in the set of fillers for that role, returning true only if the individual is present. This method does not modify any internal state.

      :param role_name: Name of the abstract role to check for filler visibility.
      :type role_name: str
      :param ind_name: Name of the individual to check if they are marked to display all fillers of the abstract role.
      :type ind_name: str

      :return: True if the abstract role is globally enabled or if the individual is explicitly marked to show fillers for that role; otherwise, False.

      :rtype: bool



   .. py:method:: show_concepts(concept_name: str) -> bool

      Checks whether a given atomic concept is included in the internal registry of concepts designated for visualization or detailed output. This method verifies the presence of the specified concept name within the helper's stored collection, effectively determining if the membership degrees of individuals for this concept should be displayed. The check is case-sensitive and relies on exact string matching. Since this is a query operation, it does not modify the internal state of the object or the provided arguments.

      :param concept_name: The name of the atomic concept to check for display status.
      :type concept_name: str

      :return: True if the atomic concept is marked to show the membership degree of every individual; otherwise, False.

      :rtype: bool



   .. py:method:: show_concrete_fillers(f_name: str, ind_name: str) -> bool

      Determines whether the fillers of a specific concrete feature should be displayed for a given individual. If the feature is currently marked as global, the method returns True, indicating that fillers are shown for all individuals. Otherwise, it checks the specific configuration for that feature to see if the individual is explicitly listed; the method returns False if the feature is not global and the individual is not found in the specific configuration or if the configuration for the feature is missing. This method performs a read-only check and does not modify the state of the helper.

      :param f_name: The name of the concrete feature for which filler visibility is being determined.
      :type f_name: str
      :param ind_name: Name of the individual to check for the display setting.
      :type ind_name: str

      :return: True if the fillers for the specified concrete feature should be displayed for the given individual, based on global feature settings or explicit individual markings.

      :rtype: bool



   .. py:method:: show_individuals(ind_name: str) -> bool

      Evaluates the visibility status of a specific individual by checking if its name exists within the internal registry of active individuals. This method acts as a filter, returning `True` if the individual is present in the registry and should be shown, and `False` otherwise. It performs a read-only lookup and does not modify the internal state of the helper object.

      :param ind_name:
      :type ind_name: str

      :return: True if the specified individual is marked to be shown, False otherwise.

      :rtype: bool



   .. py:method:: show_variable(var: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> bool

      Determines whether a specific variable is present within the internal collection managed by the helper. It performs a membership check against the stored variables and returns a boolean value indicating if the variable is currently tracked. This method is a read-only operation and does not modify the state of the helper or the variable itself.

      :param var: The variable to check for existence.
      :type var: Variable

      :return: True if the variable exists, False otherwise.

      :rtype: bool



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

