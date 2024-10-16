#!/usr/bin/env python3
"""Duck writing sum_mixed_list function"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Adds all numbers argumts of type float in a list
    Args:
        mxd_list (List[Union[float]]): list of floats
    Returns:
        float: sum
    """
    sum = 0.0
    for val in mxd_list:
        sum += val
    return sum
