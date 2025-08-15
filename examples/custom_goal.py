from pprint import pprint

from pgsn.pgsn_term import prettify
from pgsn.stdlib import *

# Define a custom subclass of Goal
CustomGoal = define_class(inherit=goal_class, name="GoalWithProject", attributes=["project"])

g = instantiate(CustomGoal, description="Secure connection established",
                project='Alpha',
                support=evidence(description="Verified by audit"))

pprint(prettify(g.fully_eval()))