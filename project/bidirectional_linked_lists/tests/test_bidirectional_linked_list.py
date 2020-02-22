import pytest
from project.bidirectional_linked_lists.bidirectional_linked_list import Node, LinkedList2


@pytest.fixture
def bidirectional_linked_list():
    def _bidirectional_linked_list(list_of_numbers):
        linked_list = LinkedList2()

        for node in [Node(number) for number in list_of_numbers]:
            linked_list.add_in_tail(node)

        return linked_list

    return _bidirectional_linked_list


def get_node_values_list(linked_list):
    result_list = list()
    node = linked_list.head
    while node:
        result_list.append(node.value)
        node = node.next

    return result_list


@pytest.mark.parametrize('nodes_values', [
    [1, 2, 3, 4, 5],
    [3],
    [3, 4],
    [3, 3],
    [4, 3],
])
def test_find_one_value(nodes_values, bidirectional_linked_list):
    linked_list = bidirectional_linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    assert linked_list.find(3).value == 3


@pytest.mark.parametrize('nodes_values', [
    [4, 5],
    [4]
])
def test_not_find_one_value(nodes_values, bidirectional_linked_list):
    linked_list = bidirectional_linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    assert linked_list.find(3) is None


@pytest.mark.parametrize('nodes_values', [
    [3, 4, 5, 3],
    [3, 3],
    [3, 3, 4, 5],
    [4, 5, 3, 3],
])
def test_find_all_values(nodes_values, bidirectional_linked_list):
    linked_list = bidirectional_linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    assert [node.value for node in linked_list.find_all(3)] == [3, 3]


@pytest.mark.parametrize('nodes_values', [
    [4, 5],
    [],
])
def test_not_find_all_values(nodes_values, bidirectional_linked_list):
    linked_list = bidirectional_linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    assert [node.value for node in linked_list.find_all(3)] == []


@pytest.mark.parametrize('nodes_values', [
    [4, 5],
])
def test_len(nodes_values, bidirectional_linked_list):
    linked_list = bidirectional_linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    assert linked_list.len() == 2


@pytest.mark.parametrize('nodes_values', [
    [],
])
def test_no_len(nodes_values, bidirectional_linked_list):
    linked_list = bidirectional_linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    assert linked_list.len() == 0


@pytest.mark.parametrize('nodes_values', [
    [4, 5],
    [],
])
def test_clean(nodes_values, bidirectional_linked_list):
    linked_list = bidirectional_linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    linked_list.clean()

    assert linked_list.len() == 0
    assert linked_list.head is None
    assert linked_list.tail is None


# noinspection DuplicatedCode
@pytest.mark.parametrize('nodes_values', [
    [4, 3, 5],
    [3, 4, 5],
    [4, 5, 3],
])
def test_delete_one_from_many(nodes_values, bidirectional_linked_list):
    linked_list = bidirectional_linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    linked_list.delete(3)

    assert linked_list.len() == 2

    assert linked_list.head.value == 4
    assert linked_list.head.prev is None
    assert linked_list.head.next.value == 5

    assert linked_list.tail.value == 5
    assert linked_list.tail.prev.value == 4
    assert linked_list.tail.next is None


# noinspection DuplicatedCode
@pytest.mark.parametrize('nodes_values', [
    [3, 5],
    [5, 3],
])
def test_delete_one_from_two(nodes_values, bidirectional_linked_list):
    linked_list = bidirectional_linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    linked_list.delete(3)

    assert linked_list.len() == 1

    assert linked_list.head.value == 5
    assert linked_list.head.prev is None
    assert linked_list.head.next is None

    assert linked_list.tail.value == 5
    assert linked_list.tail.prev is None
    assert linked_list.tail.next is None


@pytest.mark.parametrize('nodes_values', [
    [3],
    [],
])
def test_delete_empty(nodes_values, bidirectional_linked_list):
    linked_list = bidirectional_linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    linked_list.delete(3)

    assert linked_list.len() == 0

    assert linked_list.tail is None
    assert linked_list.head is None


@pytest.mark.parametrize('nodes_values', [
    [3, 3, 3],
    [],
])
def test_delete_all_empty(nodes_values, bidirectional_linked_list):
    linked_list = bidirectional_linked_list(nodes_values)
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
def test_delete_all_from_many(nodes_values, bidirectional_linked_list):
    linked_list = bidirectional_linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    linked_list.delete(3, True)

    assert linked_list.len() == 2

    assert linked_list.head.value == 4
    assert linked_list.head.prev is None
    assert linked_list.head.next.value == 5

    assert linked_list.tail.value == 5
    assert linked_list.tail.prev.value == 4
    assert linked_list.tail.next is None


# noinspection DuplicatedCode
@pytest.mark.parametrize('nodes_values', [
    [3, 5, 3],
    [5, 3, 3],
    [3, 3, 5],
])
def test_delete_many_leave_one(nodes_values, bidirectional_linked_list):
    linked_list = bidirectional_linked_list(nodes_values)
    assert get_node_values_list(linked_list) == nodes_values

    linked_list.delete(3, True)

    assert linked_list.len() == 1

    assert linked_list.head.value == 5
    assert linked_list.head.prev is None
    assert linked_list.head.next is None

    assert linked_list.tail.value == 5
    assert linked_list.tail.prev is None
    assert linked_list.tail.next is None


@pytest.mark.parametrize('nodes_values_results', [
    ([5, 3], [666, 5, 3]),
    ([], [666]),
    ([3], [666, 3])
])
def test_insert_in_head(nodes_values_results, bidirectional_linked_list):
    linked_list = bidirectional_linked_list(nodes_values_results[0])
    assert get_node_values_list(linked_list) == nodes_values_results[0]

    linked_list.add_in_head(Node(666))

    assert linked_list.head.value == 666
    assert get_node_values_list(linked_list) == nodes_values_results[1]


def test_insert():
    linked_list = LinkedList2()
    node_list = [Node(number) for number in [1, 2, 3, 4]]

    for node in node_list:
        linked_list.add_in_tail(node)

    linked_list.insert(node_list[0], Node(666))
    assert get_node_values_list(linked_list) == [1, 666, 2, 3, 4]