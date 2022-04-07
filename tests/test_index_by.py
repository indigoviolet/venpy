from venpy import index_by
from typing import Callable
import pytest


def test_index_by_func():

    items = [1, 2, 3, 4]
    by_func: Callable[[int], int] = lambda i: i % 2

    idx = index_by(items, by=by_func, collection="list")
    assert idx[1] == [1, 3]
    assert idx[0] == [2, 4]


def test_index_by_collection():

    items = [1, 2, 2, 4, 3, 3, 5]
    by_func: Callable[[int], int] = lambda i: i % 2

    uniq_idx = index_by(items, by=by_func)
    set_idx = index_by(items, by=by_func, collection="set")
    list_idx = index_by(items, by=by_func, collection="list")

    assert uniq_idx == {1: 5, 0: 4}
    assert set_idx == {1: set([1, 3, 5]), 0: set([2, 4])}
    assert list_idx == {1: [1, 3, 3, 5], 0: [2, 2, 4]}
