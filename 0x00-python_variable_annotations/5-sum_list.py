#!/usr/bin/env python3
"""Duck writing sum_list function"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Adds all numbers argumts of type float in a list
    Args:
        input_list (List[float]): list of floats
    Returns:
        float: sum
    """
    sum = 0
    for val in input_list:
        sum += val
    return sum
