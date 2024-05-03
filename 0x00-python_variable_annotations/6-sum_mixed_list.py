#!/usr/bin/env python3
''' 6-sum_mixed_list module'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Returns the sum of a list of mixed integers and floats.'''
    return float(sum(mxd_lst))
