# Summary

Models a fuzzy logic assertion that associates an individual with a concept subject to a minimum membership degree threshold.

## Description

The software represents a logical constraint where an individual entity belongs to a concept with a specific lower bound, effectively capturing the expression $a:C \ge d$. It maintains references to the subject, the category, and the required degree, providing mechanisms to access and modify these internal states. A distinctive feature of the implementation is its custom equality logic, which treats two assertions as equivalent if they share the same subject and concept while the numeric degree of the first is strictly less than the second, alongside standard string-based equality. Furthermore, the design supports object cloning and produces a string representation that clearly delineates the individual, concept, and threshold value.
