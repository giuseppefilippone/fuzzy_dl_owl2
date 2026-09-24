# Summary

A comprehensive vocabulary of fuzzy description-logic concept expressions — spanning atomic concepts, quantified role restrictions, weighted aggregations and fuzzy integrals, linguistic modifiers, and concrete-domain membership functions — through which knowledge bases express graded membership over both symbolic and numeric features.

## Description

Fuzzy description logics extend classical description logics by letting concepts carry degrees of satisfaction in [0, 1] rather than crisp truth values, and the expression language built around that gradation spans the full spectrum: atomic concepts and nominals, quantified role restrictions such as ∃R.C and ∀R.C, has-value and self restrictions, threshold, truth-value, and implication-style constructs, and an extensive family of aggregation operators — weighted sums, weighted maxima and minima, ordered weighted averaging (OWA and QOWA), sigma-count quantifiers, and the Sugeno, quasi-Sugeno, and Choquet integrals — that fuse several sub-concepts into a single graded whole. Everything hangs off a common concept root, and logical composition is uniform across the board: negation, conjunction, and disjunction are exposed through Python's operator protocol — unary minus, `&`, and `|` — and delegated to a shared operator-concept factory, so any two expressions, however different their internal mathematics, combine into larger formulas with identical semantics and always yield fresh objects rather than mutating their operands. Instances behave as value-like types throughout: hashes and equality derive from structure rather than object identity, so expressions denoting the same logical construct deduplicate in sets and dictionaries, while cloning, recursive decomposition into atomic concepts and roles, and non-destructive substitution of one sub-concept by another are available across the whole hierarchy.

Operand storage is factored out of the concrete constructors into a layer of small abstract mixin interfaces, each declaring property-based storage for one kind of payload — a single wrapped concept, a collection of concepts, a role, an arbitrary filler value, or a weighted set of concepts — so every operand-bearing expression inherits a predictable, encapsulated way to track what it operates on. The weighted-concepts contract in particular is reused by the weighted aggregation family, one of whose members, the weighted sum zero constructor, validates at build time that its weights total no more than 1.0 and reports violations through a central error-handling utility.

Concrete-domain reasoning — graded truth over real-valued features such as temperature or price — rests on a template-method hierarchy in which an abstract base owns and validates the numeric domain interval while subclasses supply the actual membership curves: crisp intervals, left- and right-shoulder ramps, triangular and trapezoidal functions, and knee-pointed linear ramps, complemented by triangular fuzzy numbers that embed uncertain quantities directly into knowledge bases and carry their own fuzzy arithmetic (addition, subtraction, multiplication, and division via the extension principle) together with defuzzification. Linguistic hedges such as *very* or *somewhat* are applied through a decorator pattern — thin wrappers that pair any concept with a modifier and reshape its degrees linearly or non-linearly while delegating all structural questions to the wrapped concept — and the same idea reappears inside the concrete-domain family, where modified concrete concepts transform the membership degrees of any wrapped numeric term. Constructors validate fail-fast so malformed shapes never reach the reasoning engine, and several membership evaluations deliberately correct latent defects inherited from the original Java implementation.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.concept.all_some_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.approximation_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.atomic_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.choquet_integral`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.ext_threshold_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.has_value_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.implies_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.negated_nominal`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.operator_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.owa_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.qowa_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.quasi_sugeno_integral`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.self_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.sigma_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.sigma_count`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.string_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.sugeno_integral`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.threshold_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.truth_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.value_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.weighted_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.weighted_max_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_concept`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_zero_concept`] — A fuzzy description-logic concept that aggregates multiple sub-concepts under individually assigned weights, enforcing the constraint that those weights sum to no more than 1.0.

## Sub-packages

- [`fuzzy_dl_owl2.fuzzydl.concept.concrete`] — A family of concrete-domain fuzzy concepts for fuzzy description-logic reasoning, defining graded membership over numeric intervals in shapes ranging from crisp intervals and shoulder ramps to triangular, trapezoidal, and piecewise-linear curves, and extended with linguistic modifiers and triangular fuzzy numbers that carry their own fuzzy arithmetic.
- [`fuzzy_dl_owl2.fuzzydl.concept.interface`] — A family of abstract mixin interfaces that standardise how fuzzy description-logic concept expressions store, inspect, and replace the operands they carry, whether a single concept, a collection of concepts, a role, a filler value, or a weighted set of concepts.
- [`fuzzy_dl_owl2.fuzzydl.concept.modified`] — A family of fuzzy description-logic concepts that pair an arbitrary concept with a linguistic modifier such as "very" or "slightly", reshaping the degree to which individuals satisfy the wrapped concept.
