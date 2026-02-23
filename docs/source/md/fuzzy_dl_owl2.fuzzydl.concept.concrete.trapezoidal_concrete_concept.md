# Summary

Implements a trapezoidal concrete concept that models fuzzy membership degrees using a four-point geometric shape within a defined domain.

## Description

The logic calculates membership values by defining a support interval where the degree is zero, a core interval where the degree is one, and linear transitions between these states based on specific vertex parameters. Strict validation ensures that the geometric parameters adhere to the required ordering and that the universe of discourse fully contains the trapezoid's shape to prevent mathematical inconsistencies. By overriding standard operators, the implementation enables logical combinations such as AND, OR, and NOT, delegating the complex computations to a dedicated operator utility. Additional functionality includes generating string representations for identification and creating independent copies of the instance to preserve state integrity during manipulation.
