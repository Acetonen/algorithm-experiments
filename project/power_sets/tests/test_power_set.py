import string
from collections import namedtuple
from random import choice

import pytest

from project.power_sets.power_set import PowerSet

TestFixture = namedtuple('TestFixture', 'init_list result')
TwoPowerSetsFixture = namedtuple('TwoPowerSetsFixture', 'first_set second_set result')


def get_random_string():
    return ''.join([choice(string.ascii_letters + string.digits) for n in range(32)])


def create_power_Set_from_list(init_list):
    power_set = PowerSet()
    for item in init_list:
        power_set.put(item)

    return power_set


@pytest.mark.parametrize('fixture', [
    TestFixture([None, 1, 2, None], 2),
    TestFixture([], 0)
])
def test_size(fixture):
    power_set = PowerSet()
    power_set.slots = fixture.init_list  # noqa

    assert power_set.size() == fixture.result  # noqa


@pytest.mark.parametrize('fixture', [
    TestFixture([1, 2, 3, 4, None], [1, 2, 3, 4, 'test', 4]),
    TestFixture([1, 2, 3, None, 5], [1, 2, 3, 'test', 5, 3]),
    TestFixture([1, 2, None, 4, 5], [1, 2, 'test', 4, 5, 2]),
    TestFixture([1, None, 3, 4, 5], [1, 'test', 3, 4, 5, 1]),
    TestFixture([None, 2, 3, 4, 5], ['test', 2, 3, 4, 5, 0]),
    TestFixture([1, 2, 3, 'test', 5], [1, 2, 3, 'test', 5, 3]),
    TestFixture([1, 2, 'test', 4, 5], [1, 2, 'test', 4, 5, 2]),
    TestFixture([1, 'test', 3, 4, 5], [1, 'test', 3, 4, 5, 1]),
    TestFixture(['test', 2, 3, 4, 5], ['test', 2, 3, 4, 5, 0]),
])
def test_put(fixture):
    power_set = PowerSet()
    power_set.slots = fixture.init_list  # noqa
    power_set.table_size = 5
    power_set.step = 2

    assert power_set.put('test') == fixture.result.pop()  # noqa
    assert power_set.slots == fixture.result  # noqa


@pytest.mark.parametrize('fixture', [
    'test string',
    't',
    '',
    get_random_string(),
])
def test_put_twice(fixture):
    power_set = PowerSet()

    power_set.put(fixture)
    power_set.put(fixture)

    assert power_set.size() == 1


@pytest.mark.parametrize('fixture', [
    'test string',
    't',
    '',
    get_random_string(),
])
def test_get(fixture):
    power_set = PowerSet()
    power_set.put(fixture)

    assert power_set.get(fixture) is True


@pytest.mark.parametrize('fixture', [
    'test string',
    't',
    '',
    get_random_string(),
])
def test_remove(fixture):
    power_set = PowerSet()
    power_set.put(fixture)

    assert power_set.size() == 1
    assert power_set.get(fixture) is True

    power_set.remove(fixture)

    assert power_set.size() == 0
    assert power_set.get(fixture) is False


@pytest.mark.parametrize('fixture', [
    TwoPowerSetsFixture([], [], []),
    TwoPowerSetsFixture(['1', '2'], ['2', '3'], ['2']),
    TwoPowerSetsFixture(['1', '2'], ['3', '4'], []),
    TwoPowerSetsFixture(list(range(1, 1000)), list(range(999, 2000)), [999]),
])
def test_intersection(fixture):
    power_set_one = create_power_Set_from_list(fixture.first_set)  # noqa
    power_set_two = create_power_Set_from_list(fixture.second_set)  # noqa

    result_set = power_set_one.intersection(power_set_two)

    assert result_set.slots == create_power_Set_from_list(fixture.result).slots  # noqa


@pytest.mark.parametrize('fixture', [
    TwoPowerSetsFixture([], [], []),
    TwoPowerSetsFixture([1, '2'], ['2', '3'], [1, '2', '3']),
    TwoPowerSetsFixture(['1', '2'], ['3', '4'], ['1', '2', '3', '4']),
    TwoPowerSetsFixture(list(range(1, 1000)), list(range(999, 2000)), list(range(1, 2000))),
])
def test_union(fixture):
    power_set_one = create_power_Set_from_list(fixture.first_set)  # noqa
    power_set_two = create_power_Set_from_list(fixture.second_set)  # noqa

    result_set = power_set_one.union(power_set_two)

    assert result_set.slots == create_power_Set_from_list(fixture.result).slots  # noqa


@pytest.mark.parametrize('fixture', [
    TwoPowerSetsFixture([], [], []),
    TwoPowerSetsFixture([1, '2'], ['2', '3'], [1]),
    TwoPowerSetsFixture(['1', '2'], ['3', '4'], ['1', '2']),
    TwoPowerSetsFixture(list(range(1, 1000)), list(range(999, 2000)), list(range(1, 999))),
])
def test_difference(fixture):
    power_set_one = create_power_Set_from_list(fixture.first_set)  # noqa
    power_set_two = create_power_Set_from_list(fixture.second_set)  # noqa

    result_set = power_set_one.difference(power_set_two)

    assert result_set.slots == create_power_Set_from_list(fixture.result).slots  # noqa


@pytest.mark.parametrize('fixture', [
    TwoPowerSetsFixture([], [], True),
    TwoPowerSetsFixture([1, '2', '3'], ['2', '3'], True),
    TwoPowerSetsFixture(['1', '2'], ['3', '4'], False),
    TwoPowerSetsFixture(list(range(1, 1000)), list(range(500, 666)), True),
])
def test_issubset(fixture):
    power_set_one = create_power_Set_from_list(fixture.first_set)  # noqa
    power_set_two = create_power_Set_from_list(fixture.second_set)  # noqa

    assert power_set_one.issubset(power_set_two) == fixture.result  # noqa
