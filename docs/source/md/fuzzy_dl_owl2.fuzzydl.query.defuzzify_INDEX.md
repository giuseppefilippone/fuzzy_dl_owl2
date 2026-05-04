# Summary

A suite of defuzzification strategies converts fuzzy membership degrees into crisp numerical values by leveraging Mixed-Integer Linear Programming to optimize objective expressions within a constrained knowledge base.

## Description

An abstract base class orchestrates the common workflow required to transform fuzzy logic results into precise numbers, establishing a constrained environment by asserting the maximum degree of membership into a cloned knowledge base. By identifying the mathematical variable associated with a target feature, the system utilizes a mathematical optimization engine to solve Mixed-Integer Linear Programming problems, where the specific objective function determines the final crisp output. Subclasses implement distinct defuzzification methods by defining unique optimization objectives, such as identifying the smallest or largest value within the region of maximum membership or calculating the arithmetic mean of these boundaries. This architecture centralizes the logic for handling ontology inconsistencies and solving constraints while allowing flexibility in how the target variable is manipulated to achieve the desired numerical result.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query`] — An abstract base class that defines the structure for defuzzifying fuzzy logic queries by converting membership degrees into crisp values using Mixed-Integer Linear Programming.
- [`fuzzy_dl_owl2.fuzzydl.query.defuzzify.lom_defuzzify_query`] — Implements the Largest of Maxima defuzzification strategy to determine the highest crisp value within the region of maximum membership for a specific feature.
- [`fuzzy_dl_owl2.fuzzydl.query.defuzzify.mom_defuzzify_query`] — Implements the Mean of Maxima defuzzification strategy to calculate a crisp feature value for an individual within a fuzzy ontology.
- [`fuzzy_dl_owl2.fuzzydl.query.defuzzify.som_defuzzify_query`] — A specialized query implementation applies the Smallest of Maxima strategy to convert fuzzy logic values into crisp numerical outputs.
