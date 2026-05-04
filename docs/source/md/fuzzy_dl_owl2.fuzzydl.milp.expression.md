# Summary

A linear mathematical expression model represents the degree of satisfaction of concepts within fuzzy description logic ontologies.

## Description

It supports flexible construction from numeric constants, collections of variables, or existing expression instances, allowing for the representation of forms such as $c + c_1x_1 + \dots + c_nx_n$. The design incorporates operator overloading to handle arithmetic operations like addition, subtraction, and scalar multiplication seamlessly, ensuring that interactions with other expressions, terms, or numbers behave intuitively. To maintain a canonical internal structure, the logic automatically consolidates terms by merging coefficients whenever operations involve the same variable, thereby preventing duplicate entries. Furthermore, the implementation includes capabilities for cloning, negation, and string generation, which facilitate its use in complex algebraic computations and mixed-integer linear programming contexts.
