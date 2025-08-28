from attr import attributes

import pgsn.dsl

gsn_class = pgsn.dsl.define_class(inherit=pgsn.dsl.base_class,
                                     name='GSN_Node',
                                     attributes=["description"])

support_class = pgsn.dsl.define_class(inherit=gsn_class, name='Support')
undeveloped = support_class(description='Undeveloped')
evidence_class = pgsn.dsl.define_class(inherit=support_class, name='Evidence')
strategy_class = pgsn.dsl.define_class(inherit=support_class, name='Strategy',
                                          attributes=["sub_goals"])

goal_class = pgsn.dsl.define_class(inherit=gsn_class,
                                      name='Goal',
                                      attributes=["assumptions", "contexts", "support"],
                                      defaults={"assumptions":[], "contexts": [], "support": undeveloped}
                                      )
assumption_class = pgsn.dsl.define_class(inherit=gsn_class, name='Assumption')
context_class = pgsn.dsl.define_class(inherit=gsn_class, name='Context')

_d = pgsn.dsl.variable('x')
_support = pgsn.dsl.variable('support')
_assumptions = pgsn.dsl.variable('assumptions')
_contexts = pgsn.dsl.variable('contexts')
_sub_goals = pgsn.dsl.variable('sub_goals')

evidence = pgsn.dsl.lambda_abs_keywords(arguments={'description': _d},
                                           body=evidence_class(description=_d))
strategy = pgsn.dsl.lambda_abs_keywords(arguments={'description': _d, 'sub_goals': _sub_goals},
                                           body=strategy_class
                               (description=_d, sub_goals=_sub_goals))
goal = pgsn.dsl.lambda_abs_keywords(arguments={'description': _d,
                                      'assumptions': _assumptions,
                                      'contexts': _contexts,
                                      'support': _support},
                                       defaults=pgsn.dsl.record({
                               'assumptions': pgsn.dsl.empty,
                               'contexts': pgsn.dsl.empty}),
                                       body=goal_class(description=_d, contexts=_contexts, support=_support))
assumption = pgsn.dsl.lambda_abs_keywords(arguments={'description': _d},
                                             body=assumption_class(description=_d))
context = pgsn.dsl.lambda_abs_keywords(arguments={'description': _d},
                                          body=context_class(description=_d))

_goals = pgsn.dsl.variable('goals')
immediate = pgsn.dsl.lambda_abs(_goals, strategy(description="immediate", sub_goals=_goals))

_evd = pgsn.dsl.variable('evidence')
evidence_as_goal = pgsn.dsl.lambda_abs(_evd, goal(description=_evd('description'), support=_evd))


