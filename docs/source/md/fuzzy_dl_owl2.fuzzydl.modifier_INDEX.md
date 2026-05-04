# Summary

A fuzzy logic subsystem that transforms the membership degrees of concepts through configurable mathematical functions.

## Description

An abstract base class defines the structural blueprint for these transformations, enforcing a consistent interface that ensures all resulting values remain strictly bounded within the normalized range of zero to one. Concrete implementations utilize this foundation to apply specific geometric or algebraic rules, such as piecewise linear scaling or triangular shaping, thereby adjusting the intensity of linguistic hedges. By wrapping existing concepts and supporting standard logical operators like conjunction and disjunction, the architecture facilitates the dynamic composition of complex fuzzy expressions from these fundamental modifications.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier`] — A fuzzy logic modifier that applies a configurable piecewise linear transformation to the membership degrees of concepts.
- [`fuzzy_dl_owl2.fuzzydl.modifier.modifier`] — An abstract base class defines the interface for fuzzy logic modifiers that transform concepts and calculate adjusted membership degrees.
- [`fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier`] — A fuzzy logic modifier that applies a triangular membership function to concepts based on three defining parameters.
