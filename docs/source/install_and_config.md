# Installation and Configuration

Check the [repository](https://github.com/giuseppefilippone/fuzzy_dl_owl2/). The library is available on PyPI, so you can install it using pip: `pip install fuzzy-dl-owl2`.

Examples of supported Fuzzy Description Logic Constructs

| Python Class         | Description                       |
|----------------------|-----------------------------------|
| AtomicConcept        | Define an atomic concept          |
| ChoquetIntegral      | Define a choquet integral concept |
| ApproximationConcept | Define a tight/upper/* lower/upper approximation concept |

## Configuration of the MILP solver

Since version 1.0.1 uses `Gurobi Optimizer` (see [gurobipy](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python) for the Fuzzy DL reasoning, please create a GUROBI license to use this library.

For the configuration, create a `CONFIG.ini` file in the same directory used for the execution of the library.
Example of your execution directory:
```text
your_directory
├── CONFIG.ini
├── your_file.py
```

The file `CONFIG.ini` is structured as follows:
```text
[DEFAULT]
debugPrint = False
epsilon = 0.001
maxIndividuals = -1
owlAnnotationLabel = fuzzyLabel
milpProvider = mip
```

| Configuration Variable | Description                       |
|----------------------|-----------------------------------|
| debugPrint        | Enable/disable debugging          |
| epsilon | Define the precision of the solution. For instance, epsilon = 0.001 means that the solution will be calculated with an accuracy to the third decimal place |
| maxIndividuals | Define the maximal number of individuals to handle. The value $-1$ indicates that there is no maximum |
| owlAnnotationLabel | Define the Annotation label used to build the Fuzzy OWL 2 RDF/XML ontology |
| milpProvider | Define the MILP provider used by the reasoner. The supported providers are listed below. |

Supported MILP Providers:
| Provider | milpProvider |
|--------------|----------------------|
| Gurobi | gurobi |
| CPLEX | pulp_cplex |
| CBC | pulp |
| GLPK | pulp_glpk |
| HiGHS | pulp_highs |
| MIP | mip |

## MILP Provider Usage and Configuration

### GUROBI

- Install [gurobipy](https://pypi.org/project/gurobipy/): `pip install gurobipy==12.0.0`
- Download the GUROBI license from their [website](https://www.gurobi.com/solutions/licensing/).
- Add Gurobi to the PATH

### MIP

- Install Python [MIP](https://www.python-mip.com/): `pip install mip==1.16rc0`

### GLPK

- Install [GLPK](https://www.gnu.org/software/glpk/) v5.0 and [GMP](https://gmplib.org/) v6.3.0
- Install Python [pulp](https://github.com/coin-or/PuLP?tab=readme-ov-file): `pip install pulp==3.2.1`
- Add GLPK to the PATH

### CBC

- Install [CBC](https://github.com/coin-or/Cbc)
- Install Python [pulp](https://github.com/coin-or/PuLP?tab=readme-ov-file): `pip install pulp==3.2.1`
- Add CBC to the PATH

### CPLEX

- Install [CPLEX](https://www.ibm.com/it-it/products/ilog-cplex-optimization-studio) v22.11
- Install Python [pulp](https://github.com/coin-or/PuLP?tab=readme-ov-file): `pip install pulp==3.2.1`
- Add CPLEX to the PATH

### HiGHS

- Install [HiGHS](https://ergo-code.github.io/HiGHS/dev/interfaces/cpp/) v1.10.0
- Install python [pulp](https://github.com/coin-or/PuLP?tab=readme-ov-file): `pip install pulp==3.2.1`
- Add HiGHS to the PATH