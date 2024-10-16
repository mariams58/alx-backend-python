#!/usr/bin/env python3
"""Duck writing to_kv function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple
    Args:
        k (str): string
        v (Union[int, float]): int or float
    Returns:
        Tuple[str, float]: tuple
    """
    return (k, v ** 2)
