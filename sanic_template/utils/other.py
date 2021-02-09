from types import FunctionType
from typing import List, Tuple, Union


def count(items: list, clause: FunctionType) -> int:
    """
    Returns number of matching items.
    :param items:
    :param clause:
    :return:
    """
    k = 0
    if not items:
        return k
    for item in items:
        if clause(item):
            k += 1
    return k


def flat(data: List[Tuple]):
    """
    Removes unnecessary nesting from list.
    Ex: [(1,), {2,}, {3,}] return [1, 2, 3]
    """
    if not data:
        return data
    return [d for d, in data]


def first(data: Union[List, Tuple]):
    """
    Returns first element from list or tuple.
    """
    if isinstance(data, (list, tuple)) and data:
        return data[0]
    return None
