# Summary

Defines the AtomicConcept class as an indivisible base unit within a conceptual hierarchy, serving as the fundamental building block for constructing complex logical expressions.

## Description

The class represents the most granular element in the system, identified uniquely by a string name, and functions as a leaf node that cannot be decomposed further into sub-concepts. To facilitate the construction of complex logical structures, it overloads standard Python operators for conjunction, disjunction, and negation, delegating the actual creation of composite objects to a separate operator class. Identity and comparison rely strictly on the assigned name, ensuring that distinct instances with identical labels are treated as the same entity, which is crucial for hashing and storage in collections. Traversal and manipulation methods, such as retrieving atomic components or performing replacements, consistently return the instance itself or a singleton collection, acting as the base case for recursive algorithms operating on the concept graph. Additionally, a static factory method enables the automatic generation of unique identifiers using a global counter, supporting the dynamic creation of concepts during runtime.
