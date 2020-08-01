import pytest

@pytest.mark.parametrize(['s', 'r'], [({a: a ** 2 for a in range(7)}, [0, 1, 2, 3, 4, 5, 6]),
                                     (dict.fromkeys(['a', 'b'], 100), ['a', 'b'])])
def test_keys(s, r):
    print(s.keys())
    assert list(s.keys()) == r