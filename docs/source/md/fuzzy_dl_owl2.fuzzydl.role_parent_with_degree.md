# Summary

Models a weighted hierarchical relationship between a role and its parent by storing a parent identifier and an associated degree of inclusion.

## Description

Designed to support complex role inheritance logic, this structure captures the extent to which a parent role is included within a child role. It associates a string identifier representing the parent with a floating-point value that quantifies the strength or probability of the relationship, typically ranging from zero to one. The implementation acts as a simple data container, storing these values directly upon initialization without applying validation logic. Accessor methods are provided to retrieve the stored parent name and degree, allowing other components of the system to inspect the specific weights assigned to hierarchical connections.
