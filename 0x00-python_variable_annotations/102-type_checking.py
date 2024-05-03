#!/usr/bin/env python3
''' 12-type_checking module'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    ''' Returns a list of tuples containing the element and its length.'''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
