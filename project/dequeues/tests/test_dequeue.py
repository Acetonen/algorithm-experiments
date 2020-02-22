from collections import namedtuple

import pytest

from project.dequeues.dequeue import Deque, rotate_queue_left, rotate_queue_right, check_palindrome

TestFixture = namedtuple('TestFixture', 'init_list result')


@pytest.mark.parametrize('fixture', [
    TestFixture([1, 2, 3], [2, 3, 1]),
    TestFixture([1], [1]),
    TestFixture([], []),
])
def test_rotate_queue_left(fixture):
    queue = Deque()
    queue.queue = fixture.init_list  # noqa

    assert rotate_queue_left(queue, 5).queue == fixture.result  # noqa


@pytest.mark.parametrize('fixture', [
    TestFixture([1, 2, 3], [3, 1, 2]),
    TestFixture([1], [1]),
    TestFixture([], []),
])
def test_rotate_queue_right(fixture):
    queue = Deque()
    queue.queue = fixture.init_list  # noqa

    assert rotate_queue_right(queue, 5).queue == fixture.result  # noqa


@pytest.mark.parametrize('fixture', [
    TestFixture('asddsa', True),
    TestFixture('asdtdsa', True),
    TestFixture('asdtsa', False),
    TestFixture('a', True),
    TestFixture('', True),
])
def test_check_palindrome(fixture):
    assert check_palindrome(fixture.init_list) == fixture.result  # noqa
