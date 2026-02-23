# Summary

Defines a crisp function data structure for modeling precise mathematical intervals within the FuzzyOWL2 ontology framework.

## Description

The software implements a specialized datatype designed to integrate exact, non-fuzzy mathematical constraints into a fuzzy logic environment. By extending the base fuzzy datatype, it allows for the representation of linear transformations or precise intervals defined by specific coefficients. The core functionality revolves around storing two primary numerical parameters, typically interpreted as coefficients for a linear equation, while relying on inherited attributes to define the lower and upper bounds of the interval. Access to these internal values is provided through getter methods, ensuring that the precise state of the function can be retrieved without modification. A string representation formats the bounds and coefficients together, facilitating debugging and display within the broader ontology system.
