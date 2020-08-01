import pytest

@pytest.mark.parametrize(['s', 'r'], [({a: a ** 2 for a in range(7)}, [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]),
                                     (dict.fromkeys(['a', 'b'], 100), [('a', 100), ('b', 100)])])
def test_items(s, r):
    assert list(s.items()) == r