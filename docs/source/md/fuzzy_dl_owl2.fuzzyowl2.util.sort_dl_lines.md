# Summary

Sorts fuzzy-DL statements according to a specific syntax hierarchy derived from the official language documentation.

## Description

The software defines a comprehensive list of regular expressions that correspond to the specific sequence of commands presented in the fuzzy-DL reference manual, ensuring that generated or processed code adheres to this canonical structure. By matching input statements against these compiled patterns, the logic assigns a numerical rank to each line, effectively classifying commands like concept definitions, role properties, and queries into their correct positions. Once ranked, the statements are sorted primarily by this rank and secondarily by their content, with the added capability to insert a separator string between distinct groups of command types. Unrecognized statements that do not match any defined pattern are automatically relegated to the end of the output to maintain stability without disrupting the known order.
