from pgsn import dsl
from pgsn.pgsn_term import List


def test_list():
    x = stdlib.constant('x')
    y = stdlib.constant('y')
    z = stdlib.constant('z')
    ll = List.named(terms=(x, y, z))
    assert ll.terms == (x, y, z)
    i = stdlib.integer(1)
    assert ll(i).eval().name == 'y'