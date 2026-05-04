# Summary

A class representing a fuzzy role assertion that connects two individuals via a specific relationship type and a lower bound degree.

## Description

The software models a role assertion within a fuzzy description logic framework, defining a binary connection between a subject individual and an object individual. It encapsulates the properties of the relationship, including the role name, the two participating entities, and a lower bound degree that represents the minimum truth value required for the assertion to hold. The design allows for the dynamic modification of the subject and object individuals after instantiation, ensuring flexibility in constructing and updating knowledge graphs. Furthermore, the implementation provides mechanisms for cloning the assertion to create independent copies and generating string representations that either include or exclude the degree constraint for various reporting needs.
