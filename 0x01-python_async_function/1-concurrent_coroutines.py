#!/usr/bin/env python3

"""
Let's execute multiple coroutines at the same time with async
"""


from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay"""
    delays: List[float] = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
