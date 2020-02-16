import pytest
from stacks.stack import ReverseStack, Stack, validate_parentheses, postfix_count
from collections import namedtuple

TestFixture = namedtuple('TestFixture', 'init_list result')


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture([2, 1, 3], [666, 2, 1, 3]),
    TestFixture([2], [666, 2]),
    TestFixture([], [666]),
])
def test_push_reverse(fixture):
    stack = ReverseStack()
    stack.stack = fixture.init_list

    stack.push(666)

    assert stack.stack == fixture.result


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture([666, 2, 1, 3], [2, 1, 3]),
    TestFixture([666, 2], [2]),
    TestFixture([666], []),
])
def test_pop_reverse(fixture):
    stack = ReverseStack()
    stack.stack = fixture.init_list

    poped_value = stack.pop()

    assert poped_value == 666
    assert stack.stack == fixture.result


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture([2, 1, 3], [2, 1, 3, 666]),
    TestFixture([2], [2, 666]),
    TestFixture([], [666]),
])
def test_push(fixture):
    stack = Stack()
    stack.stack = fixture.init_list

    stack.push(666)

    assert stack.stack == fixture.result


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture([2, 1, 3, 666], [2, 1, 3]),
    TestFixture([2, 666], [2]),
    TestFixture([666], []),
])
def test_pop(fixture):
    stack = Stack()
    stack.stack = fixture.init_list

    poped_value = stack.pop()

    assert poped_value == 666
    assert stack.stack == fixture.result


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture([], []),
])
def test_empty_pop(fixture):
    stack = Stack()
    stack.stack = fixture.init_list
    reverse_stack = ReverseStack()
    reverse_stack.stack = fixture.init_list

    poped_stack_value = stack.pop()
    poped_reverse_stack_value = reverse_stack.pop()

    assert poped_stack_value is None
    assert poped_reverse_stack_value is None
    assert stack.stack == fixture.result
    assert reverse_stack.stack == fixture.result


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture('(()((())()))', 'Balanced string'),
    TestFixture('(()()(()))', 'Balanced string'),
    TestFixture('())(', 'Not balanced string'),
    TestFixture('))((', 'Not balanced string'),
    TestFixture('((())', 'Not balanced string'),
])
def test_validate_parentheses(fixture):
    result = validate_parentheses(fixture.init_list)

    assert result == fixture.result


# noinspection PyUnresolvedReferences
@pytest.mark.parametrize('fixture', [
    TestFixture('8 2 + 5 * 9 + =', 59),
    TestFixture('1 2 + 3 * =', 9),
])
def test_postfix_count(fixture):
    result = postfix_count(fixture.init_list)

    assert result == fixture.result
