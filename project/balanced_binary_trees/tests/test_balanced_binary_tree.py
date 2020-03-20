from collections import namedtuple

from project.balanced_binary_trees.balanced_binary_tree import GenerateBBSTArray

TestFixture = namedtuple('TestFixture', 'list index')

RESULT = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]


def test_generate_binary_array():
    assert GenerateBBSTArray(RESULT) == RESULT
