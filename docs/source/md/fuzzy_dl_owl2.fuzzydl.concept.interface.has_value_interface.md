# Summary

An abstract interface is provided for managing concepts that require both a specific role and an associated generic value.

## Description

Building upon the foundation of role management, this abstract class introduces the capability to associate an arbitrary value with a specific role. It encapsulates this data through a private attribute that is accessible and modifiable via public properties, ensuring that subclasses can represent or manipulate specific data within a defined context. The initialization process delegates role handling to the parent class while simultaneously storing the provided value, thereby combining role and value attributes into a cohesive interface. Although the documentation suggests isolation of state, the current implementation of the value setter assigns the object by reference rather than creating a deep copy, meaning that modifications to mutable objects will affect the internal state directly.
