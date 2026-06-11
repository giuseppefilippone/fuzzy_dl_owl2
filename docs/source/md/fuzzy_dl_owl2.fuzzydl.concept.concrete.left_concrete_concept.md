# Summary

Implements a left shoulder fuzzy set concept where membership degrees are maximized at lower values and decrease linearly towards zero based on defined interval parameters.

## Description

The software models a left shoulder fuzzy set, a mathematical construct used to represent concepts where membership is highest at lower numerical values and diminishes as values increase. It relies on four numerical parameters—two defining the domain of validity and two defining the transition interval—to calculate membership degrees, ensuring that inputs satisfy strict ordering constraints during initialization to maintain logical consistency. Membership calculation returns full validity for values below a specific threshold, zero validity for values above an upper threshold, and a linearly interpolated score for values falling within the transition range. By overloading standard Python operators, the implementation supports logical combinations such as negation, conjunction, and disjunction, allowing these fuzzy concepts to be integrated into complex logical expressions within a broader fuzzy description logic framework.
