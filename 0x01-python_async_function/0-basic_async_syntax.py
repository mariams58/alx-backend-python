#!/usr/bin/env python3
"""Wrinting an asyncio coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Await for a random second and return its value
    Args:
        max_delay (int): delay value
    Returns:
        float: n
    """
    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n
