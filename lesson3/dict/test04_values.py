import pytest

@pytest.mark.parametrize(['s', 'r'], [({a: a ** 2 for a in range(7)}, [0, 1, 4, 9, 16, 25, 36]),
                                     (dict.fromkeys(['a', 'b'], 100), [100, 100])])
def test_values(s, r):
    print(s.values())
    assert list(s.values()) == r