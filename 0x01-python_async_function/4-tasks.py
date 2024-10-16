#!/usr/bin/env python3
"""Wrinting an asyncio coroutine that runs concurrently"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Await for a random second and return its value
    Args:
        n (int): spawning value
        max_delay (int): delay value
    Returns:
        List[float]: list of all delays
    """
    runtimes: List[float] = []
    for _ in range(n):
        runtimes.append(task_wait_random(max_delay))
    return [await runtime for runtime in asyncio.as_completed(runtimes)]
