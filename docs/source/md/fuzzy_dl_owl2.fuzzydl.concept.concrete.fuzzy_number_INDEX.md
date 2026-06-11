# Summary

A concrete implementation of triangular fuzzy numbers that supports fuzzy arithmetic, logical operations, and defuzzification.

## Description

Triangular fuzzy numbers are modeled using three distinct parameters defining the lower bound, peak, and upper bound of a membership function to represent uncertain or imprecise values. Standard arithmetic operations such as addition, subtraction, multiplication, and division are executed by applying interval arithmetic rules to these parameters, ensuring the generation of new instances with correctly calculated bounds. Logical operations like conjunction and disjunction are facilitated through delegation to an operator concept handler, allowing these numbers to integrate seamlessly into broader fuzzy logic expressions. Functionality for defuzzification converts the fuzzy representation into a single crisp value for performance evaluation, while utility methods assist in determining if an instance represents a crisp value or requires cloning for independent manipulation.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number`] — A concrete implementation of a triangular fuzzy number that supports fuzzy arithmetic, logical operations, and defuzzification.
