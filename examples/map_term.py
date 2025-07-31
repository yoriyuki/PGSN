from pprint import pprint

from pgsn import prettify
from pgsn.stdlib import *
from pgsn.gsn_term import *

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
