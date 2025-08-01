from __future__ import annotations
import uuid
from abc import ABC, abstractmethod
from attrs import field, frozen

import pgsn.pgsn_term
from pgsn import helpers
from pgsn import pgsn_term
from pgsn import stdlib


@frozen
class GSN(ABC):
    description: str = field(validator=helpers.not_none)

    @abstractmethod
    def gsn_parts(self, parent_id: str, my_id: str) -> list[dict[str, str]]:
        pass


@frozen
class Assumption(GSN):

    def gsn_parts(self, parent_id, my_id):
        return [{
            "partsID": my_id,
            "parent": parent_id,
            "children": [],
            "kind": "Assumption",
            "detail": self.description,
        }]


@frozen
class Context(GSN):

    def gsn_parts(self, parent_id, my_id):
        return [{
            "partsID": my_id,
            "parent": parent_id,
            "children": [],
            "kind": "Context",
            "detail": self.description,
        }]


@frozen
class Support(GSN, ABC):
    pass


@frozen
class Undeveloped(Support):
    def gsn_parts(self, parent_id, my_id):
        raise NotImplemented


@frozen
class Evidence(Support):
    def gsn_parts(self, parent_id, my_id):
        return [{
                "partsID": my_id,
                "parent": parent_id,
                "children": [],
                "kind": "Evidence",
                "detail": self.description,
            }]


@frozen
class Strategy(Support):
    sub_goals: tuple[Goal,...] = field()

    @sub_goals.validator
    def _check_sub_goals(self, _, v):
        if len(v) == 0:
            raise ValueError('Strategy must have more than one sub-goals')

    def gsn_parts(self, parent_id, my_id):
        children_ids = [str(uuid.uuid4()) for _ in range(len(self.sub_goals))]
        parts = [{
            "partsID": my_id,
            "parent": parent_id,
            "children": children_ids,
            "kind": "Strategy",
            "detail": self.description,
        }]
        for i in range(len(self.sub_goals)):
            part = self.sub_goals[i].gsn_parts(my_id, children_ids[i])
            parts = parts + part
        return parts


@frozen
class Goal(GSN):
    support: Support = field(validator=helpers.not_none)
    assumptions: tuple[Assumption,...] = field(default=tuple())
    contexts: tuple[Context,...] = field(default=tuple())

    def gsn_parts(self, parent_id, my_id):
        support_id = str(uuid.uuid4())
        return [
            {'partsID': my_id,
             'parent': parent_id,
             'children': [support_id],
             'kind': 'Goal',
             'detail': self.description}
        ] + self.support.gsn_parts(parent_id=my_id, my_id=support_id)


undeveloped: Undeveloped = Undeveloped(description='Undeveloped')


def _dict_to_gsn(v: dict):
    if 'gsn_type' not in v:
        raise ValueError('PGSN term does not normalizes a GSN')
    match v['gsn_type']:
        case 'GSN_Node':
            raise ValueError('Node with unspecified kind')
        case 'Support':
            if v['description'] == 'Undeveloped':
                return undeveloped
            else:
                raise ValueError(f'Support {v} without specific type')
        case 'Evidence':
            return Evidence(description=v['description'])
        case 'Strategy':
            if len(v['sub_goals']) == 0:
                raise ValueError('Strategy must have more than one sub-goals')
            sub_goals = [_dict_to_gsn(g) for g in v['sub_goals']]
            if not all(isinstance(g, Goal) for g in sub_goals):
                raise ValueError(f'Sub-goals {sub_goals} must be goals')
            return Strategy(description=v['description'],
                            sub_goals=tuple(sub_goals))
        case 'Goal':
            assumptions = [_dict_to_gsn(a) for a in v['assumptions']]
            if not all(isinstance(a, Assumption) for a in assumptions):
                raise ValueError('Assumptions must be assumptions')
            contexts = [_dict_to_gsn(c) for c in v['contexts']]
            if not all(isinstance(c, Assumption) for c in contexts):
                raise ValueError('Contexts must be Contexts')
            support = _dict_to_gsn(v['support'])
            if not (isinstance(support, Strategy) or
                    isinstance(support, Evidence) or
                    support == undeveloped):
                raise ValueError(f'support {support} must be either a strategy, an evidence or undeveloped')
            return Goal(description=v['description'],
                        assumptions=assumptions,
                        contexts=contexts,
                        support=support)
        case 'Assumption':
            return Assumption(description=v['description'])
        case 'Context':
            return Context(description=v['description'])


def pgsn_to_gsn(t: pgsn_term.Term, steps=1000):
    v = pgsn.pgsn_term.value_of(t, steps=steps)
    if not isinstance(v, dict):
        raise ValueError('Term does not have a GSN')
    return _dict_to_gsn(v)


def python_val(gsn):
    return gsn.gsn_parts(str(uuid.uuid4()), str(uuid.uuid4()))

