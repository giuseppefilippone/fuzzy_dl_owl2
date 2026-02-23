# Summary

A fuzzy description logic restriction that enforces a specific value for a given role, constrained by a degree of membership.

## Description

Models a logical constraint where a specific role must be associated with a particular individual, incorporating a fuzzy degree to represent the strength or lower bound of this relationship. Extending the base `Restriction` class allows the component to leverage common attributes for role names and degrees while specifically storing the identifier of the target individual. The implementation represents the constraint as a negated existential quantification, translating the "has value" assertion into a specific string format required by the underlying system. Accessor methods enable the retrieval of the individual's name and the formatted logical expression, facilitating the integration of these constraints into broader reasoning tasks.
