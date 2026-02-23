# Summary

Defines a class that applies linear transformations to fuzzy logic membership degrees within the FuzzyOWL2 framework.

## Description

Extending the base functionality of fuzzy modifiers, this implementation introduces a linear transformation mechanism designed to scale or adjust membership degrees. The core logic relies on a single floating-point coefficient provided during instantiation, which dictates the intensity or nature of the linear adjustment applied to fuzzy values. By encapsulating this coefficient as a private attribute, the design ensures that the transformation parameter remains consistent and accessible only through specific accessor methods. Furthermore, the implementation includes a string representation that clearly identifies the modifier type and its associated coefficient, facilitating easier debugging and logging within the broader system.
