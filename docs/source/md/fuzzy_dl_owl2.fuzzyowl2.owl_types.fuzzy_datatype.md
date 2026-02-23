# Summary

An abstract base class defines the structure for fuzzy datatypes characterized by a lower and an upper bound within the FuzzyOWL2 framework.

## Description

The class establishes a foundational structure for representing fuzzy intervals by managing two primary attributes that correspond to the minimum and maximum values of the range. By initializing these boundaries to zero by default, the implementation provides a neutral state that concrete subclasses can modify to define specific fuzzy logic behaviors. Accessor and mutator methods are provided to retrieve and modify these internal values, allowing for dynamic adjustment of the interval's shape and support without enforcing strict validation logic during assignment. Designed for extensibility, the abstract nature of the class ensures that specific fuzzy set implementations can inherit this boundary management logic while defining their own operational semantics.
