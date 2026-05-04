# Summary

A data structure representing a weighted fuzzy concept that pairs a semantic category with a specific degree of satisfaction.

## Description

The software implements a mechanism for annotating entities within a fuzzy logic framework by associating a specific semantic concept with a quantitative degree of truth. This pairing allows for nuanced representation where an individual does not simply belong to a category but does so with a certain strength or probability. Equality comparisons are handled with strict type checking to ensure that two labels are considered identical only if their underlying concepts match and their weights are of the same class and value. The design supports both numeric and non-numeric degrees, providing flexibility in how truth values are calculated and compared while maintaining a consistent string representation for debugging and display.
