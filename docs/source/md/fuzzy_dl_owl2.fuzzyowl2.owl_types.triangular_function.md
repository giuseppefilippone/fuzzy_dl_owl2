# Summary

Implements a triangular membership function for fuzzy logic systems, characterized by three defining points.

## Description

The software models a specific type of fuzzy set using a geometric shape defined by three distinct floating-point parameters representing the left boundary, the peak, and the right boundary. By inheriting from a base datatype class, it integrates into a broader framework designed for handling fuzzy constraints and reasoning within ontologies. Encapsulation is achieved through private attributes and public accessor methods, ensuring that the geometric configuration remains immutable after initialization while allowing read access for computational purposes. A string representation method is provided to facilitate debugging and logging by displaying the current configuration in a constructor-like format, including parameters potentially inherited from the parent class.
