#!/usr/bin/env python3
""" Duck writing zoom_array function"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ The zoomed array
    Args:
        lst (Tuple): lst
        factor (int, optional): _description_. Defaults to 2
    Returns:
        List: zoomed_in
    """
    zoomed_in: List = [
        item for item in list(lst)
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
