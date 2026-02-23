# Summary

A configuration manager that controls the visibility and display of elements within a fuzzy description logic ontology, including atomic concepts, individuals, abstract roles, and concrete features.

## Description

The software acts as a centralized registry for determining which components of a fuzzy description logic ontology should be rendered or tracked during processing. It distinguishes between global visibility, where specific roles or features apply to every individual, and targeted visibility, which restricts display settings to a defined subset of individuals. By maintaining separate collections for atomic concepts, individuals, abstract roles, and concrete features, the system allows fine-grained control over the output of membership degrees and filler values. Furthermore, it integrates fuzzy logic by associating concrete feature fillers with linguistic labels and maps internal variable objects to human-readable strings for presentation. The design supports state cloning, enabling the preservation of specific display configurations without affecting the original state, which is crucial for iterative processing or branching logic within the MILP solver context.
