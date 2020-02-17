from collections import namedtuple

import pytest

from queues.queue import Queue, rotate_queue, QueueFromTwoStack
from stacks.stack import Stack

TestFixture = namedtuple('TestFixture', 'init_list result')


@pytest.mark.parametrize('fixture', [
    TestFixture([1, 2, 3], [3, 1, 2]),
    TestFixture([1], [1]),
    TestFixture([], []),
])
def test_rotate_queue(fixture):
    queue = Queue()
    queue.queue = fixture.init_list  # noqa

    assert rotate_queue(queue, 5).queue == fixture.result  # noqa


def test_que_from_two_stacks_create():
    stack_one = Stack()
    stack_two = Stack()
    stack_one.stack = [1, 2, 3]
    stack_two.stack = [4]

    queue = QueueFromTwoStack(stack_one, stack_two)

    assert queue.size() == 4
    assert queue.dequeue() == 4
    assert queue.dequeue() == 1
    assert queue.size() == 2


@pytest.mark.parametrize('fixture', [
    TestFixture([1, 2, 3], [3, 1, 2]),
    TestFixture([1], [1]),
    TestFixture([], []),
])
def test_rotate_two_stack_queue(fixture):
    stack_one = Stack()
    stack_two = Stack()
    stack_one.stack = fixture.init_list  # noqa
    stack_two.stack = list()

    queue = QueueFromTwoStack(stack_one, stack_two)
    rotated_queue = rotate_queue(queue, 5)

    assert rotated_queue.size() == len(fixture.result)  # noqa