#!/usr/bin/env python3

"""
Safe first element
"""


from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safe first element
    """
    if lst:
        return lst[0]
    else:
        return None
