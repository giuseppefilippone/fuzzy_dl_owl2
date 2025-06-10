fuzzy_dl_owl2.fuzzyowl2.util.constants
======================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.util.constants


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.util.constants.ConceptType
   fuzzy_dl_owl2.fuzzyowl2.util.constants.FuzzyOWL2Keyword


Module Contents
---------------

.. py:class:: ConceptType

   Bases: :py:obj:`enum.StrEnum`


   Enum where members are also (and must be) strings


   .. py:method:: __repr__() -> str

      Return repr(self).



   .. py:method:: __str__() -> str

      Return str(self).



   .. py:attribute:: CHOQUET


   .. py:attribute:: FUZZY_NOMINAL


   .. py:attribute:: MODIFIED_CONCEPT


   .. py:attribute:: OWA


   .. py:attribute:: QUANTIFIED_OWA


   .. py:attribute:: QUASI_SUGENO


   .. py:attribute:: SUGENO


   .. py:attribute:: WEIGHTED_CONCEPT


   .. py:attribute:: WEIGHTED_MAX


   .. py:attribute:: WEIGHTED_MIN


   .. py:attribute:: WEIGHTED_SUM


   .. py:attribute:: WEIGHTED_SUM_ZERO


.. py:class:: FuzzyOWL2Keyword(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Create a collection of name/value pairs.

   Example enumeration:

   >>> class Color(Enum):
   ...     RED = 1
   ...     BLUE = 2
   ...     GREEN = 3

   Access them by:

   - attribute access::

   >>> Color.RED
   <Color.RED: 1>

   - value lookup:

   >>> Color(1)
   <Color.RED: 1>

   - name lookup:

   >>> Color['RED']
   <Color.RED: 1>

   Enumerations can be iterated over, and know how many members they have:

   >>> len(Color)
   3

   >>> list(Color)
   [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

   Methods can be added to enumerations, and members can have their own
   attributes -- see the documentation for details.


   .. py:method:: __eq__(value: object) -> bool


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: get_name() -> str


   .. py:method:: get_str_value() -> str


   .. py:method:: get_tag_name() -> str


   .. py:method:: get_value() -> Union[pyparsing.CaselessKeyword, pyparsing.Word]


   .. py:attribute:: A


   .. py:attribute:: AXIOM


   .. py:attribute:: B


   .. py:attribute:: BASE


   .. py:attribute:: C


   .. py:attribute:: CHOQUET


   .. py:attribute:: CLOSE_TAG


   .. py:attribute:: CONCEPT


   .. py:attribute:: CONCEPT_NAMES


   .. py:attribute:: CRISP


   .. py:attribute:: D


   .. py:attribute:: DATATYPE


   .. py:attribute:: DEGREE_DEF


   .. py:attribute:: DEGREE_VALUE


   .. py:attribute:: EQUAL


   .. py:attribute:: FUZZY_LABEL


   .. py:attribute:: FUZZY_LOGIC


   .. py:attribute:: FUZZY_OWL_2


   .. py:attribute:: FUZZY_TYPE


   .. py:attribute:: GEQ


   .. py:attribute:: GOEDEL


   .. py:attribute:: GRE


   .. py:attribute:: INDIVIDUAL


   .. py:attribute:: LEFT_SHOULDER


   .. py:attribute:: LEQ


   .. py:attribute:: LES


   .. py:attribute:: LINEAR


   .. py:attribute:: LOGIC


   .. py:attribute:: LUKASIEWICZ


   .. py:attribute:: MODIFIED


   .. py:attribute:: MODIFIER


   .. py:attribute:: NAME


   .. py:attribute:: NOMINAL


   .. py:attribute:: ONTOLOGY


   .. py:attribute:: OPEN_TAG


   .. py:attribute:: OWA


   .. py:attribute:: PRODUCT


   .. py:attribute:: QUANTIFIER


   .. py:attribute:: QUASI_SUGENO


   .. py:attribute:: Q_OWA


   .. py:attribute:: RIGHT_SHOULDER


   .. py:attribute:: ROLE


   .. py:attribute:: SINGLE_CLOSE_TAG


   .. py:attribute:: SLASH


   .. py:attribute:: SUGENO


   .. py:attribute:: TRAPEZOIDAL


   .. py:attribute:: TRIANGULAR


   .. py:attribute:: TYPE


   .. py:attribute:: WEIGHT


   .. py:attribute:: WEIGHTED


   .. py:attribute:: WEIGHTED_MAXIMUM


   .. py:attribute:: WEIGHTED_MINIMUM


   .. py:attribute:: WEIGHTED_SUM


   .. py:attribute:: WEIGHTED_SUMZERO


   .. py:attribute:: WEIGHTS


   .. py:attribute:: ZADEH


