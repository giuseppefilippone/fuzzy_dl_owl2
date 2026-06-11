# Summary

Implements a fuzzy logic modifier that transforms concept membership degrees using a configurable piecewise linear function.

## Description

The software defines a mechanism for altering the membership degrees of fuzzy concepts through a piecewise linear transformation, controlled by a single shape coefficient. Upon initialization, the coefficient is used to derive two internal weights that define the inflection point and slope of the transformation, ensuring the output remains normalized within the zero-to-one range. When applied to a concept, the logic generates a specialized wrapper object that encapsulates both the original concept and the transformation rules, allowing the modified membership to be calculated dynamically based on input values. To support complex logical reasoning, the implementation includes operator overloading for conjunction, disjunction, and negation, delegating these operations to a central factory for concept construction while maintaining immutability of the original modifier.
