import json
from xml.etree.ElementTree import indent

from pgsn import pgsn_term, stdlib, gsn_term
from pgsn.gsn_term import goal, evidence, immediate
from pgsn.stdlib import let, lambda_abs, lambda_abs_vars, variable, define_class, base_class, list_term, record
import pprint

requirements = ["Firewall enabled", "Encrypted communication", "Access control active"]


goal_template = lambda_abs(variable("desc"),
    goal(description=variable("desc"),
         support=evidence(description=variable("desc")))
)

goals = stdlib.map_term(goal_template, requirements)

secure_goal = gsn_term.goal(
    description="Security requirements fulfilled",
    support=immediate(goals)
)

def test_var():
    var_x = variable("x")
    s = pgsn_term.json_dumps(var_x, indent=2)
    t = pgsn_term.json_loads(s)
    s1 = pgsn_term.json_dumps(t, indent=2)
    assert var_x == t
    assert s == s1


def test_term_id():
    x = variable('x')
    id_f = lambda_abs(x, x)
    s = pgsn_term.json_dumps(id_f, indent=2)
    t = pgsn_term.json_loads(s)
    s1 = pgsn_term.json_dumps(t, indent=2)
    assert id_f == t
    assert s == s1


def test_term_id_id():
    x = variable('x')
    id_f = lambda_abs(x, x)
    t = id_f(id_f)
    s = pgsn_term.json_dumps(id_f(id_f), indent=2)
    t1 = pgsn_term.json_loads(s)
    s1 = pgsn_term.json_dumps(t, indent=2)
    assert t == t1
    assert s == s1


def test_list():
    x = variable("x")
    y = variable("y")
    z = list_term((x, y))
    s = pgsn_term.json_dumps(z, indent=2)
    t1 = pgsn_term.json_loads(s)
    s1 = pgsn_term.json_dumps(z, indent=2)
    assert z == t1
    assert s == s1


def test_record():
    x = variable("x")
    y = variable("y")
    z = record({"x": x, "y": y})
    s = pgsn_term.json_dumps(z, indent=2)
    t1 = pgsn_term.json_loads(s)
    s1 = pgsn_term.json_dumps(z, indent=2)
    assert z == t1
    assert s == s1


def test_class():
    cls = define_class(name="test", inherit=base_class)
    s = pgsn_term.json_dumps(cls, indent=2)
    t1 = pgsn_term.json_loads(s)
    s1 = pgsn_term.json_dumps(cls, indent=2)
    assert cls == t1
    assert s == s1



def test_json_1():
    s = pgsn_term.json_dumps(goal_template, indent=2)
    t = pgsn_term.json_loads(s)
    s1 = pgsn_term.json_dumps(t, indent=2)
    #assert goal_template == t # structural (==) is very slow
    assert s == s1


def test_json_2():
    s = pgsn_term.json_dumps(goals, indent=2)
    t = pgsn_term.json_loads(s)
    s1 = pgsn_term.json_dumps(t, indent=2)
    #assert goals == t # structural (==) is very slow
    assert s == s1


def test_json_3():
    s = pgsn_term.json_dumps(secure_goal, indent=2)
    t = pgsn_term.json_loads(s)
    s1 = pgsn_term.json_dumps(t, indent=2)
    #assert secure_goal == t # structural (==) is very slow
    assert s == s1
    v = t.fully_eval()
    assert v

