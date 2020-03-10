from collections import namedtuple

import pytest

TestFixture = namedtuple('TestFixture', 'order node_values')


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture(0, tuple(range(1, 16))),
    TestFixture(1, (1, 3, 2, 5, 7, 6, 4, 9, 11, 10, 13, 15, 14, 12, 8)),
    TestFixture(2, (8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15)),
])
def test_deep_all_nodes(full_binary_tree, fixture):
    bypass_result = full_binary_tree.DeepAllNodes(fixture.order)
    assert tuple([node.NodeKey for node in bypass_result]) == fixture.node_values


def test_wide_all_nodes(full_binary_tree):
    bypass_result = full_binary_tree.WideAllNodes()
    assert tuple([node.NodeKey for node in bypass_result]) == (8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15)
