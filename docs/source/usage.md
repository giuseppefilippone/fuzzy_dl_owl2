
# Usage

## Reasoning

### Knowledge base in example.fdl
```python
(define-fuzzy-logic lukasiewicz)
(define-modifier very linear-modifier(0.8))
(define-fuzzy-concept eq243 crisp(0, 400, 243, 243))
(define-fuzzy-concept geq300 crisp(0, 400, 300, 400))
(define-fuzzy-concept High right-shoulder(0, 400, 180, 250))
(define-concept SportCar (and Car (some speed (very High))))
(instance ferrari (and Car (some speed geq300)) 1)
(instance audi (and Car (some speed eq243)) 1)

(min-instance? audi SportCar)
```

### Python code

```python
from fuzzy_dl_owl2 import DLParser

DLParser.main("./example.fdl")  # "Is audi instance of SportCar ? >= 0.92"
```

## Fuzzy OWL 2

### From *.fdl to *.owl

```python
from fuzzy_dl_owl2 import FuzzydlToOwl2

fdl = FuzzydlToOwl2("./example.fdl", "example.owl")
fdl.run()  # save example.owl in the subdirectory "./results"
```

### From *.owl to *.fdl

```python
from fuzzy_dl_owl2 import FuzzyOwl2ToFuzzyDL

fdl = FuzzyOwl2ToFuzzyDL("./results/example.owl", "example.fdl")
fdl.translate_owl2ontology()  # save example.fdl in the subdirectory "./results"
```
