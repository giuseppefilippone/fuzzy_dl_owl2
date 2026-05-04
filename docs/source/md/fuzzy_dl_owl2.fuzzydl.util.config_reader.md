# Summary

A centralized configuration manager for a fuzzy description logic reasoning engine that loads parameters from files and command-line arguments to control precision, optimization strategies, and solver selection.

## Description

The software establishes a single source of truth for operational parameters, defining default values for critical aspects such as the precision threshold, maximum individual generation limits, and various blocking optimizations used during reasoning. By leveraging the standard configuration parser, it reads settings from an external file and supports runtime overrides through a list of string arguments, allowing users to customize behavior without modifying the source code. During the loading process, the logic automatically derives secondary values, such as the number of precision digits based on the epsilon threshold, and dynamically updates global constants within the application to align with the numerical limits of the selected Mixed-Integer Linear Programming (MILP) solver. Error handling mechanisms are included to catch file access or parsing issues, printing diagnostic messages to standard output to aid troubleshooting while attempting to preserve a valid configuration state.
