# Summary

An abstract base class, `FuzzyModifier`, that establishes the contract for linguistic hedges which mathematically transform the membership degrees of fuzzy concepts within the FuzzyOWL2 framework.

## Description

Fuzzy modifiers—linguistic hedges such as intensifiers like *very* and dilutors like *somewhat*—are the mechanism through which the FuzzyOWL2 framework adjusts the truth values attached to fuzzy concepts and axioms. By inheriting from Python's abstract base class machinery, `FuzzyModifier` deliberately provides no behaviour of its own and cannot be instantiated directly; it exists purely as a structural contract that concrete implementations are expected to fulfil. Subclasses supply the actual transformation logic applied to membership degrees, which keeps the framework extensible, since new hedges can be introduced simply by subclassing without altering the surrounding ontology-handling code. Centralising the modifier contract in a single abstraction also allows the rest of the fuzzy ontology machinery to treat every modifier uniformly, regardless of the particular mathematical function each one implements.
