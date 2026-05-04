# Summary

A Python class implementation modeling a right-shoulder fuzzy membership function within the FuzzyOWL2 framework.

## Description

The implementation extends the base fuzzy datatype to represent a specific type of membership function where values greater than a defined threshold possess full membership. Mathematically, the logic dictates that values below a lower bound have zero membership, while values above an upper bound are fully included, with a linear transition occurring between these two points. Internal state management relies on storing these boundary parameters, which are accessible via getter methods and utilized to generate a standardized string representation for debugging or serialization purposes. By inheriting from the parent datatype, the component integrates seamlessly into the broader ontology framework, allowing for the definition of vague or imprecise concepts using a right-shoulder distribution.
