# Summary

Defines a fundamental logical constraint within a fuzzy logic framework by associating a specific concept with a minimum membership degree threshold.

## Description

The software models a basic logical statement in fuzzy description logics, specifically asserting that a particular concept possesses a membership degree that is at least equal to a specified lower bound. By encapsulating a `Concept` instance and a `Degree` instance, the implementation serves as a data structure that represents the condition where a concept's truth value meets or exceeds a defined threshold. Functionality is provided to retrieve the identifier of the concept and the specific degree value, ensuring that the components of the logical constraint can be accessed and utilized by other parts of the system. The design focuses on storing these two core elements and offering a string representation for debugging or logging, thereby acting as a foundational component for constructing more complex fuzzy logic assertions.
