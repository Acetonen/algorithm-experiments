import string
from collections import namedtuple
from random import choice

import pytest
from project.hash_tables.hash_table import HashTable

SIZE = 5
STEP = 3
TestFixture = namedtuple('TestFixture', 'init_list result')


def get_random_string():
    return ''.join([choice(string.ascii_letters + string.digits) for n in range(32)])


@pytest.mark.parametrize('fixture', [
    'test string',
    't',
    '',
    get_random_string(),
])
def test_hash_fun(fixture):
    hash_table = HashTable(SIZE, STEP)

    assert hash_table.hash_fun(fixture) <= SIZE - 1


@pytest.mark.parametrize('fixture', [
    TestFixture(list(range(SIZE)), None),
    TestFixture([1, 2, 3, 4, None], 4),
    TestFixture([1, 2, 3, None, 5], 3),
    TestFixture([1, 2, None, 4, 5], 2),
    TestFixture([1, None, 3, 4, 5], 1),
    TestFixture([None, 2, 3, 4, 5], 0),
])
def test_seek_slot(fixture):
    hash_table = HashTable(SIZE, STEP)
    hash_table.slots = fixture.init_list  # noqa

    assert hash_table.seek_slot(get_random_string()) == fixture.result  # noqa


@pytest.mark.parametrize('fixture', [
    TestFixture(list(range(SIZE)), list(range(SIZE)) + [None]),
    TestFixture([1, 2, 3, 4, None], [1, 2, 3, 4, 'test', 4]),
    TestFixture([1, 2, 3, None, 5], [1, 2, 3, 'test', 5, 3]),
    TestFixture([1, 2, None, 4, 5], [1, 2, 'test', 4, 5, 2]),
    TestFixture([1, None, 3, 4, 5], [1, 'test', 3, 4, 5, 1]),
    TestFixture([None, 2, 3, 4, 5], ['test', 2, 3, 4, 5, 0]),
])
def test_put(fixture):
    hash_table = HashTable(SIZE, STEP)
    hash_table.slots = fixture.init_list  # noqa

    assert hash_table.put('test') == fixture.result.pop()  # noqa
    assert hash_table.slots == fixture.result  # noqa


@pytest.mark.parametrize('fixture', [
    TestFixture(list(range(SIZE)), None),
    TestFixture([1, 2, 3, 4, 'test'], 4),
    TestFixture([1, 2, 3, 'test', 5], 3),
    TestFixture([1, 2, 'test', 4, 5], 2),
    TestFixture([1, 'test', 3, 4, 5], 1),
    TestFixture(['test', 2, 3, 4, 5], 0),
])
def test_find(fixture):
    hash_table = HashTable(SIZE, STEP)
    hash_table.slots = fixture.init_list  # noqa

    assert hash_table.find('test') == fixture.result  # noqa
