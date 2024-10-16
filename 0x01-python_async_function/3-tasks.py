#!/usr/bin/env python3
"""Wrinting an asyncio coroutine"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Return an asynci.Task
    Args:
        max_delay (int): delay value
    Returns:
        asyncio.Task: task
    """
    return asyncio.create_task(wait_random(max_delay))
