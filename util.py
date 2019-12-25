#! /usr/bin/env python3

import collections

from typing import List, Dict

def count(data: List[int]) -> Dict[int, int]:
    ct = collections.defaultdict(int)
    for d in data:
        ct[d] += 1
    return ct
