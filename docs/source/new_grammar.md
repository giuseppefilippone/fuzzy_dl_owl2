# Fuzzy Description Logic Grammatics

## String and Numbers

```python
name    := ["][a-zA-Z_][a-zA-Z0-9_]*["]
numbers := [+-]? [0-9]+(\.[0-9]+)
```

## Define the semantics of the knowledge base

```python
logic           := 'lukasiewicz' | 'zadeh' | 'classical'
define_logic    := '(' 'define-fuzzy-logic' ["] logic ["] ')'
```

## Define truth constants

```python
constant := '(' 'define-truth-constant' name numbers ')'
```

- Example: **(define-truth-constant V 5.3)** defines the truth constant named $V$ with value $5.3$.

## Define modifiers

Modifiers change the membership function of a fuzzy concept.

```python
modifier    := (
    '(' 'define-modifier' name 'linear-modifier' '(' numbers ')' ')'                                    # linear hedge with c > 0
    | '(' 'define-modifier' name 'triangular-modifier' '(' numbers ',' numbers ',' numbers ')' ')'      # triangular function
)
```

## Define concrete fuzzy concepts

```python
concept_type    := (
        'crisp' '(' numbers ',' numbers ',' numbers ',' numbers ')'                         # crisp interval
        | 'left-shoulder' '(' numbers ',' numbers ',' numbers ',' numbers ')'               # left-shoulder function
        | 'right-shoulder' '(' numbers ',' numbers ',' numbers ',' numbers ')'              # right-shoulder function
        | 'triangular' '(' numbers ',' numbers ',' numbers ',' numbers ')'                  # triangular function
        | 'trapezoidal' '(' numbers ',' numbers ',' numbers ',' numbers ',' numbers ')'     # trapezoidal function
        | 'linear' '(' numbers ',' numbers ',' numbers ',' numbers ')'                      # linear function
        | 'modified' '(' name ',' name ')'                                                  # modified datatype
    )
fuzzy_concept   := '(' 'define-fuzzy-concept' name concept_type ')'
```

- Note: the fuzzy concept **modified** applies only to modifiers and datatype restrictions. Example: **(define-fuzzy-concept CONCEPT modified(MOD, F))**, where **CONCEPT** is the name of the created concrete fuzzy concept, **MOD** is the name of an already defined modifier, and **F** is the name of an already defined datatype restriction.

## Define fuzzy numbers

```python
fuzzy_number_range      := '(' 'define-fuzzy-number-range' numbers numbers ')'    # if fuzzy numbers are used, then define the range [k1, k2]
fuzzy_number_expression := (
    name
    | numbers                                   # if fuzzy number is a real number 'n', then it is considered as (n, n, n)
    | '(' numbers ',' numbers ',' numbers ')'
    | '(' 'f+' fuzzy_number_expression+ ')'                            # addition of fuzzy numbers
    | '(' 'f-' fuzzy_number_expression fuzzy_number_expression ')'     # subtraction of fuzzy numbers
    | '(' 'f*' fuzzy_number_expression+ ')'                            # product of fuzzy numbers
    | '(' 'f/' fuzzy_number_expression fuzzy_number_expression ')'     # division of fuzzy numbers
)
fuzzy_number            := '(' 'define-fuzzy-number' name fuzzy_number_expression ')'
```

### Fuzzy Number Operations

The fuzzy number system supports several types of expressions, each with specific mathematical definitions:

### Basic Fuzzy Number Representation

**(a, b, c)** represents a fuzzy number with the mathematical definition $(a,b,c)$.

### Real Number Conversion

**n** represents a real number that is automatically converted to the fuzzy number $(n,n,n)$.

### Addition of Fuzzy Numbers

($f+$ $f_1$ $f_2$ $\ldots$ $f_n$) performs addition of multiple fuzzy numbers, defined mathematically as $(\sum_{i = 0}^{n} a_i, \sum_{i = 0}^{n} b_i, \sum_{i = 0}^{n} c_i)$.

### Subtraction of Fuzzy Numbers

($f-$ $f_1$ $f_2$) performs subtraction between two fuzzy numbers, defined mathematically as $(a_1−c_2, b_1 − b_2, c_1 − a_2)$.

### Product of Fuzzy Numbers

($f*$ $f_1$ $f_2$ $\ldots$ $f_n$) performs multiplication of multiple fuzzy numbers, defined mathematically as $(\prod_{i = 0}^{n} a_i, \prod_{i = 0}^{n} b_i, \prod_{i = 0}^{n} c_i)$.

### Division of Fuzzy Numbers

($f/$ $f_1$ $f_2$) performs division between two fuzzy numbers, defined mathematically as $(\frac{a_1}{c_2}, \frac{b_1}{b_2}, \frac{c_1}{a_2})$.

## Define Features, i.e., functional datatypes

```python
feature         := '(' 'functional' name ')'        # first, define the feature
feature_range   := (
    '(' 'range' name '*integer*' numbers numbers ')'
    | '(' 'range' name '*real*' numbers numbers ')'
    | '(' 'range' name '*string*' ')'
    | '(' 'range' name '*boolean*' ')'
)
```

### Feature Range Specifications

Features can be defined with different data types and ranges, each serving specific purposes in the fuzzy description logic system:

### Feature Definition

**(functional F)** defines the feature F as a functional datatype that can be used throughout the knowledge base.

### Integer Range Features

**(range F `*integer*` $k_1$ $k_2$)** specifies that the range of feature $F$ consists of integer numbers within the interval $[k_1, k_2]$.

### Real Number Range Features

**(range F `*real*` $k_1$ $k_2$)** specifies that the range of feature $F$ consists of rational numbers within the interval $[k_1, k_2]$.

### String Features

**(range F `*string*`)** specifies that the range of feature $F$ consists of string values, allowing textual data to be handled within the fuzzy logic framework.

### Boolean Features

**(range F `*boolean*`)** specifies that the range of feature $F$ consists of boolean values (true/false), enabling logical propositions within the system.

## Datatype/feature restrictions

```python
# (>= ...) = at least datatype restriction
# (<= ...) = at most datatype restriction
# (= ...)  = exact datatype restriction

restriction_function    := (
    numbers
    | name
    | numbers [*]? restriction_function
    | restriction_function [-] restriction_function
    | (restriction_function [+])+ restriction_function
)
restriction             := '(' ('>=' | '<=', '=') name (name | restriction_function | fuzzy_number) ')'
```

### Datatype Restriction Operations

The system supports various types of datatype restrictions that allow precise control over feature values and relationships:

### Greater Than or Equal Restrictions with Variables

**$(\mathrm{>=}\ F\ \text{variable})$** defines a restriction where feature $F$ must be greater than or equal to a variable, mathematically expressed as ${\mathrm{sup}}_{b \in {\Delta}_D} [F^\mathcal{I} (x, b) \otimes (b \geq \text{variable})]$.

### Less Than or Equal Restrictions with Variables

**$(\mathrm{<=}\ F\ \text{variable})$** defines a restriction where feature $F$ must be less than or equal to a variable, mathematically expressed as $\mathrm{sup}_{b \in \Delta_D} [F^\mathcal{I} (x, b) \otimes (b \leq \text{variable})]$.

### Equality Restrictions with Variables

**$(=\ F\ \text{variable})$** defines an exact equality restriction for feature $F$, mathematically expressed as $\mathrm{sup}_{b \in \Delta_D} [F^\mathcal{I} (x, b) \otimes (b = \text{variable})]$.

### Greater Than or Equal Restrictions with Fuzzy Numbers

**$(\mathrm{>=}\ F\ \text{fuzzy\_number})$** extends the comparison to fuzzy numbers, mathematically defined as $\mathrm{sup}_{b^\prime, b \in \Delta_D} [F^\mathcal{I} (x, b) \otimes (b \geq b^\prime) \otimes {\text{fuzzy\_number}(b^\prime)}^\mathcal{I}]$.

### Less Than or Equal Restrictions with Fuzzy Numbers

**$(\mathrm{<=}\ F\ \text{fuzzy\_number})$** provides fuzzy number comparison for upper bounds, mathematically defined as $\mathrm{sup}_{b^\prime, b \in \Delta_D} [F^\mathcal{I} (x, b) \otimes (b \leq b^\prime) \otimes {\text{fuzzy\_number}(b^\prime)}^\mathcal{I}]$.

### Equality Restrictions with Fuzzy Numbers

**$(=\ F\ \text{fuzzy\_number})$** establishes equality constraints with fuzzy numbers, mathematically expressed as $\mathrm{sup}_{b^\prime, b \in \Delta_D} [F^\mathcal{I} (x, b) \otimes (b = b^\prime) \otimes {\text{fuzzy\_number}(b^\prime)}^\mathcal{I}]$.

### Function-Based Restrictions

**$(\mathrm{>=}\ F\ \mathrm{function}(F_1, \ldots, F_n))$**, **$(\mathrm{<=}\ F\ \mathrm{function}(F_1, \ldots, F_n))$**, and **$(=\ F\ \mathrm{function}(F_1, \ldots, F_n))$** allow restrictions based on complex functions of multiple features, with mathematical definitions following the pattern $\mathrm{sup}_{b \in \Delta_D} [F^\mathcal{I} (x, b) \otimes (b \text{ op } {\mathrm{function}(F_1, \ldots, F_n)}^{\mathcal{I}})]$ where **op** represents the comparison operator.

### Variable and Value Constraints

In datatype restrictions, the variable **variable** must be declared as a **(free variable)** before its use in a datatype restriction, utilizing the **constraints** defined below. The value for $b$ must be within the range $[k_1,k_2]$ subset or equivalent to $[- k_{\infty}, k_{\infty}]$ of the feature $F$, and the values for **variable**, $\mathbf{function}(F_1, \ldots, F_n)$ and the range of **fuzzy_number** must be in $[- k_{\infty}, k_{\infty}]$, where $k_{\infty}$ is the maximal representable integer.

In datatype restrictions, the variable **variable** may be replaced with a value, such as an integer, a real number, a string, or a boolean constant (true, false), depending on the range of the feature $F$.

### MILP Solver Constraints

The value of $k_{\infty}$ varies depending on the MILP solver used, reflecting computational limitations and precision requirements:

| MILP Solver | $k_{\infty}$ |
| --- | --- |
| Gurobi | $1000 \cdot ((1 \ll 31) - 1)$ |
| PULP CBC | $(1 \ll 31) - 1$ |
| MIP | $(1 \ll 31) - 1$ |
| PULP GLPK | $(1 \ll 28) - 1$ |
| PULP HiGHS | $(1 \ll 28) - 1$ |
| PULP CPLEX | $(1 \ll 28) - 1$ |

- Note: The value of $k_{\infty}$ is different for some MILP solvers for computational issues. In particular, higher values lead to the accumulation of errors, which can distort the results. The values currently given give the same results for the test files provided.

## Constraints

```python
operator                := '>=' | '<=' | '='
term                    := numbers | name | numbers [*] term | name [*] term
expression              := (term [+])+ term
inequation_constraint   := expression operator numbers
constraints             := '(' 'constraints' (
    inequality_constraint
    | 'binary' name             # binary variable in {0, 1}
    | 'free' name               # continuous variable in (-inf, +inf)
) ')'
```

## Show statements

```python
statements = (
    '(' 'show-concrete-fillers' name+ ')'               # show value of the fillers
    | '(' 'show-concrete-fillers-for' name{2, } ')'     # show value of the fillers for an individual
    | '(' 'show-concrete-instance-for' name{3, } ')'    # show degrees of being the filler of individual instance of a concept
    | '(' 'show-abstract-fillers' name+ ')'             # show fillers and membership to any concept
    | '(' 'show-abstract-fillers-for' name{2, } ')'     # show fillers for an individuals and membership to any concept
    | '(' 'show-concepts' name+ ')'                     # show membership of individuals to any concept
    | '(' 'show-instances' name+ ')'                    # show value of the instances of the listed concepts
    | '(' 'show-variables' name+ ')'                    # show value of the listed variables
    | '(' 'show-language' ')'                           # show language of the KB, from ALC to SHIF(D)
)
```

### Show Statement Operations

The system provides various show statements for debugging and analyzing the knowledge base contents:

### Concrete Filler Display

**(show-concrete-fillers $F_1$ $\ldots$ $F_n$)** displays the values of the fillers of the features $F_i$, providing concrete instantiations of feature relationships.

### Individual-Specific Concrete Fillers

**(show-concrete-fillers-for ind $F_1$ $\ldots$ $F_n$)** shows the values of the fillers of features $F_i$ specifically for the individual **ind**, allowing targeted analysis of individual properties.

### Concept Instance Degrees

**(show-concrete-instance-for ind $F$ $C_1$ $\ldots$ $C_n$)** displays the degrees of being the $F$ filler of the individual **ind** instance of concepts $C_i$, revealing membership strengths in fuzzy concepts.

### Abstract Filler Analysis

**(show-abstract-fillers $R_1$ $\ldots$ $R_n$)** shows fillers of roles $R_i$ and their membership to any concept, providing comprehensive relationship analysis.

### Individual Abstract Fillers

**(show-abstract-fillers-for ind $R_1$ $\ldots$ $R_n$)** displays fillers of roles $R_i$ for the individual **ind** and their membership to any concept, focusing on specific individual relationships.

### Concept Membership Display

**(show-concepts $a_1$ $\ldots$ $a_n$)** shows membership of the individuals $a_i$ to any concept, revealing the concept classification of individuals.

### Concept Instance Values

**(show-instances $C_1$ $\ldots$ $C_n$)** displays the values of the instances of the concepts $C_i$, showing which individuals belong to specific concepts.

### Variable Value Display

**(show-variables $x_1$ $\ldots$ $x_n$)** shows the values of the variables $x_i$, useful for debugging constraint satisfaction problems.

### Knowledge Base Language Display

**(show-language)** shows the language of the knowledge base, indicating the description logic expressivity from $\mathcal{ALC}$ to $\mathcal{SHIF}(\mathbf{D})$.

## Crisp declarations

```python
crisp_concepts  := '(' 'crisp-concept' name+ ')' # the listed concepts are crisp
crisp_roles     := '(' 'crisp-role' name+ ')' # the listed roles are crisp
```

## Fuzzy relations

```python
fuzzy_similarity    := '(' 'define-fuzzy-similarity'   name ')' # fuzzy similarity relation
fuzzy_equivalence   := '(' 'define-fuzzy-equivalence'  name ')' # fuzzy equivalence relation
```

## Concept expressions

```python
concept := (
    '*top*'                                                     # top concept
    | '*bottom*'                                                # bottom concept
    | name                                                      # atomic concept or concrete fuzzy concept
    | restriction                                               # datatype restriction
    | '(' 'and' concept concept ')'                             # concept conjunction
    | '(' 'g-and' concept concept ')'                           # Goedel conjunction
    | '(' 'l-and' concept concept ')'                           # Lukasiewicz conjunction
    | '(' 'or' concept concept ')'                              # concept disjunction
    | '(' 'g-or' concept concept ')'                            # Goedel disjunction
    | '(' 'l-or' concept concept ')'                            # Lukasiewicz disjunction
    | '(' 'not' concept ')'                                     # concept negation
    | '(' 'implies' concept concept ')'                         # concept implication
    | '(' 'g-implies' concept concept ')'                       # Goedel implication
    | '(' 'l-implies' concept concept ')'                       # Lukasiewicz implication
    | '(' 'kd-implies' concept concept ')'                      # Kleene-Dienes implication
    | '(' 'all' name concept ')'                                # universal role restriction
    | '(' 'some' name concept ')'                               # existential role restriction
    | '(' 'some' name name ')'                                  # individual value restriction
    | '(' 'ua' name concept ')'                                 # upper approximation
    | '(' 'lua' name concept ')'                                # loose upper approximation
    | '(' 'tua' name concept ')'                                # tight upper approximation
    | '(' 'la' name concept ')'                                 # lower approximation
    | '(' 'lla' name concept ')'                                # loose lower approximation
    | '(' 'tla' name concept ')'                                # tight lower approximation
    | '(' 'self' concept ')'                                    # local reflexivity concept
    | '(' name concept ')'                                      # modifier applied to concept
    | '(' fuzzy_number ')'                                      # fuzzy number
    | '(' '[' ('>=' | '<=') name ']' concept ')'                # threshold concept
    | '(' numbers concept ')'                                   # weighted concept
    | '(' 'w-sum' ('(' numbers concept ')')+ ')'                # weighted sum concept
    | '(' 'w-max' ('(' numbers concept ')')+ ')'                # weighted max concept
    | '(' 'w-min' ('(' numbers concept ')')+ ')'                # weighted min concept
    | '(' 'w-sum-zero' ('(' numbers concept ')')+ ')'           # weighted sum zero concept
    | '(' 'owa' numbers+ concept+ ')'                           # OWA aggregation operator
    | '(' 'q-owa' name concept+ ')'                             # quantifier-guided OWA
    | '(' 'choquet' numbers+ concept+ ')'                       # Choquet integral
    | '(' 'sugeno' numbers+ concept+ ')'                        # Sugeno integral
    | '(' 'q-sugeno' numbers+ concept+ ')'                      # Quasi-Sugeno integral
    | '(' 'sigma-count' name concept '{' name+ '}' name ')'     # Sigma-count concept
)
```

### Basic Concept Expressions

The fuzzy description logic provides fundamental concept building blocks:

### Top Concept

**`*top*`** represents the universal concept that always evaluates to true, mathematically defined as $\top\ =\ 1$.

### Bottom Concept

**`*bottom*`** represents the empty concept that always evaluates to false, mathematically defined as $\perp\ =\ 0$.

### Atomic Concepts

**A** represents an atomic concept $A$, evaluated as $A^\mathcal{I}(x)$ in the interpretation.

### Concrete Fuzzy Concepts

**CFC** represents a concrete fuzzy concept (such as crisp, left-shoulder, and so on), evaluated as $\mathrm{CFC}^\mathcal{I}(x)$.

### Datatype Restrictions

**DR** represents a datatype restriction, evaluated as $\mathrm{DR}^\mathcal{I}(x)$.

### Logical Connectives

The system supports various logical operations with different semantics:

### Standard Conjunction

**(and $C_1$ $C_2$)** performs concept conjunction of $C_1$ and $C_2$, defined as $C_1^\mathcal{I}(x) \otimes C_2^\mathcal{I}(x)$.

### Goedel Conjunction

**(g-and $C_1$ $C_2$)** performs Goedel conjunction of $C_1$ and $C_2$, defined as $C_1^\mathcal{I}(x) \otimes_G C_2^\mathcal{I}(x)$.

### Lukasiewicz Conjunction

**(l-and $C_1$ $C_2$)** performs Lukasiewicz conjunction of $C_1$ and $C_2$, defined as $C_1^\mathcal{I}(x) \otimes_L C_2^\mathcal{I}(x)$.

### Standard Disjunction

**(or $C_1$ $C_2$)** performs concept disjunction of $C_1$ and $C_2$, defined as $C_1^\mathcal{I}(x) \oplus C_2^\mathcal{I}(x)$.

### Goedel Disjunction

**(g-or $C_1$ $C_2$)** performs Goedel disjunction of $C_1$ and $C_2$, defined as $C_1^\mathcal{I}(x) \oplus_G C_2^\mathcal{I}(x)$.

### Lukasiewicz Disjunction

**(l-or $C_1$ $C_2$)** performs Lukasiewicz disjunction of $C_1$ and $C_2$, defined as $C_1^\mathcal{I}(x) \oplus_L C_2^\mathcal{I}(x)$.

### Negation

**(not $C$)** performs concept $C$ negation, defined as $\ominus_L C^\mathcal{I}(x)$.

### Implication Operations

Various forms of implication are supported for different logical semantics:

### Standard Implication

**(implies $C_1$ $C_2$)** establishes concept implication between $C_1$ and $C_2$, defined as $C_1^\mathcal{I}(x) \Rightarrow C_2^\mathcal{I}(x)$.

### Goedel Implication

**(g-implies $C_1$ $C_2$)** establishes Goedel implication between $C_1$ and $C_2$, defined as $C_1^\mathcal{I}(x) \Rightarrow_G C_2^\mathcal{I}(x)$.

### Lukasiewicz Implication

**(l-implies $C_1$ $C_2$)** establishes Lukasiewicz implication between $C_1$ and $C_2$, defined as $C_1^\mathcal{I}(x) \Rightarrow_L C_2^\mathcal{I}(x)$.

### Kleene-Dienes Implication

**(kd-implies $C_1$ $C_2$)** establishes Kleene-Dienes implication between $C_1$ and $C_2$, defined as $C_1^\mathcal{I}(x) \Rightarrow_\mathrm{KD} C_2^\mathcal{I}(x)$.

### Role Restrictions

Role-based concept formation allows complex relationship modeling:

### Universal Role Restriction

**(all $R$ $C$)** creates a universal role $R$ restriction for concept $C$, defined as $\mathrm{inf}_{y \in \Delta^\mathcal{I}}\ { R^\mathcal{I}(x, y) \Rightarrow C^\mathcal{I}(y) }$.

### Existential Role Restriction

**(some $R$ $C$)** creates an existential role $R$ restriction for concept $C$, defined as $\mathrm{sup}_{y \in \Delta^\mathcal{I}}\ { R^\mathcal{I}(x, y) \otimes C^\mathcal{I}(y) }$.

### Individual Value Restriction

**(some $R$ $a$)** creates an individual value restriction for role $R$ and individual $a$, defined as $R^\mathcal{I}(x, a)$.

### Approximation Concepts

Rough set theory concepts for handling uncertainty:

### Upper Approximation

**(ua $s$ $C$)** defines upper approximation for a fuzzy relation $s$ and concept $C$, calculated as $\mathrm{sup}_{y \in \Delta^\mathcal{I}}\ { s^\mathcal{I}(x, y) \otimes C^\mathcal{I}(y) }$.

### Loose Upper Approximation

**(lua $s$ $C$)** defines loose upper approximation for a fuzzy relation $s$ and concept $C$, calculated as $\mathrm{sup}_{z \in X}\ { s^\mathcal{I}(x, z) \otimes \mathrm{sup}_{y \in \Delta^\mathcal{I}} s^\mathcal{I}(y, z) \otimes C^\mathcal{I}(x) }$.

### Tight Upper Approximation

**(tua $s$ $C$)** defines tight upper approximation for a fuzzy relation $s$ and concept $C$, calculated as $\mathrm{inf}_{z \in X}\ { s^\mathcal{I}(x, z) \Rightarrow \mathrm{sup}_{y \in \Delta^\mathcal{I}} s^\mathcal{I}(y, z) \otimes C^\mathcal{I}(x) }$.

### Lower Approximation

**(la $s$ $C$)** defines lower approximation for a fuzzy relation $s$ and concept $C$, calculated as $\mathrm{inf}_{y \in \Delta^\mathcal{I}}\ s^\mathcal{I}(x, y) \Rightarrow C^\mathcal{I}(y)$.

### Loose Lower Approximation

**(lla $s$ $C$)** defines loose lower approximation for a fuzzy relation $s$ and concept $C$, calculated as $\mathrm{sup}_{z \in X}\ { s^\mathcal{I}(x, z) \otimes \mathrm{inf}_{y \in \Delta^\mathcal{I}} s^\mathcal{I}(y, z) \otimes C^\mathcal{I}(x) }$.

### Tight Lower Approximation

**(tla $s$ $C$)** defines tight lower approximation for a fuzzy relation $s$ and concept $C$, calculated as $\mathrm{inf}_{z \in X}\ { s^\mathcal{I}(x, z) \Rightarrow \mathrm{inf}_{y \in \Delta^\mathcal{I}} s^\mathcal{I}(y, z) \otimes C^\mathcal{I}(x) }$.

### Special Concept Constructs

Advanced concept formation techniques:

### Self Reflexivity

**(self C)** defines a local reflexivity concept, evaluated as $C^\mathcal{I}(x)(x, x)$.

### Modified Concepts

**(MOD C)** applies modifier MOD to concept $C$, evaluated as ${f_m}(C^\mathcal{I}(x))$, where $f_m$ is the modifier function associated to MOD.

### Fuzzy Numbers in Concepts

**(FN)** represents fuzzy number FN as a concept, evaluated as $\mathrm{FM}^\mathcal{I}(x)$.

### Threshold Concepts

**([>= var ] C)** creates a threshold concept that returns $C^\mathcal{I}(x)$ if $C^\mathcal{I}(x) \geq \mathrm{var}$, otherwise returns $0$.

**([<= var ] C)** creates a threshold concept that returns $C^\mathcal{I}(x)$ if $C^\mathcal{I}(x) \leq \mathrm{var}$, otherwise returns $0$.

### Weighted Concepts

Concepts with numerical weights for aggregation:

### Basic Weighted Concept

**(n C)** creates a weighted concept C with weight n, evaluated as $n C^\mathcal{I}(x)$.

### Weighted Sum

**(w-sum ($n_1$ $C_1$) $\ldots$ ($n_k$ $C_k$))** performs weighted sum of concepts, calculated as $\sum_{i=1}^{k} n_i C_i^\mathcal{I}(x)$.

### Weighted Maximum

**(w-max ($v_1$ $C_1$) $\ldots$ ($v_k$ $C_k$))** performs weighted max of concepts, calculated as $\max_{i=1}^{k} \min {v_i, x_i}$.

### Weighted Minimum

**(w-min ($v_1$ $C_1$) $\ldots$ ($v_k$ $C_k$))** performs weighted min of concepts, calculated as $\min_{i=1}^{k} \max {1 - v_i, x_i}$.

### Weighted Sum Zero

**(w-sum-zero ($n_1$ $C_1$) $\ldots$ ($n_k$ $C_k$))** performs weighted sum with zero-constraint, returning $0$ if any $C_i^\mathcal{I}(x) = 0$ for some $i \in {1, \ldots, k}$, otherwise $\sum_{i=1}^{k} n_i C_i^\mathcal{I}(x)$.

### Aggregation Operators

Advanced aggregation techniques for concept combination:

### OWA Aggregation

**(owa ($w_1$, $\ldots$, $w_n$) ($C_1$, $\ldots$, $C_n$))** performs OWA aggregation, calculated as $\sum_{i=1}^n w_i y_i$.

### Quantifier-Guided OWA

**(q-owa $Q$ ($C_1$, $\ldots$, $C_n$))** performs quantifier-guided OWA with quantifier $Q$ (where $Q$ is a right-shoulder or linear function), calculated as $\sum_{i=1}^n w_i y_i$, where $w_i = Q(\frac{i}{n}) - Q(\frac{i - 1}{n})$.

### Choquet Integral

**(choquet ($w_1$, $\ldots$, $w_n$) ($C_1$, $\ldots$, $C_n$))** computes the Choquet integral, calculated as $y_1 w_1 + \sum_{i=2}^n (y_i - y_{i - 1}) w_i$.

### Sugeno Integral

**(sugeno ($v_1$, $\ldots$, $v_n$) ($C_1$, $\ldots$, $C_n$))** computes the Sugeno integral, calculated as $\max_{i=1}^n \min {y_i, mu_i}$.

### Quasi-Sugeno Integral

**(q-sugeno ($v_1$, $\ldots$, $v_n$) ($C_1$, $\ldots$, $C_n$))** computes the Quasi-Sugeno integral, calculated as $\max_{i=1}^n y_i \otimes_L mu_i$.

### Sigma-Count Concept

**(sigma-count $R$ $C$ ${a_1\ \ldots\ a_k}$ $F_C$)** creates a Sigma-Count concept with role $R$ and associated to the concept $C$, the individuals $a_i$ and the fuzzy concrete concept $F_C$.

### Important Constraints and Notes

Several constraints apply to the proper use of these concept expressions:

- $n_1, \ldots, n_k \in [0, 1]$, with $\sum_{i=1}^k\ n_i \leq 1$
- $w_1, \ldots, w_n \in [0, 1]$, with $\sum_{i=1}^n\ w_i = 1$
- $v_1, \ldots, v_n \in [0, 1]$, with $\max_{i=1}^n\ v_i = 1$
- $y_i$ is the $i$-largest of the $C_i^\mathcal{I}(x)$
- $ow_i$ is the weight $v_i$ of the $i$-largest of the $C_i^\mathcal{I}(x)$
- $mu_i$ is defined as follows: $mu_1 = ow_1$, and $mu_i = ow_i \oplus mu_{i - 1}$ for $i \in {2, \ldots, n}$
- Fuzzy numbers can only appear in existential, universal and datatype restrictions
- In threshold concepts **var** may be replaced with $ w \in [0, 1] $
- Fuzzy relations $s$ should be previously defined as fuzzy similarity relation or a fuzzy equivalence relation as **(define-fuzzy-similarity s)** or **(define-fuzzy-equivalence s)**, respectively
- Fuzzy concrete concept $F_C$ in **sigma-count** concept has to be previously defined as **left-shoulder**, **right-shoulder** or **triangular** concept with **define-fuzzy-concept**

## Axioms

```python
degree := (
    numbers             # a rational number
    | expression        # a linear expression
    | name              # variable or an already defined truth constant
)
axioms := (
    '(' 'instance' name concept degree? ')'             # concept assertion
    | '(' 'related' name name name degree? ')'          # role assertion
    | '(' 'implies' concept concept numbers? ')'        # General Concept Inclusion (GCI) with degree 'numbers'
    | '(' 'g-implies' concept concept numbers? ')'      # Goedel GCI with degree 'numbers'
    | '(' 'kd-implies' concept concept numbers? ')'     # Kleene-Dienes GCI with degree 'numbers'
    | '(' 'l-implies' concept concept numbers? ')'      # Lukasiewicz GCI with degree 'numbers'
    | '(' 'z-implies' concept concept numbers? ')'      # Zadeh's set GCI with degree 'numbers'
    | '(' 'define-concept' name concept ')'             # concept definition
    | '(' 'define-primitive-concept' name concept ')'   # concept subsumption
    | '(' 'equivalent-concepts' concept concept ')'     # equivalent concept definition
    | '(' 'disjoint' concept+  ')'                      # concept disjointness
    | '(' 'disjoint-union' concept+ ')'                 # disjoint union of concepts
    | '(' 'range' name concept ')'                      # range restriction of a concept
    | '(' 'domain' name concept ')'                     # domain restriction of a concept
    | '(' 'functional' name ')'                         # functional role
    | '(' 'inverse-functional' name ')'                 # inverse functional role
    | '(' 'reflexive' name ')'                          # reflexive role
    | '(' 'symmetric' name ')'                          # symmetric role
    | '(' 'transitive' name ')'                         # transitive role
    | '(' 'implies-role' name name numbers? ')'         # Role Implication Axiom (RIA)
    | '(' 'inverse' name name ')'                       # inverse role
)
```

### Assertion Axioms

Basic statements about individuals and their relationships:

### Concept Assertions

**(instance $a$ $C$ $d$)** asserts that individual $a$ is an instance of concept $C$ with degree $d$, formally defined as $C^\mathcal{I}(a^\mathcal{I}) \geq d$.

### Role Assertions

**(related $a$ $b$ $R$ $d$)** asserts that individuals $a$ and $b$ are related by role $R$ with degree $d$, formally defined as $R^\mathcal{I}(a^\mathcal{I}, b^\mathcal{I}) \geq d$.

### General Concept Inclusion Axioms

Various forms of concept subsumption with different logical semantics:

### Standard General Concept Inclusion

**(implies $C_1$ $C_2$ d)** establishes that concept $C_1$ implies concept $C_2$ with degree $d$, formally defined as $\mathrm{inf}_{x \in \Delta^\mathcal{I}}\ C_1^\mathcal{I}(x) \Rightarrow C_2^\mathcal{I}(x) \geq d$.

### Goedel General Concept Inclusion

**(g-implies $C_1$ $C_2$ d)** establishes Goedel implication between concepts with degree $d$, formally defined as $\mathrm{inf}_{x \in \Delta^\mathcal{I}}\ C_1^\mathcal{I}(x) \Rightarrow_G C_2^\mathcal{I}(x) \geq d$.

### Kleene-Dienes General Concept Inclusion

**(kd-implies $C_1$ $C_2$ d)** establishes Kleene-Dienes implication between concepts with degree $d$, formally defined as $\mathrm{inf}_{x \in \Delta^\mathcal{I}}\ C_1^\mathcal{I}(x) \Rightarrow_{\mathrm{KD}} C_2^\mathcal{I}(x) \geq d$.

### Lukasiewicz General Concept Inclusion

**(l-implies $C_1$ $C_2$ d)** establishes Lukasiewicz implication between concepts with degree $d$, formally defined as $\mathrm{inf}_{x \in \Delta^\mathcal{I}}\ C_1^\mathcal{I}(x) \Rightarrow_{L} C_2^\mathcal{I}(x) \geq d$.

### Zadeh General Concept Inclusion

**(z-implies $C_1$ $C_2$ d)** establishes Zadeh set implication between concepts with degree $d$, formally defined as $\mathrm{inf}_{x \in \Delta^\mathcal{I}}\ C_1^\mathcal{I}(x) \Rightarrow_Z C_2^\mathcal{I}(x) \geq d$.

### Concept Definition Axioms

Formal concept definitions and relationships:

### Complete Concept Definition

**(define-concept $A$ $C$)** provides a complete definition of atomic concept $A$ as equivalent to complex concept $C$, formally defined as $\forall_{x \in \Delta^\mathcal{I}}\ A^\mathcal{I}(x) = C^\mathcal{I}(x)$.

### Primitive Concept Definition

**(define-primitive-concept $A$ $C$)** establishes that atomic concept $A$ is subsumed by complex concept $C$, formally defined as $\mathrm{inf}_{x \in \Delta^\mathcal{I}}\ A^\mathcal{I}(x) \leq C^\mathcal{I}(x)$.

### Concept Equivalence

**(equivalent-concepts $C_1$ $C_2$)** establishes that two concepts are equivalent, formally defined as $\forall_{x \in \Delta^\mathcal{I}}\ C_1^\mathcal{I}(x) = C_2^\mathcal{I}(x)$.

### Concept Disjointness and Union

Axioms for controlling concept overlap:

### Concept Disjointness

**(disjoint $C_1$ $\ldots$ $C_k$)** declares that the listed concepts are mutually disjoint, equivalent to (implies (g-and $C_i$ $C_j$) `*bottom*`) for all pairs, formally $\forall_{i, j \in {1, \ldots, k}, i < j}\ (C_i^\mathcal{I}(x) \otimes_G C_j^\mathcal{I}(x)) \Rightarrow \perp$.

### Disjoint Union

**(disjoint-union $C_1$ $\ldots$ $C_k$)** establishes that the first concept is the disjoint union of the others, formally $C_1 = \bigoplus_{i=2}^k C_i$ and $\forall_{i, j \in {1, \ldots, k}, i < j}\ (C_i^\mathcal{I}(x) \otimes_G C_j^\mathcal{I}(x)) \Rightarrow \perp$.

### Role Restriction Axioms

Domain and range constraints for roles:

### Role Range Restriction

**(range $R$ $C$)** restricts the range of role $R$ to concept $C$, equivalent to (implies `*top*` (all $R$ $C$)), formally $\top \Rightarrow \mathrm{inf}_{y \in \Delta^\mathcal{I}}\ { R^\mathcal{I}(x, y) \Rightarrow C^\mathcal{I}(y) }$.

### Role Domain Restriction

**(domain $R$ $C$)** restricts the domain of role $R$ to concept $C$, equivalent to (implies (some $R$ `*top*`) $C$), formally $\mathrm{sup}_{y \in \Delta^\mathcal{I}}\ { R^\mathcal{I}(x, y) \otimes \top } \Rightarrow C^\mathcal{I}(x)$.

### Role Property Axioms

Fundamental properties that roles can possess:

### Functional Roles

**(functional $R$)** declares role $R$ as functional, meaning each individual can be related to at most one other individual, formally $R^\mathcal{I}(a, b) = R^\mathcal{I}(a, c) \rightarrow b = c$.

### Inverse Functional Roles

**(inverse-functional $R$)** declares role $R$ as inverse functional, meaning each individual can be the target of at most one relationship, formally $R^\mathcal{I}(b, a) = R^\mathcal{I}(c, a) \rightarrow b = c$.

### Reflexive Roles

**(reflexive $R$)** declares role $R$ as reflexive, meaning every individual is related to itself, formally $\forall_{a \in \Delta^\mathcal{I}}\ R^\mathcal{I}(a, a) = 1$.

### Symmetric Roles

**(symmetric $R$)** declares role $R$ as symmetric, meaning if $a$ is related to $b$, then $b$ is related to $a$, formally $\forall_{a, b \in \Delta^\mathcal{I}}\ R^\mathcal{I}(a, b) = R^\mathcal{I}(b, a)$.

### Transitive Roles

**(transitive $R$)** declares role $R$ as transitive, meaning the relationship chains together, formally $\forall_{a, b \in \Delta^\mathcal{I}}\ R^\mathcal{I}(a, b) \geq \mathrm{sup}_{c \in \Delta^\mathcal{I}} R^\mathcal{I}(a, c) \otimes R^\mathcal{I}(c, b)$.

### Role Relationship Axioms

Axioms governing relationships between roles:

### Role Implication

**(implies-role $R_1$ $R_2$ $d$)** establishes that role $R_1$ implies role $R_2$ with degree $d$, formally $\mathrm{inf}_{x, y \in \Delta^\mathcal{I}}\ R_1^\mathcal{I}(x, y) \Rightarrow_L R_2^\mathcal{I}(x, y) \geq d$.

### Inverse Roles

**(inverse $R_1$ $R_2$)** declares that role $R_1$ is the inverse of role $R_2$, formally $R_1^\mathcal{I} \equiv {(R_2^\mathcal{I})}^{-1}$.

### Important Constraints

Several important constraints must be observed when using axioms:

- Transitive roles cannot be functional
- In Zadeh logic, $\Rightarrow$ is Zadeh’s set inclusion

## Queries

```python
queries := (
      '(' 'sat?' ')'                # is Knowledge base consistent?
    | '(' 'max-instance?' name concpet ')'
    | '(' 'min-instance?' name concept ')'
    | '(' 'all-instances?' concept ')'
    | '(' 'max-related?' name name name ')'
    | '(' 'min-related?' name name name')'
    | '(' 'max-subs?' concept concept ')'
    | '(' 'min-subs?' concept concept ')'
    | '(' 'max-g-subs?' concept concept ')'
    | '(' 'min-g-subs?' concept concept ')'
    | '(' 'max-l-subs?' concept concept ')'
    | '(' 'min-l-subs?' concept concept ')'
    | '(' 'max-kd-subs?' concept concept ')'
    | '(' 'min-kd-subs?' concept concept ')'
    | '(' 'max-sat?' concept name? ')'
    | '(' 'min-sat?' concept name? ')'
    | '(' 'max-var?' name ')'
    | '(' 'min-var?' name ')'
    | '(' 'defuzzify-lom?' concept name name ')'    # Defuzzify using the largest of the maxima
    | '(' 'defuzzify-mom?' concept name name ')'    # Defuzzify using the middle of the maxima
    | '(' 'defuzzify-som?' concept name name ')'    # Defuzzify using the smallest of the maxima
    | '(' 'bnp?' name ')'                           # Computes the Best Non-Fuzzy Performance (BNP) of a fuzzy number
)
```

### Knowledge Base Consistency Queries

Fundamental queries for knowledge base validation:

### Satisfiability Check

**(sat?)** checks if the knowledge base $\mathcal{K}$ is consistent, determining whether there exists a valid interpretation that satisfies all axioms.

### Instance Membership Queries

Queries for determining individual concept membership:

### Maximum Instance Membership

**(max-instance? $a$ $C$)** computes the maximum degree to which individual $a$ belongs to concept $C$, formally $\mathrm{sup}\ {n \mid \mathcal{K} \models \text{(instance a C n)}}$.

### Minimum Instance Membership

**(min-instance? $a$ $C$)** computes the minimum degree to which individual $a$ belongs to concept $C$, formally $\mathrm{inf}\ {n \mid \mathcal{K} \models \text{(instance a C n)}}$.

### All Instance Memberships

**(all-instances? $C$)** computes (min-instance? a C) for every individual $a$ in the knowledge base, providing a comprehensive view of concept membership.

### Role Relationship Queries

Queries for analyzing relationships between individuals:

### Maximum Role Relationship

**(max-related? $a$ $b$ $R$)** computes the maximum degree to which individuals $a$ and $b$ are related by role $R$, formally $\mathrm{sup}\ {n \mid \mathcal{K} \models \text{(related a b R n)} }$.

### Minimum Role Relationship

**(min-related? $a$ $b$ $R$)** computes the minimum degree to which individuals $a$ and $b$ are related by role $R$, formally $\mathrm{inf}\ {n \mid \mathcal{K} \models \text{(related a b R n)} }$.

### Concept Subsumption Queries

Queries for analyzing hierarchical relationships between concepts:

### Maximum Standard Subsumption

**(max-subs? $C$ $D$)** computes the maximum degree to which concept $D$ subsumes concept $C$, formally $\mathrm{sup}\ {n \mid \mathcal{K} \models \text{(implies D C n)} }$.

### Minimum Standard Subsumption

**(min-subs? $C$ $D$)** computes the minimum degree to which concept $D$ subsumes concept $C$, formally $\mathrm{inf}\ {n \mid \mathcal{K} \models \text{(implies D C n)} }$.

### Maximum Goedel Subsumption

**(max-g-subs? $C$ $D$)** computes the maximum degree of Goedel subsumption between concepts, formally $\mathrm{sup}\ {n \mid \mathcal{K} \models \text{(g-implies D C n)} }$.

### Minimum Goedel Subsumption

**(min-g-subs? $C$ $D$)** computes the minimum degree of Goedel subsumption between concepts, formally $\mathrm{inf}\ {n \mid \mathcal{K} \models \text{(g-implies D C n)} }$.

### Maximum Lukasiewicz Subsumption

**(max-l-subs? $C$ $D$)** computes the maximum degree of Lukasiewicz subsumption between concepts, formally $\mathrm{sup}\ {n \mid \mathcal{K} \models \text{(l-implies D C n)} }$.

### Minimum Lukasiewicz Subsumption

**(min-l-subs? $C$ $D$)** computes the minimum degree of Lukasiewicz subsumption between concepts, formally $\mathrm{inf}\ {n \mid \mathcal{K} \models \text{(l-implies D C n)} }$.

### Maximum Kleene-Dienes Subsumption

**(max-kd-subs? $C$ $D$)** computes the maximum degree of Kleene-Dienes subsumption between concepts, formally $\mathrm{sup}\ {n \mid \mathcal{K} \models \text{(kd-implies D C n)} }$.

### Minimum Kleene-Dienes Subsumption

**(min-kd-subs? $C$ $D$)** computes the minimum degree of Kleene-Dienes subsumption between concepts, formally $\mathrm{inf}\ {n \mid \mathcal{K} \models \text{(kd-implies D C n)} }$.

### Concept Satisfiability Queries

Queries for analyzing concept satisfiability across all models:

### Maximum Concept Satisfiability

**(max-sat? $C$ $a$)** computes the maximum satisfiability of concept $C$ across all interpretations, formally $\mathrm{sup}_{\mathcal{I}}\ \mathrm{sup}_{a \in \Delta^\mathcal{I}}\ C^\mathcal{I}(a)$.

### Minimum Concept Satisfiability

**(min-sat? $C$ $a$)** computes the minimum satisfiability of concept $C$ across all interpretations, formally $\mathrm{inf}_{\mathcal{I}}\ \mathrm{inf}_{a \in \Delta^\mathcal{I}}\ C^\mathcal{I}(a)$.

### Variable Optimization Queries

Queries for optimizing variable values within constraints:

### Maximum Variable Value

**(max-var? var)** computes the maximum value that variable **var** can take while maintaining knowledge base consistency, formally $\mathrm{sup}\ {\text{var} \mid \mathcal{K} \text{ is consistent}}$.

### Minimum Variable Value

**(min-var? var)** computes the minimum value that variable **var** can take while maintaining knowledge base consistency, formally $\mathrm{inf}\ {\text{var} \mid \mathcal{K} \text{ is consistent}}$.

### Defuzzification Queries

Queries for converting fuzzy values to crisp values using different strategies:

### Largest of Maxima Defuzzification

**(defuzzify-lom? $C$ $a$ $F$)** defuzzifies the value of feature $F$ using the largest of the maxima strategy, where concept $C$ represents Mamdani/Rules IF-THEN fuzzy rules for determining the feature value.

### Middle of Maxima Defuzzification

**(defuzzify-mom? $C$ $a$ $F$)** defuzzifies the value of feature $F$ using the middle of the maxima strategy, providing a balanced approach to crisp value selection.

### Smallest of Maxima Defuzzification

**(defuzzify-som? $C$ $a$ $F$)** defuzzifies the value of feature $F$ using the smallest of the maxima strategy, offering a conservative approach to defuzzification.

### Fuzzy Number Performance Analysis

### Best Non-Fuzzy Performance

**(bnp? $f$)** computes the Best Non-Fuzzy Performance (BNP) of a fuzzy number $f$, providing a measure of how well the fuzzy number can be represented as a crisp value.

### Important Notes on Defuzzification

In defuzzify queries, the concept $C$ represents several Mamdani/Rules IF-THEN fuzzy rules expressing how to obtain the value of the concrete feature $F$. These rules form the basis for the fuzzy inference process that determines the appropriate crisp output value.