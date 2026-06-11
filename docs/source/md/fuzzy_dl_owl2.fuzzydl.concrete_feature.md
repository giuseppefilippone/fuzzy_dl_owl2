# Summary

A class that models a specific attribute of an individual characterized by a name and a data type such as string, boolean, integer, or real.

## Description

The implementation provides a flexible mechanism for defining attributes that can represent various data categories, automatically inferring the specific type based on the arguments provided during instantiation. When initialized with a single string, the attribute defaults to a string type, while the presence of a boolean flag explicitly designates the attribute as boolean, and the inclusion of numeric boundaries establishes an integer or real range. Delegation to distinct helper methods ensures that the appropriate type and boundary values are assigned to the instance, while runtime modification of type and range constraints remains supported alongside a cloning capability that generates independent copies.
