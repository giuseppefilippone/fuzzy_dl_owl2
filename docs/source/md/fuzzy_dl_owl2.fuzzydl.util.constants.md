# Summary

A central configuration module that defines enumerations, type aliases, and global constants for a fuzzy description logic reasoning system.

## Description

The software establishes a comprehensive schema of types and configurations required for fuzzy description logic reasoning, utilizing Python enumerations to enforce type safety across the application. It defines specific categories for mixed-integer linear programming solvers, feature data types, and complex logical operators, including various t-norms, t-conorms, and aggregation methods like Choquet and Sugeno integrals. A significant portion of the logic is dedicated to mapping the specific vocabulary of the FuzzyDL language to parsing objects, enabling the interpretation of domain-specific syntax through the `pyparsing` library. Additionally, the module initializes global environment settings such as result storage directories and numerical limits, ensuring consistent behavior for optimization tasks and file I/O operations throughout the system.
