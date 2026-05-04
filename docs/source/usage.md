
# Usage

In this section, we will see how to use the FuzzyDL reasoner to query a knowledge base defined in the FDL language, and how to translate between FDL and OWL 2 ontologies. We will define a knowledge base in an FDL file, and then we will use the `DLParser` class to parse the file and execute the queries defined in it. We will also see how to translate an FDL knowledge base into an OWL 2 ontology, and vice versa.

## Setting up the CONFIG.ini file

Before running the examples, make sure to set up the `CONFIG.ini` file in the root directory of the project. This file contains configuration settings for the FuzzyDL reasoner, such as the debug print option, the epsilon value for numerical comparisons, the maximum number of individuals to consider in reasoning, and the label used for OWL annotations. You can adjust these settings according to your needs. For example, you can set `debugPrint` to `True` to enable debug output, or set `maxIndividuals` to a specific number to limit the number of individuals considered in reasoning.

Sample `CONFIG.ini` file:
```
[DEFAULT]
debugPrint = False
epsilon = 0.001
maxIndividuals = -1
owlAnnotationLabel = fuzzyLabel
milpProvider = mip
```

## Reasoning

In this section, we will see how to use the FuzzyDL reasoner to query a knowledge base defined in the FDL language. We will define a knowledge base in an FDL file, and then we will use the `DLParser` class to parse the file and execute the queries defined in it.

### Knowledge base in example.fdl
In the following example, we define a knowledge base in the FDL language, which includes concepts, modifiers, and instances. We then query the knowledge base to determine the membership degree of specific instances with respect to a complex concept.
Specifically, we define a fuzzy logic (`Łukasiewicz`), a linear modifier `very`, crisp concepts for speed, a crisp concept `eq243` with a crisp value of $243$, a crisp concept `geq300` with a crisp interval in $[300, 400]$, a fuzzy concept `High` with a right shoulder function in $[180, 250]$, and a modified concept `VeryHigh`.
We then define a complex concept `SportCar` that combines the concept of `Car` with the condition that its speed is `VeryHigh`.
Finally, we create two instances of `Car` with different speeds and query their membership degrees with respect to the `SportCar` concept.
The instances `audi` and `ferrari` will have different membership degrees to the `SportCar` concept based on their defined speeds and the modifiers applied to the `High` concept. The queries will return the membership degrees, which indicate how well each instance fits the definition of a `SportCar`.

```python
# Defining the logic to be used in the knowledge base, in this case, we are using the Łukasiewicz fuzzy logic.
(define-fuzzy-logic lukasiewicz)

# Defining a linear modifier "very" with a parameter of 0.8, which will be used to modify the membership degree of concepts.
(define-modifier very linear-modifier(0.8))

# Defining crisp concepts for speed with specific values
(define-fuzzy-concept eq243 crisp(0, 400, 243, 243))
(define-fuzzy-concept geq300 crisp(0, 400, 300, 400))
# Defining a fuzzy concept for speed with a right shoulder function, where the membership degree starts to increase from 180, reaches 1 at 250, and remains 1 afterwards.
(define-fuzzy-concept High right-shoulder(0, 400, 180, 250))
# Defining a modified concept "VeryHigh" by applying "very" to "High".
(define-fuzzy-concept VeryHigh modified(very, High))

# Defining the complex concept "SportCar" as a Car with a speed that is "VeryHigh".
(define-concept SportCar (and Car (some speed VeryHigh)))

# Defining two instances of Car with different speeds.
(instance ferrari (and Car (some speed geq300)) 1)
(instance audi (and Car (some speed eq243)) 1)

# What is the membership degree of "audi" with respect to the concept "SportCar"?
(min-instance? audi SportCar)
# What is the membership degree of "ferrari" with respect to the concept "SportCar"?
(min-instance? ferrari SportCar)
```

### Python code with the main function

In this case, the main function will parse the knowledge base and execute the query, printing the result in the log output.
The log output will be written in a file in the subdirectory `./logs/reasoner/CURRENT_YEAR/CURRENT_MONTH/CURRENT_DAY/` with a name that includes the time of the execution, for example `fuzzydl_HH-MM-SS.log`.

```python
from fuzzy_dl_owl2.fuzzydl.parser import DLParser

DLParser.main("./example.fdl")
# "Is audi instance of SportCar ? >= 0.92"
# "Is ferrari instance of SportCar ? >= 1.0"
```

An example of the log output is given below, where `DATETIME` is the date and time of the execution.
```
DATETIME - INFO -- Knowledge Base parsed in 0.015450833s
DATETIME - INFO -- Using Python-MIP package version 1.16rc0
DATETIME - INFO -- Is audi instance of SportCar? >= 0.92
DATETIME - INFO -- Time (s): 0.171397584
DATETIME - INFO -- Is ferrari instance of SportCar? >= 1.0
DATETIME - INFO -- Time (s): 0.004942084
```

### Python code with more control on the output

In this case, the parser will parse the knowledge base and execute the query, but it will not print the result in the log output. Instead, it will return a `Solution` object that contains the result of the query, which can be printed in a more readable format. The `Solution` object has a method `is_consistent_kb()` that checks if the knowledge base is consistent, and a `__str__()` method that returns a string representation of the solution, which includes the membership degree of the instance with respect to the concept.

```python
from fuzzy_dl_owl2.fuzzydl.parser import DLParser
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution

kb, queries = DLParser.get_kb("./example.fdl") # parse the knowledge base and get the queries
kb.solve_kb() # solve the knowledge base to check for consistency and prepare for answering queries

# Execute the queries and print the results
for query in queries:
    # Execute the query and get the result as a Solution object
    result: Solution = query.solve(kb)
    # Check if the knowledge base is consistent before printing the result
    if not result.is_consistent_kb():
        continue
    # Print the query and the result in a readable format
    print(f"{query}{result}")
    # Is audi instance of SportCar ? >= 0.92
    # Is ferrari instance of SportCar ? >= 1.0
```

## Fuzzy OWL 2

### From *.fdl to *.owl

In this example, the `example.fdl` file will be parsed and translated into an OWL 2 ontology, which will be saved in the subdirectory `./results/` with the name `example.owl`. The resulting OWL 2 ontology will contain the same knowledge base as the original FDL file, but in a format that can be used with OWL 2 reasoners.

```python
from fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2 import FuzzydlToOwl2

# The FuzzydlToOwl2 class is used to translate an FDL knowledge base into an OWL 2 ontology. The constructor takes two arguments: the path to the input FDL file and the path to the output OWL file. The run() method performs the translation and saves the resulting OWL ontology in the specified location.
fdl = FuzzydlToOwl2("./example.fdl", "example.owl")
fdl.run()  # save example.owl in the subdirectory "./results"
```

### From *.owl to *.fdl

In this example, the `example.owl` file will be parsed and translated into an FDL knowledge base, which will be saved in the subdirectory `./results/` with the name `example.fdl`. The resulting FDL knowledge base will contain the same knowledge as the original OWL 2 ontology, but in a format that can be used with FDL reasoners.

```python
from fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2_to_fuzzydl import FuzzyOwl2ToFuzzyDL

# The FuzzyOwl2ToFuzzyDL class is used to translate an OWL 2 ontology into an FDL knowledge base. The constructor takes two arguments: the path to the input OWL file and the path to the output FDL file. The translate_owl2ontology() method performs the translation and saves the resulting FDL knowledge base in the specified location.
fdl = FuzzyOwl2ToFuzzyDL("./results/example.owl", "example.fdl")
fdl.translate_owl2ontology()  # save example.fdl in the subdirectory "./results"
```
