# Fuzzy DL OWL 2
A python porting of the [Fuzzy Description Language](https://www.umbertostraccia.it/cs/software/fuzzyDL/fuzzyDL.html) and the [Fuzzy OWL 2](https://www.umbertostraccia.it/cs/software/FuzzyOWL/index.html) framework.

A lightweight Python porting of the Fuzzy Description Language (FuzzyDL) and the Fuzzy OWL 2 framework, designed for representing fuzzy logic within description logic and for mapping an knowledge base represented in FuzzyDL to a Fuzzy OWL 2 construct in RDF/XML format.

Features:
- Object-oriented representation of Fuzzy Description Logic elements
- Object-oriented representation of Fuzzy OWL 2 elements
- Mapping from FuzzyDL to Fuzzy OWL 2
- Mapping from Fuzzy OWL 2 to FuzzyDL
- Reasoning in FuzzyDL

## Directory dl-examples

The directory `dl-examples` contains a few examples of Knowledge Bases written using the Fuzzy Description Logic language.

## Project Structure

```text
fuzzy_dl_owl2
├── __init__.py
├── fuzzydl
│   ├── __init__.py
│   ├── assertion
│   │   ├── __init__.py
│   │   ├── assertion.py
│   │   └── atomic_assertion.py
│   ├── classification_node.py
│   ├── concept
│   │   ├── __init__.py
│   │   ├── all_some_concept.py
│   │   ├── approximation_concept.py
│   │   ├── atomic_concept.py
│   │   ├── choquet_integral.py
│   │   ├── concept.py
│   │   ├── concrete
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   ├── crisp_concrete_concept.py
│   │   │   ├── fuzzy_concrete_concept.py
│   │   │   ├── fuzzy_number
│   │   │   │   ├── __init__.py
│   │   │   │   └── triangular_fuzzy_number.py
│   │   │   ├── left_concrete_concept.py
│   │   │   ├── linear_concrete_concept.py
│   │   │   ├── modified_concrete_concept.py
│   │   │   ├── right_concrete_concept.py
│   │   │   ├── trapezoidal_concrete_concept.py
│   │   │   └── triangular_concrete_concept.py
│   │   ├── ext_threshold_concept.py
│   │   ├── has_value_concept.py
│   │   ├── implies_concept.py
│   │   ├── interface
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   ├── has_concept_interface.py
│   │   │   ├── has_concepts_interface.py
│   │   │   ├── has_role_concept_interface.py
│   │   │   ├── has_role_interface.py
│   │   │   ├── has_value_interface.py
│   │   │   └── has_weighted_concepts_interface.py
│   │   ├── modified
│   │   │   ├── __init__.py
│   │   │   ├── linearly_modified_concept.py
│   │   │   ├── modified_concept.py
│   │   │   └── triangularly_modified_concept.py
│   │   ├── negated_nominal.py
│   │   ├── operator_concept.py
│   │   ├── owa_concept.py
│   │   ├── qowa_concept.py
│   │   ├── quasi_sugeno_integral.py
│   │   ├── self_concept.py
│   │   ├── sigma_concept.py
│   │   ├── sigma_count.py
│   │   ├── string_concept.py
│   │   ├── sugeno_integral.py
│   │   ├── threshold_concept.py
│   │   ├── truth_concept.py
│   │   ├── value_concept.py
│   │   ├── weighted_concept.py
│   │   ├── weighted_max_concept.py
│   │   ├── weighted_min_concept.py
│   │   ├── weighted_sum_concept.py
│   │   └── weighted_sum_zero_concept.py
│   ├── concept_equivalence.py
│   ├── concrete_feature.py
│   ├── degree
│   │   ├── __init__.py
│   │   ├── degree_expression.py
│   │   ├── degree_numeric.py
│   │   ├── degree_variable.py
│   │   └── degree.py
│   ├── domain_axiom.py
│   ├── exception
│   │   ├── __init__.py
│   │   ├── fuzzy_ontology_exception.py
│   │   └── inconsistent_ontology_exception.py
│   ├── feature_function.py
│   ├── fuzzydl_to_owl2.py
│   ├── general_concept_inclusion.py
│   ├── individual
│   │   ├── __init__.py
│   │   ├── created_individual.py
│   │   ├── individual.py
│   │   └── representative_individual.py
│   ├── knowledge_base.py
│   ├── label.py
│   ├── milp
│   │   ├── __init__.py
│   │   ├── expression.py
│   │   ├── inequation.py
│   │   ├── milp_helper.py
│   │   ├── show_variables_helper.py
│   │   ├── solution.py
│   │   ├── term.py
│   │   └── variable.py
│   ├── modifier
│   │   ├── __init__.py
│   │   ├── linear_modifier.py
│   │   ├── modifier.py
│   │   └── triangular_modifier.py
│   ├── parser
│   │   ├── __init__.py
│   │   └── dl_parser.py
│   ├── primitive_concept_definition.py
│   ├── query
│   │   ├── __init__.py
│   │   ├── all_instances_query.py
│   │   ├── bnp_query.py
│   │   ├── classification_query.py
│   │   ├── defuzzify
│   │   │   ├── __init__.py
│   │   │   ├── defuzzify_query.py
│   │   │   ├── lom_defuzzify_query.py
│   │   │   ├── mom_defuzzify_query.py
│   │   │   └── som_defuzzify_query.py
│   │   ├── instance_query.py
│   │   ├── kb_satisfiable_query.py
│   │   ├── max
│   │   │   ├── __init__.py
│   │   │   ├── max_instance_query.py
│   │   │   ├── max_query.py
│   │   │   ├── max_related_query.py
│   │   │   ├── max_satisfiable_query.py
│   │   │   └── max_subsumes_query.py
│   │   ├── min
│   │   │   ├── __init__.py
│   │   │   ├── min_instance_query.py
│   │   │   ├── min_query.py
│   │   │   ├── min_related_query.py
│   │   │   ├── min_satisfiable_query.py
│   │   │   └── min_subsumes_query.py
│   │   ├── query.py
│   │   ├── related_query.py
│   │   ├── satisfiable_query.py
│   │   └── subsumption_query.py
│   ├── range_axiom.py
│   ├── relation.py
│   ├── restriction
│   │   ├── __init__.py
│   │   ├── has_value_restriction.py
│   │   └── restriction.py
│   ├── role_parent_with_degree.py
│   └── util
│       ├── __init__.py
│       ├── config_reader.py
│       ├── constants.py
│       ├── util.py
│       └── utils.py
└── fuzzyowl2
    ├── __init__.py
    ├── fuzzyowl2_to_fuzzydl.py
    ├── fuzzyowl2.py
    ├── owl_types
    │   ├── __init__.py
    │   ├── choquet_concept.py
    │   ├── concept_definition.py
    │   ├── fuzzy_datatype.py
    │   ├── fuzzy_modifier.py
    │   ├── fuzzy_nominal_concept.py
    │   ├── fuzzy_property.py
    │   ├── left_shoulder_function.py
    │   ├── linear_function.py
    │   ├── linear_modifier.py
    │   ├── modified_concept.py
    │   ├── modified_function.py
    │   ├── modified_property.py
    │   ├── owa_concept.py
    │   ├── property_definition.py
    │   ├── qowa_concept.py
    │   ├── quasi_sugeno_concept.py
    │   ├── right_shoulder_function.py
    │   ├── sugeno_concept.py
    │   ├── trapezoidal_function.py
    │   ├── triangular_function.py
    │   ├── triangular_modifer.py
    │   ├── weighted_concept.py
    │   ├── weighted_max_concept.py
    │   ├── weighted_min_concept.py
    │   ├── weighted_sum_concept.py
    │   └── weighted_sum_zero_concept.py
    ├── parser
    │   ├── __init__.py
    │   ├── owl2_parser.py
    │   └── owl2_xml_parser.py
    └── util
        ├── __init__.py
        ├── constants.py
        └── fuzzy_xml.py
```

## Test

The directory `test` contains the `unittest` files. In particular, the file `test_suite.py` contains all the test suite.
The directory `examples/TestSuite` contains all the knowledge bases used for the tests.

## License

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International.
