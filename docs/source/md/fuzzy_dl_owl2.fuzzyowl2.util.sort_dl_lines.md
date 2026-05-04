# Summary

Implements a sorting mechanism for fuzzyDL statements that arranges them according to the specific syntax order presented in the official PDF documentation.

## Description

The software relies on a comprehensive list of regular expressions that mirror the sequential appearance of commands in the fuzzyDL reference manual, ensuring that generated or processed code adheres to a standardized visual structure. By matching input strings against these compiled patterns, the logic assigns a specific rank to each statement, allowing for a primary sort based on documentation order and a secondary sort based on the string content itself. Once sorted, the results are grouped by their assigned rank, and a customizable separator is inserted between distinct groups to visually distinguish different categories of fuzzyDL commands. Statements that do not match any known pattern are assigned a high priority value, effectively pushing them to the end of the output while maintaining the overall organization of recognized elements.
