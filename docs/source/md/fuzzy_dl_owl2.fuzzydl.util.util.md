# Summary

Centralizes logging infrastructure and provides static helper methods for mathematical operations and data manipulation within the fuzzy description logic reasoner.

## Description

It establishes a robust logging framework that automatically creates timestamped directories and files to track reasoner activity, ensuring that debug output is only generated when explicitly enabled via configuration settings. The core functionality is encapsulated within a static utility class that acts as a centralized namespace for common operations, abstracting away the complexity of the underlying logging library and providing consistent error handling through custom exceptions. Mathematical helpers are included to handle precise decimal rounding using specific half-up logic and to perform calculations like determining the ceiling of a base-2 logarithm, which are essential for the numerical stability and logic processing of the reasoner. By integrating directly with the global configuration reader, these utilities ensure that behavior such as rounding precision and debug verbosity remains consistent across the entire application without requiring repeated setup.
