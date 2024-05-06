#!/usr/bin/env python3
'''2 - Measure Runtime.
'''
from typing import Callable
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    '''Measures the total execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of coroutines to execute.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: Total execution time divided by n.
    '''
    # Record the start time
    start_time = time.time()

    # Run wait_n to measure execution time
    asyncio.run(wait_n(n, max_delay))

    # Calculate the total execution time
    total_time = time.time() - start_time

    # Return the average time per coroutine
    return total_time / n

# Test the function
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
