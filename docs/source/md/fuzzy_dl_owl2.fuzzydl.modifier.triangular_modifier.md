# Summary

A fuzzy logic modifier that applies a triangular membership function to concepts based on three defining parameters.

## Description

The software implements a specific type of fuzzy logic modifier characterized by a triangular membership function, which determines the degree to which a value belongs to a concept based on three distinct parameters: a left boundary, a peak, and a right boundary. By enforcing the constraint that the left boundary must be less than or equal to the peak, which in turn must be less than or equal to the right boundary, the implementation ensures a valid geometric shape where membership increases linearly from zero to one and then decreases back to zero. When applied to a base concept, the logic wraps the original entity into a specialized structure that incorporates these triangular characteristics, allowing for the dynamic calculation of membership degrees for any given input value. Furthermore, the design supports logical composition by overloading standard operators to perform conjunctions, disjunctions, and negations, effectively enabling the combination of multiple triangular modifiers into complex fuzzy expressions.
