from collections import namedtuple

import pytest

from project.caches.cache import NativeCache

SIZE = 5
TestFixture = namedtuple('TestFixture', 'init_list result element')


def get_node_values_list(ordered_list):
    return [node.value for node in ordered_list.get_all()]


@pytest.mark.parametrize('fixture', [
    TestFixture([1, 'test', 3, 6, 5], [1, 2, 0, 0, 0], 'test'),
    TestFixture([1, 2, 3, 4, 5], [1, 2, 0, 0, 0], 2),
])
def test_get(fixture):
    native_cache = NativeCache(SIZE)
    native_cache.slots = fixture.init_list  # noqa
    native_cache.values = [1, 2, 3, 4, 5]

    native_cache.get(fixture.element)  # noqa
    assert get_node_values_list(native_cache.hits_order) == [1]
    native_cache.get(fixture.element)  # noqa
    assert get_node_values_list(native_cache.hits_order) == [2]
    native_cache.get(1)
    assert get_node_values_list(native_cache.hits_order) == [1, 2]

    assert native_cache.hits == fixture.result  # noqa
    assert native_cache.hits_mapping.get(2) == [1]
    assert native_cache.hits_mapping.get(1) == [0]


def test_put_in_full_cache():
    native_cache = NativeCache(SIZE)
    native_cache.slots = [1, 2, 3, 4, 5]
    native_cache.values = [1, 2, 3, 4, 5]

    for item in range(1, 6):  # noqa
        native_cache.get(item)

    native_cache.get(2)
    native_cache.get(2)
    native_cache.get(3)
    native_cache.get(1)
    native_cache.get(5)

    assert native_cache.hits == [2, 3, 2, 1, 2]

    native_cache.put('test', 'test')

    assert native_cache.slots == [1, 2, 3, 'test', 5]
    assert native_cache.values == [1, 2, 3, 'test', 5]
    assert native_cache.hits == [2, 3, 2, 0, 2]

    native_cache.get('test')
    native_cache.get('test')
    native_cache.get('test')
    native_cache.get(5)
    native_cache.get(1)

    assert native_cache.hits == [3, 3, 2, 3, 3]

    native_cache.put('final_test', 'final_test')

    assert native_cache.slots == [1, 2, 'final_test', 'test', 5]
    assert native_cache.values == [1, 2, 'final_test', 'test', 5]
    assert native_cache.hits == [3, 3, 0, 3, 3]


def test_put_in_full_cache_with_empty_hits():
    native_cache = NativeCache(SIZE)
    native_cache.slots = [1, 2, 3, 4, 5]
    native_cache.values = [1, 2, 3, 4, 5]

    native_cache.put('test', 'test')

    assert native_cache.slots == ['test', 2, 3, 4, 5]
    assert native_cache.values == ['test', 2, 3, 4, 5]
    assert native_cache.hits == [0, 0, 0, 0, 0]