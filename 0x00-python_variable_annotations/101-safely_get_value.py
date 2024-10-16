#!/usr/bin/env python3
"""Augumented Annotated safely_get_value function"""

from typing import Any, Union, Mapping, TypeVar

T = TypeVar('T')
NoneType = TypeVar('NoneType', None, None)
U = Union[Any, T]
V = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: V) -> U:
    """Safely returns a value
    Args:
        dct (Mapping): dct
        key (Any): key
        defaults (Defaults, optional): defaults to None
    Returns:
        Return: value
    """
    if key in dct:
        return dct[key]
    else:
        return default
