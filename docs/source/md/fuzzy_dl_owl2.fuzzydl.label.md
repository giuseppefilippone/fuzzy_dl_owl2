# Summary

Encapsulates a fuzzy concept paired with a specific degree of satisfaction to form a weighted annotation.

## Description

The implementation associates a semantic category, defined by a `Concept` object, with a quantitative strength represented by a `Degree` instance. Equality comparisons are handled with strict type checking to ensure that two labels are considered identical only if their underlying concepts match and their weights are of the same class and value. A static helper method manages the comparison logic for degrees, distinguishing between numeric values that require exact matching and non-numeric types that rely on class identity. By overriding standard magic methods, the class ensures that instances behave predictably when compared for equality or converted to string representations for display.
