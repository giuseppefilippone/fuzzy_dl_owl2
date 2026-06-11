# Summary

A semantic action handler that transforms parsed tokens into a Fuzzy Description Logic knowledge base and associated query objects.

## Description

The software serves as a collection of semantic callbacks designed to construct a domain model from raw input tokens, effectively bridging the gap between syntactic parsing and the internal representation of a Fuzzy Description Logic knowledge base. By converting strings and numeric values into specialized objects such as concepts, individuals, degrees, and mathematical expressions, the logic ensures that the resulting structure adheres to the specific semantics of the chosen fuzzy logic, whether it be Zadeh, Lukasiewicz, or classical. Beyond simple object creation, the implementation enforces strict validation rules, such as distinguishing between abstract and concrete roles or verifying that fuzzy-specific operators are not used in incompatible reasoning contexts. Furthermore, the system manages the accumulation of query objects and Mixed-Integer Linear Programming constraints, preparing the entire model for subsequent reasoning and execution tasks.
