import string
from collections import namedtuple
from random import choice

import pytest

from project.native_dictionaries.native_dictionary import NativeDictionary

SIZE = 5
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
    hash_table = NativeDictionary(SIZE)

    assert hash_table.hash_fun(fixture) < SIZE


@pytest.mark.parametrize('fixture', [
    TestFixture([1, None, 3, 6, 5], True),
    TestFixture([1, 2, 3, 4, 5], False),
])
def test_is_key(fixture):
    native_dictionary = NativeDictionary(SIZE)
    native_dictionary.slots = fixture.init_list  # noqa

    assert native_dictionary.is_key(6) == fixture.result  # noqa


@pytest.mark.parametrize('fixture', [
    TestFixture([1, None, 3, 6, 5], [None, 'test', None, None, None]),
    TestFixture([1, 2, 3, None, 5], [None, None, None, 'test', None]),
    TestFixture([1, 2, 3, 4, 'test'], [None, None, None, None, 'test']),
])
def test_put(fixture):
    native_dictionary = NativeDictionary(SIZE)
    native_dictionary.slots = fixture.init_list  # noqa
    native_dictionary.put('test', 'test')

    assert native_dictionary.values == fixture.result  # noqa


@pytest.mark.parametrize('fixture', [
    TestFixture([1, 'test', 3, 6, 5], 2),
    TestFixture([1, 2, 3, 4, 5], None),
])
def test_get(fixture):
    native_dictionary = NativeDictionary(SIZE)
    native_dictionary.slots = fixture.init_list  # noqa
    native_dictionary.values = [1, 2, 3, 4, 5]  # noqa
    value = native_dictionary.get('test')

    assert value == fixture.result  # noqa