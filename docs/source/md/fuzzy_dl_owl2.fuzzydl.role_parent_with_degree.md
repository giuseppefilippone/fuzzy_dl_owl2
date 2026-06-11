# Summary

Encapsulates a weighted relationship between a role and its parent by storing the parent's identifier and an associated degree of inclusion.

## Description

Designed to represent fuzzy inheritance or hierarchical connections where a parent role contributes to a child role with a specific weight or probability, a string identifier for the parent entity is stored alongside a floating-point value that quantifies the strength or degree of this relationship. Access to these attributes enables complex reasoning about role hierarchies where relationships are not absolute but graded, allowing the system to calculate the extent to which a parent role is included. The implementation acts as a simple container, allowing other components to query the parent name and the associated metric to determine how much influence the parent role exerts.
