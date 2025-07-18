from attr import attributes

import pgsn.stdlib

gsn_class = pgsn.stdlib.define_class(inherit=pgsn.stdlib.base_class,
                                     name='GSN_Node',
                                     attributes=["description"])

support_class = pgsn.stdlib.define_class(inherit=gsn_class, name='Support')
undeveloped = support_class(description='Undeveloped', name='Undeveloped')
evidence_class = pgsn.stdlib.define_class(inherit=support_class, name='Evidence')
strategy_class = pgsn.stdlib.define_class(inherit=support_class, name='Strategy',
                                          attributes=["sub_goals"])

goal_class = pgsn.stdlib.define_class(inherit=gsn_class,
                                      name='Goal',
                                      attributes=["assumptions", "contexts", "support"],
                                      defaults={"assumptions":[], "contexts": [], "support": undeveloped}
                                      )
assumption_class = pgsn.stdlib.define_class(inherit=gsn_class, name='Assumption')
context_class = pgsn.stdlib.define_class(inherit=gsn_class, name='Context')

_d = pgsn.stdlib.variable('x')
_support = pgsn.stdlib.variable('support')
_assumptions = pgsn.stdlib.variable('assumptions')
_contexts = pgsn.stdlib.variable('contexts')
_sub_goals = pgsn.stdlib.variable('sub_goals')

evidence = pgsn.stdlib.lambda_abs_keywords(arguments={'description': _d},
                                           body=evidence_class(description=_d))
strategy = pgsn.stdlib.lambda_abs_keywords(arguments={'description': _d, 'sub_goals': _sub_goals},
                                           body=strategy_class
                               (description=_d, sub_goals=_sub_goals))
goal = pgsn.stdlib.lambda_abs_keywords(arguments={'description': _d,
                                      'assumptions': _assumptions,
                                      'contexts': _contexts,
                                      'support': _support},
                                       defaults=pgsn.stdlib.record({
                               'assumptions': pgsn.stdlib.empty,
                               'contexts': pgsn.stdlib.empty}),
                                       body=goal_class(description=_d, support=_support))
assumption = pgsn.stdlib.lambda_abs_keywords(arguments={'description': _d},
                                             body=assumption_class(description=_d))
context = pgsn.stdlib.lambda_abs_keywords(arguments={'description': _d},
                                          body=context_class(description=_d))

_goals = pgsn.stdlib.variable('goals')
immediate = pgsn.stdlib.lambda_abs(_goals, strategy(description="immediate", sub_goals=_goals))

_evd = pgsn.stdlib.variable('evidence')
evidence_as_goal = pgsn.stdlib.lambda_abs(_evd, goal(description=_evd('description'), support=_evd))


