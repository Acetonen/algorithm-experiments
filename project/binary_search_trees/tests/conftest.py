import pytest

from project.binary_search_trees.binary_search_tree import BST, BSTNode
from project.binary_search_trees.tests.test_binary_search_tree import TREE_KEYS


@pytest.fixture
def full_binary_tree():
    binary_tree = BST(BSTNode(8, 8, None))
    for value in TREE_KEYS:
        binary_tree.AddKeyValue(value, value)

    assert binary_tree.Count() == 15

    return binary_tree