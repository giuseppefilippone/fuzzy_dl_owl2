# Summary

Determines the maximum degree to which one fuzzy concept is subsumed by another by transforming the logical relationship into a minimization problem within a knowledge base.

## Description

MaxSubsumesQuery handles the computation of subsumption degrees by leveraging mixed-integer linear programming to optimize an objective derived from fuzzy logic implications. Depending on the configured operator type, such as Łukasiewicz or Zadeh, the logic constructs a corresponding implication or operator concept to represent the relationship between the input concepts. To preserve the integrity of the original data, the process operates on a cloned instance of the knowledge base, optionally solving the ABox before proceeding with the optimization. The preprocessing phase creates a new individual and links it to the constructed concept, setting the associated variable as the objective to be minimized. Finally, the optimization routine attempts to find the minimum value for this variable, which corresponds to the maximum subsumption degree, while gracefully managing exceptions related to inconsistent ontologies.
