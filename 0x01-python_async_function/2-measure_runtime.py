#!/usr/bin/env python3
"""Writing an asyncio coroutine that measures time a coroutime runs concurrently"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure and returns total time it takes for a coroutint tro run
    Args:
        n (int): spawning value
        max_delay (int): delay value
    Returns:
        float: total time
    """
    t: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = (time.perf_counter() - t) / n
    return end
