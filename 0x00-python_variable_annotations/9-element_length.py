#!/usr/bin/env python3
''' 9-element_length module'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Returns a list of tuples containing the element and its length.'''
    return [(i, len(i)) for i in lst]
