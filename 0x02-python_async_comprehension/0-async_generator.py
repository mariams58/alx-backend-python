#!/usr/bin/env python3
"""Writing the async_generator coroutine"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ An async coroutine that loops 10 times and return random number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, i)
