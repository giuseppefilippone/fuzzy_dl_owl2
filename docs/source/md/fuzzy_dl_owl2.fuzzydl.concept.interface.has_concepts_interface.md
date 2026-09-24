# Summary

An abstract base class that provides its subclasses with shared, mutable storage for a collection of fuzzy concepts, along with a property for reading and replacing them.

## Description

**HasConceptsInterface** acts as a small reusable building block for objects in the fuzzy description-logic toolkit that wrap several **Concept** operands at once, such as compound concept expressions. Its constructor accepts any iterable of concepts and immediately materialises it into a plain Python list, which both exhausts one-shot generators and creates a shallow copy that decouples the object's internal state from the caller's original collection. The stored list is exposed through a property whose getter returns it unchanged and whose setter replaces it wholesale — again converting the incoming iterable to a list — so callers can swap the entire set of operands but never append to it piecemeal. Because the class is abstract and contributes no behaviour beyond this storage contract, concrete subclasses remain free to decide how the concepts they hold are interpreted or combined, while relying on the interface for consistent access to their operands.
