from collections import namedtuple

import pytest

from project.binary_search_trees.binary_search_tree import BSTNode, BST

TestFixture = namedtuple('TestFixture', 'value count result')

TREE_KEYS = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]


@pytest.fixture
def super_simple_binary_tree():
    root_node = BSTNode(8, 8, None)
    binary_tree = BST(root_node)
    right_node = BSTNode(9, 9, root_node)
    left_node = BSTNode(7, 7, root_node)
    root_node.RightChild = right_node
    root_node.LeftChild = left_node

    return binary_tree


@pytest.fixture
def full_binary_tree():
    binary_tree = BST(BSTNode(8, 8, None))
    for value in TREE_KEYS:
        binary_tree.AddKeyValue(value, value)

    assert binary_tree.Count() == 15

    return binary_tree


def test_count(super_simple_binary_tree):
    assert super_simple_binary_tree.Count() == 3


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture(10, 4, True),
    TestFixture(6, 4, True),
    TestFixture(7, 3, False),
])
def test_add(super_simple_binary_tree, fixture):
    result = super_simple_binary_tree.AddKeyValue(fixture.value, fixture.value)

    assert super_simple_binary_tree.Count() == fixture.count
    assert result == fixture.result


@pytest.mark.parametrize('value', TREE_KEYS)
def test_find_by_key_exists(full_binary_tree, value):
    result = full_binary_tree.FindNodeByKey(value)

    assert result.Node.NodeKey == value
    assert result.NodeHasKey is True
    assert result.ToLeft is False


def test_find_by_key_empty_tree():
    empty_tree = BST(None)
    result = empty_tree.FindNodeByKey(10)

    assert result.Node is None
    assert result.NodeHasKey is False
    assert result.ToLeft is False


TestFixture = namedtuple('TestFixture', 'value parent_value to_left')


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture(-1, 1, True),
    TestFixture(16, 15, False),
])
def test_find_by_key_not_exists(full_binary_tree, fixture):
    result = full_binary_tree.FindNodeByKey(fixture.value)

    assert result.Node.NodeKey == fixture.parent_value
    assert result.NodeHasKey is False
    assert result.ToLeft == fixture.to_left


def test_delete_node_by_key_exists(full_binary_tree):
    full_binary_tree.DeleteNodeByKey(6)

    assert full_binary_tree.Count() == 12

    result = full_binary_tree.FindNodeByKey(6)

    assert result.Node.NodeKey == 4
    assert result.NodeHasKey is False
    assert result.ToLeft is False


def test_delete_node_by_key_not_exists(full_binary_tree):
    assert full_binary_tree.DeleteNodeByKey(666) is False


def test_find_max(full_binary_tree):
    node = full_binary_tree.FinMinMax(full_binary_tree.Root, True)
    assert node.NodeKey == 15


def test_find_min(full_binary_tree):
    node = full_binary_tree.FinMinMax(full_binary_tree.Root, False)
    assert node.NodeKey == 1