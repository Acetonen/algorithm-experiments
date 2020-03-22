from collections import namedtuple

import pytest

from project.heaps.heap import Heap

TestFixture = namedtuple('TestFixture', 'array result')

TREE_KEYS = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]


@pytest.mark.parametrize('fixture', [
    TestFixture([1], [1, None, None, None, None, None, None]),
    TestFixture([1, 2], [2, 1, None, None, None, None, None]),
    TestFixture([6, 5, 4], [6, 5, 4, None, None, None, None]),
    TestFixture([6, 5, 4, 7], [7, 6, 4, 5, None, None, None]),
    TestFixture([7, 6, 4, 5, 4, 3, 2], [7, 6, 4, 5, 4, 3, 2]),
])
def test_add(fixture):
    heap = Heap()
    heap._make_heap(2)

    for key in fixture.array:
        heap.Add(key)

    assert heap.HeapArray == fixture.result


@pytest.mark.parametrize('fixture', [
    TestFixture([1, 1, 1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 1, 1]),
])
def test_add_extra(fixture):
    heap = Heap()
    heap._make_heap(2)
    result = True

    for key in fixture.array:
        result = heap.Add(key)

    assert result is False
    assert heap.HeapArray == fixture.result


@pytest.mark.parametrize('fixture', [
    TestFixture([1, 1, 1, 1, 1, 1, 2], [2, 1, 1, 1, 1, 1, 1]),
    TestFixture([1, 1, 1, 1, 1, 2, 3], [3, 1, 2, 1, 1, 1, 1]),
    TestFixture([1, 1, 1, 1, 2, 3, 4], [4, 1, 3, 1, 1, 1, 2]),
    TestFixture([1, 1, 1, 2, 3, 4, 5], [5, 2, 4, 1, 1, 1, 3]),
    TestFixture([1], [1, None, None, None, None, None, None]),
])
def test_make_heap(fixture):
    heap = Heap()
    heap.MakeHeap(fixture.array, 2)

    assert heap.HeapArray == fixture.result


TestFixture = namedtuple('TestFixture', 'array maximum result')


@pytest.mark.parametrize('fixture', [
    TestFixture([None for _ in range(7)], -1, [None for _ in range(7)]),
    TestFixture([7, 6, 4, 5, 4, 3, 2], 7, [6, 5, 4, 2, 4, 3, None]),
    TestFixture([7, 4, 6, 3, 2, 5, 4], 7, [6, 4, 5, 3, 2, 4, None]),
    TestFixture([7], 7, [None for _ in range(7)]),
])
def test_get_max(fixture):
    heap = Heap()
    heap.MakeHeap(fixture.array, 2)

    assert heap.GetMax() == fixture.maximum  # noqa
    assert heap.HeapArray == fixture.result
