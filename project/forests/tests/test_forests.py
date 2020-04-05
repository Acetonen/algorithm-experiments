from collections import namedtuple
import pytest
from project.forests.forest import SimpleTree, SimpleTreeNode

TestFixture = namedtuple('TestFixture', 'init_list result')


def test_add_child():
    simple_tree = SimpleTree(SimpleTreeNode(0, None))
    assert simple_tree.Root.NodeValue == 0

    new_node = SimpleTreeNode(777, None)
    simple_tree.AddChild(simple_tree.Root, new_node)

    assert new_node in simple_tree.Root.Children
    assert new_node.Parent == simple_tree.Root
    assert len(simple_tree.Root.Children) == 1


@pytest.fixture
def get_odd_tree():
    simple_tree = SimpleTree(SimpleTreeNode(1, None))
    nodes_to_add = [
        SimpleTreeNode(2, None),
        SimpleTreeNode(3, None),
        SimpleTreeNode(4, None),
        SimpleTreeNode(5, None),
    ]
    simple_tree.AddChild(simple_tree.Root, nodes_to_add[0])
    simple_tree.AddChild(simple_tree.Root, nodes_to_add[1])
    simple_tree.AddChild(nodes_to_add[0], nodes_to_add[2])
    simple_tree.AddChild(nodes_to_add[1], nodes_to_add[3])

    return simple_tree, nodes_to_add


@pytest.fixture
def get_even_tree():
    simple_tree = SimpleTree(SimpleTreeNode(1, None))
    nodes_to_add = [
        SimpleTreeNode(2, None),
        SimpleTreeNode(3, None),
        SimpleTreeNode(4, None),
        SimpleTreeNode(5, None),
        SimpleTreeNode(6, None),
        SimpleTreeNode(7, None),
        SimpleTreeNode(8, None),
        SimpleTreeNode(9, None),
        SimpleTreeNode(10, None),
        SimpleTreeNode(11, None),
        SimpleTreeNode(12, None),
        SimpleTreeNode(13, None),
        SimpleTreeNode(14, None),
    ]

    simple_tree.AddChild(simple_tree.Root, nodes_to_add[0])

    simple_tree.AddChild(nodes_to_add[0], nodes_to_add[1])
    simple_tree.AddChild(nodes_to_add[0], nodes_to_add[2])
    simple_tree.AddChild(nodes_to_add[0], nodes_to_add[3])

    simple_tree.AddChild(nodes_to_add[1], nodes_to_add[4])
    simple_tree.AddChild(nodes_to_add[1], nodes_to_add[5])
    simple_tree.AddChild(nodes_to_add[2], nodes_to_add[6])
    simple_tree.AddChild(nodes_to_add[3], nodes_to_add[7])
    simple_tree.AddChild(nodes_to_add[3], nodes_to_add[8])

    simple_tree.AddChild(nodes_to_add[4], nodes_to_add[9])
    simple_tree.AddChild(nodes_to_add[4], nodes_to_add[10])
    simple_tree.AddChild(nodes_to_add[4], nodes_to_add[11])
    simple_tree.AddChild(nodes_to_add[5], nodes_to_add[12])

    # 1 - 2 - 3 - 6 - 11
    #               - 12
    #               - 13
    #           - 7 - 14
    #       - 4 - 8
    #       - 5 - 9
    #           - 10
    return simple_tree, nodes_to_add


def test_get_all_nodes(get_even_tree):
    simple_tree, nodes_to_add = get_even_tree
    all_nodes = simple_tree.GetAllNodes()
    assert len(all_nodes) == 14

    for node in nodes_to_add:
        assert node in all_nodes


def test_sort_all_nodes(get_even_tree):
    simple_tree, nodes_to_add = get_even_tree
    all_nodes = simple_tree.GetAllNodes()
    assert len(all_nodes) == 14

    sorted_nodes = sorted(all_nodes, key=lambda node: node.Level, reverse=True)
    levels = [node.Level for node in sorted_nodes]
    values = [node.NodeValue for node in sorted_nodes]

    assert levels == [4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
    assert values == [11, 12, 13, 14, 6, 7, 8, 9, 10, 3, 4, 5, 2, 1]


def test_even_trees(get_even_tree):
    simple_tree, nodes_to_add = get_even_tree
    even_trees = simple_tree.EvenTrees()

    assert len(even_trees) == 6
    for node_index in [0, 1, 2, 4, 5]:
        assert nodes_to_add[node_index] in even_trees


def test_odd_trees(get_odd_tree):
    simple_tree, nodes_to_add = get_odd_tree
    even_trees = simple_tree.EvenTrees()

    assert len(even_trees) == 0
