# Fuzzy Concepts

The fuzzy concept currently implemented are as follows.

## Base Concepts

### Concept

Defines a base class of any concept. This is the fundamental class from which all other concept implementations derive.

### AtomicConcept

Defines an atomic concept. This represents the smallest, indivisible unit in the fuzzy logic system.

### TruthConcept

Defines the top $\top$ and bottom $\perp$ concepts. These represent absolute truth and absolute falsehood respectively in the logical system.

## Logical Operators

### OperatorConcept

It is the class to handle a logic (Zadeh, Lukasiewicz, and product) connectives (AND, OR, NOT) between fuzzy concepts. This class implements the fundamental logical operations in fuzzy logic systems.

### AllSomeConcept

Defines a universal ($\forall$) and existential ($\exists$) restrictions on fuzzy concepts. These allow for expressing quantifications in the fuzzy domain.

### ImpliesConcept

Defines a zadeh and goedel implies concept. This handles implication operations in fuzzy logic.

## Fuzzy Integrals

### ChoquetIntegral

Defines a Choquet integral of fuzzy concept. This integral is used for aggregating information when measures are non-additive.

### SugenoIntegral

Defines a Sugeno integral of fuzzy concept. This is a particular type of non-linear integral with respect to fuzzy measures.

### QsugenoIntegral

Defines a Quasi-Sugeno integral of fuzzy concept. This extends the Sugeno integral with additional flexibility.

## OWA Concepts

### OwaConcept

Defines a OWA concept. OWA (Ordered Weighted Averaging) operators provide a family of aggregation operators.

### QowaConcept

Defines a quantified-guided OWA concept. This extends the OWA concept with quantifier-guided behavior.

## Approximation and Threshold Concepts

### ApproximationConcept

Defines uppers and lowers approximation concept. This handles rough set approximations in the fuzzy context.

### ThresholdConcept

Defines a positives and negatives threshold concept. This implements threshold-based classification in fuzzy systems.

### ExtendedThresholdConcept

Defines a extended positives and negatives threshold concept. This provides enhanced threshold functionality beyond the basic threshold concept.

## Value-Based Concepts

### HasValueConcept

Defines a concept associated with a value. This links concepts to specific values in the domain.

### ValueConcept

Defines a datatype restriction (at most, at least, and exact) concept. This handles numerical constraints and restrictions.

### SelfConcept

Defines a self reflexivity concept. This implements self-referential properties in fuzzy logic.

### NegatedNominal

Defines a negated nominal concept. This handles the negation of nominal (named) concepts.

## Weighted Concepts

### WeightedConcept

Defines a weighted concept. This provides basic weighting functionality for concepts.

### WeightedMinConcept

Defines a weighted min concept. This implements weighted minimum operations.

### WeightedMaxConcept

Defines a weighted max concept. This implements weighted maximum operations.

### WeightedSumConcept

Defines a weighted sum concept. This implements weighted summation operations.

### WeightedSumZeroConcept

Defines a weighted sum-zero concept. This implements weighted sum operations with zero-centering.

## Counting and Modification Concepts

### SigmaConcept

Defines a sigma-count concept. This handles counting operations in fuzzy contexts.

### ModifiedConcept

Defines the base class for modified (linear and triangular) concepts. This is the parent class for concepts that can be modified through various functions.

### LinearlyModifiedConcept

Define a linearly modified concept. This applies linear modifications to base concepts.

### TriangularlyModifiedConcept

Define a triangularly modified concept. This applies triangular function modifications to base concepts.

## Concrete Fuzzy Concepts

### FuzzyConcreteConcept

Defines the base class for concrete (crisp, left-shoulder, right-shoulder, and so on) concepts. This is the parent class for all concrete implementations of fuzzy concepts.

### CrispConcreteConcept

Define a crisp concept. This represents classical, non-fuzzy (crisp) concepts within the fuzzy framework.

### ModifiedConcreteConcept

It is a modified datatype concept. This applies modifications to concrete datatype concepts.

### LinearConcreteConcept

It is a concept defined by a linear function. This implements concepts using linear mathematical functions.

### LeftConcreteConcept

It is a concept defined by a left-shoulder function. This implements concepts using left-shoulder membership functions.

### RightConcreteConcept

It is a concept defined by a right-shoulder function. This implements concepts using right-shoulder membership functions.

### TriangularConcreteConcept

It is a concept defined by a triangular function. This implements concepts using triangular membership functions.

### TrapezoidalConcreteConcept

It is a concept defined by a trapezoidal function. This implements concepts using trapezoidal membership functions.

### TriangularFuzzyNumber

It is a sub-class of the TriangularConcreteConcept and represents a fuzzy triangular number. This provides a specialized implementation for triangular fuzzy numbers.