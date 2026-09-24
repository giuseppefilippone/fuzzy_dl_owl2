# Summary

An abstract base class for fuzzy description-logic queries that determine the degree to which a specific individual is an instance of a given concept, typically to find minimum or maximum membership degrees.

## Description

InstanceQuery anchors a family of graded-membership queries in a fuzzy description-logic reasoner, where an individual's belonging to a concept is a matter of degree rather than a simple yes-or-no fact. It extends a generic query abstraction and enforces a key modelling constraint at construction time: the supplied concept must be abstract, and passing a concrete (datatype-style) concept raises an error, since graded membership is only meaningful for abstract concepts. The concept and individual are kept as state, while a placeholder for a linear expression is deliberately left empty for subclasses to populate; once the query has been compiled into a mixed-integer linear program, that expression encodes the individual's degree of membership in the concept. By deferring both the expression construction and the solving logic to concrete subclasses, the design allows variants such as minimum- and maximum-degree queries to share validation and state management while specialising only the reasoning machinery.
