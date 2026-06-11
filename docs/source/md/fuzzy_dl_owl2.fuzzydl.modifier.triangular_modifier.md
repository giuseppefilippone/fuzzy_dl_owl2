# Summary

Implements a fuzzy logic modifier that applies a triangular membership function to concepts using three distinct boundary parameters to define degrees of membership.

## Description

The implementation defines a mathematical model where membership degrees increase linearly from a lower bound to a peak and then decrease linearly to an upper bound, effectively modeling vague or imprecise linguistic terms within a fuzzy description logic system. Upon initialization, the logic enforces strict ordering constraints on the boundary parameters to ensure the formation of a valid triangle, raising an error if the configuration is geometrically impossible. By wrapping base concepts into a specialized modified structure, the software allows for the dynamic evaluation of membership values based on the specific triangular shape defined by the instance. Furthermore, the design supports logical composition through operator overloading, enabling the combination or negation of modifiers to construct more complex fuzzy expressions while maintaining immutability and hashability for use in collections.
