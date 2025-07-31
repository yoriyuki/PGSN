from pprint import pprint

from pgsn import *
from pgsn import prettify

g = goal(
    description="System is secure",
    support=strategy(
        description="Break into sub-goals",
        sub_goals=[
            goal(description="Input validated",
                 support=evidence(description="Static analysis passed")),
            goal(description="Output sanitized",
                 support=evidence(description="Fuzzing test succeeded"))
        ]
    )
)

pprint(prettify(g.fully_eval()))