import uuid
from treelib import Tree

import pgsn.dsl
import pgsn.pgsn_term

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
                                       body=goal_class(description=_d,
                                                       contexts=_contexts,
                                                       assumptions=_assumptions,
                                                       support=_support))
assumption = pgsn.dsl.lambda_abs_keywords(arguments={'description': _d},
                                             body=assumption_class(description=_d))
context = pgsn.dsl.lambda_abs_keywords(arguments={'description': _d},
                                          body=context_class(description=_d))

_goals = pgsn.dsl.variable('goals')
immediate = pgsn.dsl.lambda_abs(_goals, strategy(description="immediate", sub_goals=_goals))

_evd = pgsn.dsl.variable('evidence')
evidence_as_goal = pgsn.dsl.lambda_abs(_evd, goal(description=_evd('description'), support=_evd))

# Keys for lists that should be hidden if empty
GSN_KEYS_TO_HIDE_IF_EMPTY = {"contexts", "assumptions"}

# Keys for lists whose children should be attached directly to the parent
GSN_KEYS_TO_FLATTEN = {"support", "sub_goals", "contexts", "assumptions"}
GSN_TYPES = {"Goal", "Strategy", "Evidence", "Context", "Assumption"}


# Term and to_python are assumed to be in your module
# from your_module import Term, to_python

def gsn_tree(root_term: pgsn.pgsn_term.Term) -> Tree:
    tree = Tree()
    py_data = pgsn.dsl.python_value(root_term)

    def _add_nodes(data, parent_id=None, key_name="root"):

        # Hide specific GSN keys if their list is empty
        if key_name in GSN_KEYS_TO_HIDE_IF_EMPTY and isinstance(data, list) and not data:
            return

        node_id = str(uuid.uuid4())

        if isinstance(data, dict):
            # (Dictionary processing logic remains the same)
            has_meaningful_keys = any(not (k.startswith('__') and k.endswith('__')) for k in data)
            class_name_key = next((k for k in data if k.startswith('__') and k.endswith('__')), None)
            class_name = class_name_key.strip('_') if class_name_key is not None else None

            if not has_meaningful_keys:
                node_tag = f"{key_name}: {{}}"
            elif class_name_key:
                # special handling for GSN node
                if class_name in GSN_TYPES:
                    description = data["description"] if "description" in data else ""
                    node_tag = f"{class_name}: {description}"
                else:
                    node_tag = f"{key_name}: <{class_name}>"
            else:
                node_tag = f"{key_name}: <Record>"

            tree.create_node(tag=node_tag, identifier=node_id, parent=parent_id)

            for key, value in data.items():
                if class_name in GSN_TYPES and key=="description":
                    continue
                if not (key.startswith('__') and key.endswith('__')):
                    # Special handling to flatten key
                    if key in GSN_KEYS_TO_FLATTEN and isinstance(value, list):
                        for item in value:
                            # Attach each item directly to the parent (node_id)
                            _add_nodes(item, parent_id=node_id, key_name=key)
                    else:
                        _add_nodes(value, parent_id=node_id, key_name=key)

        elif isinstance(data, list):
            # (List handling logic remains the same)
            if not data:
                node_tag = f"{key_name}: [List] = []"
            else:
                node_tag = f"{key_name}: [List]"

            tree.create_node(tag=node_tag, identifier=node_id, parent=parent_id)

            for i, item in enumerate(data):
                _add_nodes(item, parent_id=node_id, key_name=f"[{i}]")

        else:
            node_tag = f"{key_name}: {data}"
            tree.create_node(tag=node_tag, identifier=node_id, parent=parent_id)

    _add_nodes(py_data)
    return tree


