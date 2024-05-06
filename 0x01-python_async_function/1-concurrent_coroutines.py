#!/usr/bin/env python3
'''1 - Concurrent Coroutines.'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes multiple coroutines concurrently.

    Args:
        n (int): Number of coroutines to execute.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        List[float]: List of delays in ascending order.
    '''
    # List to store the results
    delays = []

    # Run wait_random n times concurrently
    # and store the results in delays
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    # Sort the delays in ascending order
    delays.sort()

    return delays

# Test the coroutine
if __name__ == "__main__":
    import asyncio

    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
  
