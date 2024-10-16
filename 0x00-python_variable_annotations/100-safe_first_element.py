#!/usr/bin/env python3
"""Augument safe_first_element function"""

from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augument sfe_first_element function
    Args:
        lst (Sequence[Any]): Any type of list
    Return:
        Union[Any, None]: the first element or None
    """
    if lst:
        return lst[0]
    else:
        return None
