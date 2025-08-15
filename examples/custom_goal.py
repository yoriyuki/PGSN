from pprint import pprint

from pgsn.dsl import *
from pgsn.gsn import *

# Define a custom subclass of Goal
CustomGoal = define_class(inherit=goal_class, name="GoalWithProject", attributes=["project"])

g = instantiate(CustomGoal, description="Secure connection established",
                project='Alpha',
                support=evidence(description="Verified by audit"))

pprint(python_value(g.fully_eval()))