from collections import namedtuple

import pytest

from project.linked_lists.linked_list import LinkedList, Node

TestFixture = namedtuple('TestFixture', 'init_list result')


@pytest.fixture
def linked_list():
    def _linked_list(list_of_numbers):
        linked_list = LinkedList()

        for node in [Node(number) for number in list_of_numbers]:
            linked_list.add_in_tail(node)

        return linked_list

    return _linked_list


def get_node_values_list(linked_list):
    result_list = list()
    node = linked_list.head
    while node:
        result_list.append(node.value)
        node = node.next

    return result_list


@pytest.fixture
def bidirectional_linked_list():
    def _bidirectional_linked_list(list_of_numbers):
        linked_list = LinkedList()

        for node in [Node(number) for number in list_of_numbers]:
            linked_list.add_in_tail(node)

        return linked_list

    return _bidirectional_linked_list


@pytest.mark.parametrize('nodes_values', [
    [1, 2, 3, 4, 5],
    [3],
    [3, 4],
    [3, 3],
    [4, 3],
])
def test_find_one_value(nodes_values, linked_list):
    linked_list = linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    assert linked_list.find(3).value == 3


@pytest.mark.parametrize('nodes_values', [
    [4, 5],
    [4]
])
def test_not_find_one_value(nodes_values, linked_list):
    linked_list = linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    assert linked_list.find(3) is None


@pytest.mark.parametrize('nodes_values', [
    [3, 4, 5, 3],
    [3, 3],
    [3, 3, 4, 5],
    [4, 5, 3, 3],
])
def test_find_all_values(nodes_values, linked_list):
    linked_list = linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    assert [node.value for node in linked_list.find_all(3)] == [3, 3]


@pytest.mark.parametrize('nodes_values', [
    [4, 5],
    [],
])
def test_not_find_all_values(nodes_values, linked_list):
    linked_list = linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    assert [node.value for node in linked_list.find_all(3)] == []


@pytest.mark.parametrize('nodes_values', [
    [4, 5],
])
def test_len(nodes_values, linked_list):
    linked_list = linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    assert linked_list.len() == 2


@pytest.mark.parametrize('nodes_values', [
    [],
])
def test_no_len(nodes_values, linked_list):
    linked_list = linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    assert linked_list.len() == 0


@pytest.mark.parametrize('nodes_values', [
    [4, 5],
    [],
])
def test_clean(nodes_values, linked_list):
    linked_list = linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    linked_list.clean()

    assert linked_list.len() == 0
    assert linked_list.head is None
    assert linked_list.tail is None


# noinspection DuplicatedCode
@pytest.mark.parametrize('nodes_values', [
    [4, 3, 5, 3],
    [3, 4, 5, 3],
    [4, 5, 3, 3],
])
def test_delete_one_from_many(nodes_values, linked_list):
    linked_list = linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    linked_list.delete(3)

    assert linked_list.len() == 3

    assert linked_list.head.value == 4
    assert linked_list.head.next.value == 5

    assert linked_list.tail.value == 3
    assert linked_list.tail.next is None


# noinspection DuplicatedCode
@pytest.mark.parametrize('nodes_values', [
    [3, 5],
    [5, 3],
])
def test_delete_one_from_two(nodes_values, linked_list):
    linked_list = linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    linked_list.delete(3)

    assert linked_list.len() == 1

    assert linked_list.head.value == 5
    assert linked_list.head.next is None

    assert linked_list.tail.value == 5
    assert linked_list.tail.next is None


@pytest.mark.parametrize('nodes_values', [
    [3],
    [],
])
def test_delete_empty(nodes_values, linked_list):
    linked_list = linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    linked_list.delete(3)

    assert linked_list.len() == 0

    assert linked_list.tail is None
    assert linked_list.head is None


@pytest.mark.parametrize('nodes_values', [
    [3, 3, 3],
    [],
])
def test_delete_all_empty(nodes_values, linked_list):
    linked_list = linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    linked_list.delete(3, True)

    assert linked_list.len() == 0

    assert linked_list.tail is None
    assert linked_list.head is None


# noinspection DuplicatedCode
@pytest.mark.parametrize('nodes_values', [
    [4, 3, 3, 5],
    [3, 3, 4, 5],
    [4, 5, 3, 3],
    [3, 4, 3, 5, 3],
])
def test_delete_all_from_many(nodes_values, linked_list):
    linked_list = linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    linked_list.delete(3, True)

    assert linked_list.len() == 2

    assert linked_list.head.value == 4
    assert linked_list.head.next.value == 5

    assert linked_list.tail.value == 5
    assert linked_list.tail.next is None


# noinspection DuplicatedCode
@pytest.mark.parametrize('nodes_values', [
    [3, 5, 3],
    [5, 3, 3],
    [3, 3, 5],
])
def test_delete_many_leave_one(nodes_values, linked_list):
    linked_list = linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    linked_list.delete(3, True)

    assert linked_list.len() == 1

    assert linked_list.head.value == 5
    assert linked_list.head.next is None

    assert linked_list.tail.value == 5
    assert linked_list.tail.next is None


@pytest.mark.parametrize('nodes_values_results', [
    ([], [666]),
])
def test_insert_in_empty_list(nodes_values_results, linked_list):
    linked_list = linked_list(nodes_values_results[0])
    assert get_node_values_list(linked_list) == nodes_values_results[0]

    linked_list.insert(None, Node(666))

    assert linked_list.head.value == 666
    assert get_node_values_list(linked_list) == nodes_values_results[1]


@pytest.mark.parametrize('nodes_values_results', [
    ([5, 3], [666, 5, 3]),
    ([], [666]),
    ([3], [666, 3])
])
def test_insert_after_none(nodes_values_results, linked_list):
    linked_list = linked_list(nodes_values_results[0])
    assert get_node_values_list(linked_list) == nodes_values_results[0]

    linked_list.insert(None, Node(666))

    assert linked_list.head.value == 666
    assert linked_list.tail.value is not None
    assert get_node_values_list(linked_list) == nodes_values_results[1]


def test_insert_after_tail():
    linked_list = LinkedList()
    node_list = [Node(number) for number in [1, 2, 3, 4]]

    for node in node_list:
        linked_list.add_in_tail(node)

    linked_list.insert(node_list[-1], Node(666))

    assert linked_list.tail.value == 666
    assert get_node_values_list(linked_list) == [1, 2, 3, 4, 666]


def test_insert():
    linked_list = LinkedList()
    node_list = [Node(number) for number in [1, 2, 3, 4]]

    for node in node_list:
        linked_list.add_in_tail(node)

    new_node = Node(666)
    linked_list.insert(node_list[0], new_node)
    assert get_node_values_list(linked_list) == [1, 666, 2, 3, 4]
