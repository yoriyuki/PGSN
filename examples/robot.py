import sys

import pgsn.pgsn_term

sys.path.append("..")
import pprint
import pgsn.gsn_term

from typeguard import install_import_hook

install_import_hook('robot')

install_import_hook('gsn')
install_import_hook('gsn_term')
install_import_hook('helpers')
install_import_hook('pgsn_term')
install_import_hook('stdlib')

robot = pgsn.gsn_term.goal(description="There is no known vulnerability in the robot",
                           support=pgsn.gsn_term.strategy(description="Argument over each vulnerability",
                                                          sub_goals=[
                                  pgsn.gsn_term.goal(description="Vulnerability A is not exploited",
                                                     support=pgsn.gsn_term.evidence(description="Test results")),
                                  pgsn.gsn_term.goal(description="Vulnerability B is not exploited",
                                                     support=pgsn.gsn_term.evidence(description="Test results"))
                              ]
                                                          )
                           )


s = pgsn.gsn_term.strategy(description="Argument over each vulnerability",
                                                          sub_goals=[
                                  pgsn.gsn_term.goal(description="Vulnerability A is not exploited",
                                                     support=pgsn.gsn_term.evidence(description="Test results")),
                                  pgsn.gsn_term.goal(description="Vulnerability B is not exploited",
                                                     support=pgsn.gsn_term.evidence(description="Test results"))
                              ]
                                                          )

pprint.pprint(pgsn.pgsn_term.to_python(pgsn.gsn_term.evidence(description="Test results").fully_eval()), indent=2)

e1 = pgsn.gsn_term.evidence(description="Test results")
pprint.pprint(pgsn.pgsn_term.to_python(e1.fully_eval()), indent=2)

g1 = pgsn.gsn_term.goal(description="Vulnerability A is not exploited",
                                                     support=pgsn.gsn_term.evidence(description="Test results"))
pprint.pprint(pgsn.pgsn_term.to_python(g1.fully_eval()), indent=2)

pprint.pprint(pgsn.pgsn_term.to_python(s.fully_eval()), indent=2)
pprint.pprint(pgsn.pgsn_term.to_python(robot.fully_eval()), indent=2)


pprint.pprint(pgsn.pgsn_term.to_python(robot.fully_eval()), indent=2)

web_server = pgsn.gsn_term.goal(description="The server can deal with DoS attacks on the server",
                                support=pgsn.gsn_term.evidence(description="Access restriction"))

system = pgsn.gsn_term.goal(description="The robot does not make unintended movements",
                            support=pgsn.gsn_term.strategy(description="Argument over the robot and the server",
                                                           sub_goals=[
                                   pgsn.gsn_term.goal(description="The robot behaves according to commands",
                                                      support=pgsn.gsn_term.strategy(description="Argument over each threat",
                                                                                     sub_goals=[robot]
                                                                                     )),
                                   pgsn.gsn_term.goal(description="The server gives correct commands to the robot",
                                                      support=pgsn.gsn_term.strategy(description="Argument over each threat",
                                                                                     sub_goals=[web_server])
                                                      )
                               ]
                                                           )
                            )

if __name__ == '__main__':
    system_evaluated = system.fully_eval()
    pprint.pprint(pgsn.pgsn_term.to_python(system_evaluated), indent=2)
    # n = gsn.pgsn_to_gsn(system_evaluated, steps=1)
    # js = json.dumps(gsn.python_val(n), sort_keys=True, indent=4)
    # print(js)
