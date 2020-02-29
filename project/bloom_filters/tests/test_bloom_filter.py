import pytest
from collections import deque, namedtuple

from project.bloom_filters.bloom_filter import BloomFilter

TEST_LEN = 32

TestFixture = namedtuple('TestFixture', 'string result')


def get_tests_strings():
    items = deque('0123456789')

    test_strings = list()
    for _ in range(10):
        items.rotate(1)
        test_strings.append(''.join(items))

    return test_strings


TESTS_STRINGS_LIST = get_tests_strings()


@pytest.mark.parametrize('fixture', [
    TestFixture('013', 4),
    TestFixture('023', 21),
])
def test_hash1(fixture):
    bloom_filter = BloomFilter(32)
    assert bloom_filter.hash1(fixture.string) == fixture.result, "hash1() function don't work"  # noqa


@pytest.mark.parametrize('fixture', [
    TestFixture('013', 18),
    TestFixture('023', 17),
])
def test_hash2(fixture):
    bloom_filter = BloomFilter(32)
    assert bloom_filter.hash2(fixture.string) == fixture.result, "hash2() function don't work"  # noqa


@pytest.mark.parametrize('fixture', [
    TestFixture('013', (4, 18)),
    TestFixture('023', (21, 17)),
])
def test_add(fixture):
    bloom_filter = BloomFilter(32)
    bloom_filter.add(fixture.string)  # noqa

    for index, item in enumerate(bloom_filter.bit_array):
        if index in fixture.result:  # noqa
            assert item == 1
        else:
            assert item == 0


@pytest.mark.parametrize('fixture', TESTS_STRINGS_LIST)
def test_is_value(fixture):
    bloom_filter = BloomFilter(32)
    for string in fixture:
        bloom_filter.add(string)  # noqa

    for string in fixture:
        assert bloom_filter.is_value(string) is True
    #
    # for index, item in enumerate(bloom_filter.bit_array):
    #     if index in fixture.result:  # noqa
    #         assert item == 1
    #     else:
    #         assert item == 0
