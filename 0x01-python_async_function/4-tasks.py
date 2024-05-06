#!/usr/bin/env python3
'''4 - Tasks.
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes multiple tasks concurrently.

    Args:
        n (int): Number of tasks to execute.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: List of delays in ascending order.
    '''
    # List to store the results
    delays = []

    # Run task_wait_random n times concurrently
    # and store the results in delays
    for _ in range(n):
        delay_task = task_wait_random(max_delay)
        await delay_task
        delays.append(delay_task.result())

    # Sort the delays in ascending order
    delays.sort()

    return delays

# Test the function
if __name__ == "__main__":
    import asyncio

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
