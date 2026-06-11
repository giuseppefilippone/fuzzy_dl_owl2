fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast
===========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast

.. autoapi-nested-parse::

   Faster drop-in replacement for fuzzy_dl_owl2.fuzzydl.parser.dl_parser.DLParser.

   It uses a hand-rolled tokenizer plus a deterministic recursive-descent parser.
   The grammar accepted is identical to the legacy parser. All semantic actions
   are reused: this module imports the DLParser class from ``dl_parser_clean`` and
   invokes every ``_parse_*`` callback with a plain token list so the knowledge
   base / queries are populated exactly the same way.

   The file is written so that it can be compiled with Cython using
   ``setup_dl_parser.py`` for an additional native-code speedup. When run as
   plain Python it still parses 5-10x faster than the legacy parser because
   backtracking, packrat caching and the bounded-recursion machinery are gone.




.. ── LLM-GENERATED DESCRIPTION START ──

A high-performance recursive-descent parser that acts as a drop-in replacement for the legacy FuzzyDL parser by reusing semantic actions while eliminating backtracking and caching overhead.


Description
-----------


Designed as a high-speed alternative to the original implementation, this software employs a hand-rolled tokenizer combined with a deterministic recursive-descent strategy to process FuzzyDL syntax. Instead of reimplementing the logic for building the knowledge base, it imports the legacy ``DLParser`` class and invokes its semantic action callbacks with pre-processed token lists, ensuring identical behavior while drastically reducing computational overhead. The architecture eliminates the need for backtracking, packrat caching, and complex recursion limits found in the older version, resulting in a significant performance increase even when run as standard Python code. To handle large inputs efficiently, the implementation supports streaming the source text in bounded chunks, which keeps memory usage proportional to the chunk size rather than the total file size. Additionally, the code is structured to allow compilation with Cython for native-code execution, further accelerating the parsing of complex fuzzy description logic ontologies.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._APPROX_KW
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._AXIOM_KW
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._CMP_KW
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._CONCEPT_OP_AND_OR_IMPL
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._FEATURE_TYPE_KW
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._FUZZY_NUMBER_OP_BIN
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._FUZZY_NUMBER_OP_PAIR
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._K
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._OWA_INTEGRAL_KW
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._QUERY_KW
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._SHOW_KW
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._STATEMENT_KW
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._WEIGHTED_KW


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast.DLParserFast
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._KW
   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._Parser


Functions
---------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast._kn


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_dl_parser_fast_DLParserFast.png
       :alt: UML Class Diagram for DLParserFast
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **DLParserFast**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_dl_parser_fast_DLParserFast.pdf
       :alt: UML Class Diagram for DLParserFast
       :align: center
       :width: 14.2cm
       :class: uml-diagram

       UML Class Diagram for **DLParserFast**

.. py:class:: DLParserFast

   Bases: :py:obj:`object`


   Drop-in replacement for :class:`DLParser` using the hand-rolled parser.

   Public API is intentionally identical: :meth:`get_kb`, :meth:`main`,
   :meth:`parse_string`, :meth:`parse_string_opt`, :meth:`load_config`.
   The knowledge-base / queries-list class attributes live on DLParser so
   parse-action callbacks (which still reference DLParser.kb directly)
   continue to work without modification.


   .. py:method:: _parse_chunk(text: str) -> None
      :staticmethod:


      Tokenizes the given text and parses every top-level form it contains.
      The token list is local, so it is reclaimed as soon as this returns —
      bounding peak token memory to one chunk when called by the streaming
      path above.

      :param text: A chunk of fuzzy-DL source text to tokenize and parse.
      :type text: str



   .. py:method:: get_kb(file_path: str, **kwargs: Any) -> Tuple[fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase, List[fuzzy_dl_owl2.fuzzydl.query.query.Query]]
      :staticmethod:


      Parses a fuzzy-DL file and returns the populated knowledge base together
      with the list of parsed queries. This is the fast-parser mirror of
      :meth:`DLParser.get_kb` so callers can swap implementations without
      changing their call site.

      :param file_path: Path to the fuzzy-DL source file.
      :type file_path: str
      :param kwargs: Configuration overrides forwarded to :meth:`load_config`.
      :type kwargs: typing.Any

      :raises FuzzyOntologyException: if parsing fails or the file is not found.

      :return: The parsed knowledge base and the list of queries.

      :rtype: typing.Tuple[KnowledgeBase, typing.List[Query]]



   .. py:method:: load_config(**kwargs: Any) -> None
      :staticmethod:


      Loads reasoner/parser configuration by delegating to :meth:`DLParser.load_config`, so the fast parser shares the exact same configuration handling as the legacy one. Any keyword overrides are forwarded unchanged; the call updates global configuration state and returns nothing.

      :param kwargs: Configuration overrides forwarded to :meth:`DLParser.load_config`.
      :type kwargs: typing.Any



   .. py:method:: main(file_path: str, **kwargs: Any) -> dict[fuzzy_dl_owl2.fuzzydl.query.query.Query, fuzzy_dl_owl2.fuzzydl.milp.solution.Solution]
      :staticmethod:


      Runs the full fast-parser pipeline for a fuzzy-DL file: it parses the file into a knowledge base, solves the TBox, and answers every parsed query, collecting the per-query solutions into a dictionary. ``all-instances`` queries short-circuit to an informational message when the KB has no individuals. The cyclic garbage collector is disabled for the duration (and restored afterwards) since the run builds a large acyclic object graph that would otherwise be scanned repeatedly; an inconsistent ontology is reported as the answer ``1.0`` rather than propagated.

      :param file_path: Path to the fuzzy-DL source file to run.
      :type file_path: str
      :param kwargs: Configuration overrides forwarded to :meth:`get_kb`.
      :type kwargs: typing.Any

      :return: A mapping from each parsed query to its computed solution.

      :rtype: dict[Query, Solution]



   .. py:method:: parse_string(instring: str) -> None
      :staticmethod:


      Parses a complete fuzzy-DL source string. The constructed knowledge base
      and queries are accumulated as side effects in ``DLParser.kb`` and
      ``DLParser.queries_list``; the method itself returns nothing.

      Small sources are tokenized and parsed in a single pass. Sources above
      ``_STREAM_THRESHOLD`` are streamed form-by-form in bounded chunks so the
      live token set stays proportional to one chunk rather than the whole file;
      the resulting knowledge base is identical either way.

      :param instring: The fuzzy-DL source text to parse.
      :type instring: str



   .. py:method:: parse_string_opt(filename: str) -> None
      :staticmethod:


      Parses an entire fuzzy-DL file using the fastest available path. When the compiled re2c/flex backend is present, the file is mmap-ed and tokenized in C and parsed form-by-form so peak token memory stays bounded even for large inputs (timing is logged per chunk). Otherwise it falls back to reading the whole file into a string and delegating to :meth:`parse_string`. Parsing populates the shared knowledge base as a side effect and returns nothing.

      :param filename: Path to the fuzzy-DL source file to parse.
      :type filename: str



.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_dl_parser_fast__KW.png
       :alt: UML Class Diagram for _KW
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **_KW**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_dl_parser_fast__KW.pdf
       :alt: UML Class Diagram for _KW
       :align: center
       :width: 4.6cm
       :class: uml-diagram

       UML Class Diagram for **_KW**

.. py:class:: _KW

   Namespace of every FuzzyDLKeyword token literal used in dispatch.


   .. py:attribute:: ALL_INSTANCES_QUERY


   .. py:attribute:: BINARY


   .. py:attribute:: BNP_QUERY


   .. py:attribute:: CONSTRAINTS


   .. py:attribute:: CRISP_CONCEPT


   .. py:attribute:: CRISP_ROLE


   .. py:attribute:: DEFINE_CONCEPT


   .. py:attribute:: DEFINE_FUZZY_CONCEPT


   .. py:attribute:: DEFINE_FUZZY_EQUIVALENCE


   .. py:attribute:: DEFINE_FUZZY_LOGIC


   .. py:attribute:: DEFINE_FUZZY_NUMBER


   .. py:attribute:: DEFINE_FUZZY_NUMBER_RANGE


   .. py:attribute:: DEFINE_FUZZY_SIMILARITY


   .. py:attribute:: DEFINE_MODIFIER


   .. py:attribute:: DEFINE_PRIMITIVE_CONCEPT


   .. py:attribute:: DEFINE_TRUTH_CONSTANT


   .. py:attribute:: DEFUZZIFY_LOM_QUERY


   .. py:attribute:: DEFUZZIFY_MOM_QUERY


   .. py:attribute:: DEFUZZIFY_SOM_QUERY


   .. py:attribute:: DISJOINT


   .. py:attribute:: DISJOINT_UNION


   .. py:attribute:: DOMAIN


   .. py:attribute:: EQ


   .. py:attribute:: EQUIVALENT_CONCEPTS


   .. py:attribute:: FREE


   .. py:attribute:: FUNCTIONAL


   .. py:attribute:: GE


   .. py:attribute:: GOEDEL_IMPLIES


   .. py:attribute:: HAS_VALUE


   .. py:attribute:: IMPLIES


   .. py:attribute:: IMPLIES_ROLE


   .. py:attribute:: INSTANCE


   .. py:attribute:: INVERSE


   .. py:attribute:: INVERSE_FUNCTIONAL


   .. py:attribute:: KLEENE_DIENES_IMPLIES


   .. py:attribute:: LE


   .. py:attribute:: LUKASIEWICZ_IMPLIES


   .. py:attribute:: MAX_G_SUBS_QUERY


   .. py:attribute:: MAX_INSTANCE_QUERY


   .. py:attribute:: MAX_KD_SUBS_QUERY


   .. py:attribute:: MAX_L_SUBS_QUERY


   .. py:attribute:: MAX_RELATED_QUERY


   .. py:attribute:: MAX_SAT_QUERY


   .. py:attribute:: MAX_SUBS_QUERY


   .. py:attribute:: MAX_VAR_QUERY


   .. py:attribute:: MIN_G_SUBS_QUERY


   .. py:attribute:: MIN_INSTANCE_QUERY


   .. py:attribute:: MIN_KD_SUBS_QUERY


   .. py:attribute:: MIN_L_SUBS_QUERY


   .. py:attribute:: MIN_RELATED_QUERY


   .. py:attribute:: MIN_SAT_QUERY


   .. py:attribute:: MIN_SUBS_QUERY


   .. py:attribute:: MIN_VAR_QUERY


   .. py:attribute:: MUL


   .. py:attribute:: NOT


   .. py:attribute:: Q_OWA


   .. py:attribute:: RANGE


   .. py:attribute:: REFLEXIVE


   .. py:attribute:: RELATED


   .. py:attribute:: SAT_QUERY


   .. py:attribute:: SELF


   .. py:attribute:: SHOW_ABSTRACT_FILLERS


   .. py:attribute:: SHOW_ABSTRACT_FILLERS_FOR


   .. py:attribute:: SHOW_CONCEPTS


   .. py:attribute:: SHOW_CONCRETE_FILLERS


   .. py:attribute:: SHOW_CONCRETE_FILLERS_FOR


   .. py:attribute:: SHOW_CONCRETE_INSTANCE_FOR


   .. py:attribute:: SHOW_INSTANCES


   .. py:attribute:: SHOW_LANGUAGE


   .. py:attribute:: SHOW_VARIABLES


   .. py:attribute:: SIGMA_COUNT


   .. py:attribute:: SOME


   .. py:attribute:: SUB


   .. py:attribute:: SUM


   .. py:attribute:: SYMMETRIC


   .. py:attribute:: TRANSITIVE


   .. py:attribute:: ZADEH_IMPLIES


.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_dl_parser_fast__Parser.png
       :alt: UML Class Diagram for _Parser
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **_Parser**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_parser_dl_parser_fast__Parser.pdf
       :alt: UML Class Diagram for _Parser
       :align: center
       :width: 11.3cm
       :class: uml-diagram

       UML Class Diagram for **_Parser**

.. py:class:: _Parser(tokens: List[fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler.Token])

   Bases: :py:obj:`object`


   Single-pass recursive descent over a pre-lexed token stream.

   Every ``parse_*`` method mirrors one non-terminal of the original
   grammar.  There is **no backtracking**: once a method
   commits to a branch it consumes tokens greedily.  This is safe because
   the fuzzy-DL grammar is LL(1) at the top level and the tokenizer has
   already disambiguated numbers, identifiers and punctuation.


   .. py:method:: _advance() -> fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler.Token

      Consumes the current token and advances the cursor by one. The token at the old position is returned, so callers can read and step in a single call.

      :return: The token that was at the cursor before advancing.

      :rtype: Token



   .. py:method:: _eat(kind: int) -> bool

      Conditionally consumes the current token if it matches the given type code. Unlike :meth:`_expect`, a mismatch is not an error: the cursor is advanced and ``True`` returned only on a match, otherwise the cursor stays put and ``False`` is returned.

      :param kind: The token type code to consume if present.
      :type kind: int

      :return: ``True`` if a matching token was consumed, ``False`` otherwise.

      :rtype: bool



   .. py:method:: _expect(kind: int) -> fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler.Token

      Requires the current token to have the given type code, consuming and returning it on a match. If the token's kind does not match, a :class:`FuzzyOntologyException` is raised with the byte offset and the offending token, and the cursor is left unmoved.

      :param kind: The expected token type code.
      :type kind: int

      :raises FuzzyOntologyException: if the current token is not of the expected kind.

      :return: The consumed token of the expected kind.

      :rtype: Token



   .. py:method:: _parse_weighted_part_inline() -> Any

      Parses an inline weighted part, matching the grammar rule
      ``weighted_part ::= "(" number concept ")"``. The weight and concept are
      consumed and forwarded as a flat list.

      :return: The parsed weighted part.

      :rtype: typing.Any



   .. py:method:: _peek(offset: int = 0) -> fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler.Token

      Returns the token at ``pos + offset`` without advancing the cursor. Lookahead past the end of the stream is clamped to the last token (the EOF sentinel), so callers can peek freely without bounds checks.

      :param offset: How many tokens ahead of the current position to look.
      :type offset: int

      :return: The token at the requested position, or the final token if out of range.

      :rtype: Token



   .. py:method:: parse_approx_concept() -> Any

      Parses an approximation concept, matching the grammar rule
      ``approx_concept ::= "(" approx_op role concept ")"``. The approximation
      operator, role, and inner concept are consumed and forwarded as a flat list.

      :return: The parsed approximation concept.

      :rtype: typing.Any



   .. py:method:: parse_axioms() -> None

      Parses an axiom, matching the grammar rule covering instance assertions,
      role assertions, implications, concept definitions, equivalent concepts,
      disjoint unions, range/domain declarations, role characteristics, and
      inverse role declarations. The keyword after ``(`` selects the branch;
      the branch-specific tokens are consumed and forwarded as a flat list to
      ``DLParser._parse_axioms``.

      :raises FuzzyOntologyException: if the axiom keyword is unrecognised.



   .. py:method:: parse_concept() -> Any

      concept ::=
        variable
      | "top" | "bottom"
      | "(" datatype_restriction ")"
      | "(" number concept ")"                               -- weighted part
      | "(" "[" ("<=" | ">=") number|variable "]" concept ")"
      | "(" binary_connective concept+ ")"
      | "(" "some" role (concept | variable) ")"
      | "(" "has-value" role individual ")"
      | "(" approx_op role concept ")"
      | "(" "not" concept ")"
      | "(" "self" variable ")"
      | "(" weighted_op weighted_part+ ")"
      | "(" "q-owa" variable concept+ ")"
      | "(" owa_integral_op "(" number+ ")" "(" concept+ ")" ")"
      | "(" "sigma-count" role concept "{" individual* "}" fuzzy_name ")"
      | "(" modifier_name concept ")"

      Dispatches on the leading token (a bare identifier yields a variable /
      top / bottom; otherwise the keyword after ``(`` selects the concept
      sub-parser) and consumes the whole concept form.

      :raises FuzzyOntologyException: if the tokens do not form a valid concept.

      :return: The parsed concept node.

      :rtype: typing.Any



   .. py:method:: parse_constraints() -> None

      constraints ::=
      "(" "constraints"
          ( "(" ("binary" | "free") variable ")"
          | "(" expression cmp_op number ")" )+
      ")"



   .. py:method:: parse_crisp_declarations() -> None

      crisp_declarations ::= "(" ("crisp-concept" | "crisp-role") name+ ")"



   .. py:method:: parse_datatype_restriction() -> Any

      Parses a datatype restriction, matching the grammar rule
      ``datatype_restriction ::= "(" cmp_op role (fuzzy_number_expr | datatype_restriction_function | variable) ")"``. The comparison operator, role, and third operand are consumed and forwarded as a flat list. Feature-type dispatch for ``STRING`` values lives in ``DLParser._parse_datatype_restriction`` so both fast and slow parsers share one source of truth.

      :return: The parsed datatype restriction.

      :rtype: typing.Any



   .. py:method:: parse_datatype_restriction_function() -> Any

      Parses a datatype restriction function, matching the grammar rule
      ``datatype_restriction_function ::= datatype_restriction_operand ( "+" datatype_restriction_operand )*``.
      The first operand is parsed, then a chain of ``+``-separated operands is
      consumed if present. The flat operand list is forwarded to the callback.

      :return: The parsed restriction function.

      :rtype: typing.Any



   .. py:method:: parse_datatype_restriction_function_or_fuzzy_number() -> Any

      Parses a datatype-restriction function or a fuzzy number expression,
      disambiguating by lookahead. Uses 1-token lookahead on the token after
      ``(`` to decide among:

      * ``(f+ ...)`` / ``(f- ...)`` / ``(f* ...)`` / ``(f/ ...)`` → fuzzy number expression
      * ``(num num num)`` → simple triangular fuzzy number
      * ``(num [*] fn)`` or ``(fn - fn)`` → datatype restriction function

      :return: The parsed restriction function or fuzzy number expression.

      :rtype: typing.Any



   .. py:method:: parse_datatype_restriction_operand() -> Any

      Parses a datatype restriction operand, matching the grammar rule
      ``datatype_restriction_operand ::= number | variable | "(" number ["*"] datatype_restriction_function ")" | "(" datatype_restriction_function ("-"|"+") datatype_restriction_function ")"``. Disambiguation is done by 1-token lookahead after the opening parenthesis.

      :return: The parsed restriction operand.

      :rtype: typing.Any



   .. py:method:: parse_degree() -> Any

      Parses a degree, matching the grammar rule
      ``degree ::= number | expression | variable``. A number becomes a numeric
      degree, a parenthesised expression is parsed as a degree expression, and
      a bare variable becomes a variable degree.

      :return: The parsed degree.

      :rtype: typing.Any



   .. py:method:: parse_expression() -> Any

      Parses a linear expression, matching the grammar rule
      ``expression ::= term ( "+" term )*``. One or more terms separated by
      ``+`` are consumed and forwarded as a flat list with explicit ``+``
      separators inserted.

      :return: The parsed expression.

      :rtype: typing.Any



   .. py:method:: parse_features() -> None

      features ::= "(" "range" variable type_kw number* ")"



   .. py:method:: parse_fuzzy_concept() -> None

      fuzzy_concept ::= "(" "define-fuzzy-concept" name shape "(" (number|variable)* ")" ")"



   .. py:method:: parse_fuzzy_equivalence() -> None

      fuzzy_equivalence ::= "(" "define-fuzzy-equivalence" name ")"



   .. py:method:: parse_fuzzy_logic() -> None

      fuzzy_logic ::= "(" "define-fuzzy-logic" logic_name ")"



   .. py:method:: parse_fuzzy_number_def() -> None

      fuzzy_number_def ::= "(" "define-fuzzy-number" name (fuzzy_number_expr | simple_fuzzy_number) ")"



   .. py:method:: parse_fuzzy_number_expr() -> Any

      Parses a fuzzy number expression, matching the grammar rule
      ``fuzzy_number_expr ::= simple_fuzzy_number | "(" ("f+"|"f*") fuzzy_number_expr+ ")" | "(" ("f-"|"f/") fuzzy_number_expr fuzzy_number_expr ")"``. Compound forms (``f+``, ``f*``, ``f-``, ``f/``) are returned as raw flat lists ``[op, *operands]`` for the consuming callback to handle.

      :raises FuzzyOntologyException: if a compound form is malformed (e.g.
          ``f+/f*`` with fewer than one operand or an unknown operator).

      :return: The parsed fuzzy number expression.

      :rtype: typing.Any



   .. py:method:: parse_fuzzy_range() -> None

      fuzzy_range ::= "(" "define-fuzzy-number-range" number number ")"



   .. py:method:: parse_fuzzy_similarity() -> None

      fuzzy_similarity ::= "(" "define-fuzzy-similarity" name ")"



   .. py:method:: parse_gformula() -> Any

      Parses a top-level ``gformula``, matching the grammar rule
      ``gformula ::= statement | axiom | query | show_statement | concept``.
      The first token must be ``(``; the keyword (or number / bracket)
      immediately after ``(`` is peeked and the stream is dispatched to the
      appropriate sub-parser. The consumed form is forwarded to the
      corresponding ``DLParser._parse_*`` callback.

      :raises FuzzyOntologyException: if the first token is not ``(`` or the
          inner keyword is unrecognised.

      :return: The parsed result (concept, axiom, statement, etc.) forwarded
          from the sub-parser.

      :rtype: typing.Any



   .. py:method:: parse_has_value_concept() -> Any

      Parses a value restriction concept, matching the grammar rule
      ``has_value_concept ::= "(" "has-value" role individual ")"``. The role
      and individual name are consumed and forwarded as a flat list.

      :return: The parsed value restriction concept.

      :rtype: typing.Any



   .. py:method:: parse_implies_like_concept() -> Any

      Parses a binary connective concept (AND, OR, IMPLIES variants), matching
      the grammar rule
      ``implies_like_concept ::= "(" op concept+ ")"``. The operator keyword
      and all operand concepts are consumed and forwarded as a flat list to
      ``DLParser._parse_binary_concept``.

      :return: The parsed binary connective concept.

      :rtype: typing.Any



   .. py:method:: parse_modifier() -> None

      modifier ::= "(" "define-modifier" name modifier_kind "(" number* ")" ")"



   .. py:method:: parse_modifier_concept() -> Any

      Parses a modifier application concept, matching the grammar rule
      ``modifier_concept ::= "(" modifier_name concept ")"``. The modifier name
      and inner concept are consumed and forwarded as a flat list.

      :return: The parsed modified concept.

      :rtype: typing.Any



   .. py:method:: parse_number() -> Union[int, float]

      Parses a numeric literal, matching the grammar rule
      ``number ::= [+-]? ( \d+ [ . \d* ] | . \d+ ) ( [eE] [+-]? \d+ )?``.
      The current token must be a number; it is consumed and converted to an ``int`` or ``float`` via ``DLParser._to_number``.

      :raises FuzzyOntologyException: if the current token is not a numeric literal.

      :return: The parsed numeric value.

      :rtype: typing.Union[int, float]



   .. py:method:: parse_owa_integral_concept() -> Any

      Parses an OWA / Choquet / Sugeno / quasi-Sugeno integral concept, matching
      the grammar rule
      ``owa_integral_concept ::= "(" op "(" number+ ")" "(" concept+ ")" ")"``.
      The operator keyword, the parenthesised weight list, and the
      parenthesised concept list are consumed and forwarded as a single flat
      list (the callback locates the weights/concepts boundary via element types).

      :return: The parsed OWA-integral concept.

      :rtype: typing.Any



   .. py:method:: parse_program() -> None

      program ::= gformula*



   .. py:method:: parse_q_owa_concept() -> Any

      Parses a quantifier-guided OWA concept, matching the grammar rule
      ``q_owa_concept ::= "(" "q-owa" variable concept+ ")"``. The quantifier
      variable and one or more operand concepts are consumed and forwarded as
      a flat list.

      :return: The parsed quantifier-guided OWA concept.

      :rtype: typing.Any



   .. py:method:: parse_queries() -> None

      Parses a query, matching the grammar rule covering all query types
      (all-instances, satisfiability, instance / subsumption / related / variable
      max/min, defuzzify, and BNP). The query keyword after ``(`` selects the
      branch; branch-specific arguments are consumed and forwarded as a flat
      list to ``DLParser._parse_queries``.

      :raises FuzzyOntologyException: if the query keyword is unrecognised.



   .. py:method:: parse_show_statement() -> None

      show_statement ::= "(" show_kw (concept | variable)* ")"



   .. py:method:: parse_sigma_count_concept() -> Any

      Parses a sigma-count concept, matching the grammar rule
      ``sigma_count_concept ::= "(" "sigma-count" role concept "{" individual* "}" fuzzy_name ")"``.
      The role, concept, brace-enclosed individual list, and fuzzy name are
      consumed and forwarded as a flat list.

      :return: The parsed sigma-count concept.

      :rtype: typing.Any



   .. py:method:: parse_simple_fuzzy_number() -> Any

      Parses a simple fuzzy number literal, matching the grammar rule
      ``simple_fuzzy_number ::= "(" number number number ")" | number | variable``.
      A parenthesised triple produces a triangular fuzzy number; a bare number
      or variable is wrapped as a scalar fuzzy number.

      :raises FuzzyOntologyException: if a triangular literal does not contain
          exactly three numbers.

      :return: The parsed fuzzy number literal.

      :rtype: typing.Any



   .. py:method:: parse_some_concept() -> Any

      Parses an existential restriction concept, matching the grammar rule
      ``some_concept ::= "(" "some" role (concept | variable) ")"``. The role
      and second argument (either a nested concept or a bare variable) are
      consumed and forwarded as a flat list.

      :return: The parsed existential restriction concept.

      :rtype: typing.Any



   .. py:method:: parse_term() -> Any

      Parses a linear term, matching the grammar rule
      ``term ::= number | variable | "(" number "*" variable ")" | number "*" variable``.
      Bare numbers, bare variables, and parenthesised or infix ``num * var`` forms
      are consumed and forwarded as a flat list.

      :return: The parsed term.

      :rtype: typing.Any



   .. py:method:: parse_threshold_concept_wrapped() -> Any

      Parses a threshold concept wrapper, matching the grammar rule
      ``threshold_concept_wrapped ::= "(" "[" ("<=" | ">=") number|variable "]" concept ")"``.

      The tokenizer may merge the operator and its operand into a single
      identifier (e.g. ``>=0.4``), so the method splits off the inline
      operator and operand before forwarding the pieces to the callback.

      :raises FuzzyOntologyException: if a threshold operator is not found or
          the inline operand is malformed.

      :return: The parsed threshold concept.

      :rtype: typing.Any



   .. py:method:: parse_truth_constants() -> None

      truth_constants ::= "(" "define-truth-constant" name number ")"



   .. py:method:: parse_unary_concept() -> Any

      Parses a unary concept (negation or self-restriction), matching the grammar
      rule
      ``unary_concept ::= "(" "not" concept ")" | "(" "self" variable ")"``.
      The keyword after the opening parenthesis selects which form to parse.

      :return: The parsed unary concept.

      :rtype: typing.Any



   .. py:method:: parse_variable() -> str

      Parses a variable, matching the grammar rule ``variable ::= identifier``. The current token must be a bare identifier; it is consumed and its source text returned.

      :raises FuzzyOntologyException: if the current token is not an identifier.

      :return: The variable name.

      :rtype: str



   .. py:method:: parse_weighted_concept() -> Any

      Parses a weighted aggregation concept, matching the grammar rule
      ``weighted_concept ::= "(" ("w-sum-zero"|"w-sum"|"w-max"|"w-min") weighted_part+ ")"``.
      The operator keyword and one or more weighted parts are consumed and
      forwarded as a flat list.

      :return: The parsed weighted aggregation concept.

      :rtype: typing.Any



   .. py:method:: parse_weighted_concept_part() -> Any

      Parses a weighted concept part, matching the grammar rule
      ``weighted_concept_part ::= "(" number concept ")"``. The three inner
      elements are consumed and forwarded to the callback as a flat list.

      :return: The parsed weighted concept part.

      :rtype: typing.Any



   .. py:attribute:: __slots__
      :value: ('tokens', 'pos', 'n')



   .. py:attribute:: n


   .. py:attribute:: pos
      :value: 0



   .. py:attribute:: tokens


.. py:function:: _kn(k: fuzzy_dl_owl2.fuzzydl.util.constants.FuzzyDLKeyword) -> str

   Returns the source-text literal (spelling) that a given :class:`FuzzyDLKeyword` matches in input.

   :param k: The keyword whose literal spelling is needed.
   :type k: FuzzyDLKeyword

   :return: The keyword's source-text literal.

   :rtype: str


.. py:data:: _APPROX_KW

.. py:data:: _AXIOM_KW

.. py:data:: _CMP_KW

.. py:data:: _CONCEPT_OP_AND_OR_IMPL

.. py:data:: _FEATURE_TYPE_KW

.. py:data:: _FUZZY_NUMBER_OP_BIN

.. py:data:: _FUZZY_NUMBER_OP_PAIR

.. py:data:: _K

.. py:data:: _OWA_INTEGRAL_KW

.. py:data:: _QUERY_KW

.. py:data:: _SHOW_KW

.. py:data:: _STATEMENT_KW

.. py:data:: _WEIGHTED_KW
