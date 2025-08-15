
# PGSN: Programmable Goal Structuring Notation

Functional Programming for Assurance Case Generation

[![Python](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## What is PGSN?

**PGSN** is a functional programming language and platform for constructing and transforming structured assurance cases based on the **Goal Structuring Notation (GSN)**.
Unlike standard GSN, which primarily consists of static diagrams, PGSN allows dynamic and structured generation of argument elements using a functional and object-oriented programming language.

**PGSN** is currently implemented as an **embedded language in Python**, but other implementations are planned.

## Key Features

-  **GSN Modeling Using Functional Programming**: Write assurance cases as functional programs
-  **Reusable**: Build assurance structures compositionally
-  **Object-Oriented**: Class/inheritance for reusable node types
-  **Security Aware**: PGSN terms are executed in a resource-limited interpreter, ensuring safe evaluation of third-party code.

## Installation

Use conda
```bash
git clone https://github.com/yoriyuki/PGSN.git
cd PGSN
conda env create -f environment.yml -n PGSN
```
or pip
```bash
git clone https://github.com/yoriyuki/PGSN.git
cd PGSN
pip install -r requirements.txt
```

## Example

```python
from pprint import pprint

from pgsn import *

g = goal(
    description=string("System is secure"),
    support=strategy(
        description=string("Break into sub-goals"),
        sub_goals=[
            goal(description="Input validated",
                 support=evidence(description="Static analysis passed")),
            goal(description="Output sanitized",
                 support=evidence(description="Fuzzing test succeeded"))
        ]
    )
)

pprint(prettify(g.fully_eval()))
```

```shell
% python -m examples.gsn
{'assumptions': [],
 'contexts': [],
 'description': 'System is secure',
 'gsn_type': 'Goal',
 'support': {'description': 'Break into sub-goals',
             'gsn_type': 'Strategy',
             'sub_goals': [{'assumptions': [],
                            'contexts': [],
                            'description': 'Input validated',
                            'gsn_type': 'Goal',
                            'support': {'description': 'Static analysis passed',
                                        'gsn_type': 'Evidence'}},
                           {'assumptions': [],
                            'contexts': [],
                            'description': 'Output sanitized',
                            'gsn_type': 'Goal',
                            'support': {'description': 'Fuzzing test succeeded',
                                        'gsn_type': 'Evidence'}}]}}
```

## Advanced Examples

### Example 1: Reusable Goal Template with Evidence

Define a reusable function that generates a goal node supported by an evidence node with the same description.

```python
from pprint import pprint

from pgsn import prettify
from pgsn.dsl import *
from pgsn.gsn import goal, evidence, strategy

# Define a reusable goal+evidence template
mk_goal_with_evidence = lambda_abs_keywords(
    {"desc": variable("desc")},
    goal(
        description=variable("desc"),
        support=evidence(description=variable("desc"))
    )
)

# Apply the template to multiple goals
g1 = mk_goal_with_evidence(desc="No hardcoded passwords")
g2 = mk_goal_with_evidence(desc="Input sanitized")
g3 = mk_goal_with_evidence(desc="Logging enabled")

# Compose a top-level goal with a strategy
top = goal(
    description="System is secure",
    support=strategy(
        description="Apply security principles",
        sub_goals=[g1, g2, g3]
    )
)

pprint(python_value(top.fully_eval()))
```

### Example 2: Auto-expanding Multiple Goals with `map_term`

Use `map_term` to generate multiple sub-goals from a list of requirements dynamically.

```python
from pprint import pprint

from pgsn.gsn import *

requirements = ["Firewall enabled", "Encrypted communication", "Access control active"]

goal_template = lambda_abs(variable("desc"),
                           goal(description=variable("desc"),
                                support=evidence(description=variable("desc")))
                           )

goals = map_term(goal_template, requirements)

secure_goal = goal(
    description="Security requirements fulfilled",
    support=immediate(goals)
)

pprint(prettify(secure_goal.fully_eval()))
```

### Example 3: Class-based Node Composition Using Object System

Use `object_term.py` to define a custom goal class and instantiate it with additional metadata.

```python
from pprint import pprint

from pgsn import *

# Define a custom subclass of Goal
CustomGoal = define_class("CustomGoal", goal_class, project="Alpha")

g = instantiate(CustomGoal, description="Secure connection established",
    support=evidence(description="Verified by audit"))

pprint(prettify(g.fully_eval()))
```

These advanced examples demonstrate how to:

| Purpose | Technique |
|---------|-----------|
| Template reuse | Define lambda abstractions and keyword arguments |
| Bulk generation | Use `map_term` over lists |
| Metadata handling | Extend GSN nodes via custom classes |

You can adapt these techniques to build domain-specific GSN templates, automate assurance case generation, or validate structural constraints programmatically.

## Summary of Common Constructs

| Construct                    | Description                             |
|-----------------------------|-----------------------------------------|
| `goal(...)`                 | Defines a GSN Goal                      |
| `strategy(...)`             | Logical inference for a Goal            |
| `evidence(...)`             | Data supporting a Goal                  |
| `context(...)`              | Context for a Goal or Strategy          |
| `assumption(...)`           | Declares an assumption                  |
| `immediate(...)`            | Binds sub-goals directly                |
| `map_term(...)`             | Functional mapping over list_term       |
| `lambda_abs(...)`           | Lambda abstraction (positional)         |
| `lambda_abs_keywords(...)`  | Lambda abstraction (keyword args)       |
| `define_class(...)`         | Defines a new object-based Goal class   |
| `instantiate(...)`          | Instantiates an object-based Goal       |

## Architecture

| Layer    | Component                  | Purpose                          |
|----------|----------------------------|----------------------------------|
| Core     | `pgsn_term.py`             | Lambda calculus interpreter      |
| DSL      | `stdlib.py`, `gsn_term.py` | Human-friendly API to define GSN |
| OO Layer | `object_term.py`           | Reusable GSN node types          |

##  License

MIT License – see [LICENSE](LICENSE).

Copyright: National Institute of Advanced Industrial Science and Technology (AIST) 2023-2024,
Yoriyuki Yamagata 2025