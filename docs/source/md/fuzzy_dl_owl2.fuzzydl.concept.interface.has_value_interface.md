# Summary

An abstract base class that augments role-based fuzzy description-logic concepts with the ability to carry and expose an arbitrary filler value.

## Description

HasValueInterface builds on HasRoleInterface, delegating all role handling to the superclass constructor and layering a single additional piece of state on top: a value of any type, held in a private attribute and exposed through a read/write property. Because the value is typed as `typing.Any`, the abstraction stays deliberately agnostic about whether the filler is an individual, a data value, or something else entirely, which makes it reusable across the different kinds of value-carrying concepts in the fuzzy DL framework, such as value restrictions and datatype fillers. Since it is an `abc.ABC`, it cannot be instantiated directly and instead acts as a mixin-style contract that concrete concept classes inherit from. One notable design point is that the setter stores the value **by reference** — the deep-copy safeguard that would isolate the internal state from external mutation survives only as a commented-out line — so mutable values assigned through the property remain shared with the caller, and the getter likewise returns the stored object without copying, meaning outside modifications to a mutable value will be visible through the interface.
