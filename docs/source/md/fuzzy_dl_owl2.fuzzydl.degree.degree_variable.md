# Summary

A symbolic degree of satisfaction that wraps a linear-programming variable, allowing unknown fuzzy truth values to be embedded in algebraic expressions and inequality constraints that a solver can later resolve.

## Description

In fuzzy description-logic reasoning, the degree to which an individual satisfies a concept is often not a known constant but an unknown that must be determined by an optimization solver. **DegreeVariable** addresses this by wrapping a single `Variable` from the mixed-integer linear programming subsystem and presenting it through the `Degree` interface, so symbolic degrees can flow through the same code paths as numeric ones. Because it is symbolic rather than a fixed quantity, it consistently reports itself as non-numeric — never a plain number, never zero, never one — which lets callers distinguish solver-resolved values from hardcoded constants.

The wrapper supplies the algebraic operations the degree abstraction demands: it can add or subtract itself from an expression (using coefficients of +1.0 and −1.0 respectively), scale itself by a constant to produce a fresh linear expression, and build an inequation comparing a given expression against the wrapped variable, which is how constraints such as "the satisfaction level must be at least this expression's value" get encoded for the solver. All of these operations are purely functional, returning new expression or inequation objects without mutating the wrapped variable or their inputs.

Identity is deliberately shallow: equality and hashing delegate entirely to the underlying variable, so two wrappers around the same variable are interchangeable and safe to use in sets and dictionaries. A static factory method and a clone operation both create new wrappers over the same variable rather than copying it, reinforcing the design decision that the wrapper acts as a transparent handle rather than an owner of state. A simple string rendering, formatted as *Degree(variable)*, supports debugging and logging.
