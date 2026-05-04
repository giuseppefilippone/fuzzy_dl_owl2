# Summary

A comprehensive framework for defining, manipulating, and evaluating fuzzy description logic concepts through a variety of mathematical constructs and architectural patterns.

## Description

The system provides a rich hierarchy of conceptual entities, ranging from weighted sums and integrals to threshold operations, to model complex fuzzy logic relationships. Abstract interfaces establish strict contracts for managing roles, values, and weights, ensuring state isolation through deep copy operations and separating data definitions from concrete implementations. Mathematical transformations are applied using a wrapper pattern that encapsulates base concepts with linear or triangular modifiers to adjust satisfaction degrees during semantic interpretation. Logical operations such as conjunction and disjunction are handled via operator overloading, while immutability is preserved during inference through recursive cloning and sub-concept replacement mechanisms.

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
- [`fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_zero_concept`] — 

## Sub-packages

- [`fuzzy_dl_owl2.fuzzydl.concept.concrete`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.interface`] — A collection of abstract interfaces defining the structural contracts for managing concepts, roles, values, and weights within a fuzzy description logic system.
- [`fuzzy_dl_owl2.fuzzydl.concept.modified`] — A collection of fuzzy description logic components that apply mathematical modifiers, such as linear scaling or triangular transformations, to adjust the satisfaction degree of base concepts.
