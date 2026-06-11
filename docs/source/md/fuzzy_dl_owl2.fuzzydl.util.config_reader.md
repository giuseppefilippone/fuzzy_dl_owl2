# Summary

A centralized configuration manager that loads and applies settings for a fuzzy reasoning engine from INI or environment files.

## Description

The software establishes a set of default parameters governing the behavior of a fuzzy reasoning engine, including precision thresholds, optimization levels, and blocking strategies. It provides a flexible loading mechanism that prioritizes a specified INI configuration file but falls back to a `.env` file located in the current working directory if the primary source is unavailable. Input values are normalized to handle case and underscore variations, ensuring compatibility between different configuration formats, while specific overrides can be applied directly to the loaded settings. Once the parameters are loaded, the system automatically derives internal precision metrics and adjusts global numerical limits within the application to match the specific capabilities of the chosen Mixed-Integer Linear Programming solver.
