# Summary

A query mechanism that calculates the maximum degree of truth for a specific relationship between two individuals within a fuzzy knowledge base.

## Description

This component extends the functionality of relationship queries by focusing on optimization rather than simple verification, specifically seeking the highest possible truth value for a role assertion between two defined entities. By leveraging Mixed-Integer Linear Programming (MILP), the logic translates the fuzzy description logic constraints into mathematical expressions that can be solved numerically. During execution, the system isolates the problem by cloning the knowledge base to prevent side effects on the original data, then formulates an objective function that targets the specific variable representing the relationship degree. Error handling is integrated directly into the workflow to manage cases where the underlying ontology is inconsistent, ensuring that the process fails gracefully without corrupting the system state.
