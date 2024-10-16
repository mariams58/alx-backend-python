#!/usr/bin/env python3
""" Duck writing - make_multiplier function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies the multiplier
    Args:
        multiplier (float): multiplier
    Returns:
        Callable[[float], float]: function that multiplies a float
    """
    def multiply(n: float) -> float:
        """ Return the product of a muliplier and float
        Args:
            n (float): n
        Returns:
            float: num
        """
        num = n * multiplier
        return num
    return multiply
