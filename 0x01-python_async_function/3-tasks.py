#!/usr/bin/env python3
'''Module for Task 3 - Tasks.
'''
import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates an asyncio.Task for wait_random.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: The task for wait_random.
    '''
    # Create and return an asyncio.Task for wait_random
    return asyncio.create_task(wait_random(max_delay))

# Test the function
if __name__ == "__main__":
    import asyncio

    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
