#!/usr/bin/env python3
"""Writing the async_comprehension coroutine"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ An async coroutine that return a list  random number"""
    return [i async for i in async_generator()]
