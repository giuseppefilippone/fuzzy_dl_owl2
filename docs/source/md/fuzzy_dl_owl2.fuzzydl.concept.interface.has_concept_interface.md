# Summary

An abstract interface that lets implementing classes wrap, inspect, and replace a single fuzzy `Concept` object through a managed property.

## Description

`HasConceptInterface` defines a small mixin contract for any entity in the fuzzy description-logic framework that operates on exactly one concept, such as unary concept constructors or modifiers. Subclasses initialise the wrapper by passing a `Concept` to the constructor, which stores it by reference in a private attribute; because no validation or deep copying is performed, later mutations of the original `Concept` remain visible through the wrapper. All access is funnelled through the `curr_concept` property, whose getter exposes the currently wrapped operand and whose setter allows that operand to be swapped for a different concept at runtime. Centralising the storage-and-update logic behind a property gives every concrete concept-wrapping type a uniform, encapsulated way to track the operand it is currently manipulating, while deriving from `abc.ABC` marks the class as intended for inheritance rather than direct instantiation.
