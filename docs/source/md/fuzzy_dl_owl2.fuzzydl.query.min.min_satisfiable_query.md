# Summary

A query implementation that determines the minimal degree of satisfiability for a fuzzy concept within a knowledge base, optionally scoped to a specific individual.

## Description

The software transforms the logical problem of determining concept satisfiability into a mathematical optimization task that minimizes a specific threshold variable. By extending the base satisfiability logic, it supports evaluation against the general ontology or a specific individual, utilizing a Mixed-Integer Linear Programming solver to compute the result. During execution, the implementation clones the provided knowledge base to ensure the original state remains unaltered, while also activating dynamic blocking mechanisms if existential quantifiers are detected in the concept definition. The process involves creating a semi-continuous variable to represent the objective function, linking it to the negated conclusion of the query, and finally optimizing the constraints to return the lowest possible degree or an inconsistency status.
