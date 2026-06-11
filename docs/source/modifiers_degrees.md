# Modifiers and Degrees

Two small but pervasive object families: **modifiers**, which reshape the
membership function of a concept (the fuzzy hedges such as *very*), and
**degrees**, which carry the truth value attached to an axiom. For the FDL
*syntax* that produces them see [Grammatics](grammar.md); this page describes the
runtime classes.

## Modifiers

A modifier is a function on the unit interval that transforms a membership
degree. They are declared in FDL with `define-modifier` and applied either to a
concept (`(very High)`) or inside a `modified` concrete concept
(`(define-fuzzy-concept VeryHigh modified(very, High))`).

### Class hierarchy

All modifiers derive from the abstract base
`fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier`, which fixes the contract:

| Member | Purpose |
|---|---|
| `compute_name()` | Canonical string name of the modifier instance. |
| `clone()` | A copy of the modifier. |
| `modify(concept)` | Wrap a `Concept` in the corresponding *modified concept*. |
| `get_membership_degree(value)` | Apply the modifier's transform to a single membership value, clamped to `[0, 1]`. |

There are two concrete modifiers:

#### `LinearModifier`

```text
(define-modifier very linear-modifier(0.8))
```

Constructed as `LinearModifier(name, c)` with a single parameter `c > 0`. The
parameter fixes the inflection point of a piecewise-linear transform; internally
the class derives an `(a, b)` break-point pair from `c`. `modify` produces a
`LinearlyModifiedConcept`. Membership is clamped to `[0, 1]`.

#### `TriangularModifier`

```text
(define-modifier around triangular-modifier(0.2, 0.5, 0.8))
```

Constructed as `TriangularModifier(name, a, b, c)` — the three break-points of a
triangular transform (leftmost `a`, peak `b`, rightmost `c`). `modify` produces
a `TriangularlyModifiedConcept`.

### How the parser wires them

`DLParser._parse_modifier` reads the `define-modifier` form, instantiates
`LinearModifier(name, c)` or `TriangularModifier(name, a, b, c)` from the
keyword, and registers it with `DLParser.kb.add_modifier(name, modifier)`. The
modifier is then available by name anywhere a modifier is expected.

> The modified *concepts* these produce (`LinearlyModifiedConcept`,
> `TriangularlyModifiedConcept`, `ModifiedConcreteConcept`) are documented in
> [Fuzzy Concepts](concepts.md).

## Degrees

A degree is the truth value on the right-hand side of an axiom — the optional
trailing value in `(instance a C 0.8)`, `(related a b R 0.8)`,
`(implies C D 0.7)`, and so on. When the value is omitted it defaults to `1`
(crisp).

### Class hierarchy

All degrees derive from the abstract base
`fuzzy_dl_owl2.fuzzydl.degree.degree.Degree`. The base provides a `get_degree`
factory and the operations the MILP layer needs to fold a degree into a
constraint:

| Member | Purpose |
|---|---|
| `get_degree(value)` | Factory: build the right `Degree` subclass for a number, variable, or expression. |
| `is_numeric()` | Whether the degree is a constant. |
| `clone()` | A copy of the degree. |
| `create_inequality_with_degree_rhs(...)` | Build the MILP inequality that has this degree on the right-hand side. |
| `add_to_expression(expr)` / `subtract_from_expression(expr)` / `multiply_constant(k)` | Combine the degree into a MILP `Expression`. |
| `is_number_not_one()` / `is_number_zero()` | Quick constant checks used during normalisation. |

Three concrete degrees:

| Class | FDL form | Carries |
|---|---|---|
| `DegreeNumeric` | a literal, e.g. `0.8` | a constant `float` |
| `DegreeVariable` | a variable name | a MILP `Variable` |
| `DegreeExpression` | a linear expression | a MILP `Expression` |

### How the parser wires them

`DLParser._parse_degree` chooses the subclass from the token type:

* a **number** -> `DegreeNumeric.get_degree(float(...))`;
* an **`Expression`** -> `DegreeExpression.get_degree(...)`;
* a **name** -> first checked against the KB's truth constants
  (`define-truth-constant`); if it matches, a `DegreeNumeric` with that constant
  is used, otherwise the name is treated as a variable and a `DegreeVariable` is
  built.

This is why a degree slot accepts a literal, a previously defined truth
constant, a free variable, or a linear expression interchangeably.

### Truth constants

`(define-truth-constant V 0.53)` registers a named constant on the knowledge
base. Wherever `V` later appears as a degree, the parser resolves it to a
`DegreeNumeric` holding `0.53` — constants are folded at parse time, not kept as
variables.

## See also

* [Grammatics](grammar.md) — FDL syntax for `define-modifier`,
  `define-truth-constant`, and the degree slot of each axiom.
* [Fuzzy Concepts](concepts.md) — the modified-concept classes produced by
  `modify`.
* [Architecture](architecture.md) — how degrees become MILP constraints.