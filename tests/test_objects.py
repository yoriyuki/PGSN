from attr import attributes

from pgsn import pgsn_term, stdlib
from pgsn.stdlib import define_class, is_subclass, is_instance
from pgsn.pgsn_term import cast

a = stdlib.string('a')
b = stdlib.string('b')
c = stdlib.string('c')
defaults = stdlib.record({'a': stdlib.boolean(True)})
self = stdlib.variable('self')
v = stdlib.lambda_abs(self, stdlib.if_then_else(self(a))(self(b))(self(c)))
# attrs1 = inherit(defaults)(record_term.record({'value': get_value_term}))
attrs1 = stdlib.record({'a': stdlib.true})
cls = define_class(inherit=stdlib.base_class, defaults=defaults, attributes=["a"], methods={})
test = stdlib.string('test')


cls1 = define_class(inherit=cls, attributes=[])
cls2 = define_class(inherit=cls, attributes=['b'])
cls3 = define_class(inherit=cls2, attributes=['c'], methods={'v': v})


def test_class():
    assert isinstance(cls.fully_eval(), pgsn_term.PGSNClass)
    assert isinstance(cls1.fully_eval(), pgsn_term.PGSNClass)
    assert isinstance(cls2.fully_eval(), pgsn_term.PGSNClass)
    assert isinstance(cls3.fully_eval(), pgsn_term.PGSNClass)
    assert cls.fully_eval().attributes() == {'a'}
    assert set(cls3.fully_eval().methods().keys()) == {'v'}


def test_subclass():
    assert isinstance(cls1.fully_eval(), pgsn_term.PGSNClass)
    assert is_subclass(cls)(cls).fully_eval().value
    assert is_subclass(cls1)(cls).fully_eval().value
    assert not is_subclass(stdlib.base_class)(cls).fully_eval().value


obj1 = cls()
obj2 = cls({'a': False})
obj3 = cls({'b': 1})
obj4 = cls2({'b': 1})
obj5 = cls3({'b': 1, 'c':2})
obj6 = cls3({'a':False, 'b': 1, 'c':2})



def test_obj_instance():
    assert isinstance(obj1.fully_eval(), pgsn_term.PGSNObject)
    assert isinstance(obj2.fully_eval(), pgsn_term.PGSNObject)
    assert not isinstance(obj3.fully_eval(), pgsn_term.PGSNObject)
    assert isinstance(obj4.fully_eval(), pgsn_term.PGSNObject)
    assert isinstance(obj5.fully_eval(), pgsn_term.PGSNObject)
    assert isinstance(obj6.fully_eval(), pgsn_term.PGSNObject)
    assert is_instance(obj1)(cls).fully_eval().value
    assert not is_instance(obj1)(cls1).fully_eval().value


def test_obj_values():
    assert obj1(a).fully_eval().value
    assert not obj2(a).fully_eval().value
    assert obj4(a).fully_eval().value
    assert obj4(b).fully_eval().value == 1
    assert obj5(a).fully_eval().value
    assert obj5(b).fully_eval().value == 1
    assert obj5(c).fully_eval().value == 2
    assert obj5(a).fully_eval().value
    assert obj5(b).fully_eval().value == 1
    assert obj5(c).fully_eval().value == 2
    assert not obj6(a).fully_eval().value
    assert obj6(b).fully_eval().value == 1
    assert obj6(c).fully_eval().value == 2
    assert obj1.a.fully_eval().value


def test_obj_methods():
    assert obj5('v').fully_eval().value == 1
    assert obj6('v').fully_eval().value == 2
    assert obj5.v.fully_eval().value == 1
    assert obj6.v.fully_eval().value == 2
