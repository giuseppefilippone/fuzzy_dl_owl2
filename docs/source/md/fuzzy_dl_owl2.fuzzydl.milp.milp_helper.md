# Summary

A comprehensive manager for Mixed-Integer Linear Programming problems that translates fuzzy description logic constructs into mathematical optimization models and interfaces with various external solvers.

## Description

It bridges the gap between abstract fuzzy logic concepts—such as individuals, roles, and assertions—and concrete decision variables by maintaining internal registries for variables, constraints, and cardinalities. The software supports multiple solver backends, including Gurobi, MIP, and PuLP, delegating the actual solving process to these libraries while handling the specific translation of variable types and linear constraints. Additionally, it provides advanced features such as problem partitioning to handle large variable sets, support for crisp logic enforcement, and utilities for tracking and displaying solution values and linguistic label memberships.
