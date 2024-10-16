#!/usr/bin/env python3
""" Duck writing - element_length function"""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return the floor of the type float argument
    Args:
        lst (Iterable[Sequence]): lst
    Returns:
        List[Tuple[Sequence, int]]: num
    """
    return [(i, len(i)) for i in lst]
