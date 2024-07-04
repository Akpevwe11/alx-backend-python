#!/usr/bin/env python3
'''Task 10's module.
'''
from typing import Any, List, Optional


def safe_first_element(lst: List[Any]) -> Optional[Any]:
    '''Retrieves the first element of a list if it exists.
    '''
    if lst:
        return lst[0]
    else:
        return None
