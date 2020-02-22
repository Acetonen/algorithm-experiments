from collections import namedtuple

import pytest

from project.ordered_lists.ordered_list import OrderedList, OrderedStringList

TestFixture = namedtuple('TestFixture', 'init_list result')


@pytest.fixture
def ordered_list():
    def _ordered_list(asc, list_of_numbers):
        ordered_list = OrderedList(asc)

        for node in list_of_numbers:
            ordered_list.add(node)

        return ordered_list

    return _ordered_list


def get_node_values_list(ordered_list):
    return [node.value for node in ordered_list.get_all()]


@pytest.mark.parametrize('fixture', [
    TestFixture([1, 2], -1),
    TestFixture([2, 2], 0),
    TestFixture([2, 1], 1),
])
def test_compare(fixture):
    assert OrderedList.compare(*fixture.init_list) == fixture.result  # noqa


@pytest.mark.parametrize('fixture', [
    TestFixture([1, 2], -1),
    TestFixture([2, 2], 0),
    TestFixture([2, 1], 1),
])
def test_compare_stas(fixture):
    assert OrderedList.compare_stas(*fixture.init_list) == fixture.result  # noqa


@pytest.mark.parametrize('fixture', [
    TestFixture([1, 2], -1),
    TestFixture([2, 2], 0),
    TestFixture([2, 1], 1),
])
def test_compare_shortest(fixture):
    assert OrderedList.compare_shortest(*fixture.init_list) == fixture.result  # noqa


@pytest.mark.parametrize('fixture', [
    TestFixture([1, 2, 3], [1, 2, 3]),
    TestFixture([3, 2, 1], [1, 2, 3]),
    TestFixture([2, 3, 1], [1, 2, 3]),
])
def test_add_for_create_list_ascending(fixture, ordered_list):
    ordered_list = ordered_list(True, fixture.init_list)  # noqa

    assert get_node_values_list(ordered_list) == fixture.result  # noqa
    assert ordered_list.head.value == 1
    assert ordered_list.tail.value == 3


@pytest.mark.parametrize('fixture', [
    TestFixture([1, 2, 3], [3, 2, 1]),
    TestFixture([3, 2, 1], [3, 2, 1]),
    TestFixture([2, 3, 1], [3, 2, 1]),
])
def test_add_for_create_list_descending(fixture, ordered_list):
    ordered_list = ordered_list(False, fixture.init_list)  # noqa

    assert get_node_values_list(ordered_list) == fixture.result  # noqa
    assert ordered_list.head.value == 3
    assert ordered_list.tail.value == 1
    assert ordered_list.head.prev is None
    assert ordered_list.head.next.value == 2
    assert ordered_list.tail.prev.value == 2
    assert ordered_list.tail.next is None


@pytest.mark.parametrize('fixture', [
    TestFixture([2, 4, 8, True], [2, 4, 5, 8]),
    TestFixture([8, 4, 2, False], [8, 5, 4, 2]),
])
def test_add_in_exists_list(fixture, ordered_list):
    ordered_list = ordered_list(fixture.init_list.pop(), fixture.init_list)  # noqa
    ordered_list.add(5)

    assert get_node_values_list(ordered_list) == fixture.result  # noqa
    assert ordered_list.head.value == fixture.init_list[0]  # noqa
    assert ordered_list.tail.value == fixture.init_list[-1]  # noqa
    assert ordered_list.head.prev is None
    assert ordered_list.head.next.value == fixture.result[1]  # noqa
    assert ordered_list.tail.prev.value == fixture.result[-2]  # noqa
    assert ordered_list.tail.next is None


# noinspection DuplicatedCode
@pytest.mark.parametrize('fixture', [
    TestFixture([2, 4, 8, True], [2, 4, 4, 8]),
    TestFixture([8, 4, 2, False], [8, 4, 4, 2]),
])
def test_add_in_exists_list_exists_element(fixture, ordered_list):
    ordered_list = ordered_list(fixture.init_list.pop(), fixture.init_list)  # noqa
    ordered_list.add(4)

    assert get_node_values_list(ordered_list) == fixture.result  # noqa
    assert ordered_list.head.value == fixture.init_list[0]  # noqa
    assert ordered_list.tail.value == fixture.init_list[-1]  # noqa
    assert ordered_list.head.prev is None
    assert ordered_list.head.next.value == fixture.result[1]  # noqa
    assert ordered_list.tail.prev.value == fixture.result[-2]  # noqa
    assert ordered_list.tail.next is None


@pytest.mark.parametrize('fixture', [
    TestFixture([], [5]),
])
def test_add_in_empty_list(fixture, ordered_list):
    ordered_list = ordered_list(True, fixture.init_list)  # noqa
    ordered_list.add(5)

    assert ordered_list.head.value == 5
    assert ordered_list.tail.value == 5


@pytest.mark.parametrize('fixture', [
    [4, 5],
    [],
])
def test_clean(fixture, ordered_list):
    ordered_list = ordered_list(True, fixture)
    assert get_node_values_list(ordered_list) == fixture

    ordered_list.clean(True)

    assert ordered_list.len() == 0
    assert ordered_list.head is None
    assert ordered_list.tail is None


# noinspection DuplicatedCode
def check_deletion(ordered_list):
    assert get_node_values_list(ordered_list) == [4, 5]
    assert ordered_list.len() == 2

    assert ordered_list.head.value == 4
    assert ordered_list.head.prev is None
    assert ordered_list.head.next.value == 5

    assert ordered_list.tail.value == 5
    assert ordered_list.tail.prev.value == 4
    assert ordered_list.tail.next is None


# noinspection DuplicatedCode
@pytest.mark.parametrize('fixture', [
    [4, 3, 5],
    [3, 4, 5],
    [4, 5, 3],
    [5, 3, 4],
    [3, 5, 4],
    [5, 4, 3],
])
def test_delete_one_from_head(fixture, ordered_list):
    ordered_list = ordered_list(True, fixture)
    assert ordered_list.head.value == 3
    assert ordered_list.tail.value == 5
    assert ordered_list.tail.prev.value == 4

    ordered_list.delete(3)

    check_deletion(ordered_list)


# noinspection DuplicatedCode
@pytest.mark.parametrize('fixture', [
    [4, 4.5, 5],
    [4.5, 4, 5],
    [4, 5, 4.5],
    [5, 4.5, 4],
    [4.5, 5, 4],
    [5, 4, 4.5],
])
def test_delete_one_from_body(fixture, ordered_list):
    ordered_list = ordered_list(True, fixture)

    ordered_list.delete(4.5)

    check_deletion(ordered_list)


# noinspection DuplicatedCode
@pytest.mark.parametrize('fixture', [
    [4, 6, 5],
    [6, 4, 5],
    [4, 5, 6],
    [5, 6, 4],
    [6, 5, 4],
    [5, 4, 6],
])
def test_delete_one_from_tail(fixture, ordered_list):
    ordered_list = ordered_list(True, fixture)

    ordered_list.delete(6)

    check_deletion(ordered_list)


# noinspection DuplicatedCode
@pytest.mark.parametrize('fixture', [
    [3, 5],
    [5, 3],
])
def test_delete_one_from_two(fixture, ordered_list):
    ordered_list = ordered_list(True, fixture)
    assert ordered_list.head.value == 3
    assert ordered_list.tail.value == 5
    assert ordered_list.tail.prev.value == 3

    ordered_list.delete(3)

    assert ordered_list.len() == 1

    assert ordered_list.head.value == 5
    assert ordered_list.head.prev is None
    assert ordered_list.head.next is None

    assert ordered_list.tail.value == 5
    assert ordered_list.tail.prev is None
    assert ordered_list.tail.next is None


@pytest.mark.parametrize('fixture', [
    [3],
    [],
])
def test_delete_empty(fixture, ordered_list):
    ordered_list = ordered_list(True, fixture)

    ordered_list.delete(3)

    assert ordered_list.len() == 0

    assert ordered_list.tail is None
    assert ordered_list.head is None


@pytest.mark.parametrize('fixture', [
    [1, 2, 3, 4, 5, 6],
])
def test_find(fixture, ordered_list):
    ordered_list = ordered_list(True, fixture)

    node = ordered_list.find(3)

    assert node.value == 3
    assert node.prev.value == 2
    assert node.next.value == 4


@pytest.mark.parametrize('fixture', [
    [1, 2, 4, 5, 6],
])
def test_find_early_break(fixture, ordered_list):
    ordered_list = ordered_list(True, fixture)

    node = ordered_list.find(3)

    assert node is None


@pytest.mark.parametrize('fixture', [
    TestFixture([' abc', 'aac '], 1),
    TestFixture(['abc', 'aac'], 1),
])
def test_string_compare(fixture):
    assert OrderedStringList(True).compare(*fixture.init_list) == fixture.result  # noqa