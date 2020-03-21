from collections import namedtuple

from project.balanced_binary_trees.balanced_binary_tree import BalancedBST, BSTNode

TestFixture = namedtuple('TestFixture', 'list index')

RESULT = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]


def _recursive_node_list_append(result_list, node, order=('LeftChild', 'Root', 'RightChild')):
    for step in order:
        if step == 'Root':
            result_list.append(node.NodeKey)
        elif getattr(node, step):
            _recursive_node_list_append(result_list, getattr(node, step), order)


def get_all_nodes_keys(tree):
    result_list = list()

    if not tree.Root:
        return list()

    _recursive_node_list_append(result_list, tree.Root)

    return result_list


def test_generate_tree():
    tree = BalancedBST()
    tree.GenerateTree(RESULT)

    assert get_all_nodes_keys(tree) == sorted(RESULT)


def test_is_balanced_true():
    tree = BalancedBST()
    tree.GenerateTree(RESULT)

    assert tree.IsBalanced(tree.Root) is True


def test_is_balanced_false():
    tree = BalancedBST()

    tree.Root = BSTNode(3, None, 1)
    second_right = BSTNode(4, tree.Root, 2)
    tree.Root.RightChild = second_right
    second_left = BSTNode(2, tree.Root, 2)
    tree.Root.LeftChild = second_left
    third_left = BSTNode(1, second_left, 3)
    second_left.LeftChild = third_left
    fourth_right = BSTNode(2, third_left, 4)
    third_left.RightChild = fourth_right

    assert get_all_nodes_keys(tree) == [1, 2, 2, 3, 4]
    assert tree.IsBalanced(tree.Root) is False


def test_is_balanced_false_case_two():
    tree = BalancedBST()

    tree.Root = BSTNode(3, None, 1)
    second_left = BSTNode(2, tree.Root, 2)
    tree.Root.LeftChild = second_left
    third_left = BSTNode(1, second_left, 3)
    second_left.LeftChild = third_left
    fourth_right = BSTNode(2, third_left, 4)
    third_left.RightChild = fourth_right

    assert get_all_nodes_keys(tree) == [1, 2, 2, 3]
    assert tree.IsBalanced(tree.Root) is False