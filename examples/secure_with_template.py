from pprint import pprint

from pgsn import prettify
from pgsn.stdlib import *
from pgsn.gsn_term import goal, evidence, strategy

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

pprint(prettify(top.fully_eval()))
