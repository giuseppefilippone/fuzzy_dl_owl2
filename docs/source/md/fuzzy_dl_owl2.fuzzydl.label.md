# Summary

Encapsulates a fuzzy concept paired with a degree of satisfaction to represent weighted annotations.

## Description

The software defines a data structure that associates a semantic category with a quantitative truth value, enabling the representation of fuzzy logic annotations where membership is not strictly binary. By storing a specific concept alongside a weight between zero and one, it allows for the nuanced description of individuals based on the extent to which they satisfy a particular property. Equality comparisons are implemented with strict type checking to ensure that two instances are considered identical only if their underlying concepts match and their weights share both the same class and numerical value. A static helper method handles the complexity of weight comparison by distinguishing between numeric degrees, which require value checks, and non-numeric degrees, which rely on type identity. This design supports the broader fuzzy description logic system by providing a fundamental unit for expressing graded relationships and ensuring consistent behavior during logical operations.
