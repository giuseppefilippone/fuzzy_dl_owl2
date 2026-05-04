# Summary

Defines a core entity class representing a specific instance within a fuzzy description logic knowledge base, managing concept assertions, role relations, and restrictions during reasoning processes.

## Description

The software implements a fundamental node structure used in description logic reasoning, specifically designed to handle the state of an entity within a knowledge base. It manages various semantic properties, including concept assertions, role connections to other entities, and specific constraints such as concrete role restrictions or "not self" rules. To support tableau-based reasoning algorithms, the architecture includes mechanisms for cloning the entire internal state, allowing the system to explore different branches of logic without mutating the original data. Additionally, the logic provides functionality to prune role relations and recursively clean up blockable successors, which optimizes memory usage and performance during complex inference tasks. The design enforces strict identity rules by raising exceptions when naming conflicts occur, ensuring that the unique name assumption is maintained throughout the reasoning process.
