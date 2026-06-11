# Summary

Models a fuzzy logic constraint stating that an individual belongs to a concept with a minimum degree of membership.

## Description

Encapsulating the logical expression $a:C \ge d$, the implementation links a specific entity to a category while enforcing a threshold for the strength of that association. Three primary components define the structure: the subject individual, the target concept, and a degree value that acts as a lower bound for the assertion's validity. Beyond simple data storage, the design supports cloning and dynamic modification of the individual or degree, allowing the constraint to be adjusted during reasoning processes. A distinctive aspect of the behavior is the equality comparison, which considers two assertions equivalent if they share the same individual and concept while the current instance holds a numerically lower degree than the compared instance, facilitating the ordering of fuzzy constraints. The textual representation follows a standard format combining the individual, concept, and degree to clearly display the logical constraint.
