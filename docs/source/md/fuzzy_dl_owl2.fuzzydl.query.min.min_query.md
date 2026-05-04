# Summary

A query implementation that calculates the minimum possible value of a specific expression within a fuzzy description logic knowledge base.

## Description

The software extends the generic query framework to support optimization tasks focused on finding the lowest possible value for a given mathematical expression. By accepting an objective expression during instantiation, the logic prepares to evaluate this target against the constraints and data contained within a fuzzy description logic knowledge base. During execution, the process first resolves the assertional box (ABox) to ensure consistency before creating a clone of the knowledge base to perform the actual optimization without altering the original state. Error handling is integrated to manage scenarios where the underlying ontology is inconsistent, returning a specific failure solution instead of crashing, while also tracking the total time required for the resolution and optimization phases.
