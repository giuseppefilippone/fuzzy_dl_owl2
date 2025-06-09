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

### Definitions
|Example | | Definition|
| --- | --- | --- |
|(a, b, c) | fuzzy number | (a,b,c)|
|n | real number | (n,n,n) |
|(f+ f1 f2 $\ldots$ fn) | addition | $(\sum_{i = 0}^{n} a_i, \sum_{i = 0}^{n} b_i, \sum_{i = 0}^{n} c_i)$|
|(f- f1 f2) | subtraction | $(a_1−c_2, b_1 − b_2, c_1 − a_2)$ |
|(f* f1 f2 $\ldots$ fn) | product | $(\prod_{i = 0}^{n} a_i, \prod_{i = 0}^{n} b_i, \prod_{i = 0}^{n} c_i)$|
|(f/ f1 f2) | division | $(\frac{a_1}{c_2}, \frac{b_1}{b_2}, \frac{c_1}{a_2})$ |

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

### Definitions
|Rule|Meaning|
|--------------|----------------------|
|(functional F)                 | Define the feature F|
|(range F ```*integer*``` $k_1$ $k_2$)    | The range of $F$ is an integer number in $[k_1, k_2]$|
|(range F ```*real*``` $k_1$ $k_2$)       | The range of $F$ is a rational number in $[k_1, k_2]$|
|(range F ```*string*```)           | The range of $F$ is a string|
|(range F ```*boolean*```)          | The range of $F$ are booleans|

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

### Definitions
|Restriction|Definition|
| -- | -- |
|$(\mathrm{>=}\ F\ \text{variable})$| ${\mathrm{sup}}_{b \in {\Delta}_D} \[F^\mathcal{I} (x, b) \otimes (b \geq \text{variable})\]$|
|$(\mathrm{<=}\ F\ \text{variable})$| $\mathrm{sup}_{b \in \Delta_D} \[F^\mathcal{I} (x, b) \otimes (b \leq \text{variable})\]$|
|$(=\ F\ \text{variable}) $| $\mathrm{sup}_{b \in \Delta_D} \[F^\mathcal{I} (x, b) \otimes (b = \text{variable})\]$|
|$(\mathrm{>=}\ F\ \text{fuzzy\_number})$|$\mathrm{sup}_{b^\prime, b \in \Delta_D} \[F^\mathcal{I} (x, b) \otimes (b \geq b^\prime) \otimes {\text{fuzzy\_number}(b^\prime)}^\mathcal{I}\]$|
|$(\mathrm{<=}\ F\ \text{fuzzy\_number})$|$\mathrm{sup}_{b^\prime, b \in \Delta_D} \[F^\mathcal{I} (x, b) \otimes (b \leq b^\prime) \otimes {\text{fuzzy\_number}(b^\prime)}^\mathcal{I}\]$|
|$(=\ F\ \text{fuzzy\_number})$|$\mathrm{sup}_{b^\prime, b \in \Delta_D} \[F^\mathcal{I} (x, b) \otimes (b = b^\prime) \otimes {\text{fuzzy\_number}(b^\prime)}^\mathcal{I}\]$|
|$(\mathrm{>=}\ F\ \mathrm{function}(F_1, \ldots, F_n))$|$\mathrm{sup}_{b \in \Delta_D} \[F^\mathcal{I} (x, b) \otimes (b \geq {\mathrm{function}(F_1, \ldots, F_n)}^{\mathcal{I}})\]$|
|$(\mathrm{<=}\ F\ \mathrm{function}(F_1, \ldots, F_n))$|$\mathrm{sup}_{b \in \Delta_D} \[F^\mathcal{I} (x, b) \otimes (b \leq {\mathrm{function}(F_1, \ldots, F_n)}^{\mathcal{I}})\]$|
|$(=\ F\ \mathrm{function}(F_1, \ldots, F_n))$|$\mathrm{sup}_{b \in \Delta_D} \[F^\mathcal{I} (x, b) \otimes (b = {\mathrm{function}(F_1, \ldots, F_n)}^{\mathcal{I}})\]$|

- In datatype restrictions, the variable **variable** has to be declared **(free variable)** before its use in a datatype
restriction, using the **constraints** defined below;
- The value for $b$ has to be in the range $\[k_1,k_2\]$ subset or equivalent to $\[- k_{\infty}, k_{\infty}\]$ of the feature $F$, and the values for **variable**, $\mathbf{function}(F_1, \ldots, F_n)$ and the range of **fuzzy_number** have to be in $\[- k_{\infty}, k_{\infty}\]$, where $k_{\infty}$ is the maximal representable integer (see below for the table);
- In datatype restrictions, the variable **variable** may be replaced with a value, i.e., an integer, a real, a string, or a boolean constant (true, false), depending on the range of the feature $F$.

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
    | '(' 'show-abstract-fillers' name+ ')'             # show fillers and membership to any concept
    | '(' 'show-abstract-fillers-for' name{2, } ')'     # show fillers for an individuals and membership to any concept
    | '(' 'show-concepts' name+ ')'                     # show membership of individuals to any concept
    | '(' 'show-instances' name+ ')'                    # show value of the instances of the listed concepts
    | '(' 'show-variables' name+ ')'                    # show value of the listed variables
    | '(' 'show-language' ')'                           # show language of the KB, from ALC to SHIF(D)
)
```

### Usage
|Statement| Meaning |
| ---- | ---- |
|(show-concrete-fillers $F_1$ $\ldots$ $F_n$) | show value of the fillers of the features $F_i$|
|(show-concrete-fillers-for ind $F_1$ $\ldots$ $F_n$) | show value of the fillers of $F_i$ for the individual 'ind' |
|(show-concrete-instance-for ind $F$ $C_1$ $\ldots$ $C_n$) | show degrees of being the $F$ filler of the individual **ind** instance of $C_i$ |
|(show-abstract-fillers $R_1$ $\ldots$ $R_n$) | show fillers of $R_i$ and membership to any concept |
|(show-abstract-fillers-for ind $R_1$ $\ldots$ $R_n$) | show fillers of $R_i$ for the individual **ind** and membership to any concept |
|(show-concepts $a_1$ $\ldots$ $a_n$) | show membership of the individuals $a_i$ to any concept |
|(show-instances $C_1$ $\ldots$ $C_n$) | show value of the instances of the concepts $C_i$ |
|(show-variables $x_1$ $\ldots$ $x_n$) | show value of the variables $x_i$ |

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

### Definitions
| Expression | | Definition
| ---- | --- | --- |
|```*top*``` | top concept | $\top\ =\ 1$ |
|```*bottom*``` | bottom concept | $\perp\ =\ 0$ |
| A | atomic concept $A$ | $A^\mathcal{I}(x)$ |
| CFC | concrete fuzzy concept $CFC$ (e.g., crisp, left-shoulder, and so on) | $\mathrm{CFC}^\mathcal{I}(x)$ |
| DR | datatype restriction $DR$ | $\mathrm{DR}^\mathcal{I}(x)$ |
| (and $C_1$ $C_2$) | concept conjunction of $C_1$ and $C_2$ | $C_1^\mathcal{I}(x) \otimes C_2^\mathcal{I}(x)$ |
| (g-and $C_1$ $C_2$) | Goedel conjunction of $C_1$ and $C_2$ | $C_1^\mathcal{I}(x) \otimes_G C_2^\mathcal{I}(x)$ |
| (l-and $C_1$ $C_2$) | Lukasiewicz conjunction of $C_1$ and $C_2$ | $C_1^\mathcal{I}(x) \otimes_L C_2^\mathcal{I}(x)$ |
| (or $C_1$ $C_2$) | concept disjunction of $C_1$ and $C_2$ | $C_1^\mathcal{I}(x) \oplus C_2^\mathcal{I}(x)$ |
| (g-or $C_1$ $C_2$) | Goedel disjunction of $C_1$ and $C_2$ | $C_1^\mathcal{I}(x) \oplus_G C_2^\mathcal{I}(x)$ |
| (l-or $C_1$ $C_2$) | Lukasiewicz disjunction of $C_1$ and $C_2$ | $C_1^\mathcal{I}(x) \oplus_L C_2^\mathcal{I}(x)$ |
| (not $C$) | concept $C$ negation | $\ominus_L C^\mathcal{I}(x)$ |
| (implies $C_1$ $C_2$) | concept implication between $C_1$ and $C_2$ | $C_1^\mathcal{I}(x) \Rightarrow C_2^\mathcal{I}(x)$ |
| (g-implies $C_1$ $C_2$) | Goedel implication between $C_1$ and $C_2$ | $C_1^\mathcal{I}(x) \Rightarrow_G C_2^\mathcal{I}(x)$ |
| (l-implies $C_1$ $C_2$) | Lukasiewicz implication between $C_1$ and $C_2$ | $C_1^\mathcal{I}(x) \Rightarrow_L C_2^\mathcal{I}(x)$ |
| (kd-implies $C_1$ $C_2$) | Kleene-Dienes implication between $C_1$ and $C_2$ | $C_1^\mathcal{I}(x) \Rightarrow_\mathrm{KD} C_2^\mathcal{I}(x)$ |
| (all $R$ $C$) | universal role $R$ restriction for concept $C$ | $\mathrm{inf}_{y \in \Delta^\mathcal{I}}\ \\{ R^\mathcal{I}(x, y) \Rightarrow C^\mathcal{I}(y) \\} $ |
| (some $R$ $C$) | existential role $R$ restriction for concept $C$ | $\mathrm{sup}_{y \in \Delta^\mathcal{I}}\ \\{ R^\mathcal{I}(x, y) \otimes C^\mathcal{I}(y) \\} $ |
| (some $R$ $a$) | individual value restriction for role $R$ and individual $a$ | $R^\mathcal{I}(x, a) $ |
| (ua $s$ $C$) | upper approximation for a fuzzy relation $s$ and individual $a$ | $\mathrm{sup}_{y \in \Delta^\mathcal{I}}\ \\{ s^\mathcal{I}(x, y) \otimes C^\mathcal{I}(y) \\} $ |
| (lua $s$ $C$) | loose upper approximation for a fuzzy relation $s$ and individual $a$ | $\mathrm{sup}\_{z \in X}\ \\{ s^\mathcal{I}(x, z) \otimes \mathrm{sup}\_{y \in \Delta^\mathcal{I}} s^\mathcal{I}(y, z) \otimes C^\mathcal{I}(x) \\}$ |
| (tua $s$ $C$) | tight upper approximation for a fuzzy relation $s$ and individual $a$ | $\mathrm{inf}\_{z \in X}\ \\{ s^\mathcal{I}(x, z) \Rightarrow \mathrm{sup}\_{y \in \Delta^\mathcal{I}} s^\mathcal{I}(y, z) \otimes C^\mathcal{I}(x) \\}$ |
| (la $s$ $C$) | lower approximation for a fuzzy relation $s$ and individual $a$ | $\mathrm{inf}_{y \in \Delta^\mathcal{I}}\ s^\mathcal{I}(x, y) \Rightarrow C^\mathcal{I}(y) $ |
| (lla $s$ $C$) | loose lower approximation for a fuzzy relation $s$ and individual $a$ | $\mathrm{sup}\_{z \in X}\ \\{ s^\mathcal{I}(x, z) \otimes \mathrm{inf}\_{y \in \Delta^\mathcal{I}} s^\mathcal{I}(y, z) \otimes C^\mathcal{I}(x) \\}$ |
| (tla $s$ $C$) | tight lower approximation for a fuzzy relation $s$ and individual $a$ | $\mathrm{inf}\_{z \in X}\ \\{ s^\mathcal{I}(x, z) \Rightarrow \mathrm{inf}\_{y \in \Delta^\mathcal{I}} s^\mathcal{I}(y, z) \otimes C^\mathcal{I}(x) \\}$ |
| (self C) | local reflexivity concept | $C^\mathcal{I}(x)(x, x)$ |
| (MOD C) | modifier MOD applied to concept $C$ | ${f_m}(C^\mathcal{I}(x))$, where $f_m$ is the modifier associated to MOD |
| (FN) | fuzzy number FN | $\mathrm{FM}^\mathcal{I}(x)$ |
| ([>= var ] C) | threshold concept | if $C^\mathcal{I}(x) \geq \mathrm{var}$, then $C^\mathcal{I}(x)$; otherwise $0$|
| ([<= var ] C) | threshold concept | if $C^\mathcal{I}(x) \leq \mathrm{var}$, then $C^\mathcal{I}(x)$; otherwise $0$|
| (n C) | weighted concept C with weight n | $n C^\mathcal{I}(x)$|
| (w-sum ($n_1$ $C_1$) $\ldots$ ($n_k$ $C_k$) ) | weighted sum of concepts | $\sum_{i=1}^{k} n_i C_i^\mathcal{I}(x)$ |
| (w-max ($v_1$ $C_1$) $\ldots$ ($v_k$ $C_k$) ) | weighted max of concepts | $\max_{i=1}^{k} \min \\{v_i, x_i\\}$|
| (w-min ($v_1$ $C_1$) $\ldots$ ($v_k$ $C_k$) ) | weighted min of concepts | $\min_{i=1}^{k} \max \\{1 - v_i, x_i\\}$|
| (w-sum-zero ($n_1$ $C_1$) $\ldots$ ($n_k$ $C_k$) ) | weighted min of concepts | if $C_i^\mathcal{I}(x) = 0$ for some $i \in \\{1, \ldots, k\\}$, then $0$; otherwise $\sum_{i=1}^{k} n_i C_i^\mathcal{I}(x)$|
|(owa ($w_1$, $\ldots$, $w_n$) ($C_1$, $\ldots$, $C_n$) | OWA aggregation operator | $\sum_{i=1}^n w_i y_i $ |
|(q-owa $Q$ ($C_1$, $\ldots$, $C_n$) | quantifier-guided OWA with name $Q$, where $Q$ is a right-shoulder or a linear function | $\sum_{i=1}^n w_i y_i $, where $w_i = Q(\frac{i}{n}) - Q(\frac{i - 1}{n})$|
|(choquet ($w_1$, $\ldots$, $w_n$) ($C_1$, $\ldots$, $C_n$) | Choquet integral | $y_1 w_1 + \sum_{i=2}^n (y_i - y_{i - 1}) w_i $ |
|(sugeno ($v_1$, $\ldots$, $v_n$) ($C_1$, $\ldots$, $C_n$) | Sugeno integral | $\max_{i=1}^n \min \\{y_i, mu_i\\}$ |
|(q-sugeno ($v_1$, $\ldots$, $v_n$) ($C_1$, $\ldots$, $C_n$) | Quasi-Sugeno integral | $\max_{i=1}^n y_i \otimes_L mu_i $|
|(sigma-count $R$ $C$ $\\{a_1\ \ldots\ a_k\\}$ $F_C$ | A Sigma-Count concept with role $R$ and associated to the concept $C$, the individuals $a_i$ and the fuzzy concrete concept $F_C$ | |

- $n_1, \ldots, n_k \in \[0, 1\]$, with $\sum_{i=1}^k\ n_i \leq 1$;
- $w_1, \ldots, w_n \in \[0, 1\]$, with $\sum_{i=1}^n\ w_i = 1$;
- $v_1, \ldots, v_n \in \[0, 1\]$, with $\max_{i=1}^n\ v_i = 1$;
- $y_i$ is the $i$-largest of the $C_i^\mathcal{I}(x)$;
- $ow_i$ is the weight $v_i$ of the $i$-largest of the $C_i^\mathcal{I}(x)$;
- $mu_i$ is defined as follows: $mu_1 = ow_1$, and $mu_i = ow_i \oplus mu_{i - 1}$ for $i \in \\{2, \ldots, n\\}$;
- Fuzzy numbers can only appear in existential, universal and datatype restrictions;
- In threshold concepts **var** may be replaced with $ w \in \[0, 1\] $;
- Fuzzy relations $s$ should be previously defined as fuzzy similarity relation or a fuzzy equivalence relation as **(define-fuzzy-similarity s)** or **(define-fuzzy-equivalence s)**, respectively;
- Fuzzy concrete concept $F_C$ in **sigma-count** concept has to be previously defined as **left-shoulder**, **right-shoulder** or **triangular** concept with **define-fuzzy-concept**.

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
    | '(' 'z-implies' concept concept numbers? ')'      # Zadeh’s set GCI with degree 'numbers'
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

### Definitions
| Axiom | Definition |
| ---- | ---- |
| (instance a C d) | $C^\mathcal{I}(a^\mathcal{I}) \geq d $ |
| (related a b R d) | $R^\mathcal{I}(a^\mathcal{I}, b^\mathcal{I}) \geq d $ |
| (implies $C_1$ $C_2$ d) | $\mathrm{inf}\_{x \in \Delta^\mathcal{I}}\ C_1^\mathcal{I}(x) \Rightarrow C_2^\mathcal{I}(x) \geq d$ |
| (g-implies $C_1$ $C_2$ d) | $\mathrm{inf}\_{x \in \Delta^\mathcal{I}}\ C_1^\mathcal{I}(x) \Rightarrow_G C_2^\mathcal{I}(x) \geq d$ |
| (kd-implies $C_1$ $C_2$ d) | $\mathrm{inf}\_{x \in \Delta^\mathcal{I}}\ C_1^\mathcal{I}(x) \Rightarrow_{\mathrm{KD}} C_2^\mathcal{I}(x) \geq d$ |
| (l-implies $C_1$ $C_2$ d) | $\mathrm{inf}\_{x \in \Delta^\mathcal{I}}\ C_1^\mathcal{I}(x) \Rightarrow_{L} C_2^\mathcal{I}(x) \geq d $ |
| (z-implies $C_1$ $C_2$ d) | $\mathrm{inf}\_{x \in \Delta^\mathcal{I}}\ C_1^\mathcal{I}(x) \Rightarrow_Z C_2^\mathcal{I}(x) \geq d$ |
| (define-concept A C) | $\forall_{x \in \Delta^\mathcal{I}}\ A^\mathcal{I}(x) = C^\mathcal{I}(x) $ |
| (define-primitive-concept A C) | $\mathrm{inf}_{x \in \Delta^\mathcal{I}}\ A^\mathcal{I}(x) \leq C^\mathcal{I}(x) $ |
| (equivalent-concepts $C_1$ $C_2$) | $\forall_{x \in \Delta^\mathcal{I}}\ C_1^\mathcal{I}(x) = C_2^\mathcal{I}(x) $ |
| (disjoint $C_1$ $\ldots$ $C_k$) | (implies (g-and $C_i$ $C_j$) ```*bottom*```), i.e., $\forall_{i, j \in \\{1, \ldots, k\\}, i < j}\ (C_i^\mathcal{I}(x) \otimes_G C_j^\mathcal{I}(x)) \Rightarrow \perp$ |
| (disjoint-union $C_1$ $\ldots$ $C_k$) | $C_1 = \bigoplus_{i=2}^k C_i$ and $\forall_{i, j \in \\{1, \ldots, k\\}, i < j}\ (C_i^\mathcal{I}(x) \otimes_G C_j^\mathcal{I}(x)) \Rightarrow \perp$ |
| (range R $C$) | (implies ```*top*``` (all R C)), i.e., $\top \Rightarrow \mathrm{inf}\_{y \in \Delta^\mathcal{I}}\ \\{ R^\mathcal{I}(x, y) \Rightarrow C^\mathcal{I}(y) \\}$ |
| (domain R $C$) | (implies (some R ```*top*```) C), i.e., $\mathrm{sup}\_{y \in \Delta^\mathcal{I}}\ \\{ R^\mathcal{I}(x, y) \otimes \top \\} \Rightarrow C^\mathcal{I}(x)$ |
| (functional R) | $R^\mathcal{I}(a, b) = R^\mathcal{I}(a, c) \rightarrow b = c$ |
| (inverse-functional R) |  $R^\mathcal{I}(b, a) = R^\mathcal{I}(c, a) \rightarrow b = c$ |
| (reflexive R) | $\forall_{a \in \Delta^\mathcal{I}}\ R^\mathcal{I}(a, a) = 1$ |
| (symmetric R) | $\forall_{a, b \in \Delta^\mathcal{I}}\ R^\mathcal{I}(a, b) = R^\mathcal{I}(b, a)$ |
| (transitive R) | $\forall_{a, b \in \Delta^\mathcal{I}}\ R^\mathcal{I}(a, b) \geq \mathrm{sup}_{c \in \Delta^\mathcal{I}} R^\mathcal{I}(a, c) \otimes R^\mathcal{I}(c, b)$ |
| (implies-role $R_1$ $R_2$ d) | $\mathrm{inf}_{x, y \in \Delta^\mathcal{I}}\ R_1^\mathcal{I}(x, y) \Rightarrow_L R_2^\mathcal{I}(x, y) \geq d$ |
| (inverse $R_1$ $R_2$) | $R_1^\mathcal{I} \equiv {(R_2^\mathcal{I})}^{-1}$ |

- Transitive roles cannot be functional.
- In Zadeh logic, $\Rightarrow$ is Zadeh’s set inclusion.

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

### Definitions
| Query | Definition |
| --- | --- |
| (sat?) | Check if $\mathcal{K}$ is consistent |
| (max-instance? a C) | $\mathrm{sup}\ \\{n \mid \mathcal{K} \models \text{(instance a C n)}\\}$ |
| (min-instance? a C)|  $\mathrm{inf}\ \\{n \mid \mathcal{K} \models \text{(instance a C n)}\\}$ |
| (all-instances? C) | (min-instance? a C) for every individual of $\mathcal{K}$ |
| (max-related? a b R) | $\mathrm{sup}\ \\{n \mid \mathcal{K} \models \text{(related a b R n)} \\}$ |
| (min-related? a b R) | $\mathrm{inf}\ \\{n \mid \mathcal{K} \models \text{(related a b R n)} \\}$ |
| (max-subs? C D) | $\mathrm{sup}\ \\{n \mid \mathcal{K} \models \text{(implies D C n)} \\}$|
| (min-subs? C D) | $\mathrm{inf}\ \\{n \mid \mathcal{K} \models \text{(implies D C n)} \\}$|
| (max-g-subs? C D) | $\mathrm{sup}\ \\{n \mid \mathcal{K} \models \text{(g-implies D C n)} \\}$ |
| (min-g-subs? C D) | $\mathrm{inf}\ \\{n \mid \mathcal{K} \models \text{(g-implies D C n)} \\}$ |
| (max-l-subs? C D) | $\mathrm{sup}\ \\{n \mid \mathcal{K} \models \text{(l-implies D C n)} \\}$ |
| (min-l-subs? C D) | $\mathrm{inf}\ \\{n \mid \mathcal{K} \models \text{(l-implies D C n)} \\}$|
| (max-kd-subs? C D) | $\mathrm{sup}\ \\{n \mid \mathcal{K} \models \text{(kd-implies D C n)} \\}$ |
| (min-kd-subs? C D) | $\mathrm{inf}\ \\{n \mid \mathcal{K} \models \text{(kd-implies D C n)} \\}$ |
| (max-sat? C a) | $\mathrm{sup}\_{\mathcal{I}}\ \mathrm{sup}\_{a \in \Delta^\mathcal{I}}\ C^\mathcal{I}(a)$|
| (min-sat? C a) | $\mathrm{inf}\_{\mathcal{I}}\ \mathrm{inf}\_{a \in \Delta^\mathcal{I}}\ C^\mathcal{I}(a)$|
| (max-var? var) | $\mathrm{sup}\ \\{\text{var} \mid \mathcal{K} \text{ is consistent}\\}$|
| (min-var? var) | $\mathrm{inf}\ \\{\text{var} \mid \mathcal{K} \text{ is consistent}\\}$|
| (defuzzify-lom? C a F) | Defuzzify the value of F using the largest of the maxima |
| (defuzzify-mom? C a F) | Defuzzify the value of F using the middle of the maxima |
| (defuzzify-som? C a F) | Defuzzify the value of F using the smallest of the maxima |
| (bnp? f) | Computes the Best Non-Fuzzy Performance (BNP) of a fuzzy number $f$ |

- In defuzzify queries, the concept $C$ represents several Mamdani/Rules IF-THEN fuzzy rules expressing how to obtain the value of the concrete feature F.
