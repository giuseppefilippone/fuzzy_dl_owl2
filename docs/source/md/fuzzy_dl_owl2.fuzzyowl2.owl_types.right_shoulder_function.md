# Summary

A Python class representing a right-shoulder fuzzy membership function used to model concepts where membership increases linearly to full certainty after a specific threshold.

## Description

The implementation extends the base fuzzy datatype to encapsulate the mathematical behavior of a right-shoulder curve, which is essential for representing vague concepts where values exceeding a certain point are considered fully true. By utilizing two floating-point parameters, the logic defines a transition interval where membership degrees rise linearly from zero to one, ensuring that values below the lower bound have no membership while those above the upper bound are fully accepted. Accessor methods are provided to retrieve the specific boundary values, allowing external systems to query the configuration of the fuzzy set. A string representation is also included to facilitate debugging and logging by displaying the internal state in a human-readable format that incorporates both the specific parameters and inherited attributes.
