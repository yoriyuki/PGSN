from __future__ import annotations
from typing import TypeAlias, TypeVar, Generic
from abc import ABC, abstractmethod
import helpers
from attrs import field, frozen, evolve
from meta_info import MetaInfo
import meta_info as meta
from lambda_term import Term, Constant, Builtin

T = TypeVar('T')


@frozen
class Data(Builtin, Generic[T], ABC):
    value: T = field(validator=helpers.not_none)

    @classmethod
    def nameless_repr(cls, value):
        assert hasattr(value, '__repr__')
        return cls.nameless(value=repr(value))

    @classmethod
    def nameless_str(cls, value):
        assert hasattr(value, '__str__')
        return cls.nameless(value=str(value))

    @classmethod
    def named_repr(cls, value):
        assert hasattr(value, '__repr__')
        return cls.named(value=repr(value))

    @classmethod
    def named_str(cls, value):
        assert hasattr(value, '__str__')
        return cls.named(value=str(value))

    def _eval_or_none(self):
        return None

    def _shift(self, d, c):
        return self

    def _subst_or_none(self, var, term):
        return None

    def _free_variables(self):
        return set()

    def _remove_name_with_context(self, _):
        return type(self).nameless(value=self.value)

    def _applicable_args(self, _):
        return False

    def _apply_args(self, _):
        assert False


class String(Data[str]):
    pass


class Integer(Data[int]):

    @classmethod
    def nameless_from_str(cls, string):
        assert isinstance(string, str)
        assert string.isdigit()
        return cls.nameless(value=int(string))

    @classmethod
    def named_from_str(cls, string):
        assert isinstance(string, str)
        assert string.isdecimal()
        return cls.named(value=int(string))


class Boolean(Data[bool]):
    pass


def string(s: str) -> String:
    return String.named(value=s)


def integer(i: int) -> Integer:
    return Integer.named(value=i)


def boolean(b: bool) -> Boolean:
    return Boolean.named(value=b)





