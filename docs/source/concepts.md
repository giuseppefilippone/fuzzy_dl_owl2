# Fuzzy Concepts

The fuzzy concept currently implemented are as follows.

| Class name | Description |
| --- | --- |
| Concept | Defines a base class of any concept |
| AtomicConcept | Defines an atomic concept |
| TruthConcept | Defines the top $\top$ and bottom $\perp$ concepts |
| OperatorConcept | It is the class to handle a logic (Zadeh, Lukasiewicz, and product) connectives (and, or, not) between fuzzy concepts |
| AllSomeConcept | Defines a universal (all) and existential (some) restrictions on fuzzy concepts |
| ChoquetIntegral | Defines a Choquet integral of fuzzy concept |
| SugenoIntegral | Defines a Sugeno integral of fuzzy concept |
| QsugenoIntegral | Defines a Quasi-Sugeno integral of fuzzy concept |
| OwaConcept | Defines a OWA concept |
| QowaConcept | Defines a quantified-guided OWA concept |
| ApproximationConcept | Defines all a uppers and lowers approximation concept |
| ThresholdConcept | Defines a positives and negatives threshold concept |
| ExtendedThresholdConcept | Defines a extended positives and negatives threshold concept |
| ImpliesConcept | Defines a zadeh and goedel implies concept |
| HasValueConcept | Defines a concept associated with a value |
| NegatedNominal | Defines a negated nominal concept |
| SelfConcept | Defines a self reflexivity concept |
| ValueConcept | Defines a datatype restriction (at most, at least, and exact) concept |
| WeightedConcept | Defines a weighted concept |
| WeightedMinConcept | Defines a weighted min concept |
| WeightedMaxConcept | Defines a weighted max concept |
| WeightedSumConcept | Defines a weighted sum concept |
| WeightedSumZeroConcept | Defines a weighted sum-zero concept |
| SigmaConcept | Defines a sigma-count concept |
| ModifiedConcept | Defines the base class for modified (linear and triangular) concepts |
| LinearlyModifiedConcept | Define a linearly modified concept |
| TriangularlyModifiedConcept | Define a triangularly modified concept |
| FuzzyConcreteConcept | Defines the base class for concrete (crisp, left-shoulder, right-shoulder, and so on) concepts |
| CrispConcreteConcept | Define a crisp concept |
| ModifiedConcreteConcept | It is a modified datatype concept |
| LinearConcreteConcept | It is a concept defined by a linear function |
| LeftConcreteConcept | It is a concept defined by a left-shoulder function |
| RightConcreteConcept | It is a concept defined by a right-shoulder function |
| TriangularConcreteConcept | It is a concept defined by a triangular function |
| TrapezoidalConcreteConcept | It is a concept defined by a trapezoidal function |
| TriangularFuzzyNumber | It is a sub-class of the TriangularConcreteConcept and represents a fuzzy triangular number |