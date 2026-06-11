# Summary

A configuration manager that controls the visibility and display settings for concepts, individuals, roles, and variables within a fuzzy description logic ontology.

## Description

The software functions as a centralized state container for determining which components of a fuzzy description logic ontology should be rendered or analyzed during the solving process. It distinguishes between global visibility, where a specific attribute applies to all entities, and targeted visibility, which restricts the display to specific individuals or roles. By maintaining mappings between internal variable objects and human-readable names, the system ensures that complex mathematical representations can be presented in an understandable format. Furthermore, it integrates fuzzy logic concepts by associating linguistic labels with concrete feature fillers, allowing for nuanced display of membership degrees. The design supports state duplication through a cloning mechanism, enabling the preservation of configuration snapshots or the creation of alternative display scenarios without altering the original state.
