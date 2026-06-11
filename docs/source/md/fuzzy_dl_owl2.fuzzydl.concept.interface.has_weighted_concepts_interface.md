# Summary

An abstract interface extending the basic concept management contract to include support for numerical weights associated with each concept.

## Description

Building upon the foundation of managing generic concepts, this abstract class introduces the capability to associate specific numerical values or magnitudes with those concepts. It enforces a structural pattern where objects must handle a mutable list of floating-point weights, allowing for dynamic updates or the complete removal of weighting information. The design utilizes property decorators to encapsulate the internal storage of these weights, ensuring that any provided iterable is converted into a list or explicitly set to null to represent an unweighted state. By integrating this functionality directly into the inheritance hierarchy, the class facilitates the creation of complex fuzzy logic constructs where concepts contribute to a result with varying degrees of importance.
