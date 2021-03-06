from collections import namedtuple

import pytest

from project.array_binary_search_trees.array_binary_search_tree import aBST

TestFixture = namedtuple('TestFixture', 'list index')

TREE_KEYS = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13]


@pytest.mark.parametrize('fixture', [
    TestFixture(1, 3),
    TestFixture(2, 7),
    TestFixture(3, 15),
])
def test_tree_create(fixture):
    tree = aBST(fixture.list)

    assert len(tree.Tree) == fixture.index


@pytest.mark.parametrize('fixture', [
    TestFixture([8, None, None], 0),
    TestFixture([16, 8, 20], 1),
    TestFixture([6, 4, 8], 2),
    TestFixture([None, None, None], 0),
    TestFixture([16, None, 20], -1),
    TestFixture([6, 4, None], -2),
])
def test_find_key(fixture):
    tree = aBST(1)
    tree.Tree = fixture.list

    assert tree.FindKeyIndex(8) == fixture.index


def test_add_key():
    tree = aBST(3)

    for key in TREE_KEYS:
        tree.AddKey(key)

    assert tree.Tree == [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, None]

    tree.AddKey(14)

    assert tree.AddKey(18) == 14
    assert tree.AddKey(14) == 6
    assert tree.AddKey(8) == 0
    assert tree.AddKey(666) == -1