#!/usr/bin/env python3

"""
Safely get value
"""


from typing import Mapping, Any, Union, TypeVar


def safely_get_value(
    dct: Mapping, key: Any, default: Union[TypeVar("T"), None] = None
) -> Union[Any, TypeVar("T")]:
    """
    Safely get value
    """
    if key in dct:
        return dct[key]
    else:
        return default
