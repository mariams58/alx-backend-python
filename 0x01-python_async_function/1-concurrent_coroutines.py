#!/usr/bin/env python3
"""Wrinting an asyncio coroutine that runs concurrently"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Await for a random second and return its value
    Args:
        n (int): spawning value
        max_delay (int): delay value
    Returns:
        List[float]: list of all delays
    """
    runtime: List[float] = []
    for _ in range(n):
        runtime.append(await wait_random(max_delay))
    return sorted(runtime)
