import sys

sys.path.append("..")
import json
import pprint
from pgsn.gsn_term import *
from pgsn import gsn, object_term

robot = goal(description="There is no known vulnerability in the robot",
             support=strategy(description="Argument over each vulnerability",
                              sub_goals=[
                                  goal(description="Vulnerability A is not exploited",
                                       support=evidence(description="Test results")),
                                  goal(description="Vulnerability B is not exploited",
                                       support=evidence(description="Test results"))
                              ]
                              )
             )

web_server = goal(description="The server can deal with DoS attacks on the server",
                  support=evidence(description="Access restriction"))

system = goal(description="The robot does not make unintended movements",
              support=strategy(description="Argument over the robot and the server",
                               sub_goals=[
                                   goal(description="The robot behaves according to commands",
                                        support=strategy(description="Argument over each threat",
                                                         sub_goals=[robot]
                                                         )),
                                   goal(description="The server gives correct commands to the robot",
                                        support=strategy(description="Argument over each threat",
                                                         sub_goals=[web_server])
                                        )
                               ]
                               )
              )

s = strategy(description="Argument over each vulnerability",
                              sub_goals=[
                                  goal(description="Vulnerability A is not exploited",
                                       support=evidence(description="Test results")),
                                  goal(description="Vulnerability B is not exploited",
                                       support=evidence(description="Test results"))
                              ]
                              )

if __name__ == '__main__':
    # n = gsn.pgsn_to_gsn(evidence_class, steps=10000)
    # print(json.dumps(gsn.python_val(n), sort_keys=True, indent=4))
    #print(s('sub_goals').fully_eval())
    system_evaluated = system.fully_eval()
    pprint.pprint(object_term.prettify(system_evaluated))
    n = gsn.pgsn_to_gsn(system_evaluated, steps=10000)
    js = json.dumps(gsn.python_val(n), sort_keys=True, indent=4)
    print(js)
