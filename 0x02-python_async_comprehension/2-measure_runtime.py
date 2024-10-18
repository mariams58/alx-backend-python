#!/usr/bin/env python3
"""An asyncio coroutine that measures runtime a coroutime runs concurrently"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure and returns total time it takes for a coroutine"""
    t: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end: float = time.perf_counter() - t
    return end
