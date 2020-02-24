# flake8: noqa
from collections import namedtuple

import pytest

from project.dynamic_arrays.dynamic_array import DynArray

TestFixture = namedtuple('TestFixture', 'init_list index result')


@pytest.fixture
def dynamic_array():
    def _dynamic_array(list_of_numbers):
        dyn_array = DynArray()

        for number in list_of_numbers:
            dyn_array.append(number)

        return dyn_array

    return _dynamic_array


def get_dyn_array_values_list(dyn_array):
    result_list = list()
    for index in range(dyn_array.count):
        result_list.append(dyn_array[index])

    return result_list


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture(range(16), 16, list(range(16)) + [666]),
    TestFixture(range(16), 0, [666] + list(range(16))),
    TestFixture(range(16), 1, [0, 666] + list(range(1, 16))),
])
def test_insert_with_resize(dynamic_array, fixture):
    dynamic_array = dynamic_array(fixture.init_list)
    assert get_dyn_array_values_list(dynamic_array) == list(range(16))
    assert len(dynamic_array) == 16
    assert dynamic_array.capacity == 16

    dynamic_array.insert(fixture.index, 666)

    assert get_dyn_array_values_list(dynamic_array) == fixture.result
    assert len(dynamic_array) == 17
    assert dynamic_array.capacity == 32


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture(range(15), 15, list(range(15)) + [666]),
    TestFixture(range(15), 0, [666] + list(range(15))),
    TestFixture(range(15), 1, [0, 666] + list(range(1, 15))),
])
def test_insert_without_resize(dynamic_array, fixture):
    dynamic_array = dynamic_array(fixture.init_list)
    assert get_dyn_array_values_list(dynamic_array) == list(range(15))
    assert len(dynamic_array) == 15
    assert dynamic_array.capacity == 16

    dynamic_array.insert(fixture.index, 666)

    assert get_dyn_array_values_list(dynamic_array) == fixture.result
    assert len(dynamic_array) == 16
    assert dynamic_array.capacity == 16


def test_insert_in_empty_array(dynamic_array):
    dynamic_array = dynamic_array([])
    assert get_dyn_array_values_list(dynamic_array) == list()
    assert len(dynamic_array) == 0
    assert dynamic_array.capacity == 16

    dynamic_array.insert(0, 666)

    assert get_dyn_array_values_list(dynamic_array) == [666]
    assert len(dynamic_array) == 1
    assert dynamic_array.capacity == 16


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture(range(3), 4, None),
    TestFixture(range(3), -1, None),
])
def test_insert_index_out_of_range(dynamic_array, fixture):
    dynamic_array = dynamic_array(fixture.init_list)
    assert get_dyn_array_values_list(dynamic_array) == list(range(3))
    assert len(dynamic_array) == 3

    with pytest.raises(IndexError):
        dynamic_array.insert(fixture.index, 666)


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture(range(3), 4, None),
    TestFixture(range(3), -1, None),
    TestFixture(list(), 0, None),
])
def test_delete_index_out_of_range(dynamic_array, fixture):
    dynamic_array = dynamic_array(fixture.init_list)

    with pytest.raises(Exception):
        dynamic_array.delete(fixture.index)


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture(range(15), 1, [0] + list(range(2, 15))),
    TestFixture(range(15), 14, list(range(14))),
    TestFixture(range(15), 0, list(range(1, 15))),
])
def test_delete_without_resize(dynamic_array, fixture):
    dynamic_array = dynamic_array(fixture.init_list)
    assert get_dyn_array_values_list(dynamic_array) == list(range(15))
    assert len(dynamic_array) == 15
    dynamic_array.capacity = 28
    assert dynamic_array.capacity == 28

    dynamic_array.delete(fixture.index)

    assert get_dyn_array_values_list(dynamic_array) == fixture.result
    assert len(dynamic_array) == 14
    assert dynamic_array.capacity == 28


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture(range(8), 1, [0] + list(range(2, 8))),
    TestFixture(range(8), 7, list(range(7))),
    TestFixture(range(8), 0, list(range(1, 8))),
])
def test_delete_without_resize_min_capacity(dynamic_array, fixture):
    dynamic_array = dynamic_array(fixture.init_list)
    assert get_dyn_array_values_list(dynamic_array) == list(range(8))
    assert len(dynamic_array) == 8
    assert dynamic_array.capacity == 16

    dynamic_array.delete(fixture.index)

    assert get_dyn_array_values_list(dynamic_array) == fixture.result
    assert len(dynamic_array) == 7
    assert dynamic_array.capacity == 16


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture(range(20), 1, [0] + list(range(2, 20))),
    TestFixture(range(20), 19, list(range(19))),
    TestFixture(range(20), 0, list(range(1, 20))),
])
def test_delete_with_resize(dynamic_array, fixture):
    dynamic_array = dynamic_array(fixture.init_list)
    dynamic_array.capacity = 40
    assert get_dyn_array_values_list(dynamic_array) == list(range(20))
    assert len(dynamic_array) == 20
    assert dynamic_array.capacity == 40

    dynamic_array.delete(fixture.index)

    assert get_dyn_array_values_list(dynamic_array) == fixture.result
    assert len(dynamic_array) == 19
    assert dynamic_array.capacity == 26


@pytest.mark.parametrize('fixture', [
    TestFixture(range(3), -1, None),
    TestFixture(range(3), 3, None),
    TestFixture(range(3), 4, None),
])
def test_get_item_out_of_range(dynamic_array, fixture):
    dynamic_array = dynamic_array(fixture.init_list)
    with pytest.raises(IndexError):
        dynamic_array[fixture.index]