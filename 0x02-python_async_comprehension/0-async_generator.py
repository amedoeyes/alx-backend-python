#!/usr/bin/env python3

"""
Async Generator
"""


import asyncio
import random

from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async_generator: coroutine that loops 10 times, each time asynchronously
    waits 1 second, then yields a random number between 0 and 10. Use the
    random module.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
