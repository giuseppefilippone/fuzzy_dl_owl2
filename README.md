![Docs](https://img.shields.io/badge/docs-passing-brightgreen.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
[![Documentation](https://img.shields.io/badge/Read%20the%20Docs-8CA1AF?logo=readthedocs&logoColor=white)](https://fuzzy-dl-owl2.readthedocs.io/en/latest)
[![PyPI](https://img.shields.io/pypi/v/fuzzy-dl-owl2.svg)](https://pypi.org/project/fuzzy-dl-owl2/)
![Python Versions](https://img.shields.io/pypi/pyversions/fuzzy-dl-owl2.svg)
![Code Style](https://img.shields.io/badge/code%20style-python-green)


# Fuzzy DL OWL 2

A Python porting of the [Fuzzy Description Language](https://www.umbertostraccia.it/cs/software/fuzzyDL/fuzzyDL.html) (FuzzyDL) and the [Fuzzy OWL 2](https://www.umbertostraccia.it/cs/software/FuzzyOWL/index.html) framework, for representing fuzzy logic within description logic and for mapping a knowledge base represented in FuzzyDL to a Fuzzy OWL 2 construct in RDF/XML format.

**📖 Full documentation: [fuzzy-dl-owl2.readthedocs.io](https://fuzzy-dl-owl2.readthedocs.io/en/latest)**

Features:
- Object-oriented representation of Fuzzy Description Logic elements
- Object-oriented representation of Fuzzy OWL 2 elements
- Mapping from FuzzyDL to Fuzzy OWL 2
- Mapping from Fuzzy OWL 2 to FuzzyDL
- Reasoning in FuzzyDL

## Installation

```bash
pip install fuzzy-dl-owl2
```

## Quick start

```python
from fuzzy_dl_owl2.fuzzydl.parser import DLParserFast as DLParser

DLParser.main("./example.fdl")
```

See the [Usage guide](https://fuzzy-dl-owl2.readthedocs.io/en/latest/usage.html) for reasoning, querying, and FuzzyDL ⇄ Fuzzy OWL 2 conversion examples.

## Documentation

The full reference lives on [Read the Docs](https://fuzzy-dl-owl2.readthedocs.io/en/latest):

- [Installation & configuration](https://fuzzy-dl-owl2.readthedocs.io/en/latest/install_and_config.html) — `CONFIG.ini` / `.env`, MILP solver setup (Gurobi, CPLEX, CBC, GLPK, HiGHS, MIP), and the optional compiled fast parser.
- [Grammar](https://fuzzy-dl-owl2.readthedocs.io/en/latest/grammar.html) — the full FuzzyDL (`.fdl`) language.
- [Fuzzy concepts](https://fuzzy-dl-owl2.readthedocs.io/en/latest/concepts.html), [queries](https://fuzzy-dl-owl2.readthedocs.io/en/latest/queries.html), [modifiers & degrees](https://fuzzy-dl-owl2.readthedocs.io/en/latest/modifiers_degrees.html).
- [Fuzzy OWL 2 XML annotations](https://fuzzy-dl-owl2.readthedocs.io/en/latest/xml.html) and the [reasoner architecture](https://fuzzy-dl-owl2.readthedocs.io/en/latest/architecture.html).

## Examples

The `dl-examples` directory contains sample knowledge bases written in the FuzzyDL language.

## Test

The `test` directory contains the `unittest` files; `test_suite.py` is the full suite. The knowledge bases used by the tests are in `examples/TestSuite`.

## License

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).