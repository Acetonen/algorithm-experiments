from collections import namedtuple
import pytest
from project.trees.tree import SimpleTree, SimpleTreeNode

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
def get_sample():
    simple_tree = SimpleTree(SimpleTreeNode(123, None))
    nodes_to_add = [
        SimpleTreeNode(000, None),
        SimpleTreeNode(111, None),
        SimpleTreeNode(222, None),
        SimpleTreeNode(333, None),
        SimpleTreeNode(444, None),
        SimpleTreeNode(555, None),
    ]

    simple_tree.AddChild(simple_tree.Root, nodes_to_add[0])
    simple_tree.AddChild(simple_tree.Root, nodes_to_add[1])
    simple_tree.AddChild(nodes_to_add[0], nodes_to_add[2])
    simple_tree.AddChild(nodes_to_add[0], nodes_to_add[3])
    simple_tree.AddChild(nodes_to_add[1], nodes_to_add[4])
    simple_tree.AddChild(nodes_to_add[4], nodes_to_add[5])

    # 123 - 111 - 444 - 555
    #     - 000 - 222
    #           - 333
    return simple_tree, nodes_to_add


def test_get_all_nodes(get_sample):
    simple_tree, nodes_to_add = get_sample
    all_nodes = simple_tree.GetAllNodes()
    assert len(all_nodes) == 7

    for node in nodes_to_add:
        assert node in all_nodes


def test_get_all_nodes_one():
    simple_tree = SimpleTree(SimpleTreeNode(0, None))
    assert len(simple_tree.GetAllNodes()) == 1


def test_get_all_nodes_none():
    simple_tree = SimpleTree(None)
    assert len(simple_tree.GetAllNodes()) == 0


def test_delete_node(get_sample):
    simple_tree, nodes_to_add = get_sample
    assert len(simple_tree.GetAllNodes()) == 7

    simple_tree.DeleteNode(nodes_to_add[4])

    # Delete actually two nodes
    assert len(simple_tree.GetAllNodes()) == 5


def test_delete_node_one():
    one_node = SimpleTreeNode(0, None)
    simple_tree = SimpleTree(one_node)
    assert len(simple_tree.GetAllNodes()) == 1

    simple_tree.DeleteNode(one_node)
    assert len(simple_tree.GetAllNodes()) == 0


def test_find_node_by_value(get_sample):
    simple_tree, nodes_to_add = get_sample
    assert len(simple_tree.GetAllNodes()) == 7

    result = simple_tree.FindNodesByValue(111)

    assert nodes_to_add[1] in result
    assert len(result) == 1


def test_find_node_by_value_not_find(get_sample):
    simple_tree, nodes_to_add = get_sample
    assert len(simple_tree.GetAllNodes()) == 7

    result = simple_tree.FindNodesByValue(999)

    assert len(result) == 0


def test_count(get_sample):
    simple_tree, nodes_to_add = get_sample
    assert len(simple_tree.GetAllNodes()) == 7

    assert simple_tree.Count() == 7


def test_leaf_count(get_sample):
    simple_tree, nodes_to_add = get_sample
    assert len(simple_tree.GetAllNodes()) == 7

    assert simple_tree.LeafCount() == 3


def test_move_node(get_sample):
    simple_tree, nodes_to_add = get_sample
    assert len(simple_tree.GetAllNodes()) == 7

    simple_tree.MoveNode(nodes_to_add[0], nodes_to_add[5])
    assert len(simple_tree.GetAllNodes()) == 7
    assert nodes_to_add[0].Parent == nodes_to_add[5]