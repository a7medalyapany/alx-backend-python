#!/usr/bin/env python3
'''Module for Task 0 - Async Basics.'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random duration.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The randomly generated delay.
    '''
    # Generate a random delay
    wait_time = random.random() * max_delay
    # Wait for the random delay
    await asyncio.sleep(wait_time)
    # Return the delay
    return wait_time
