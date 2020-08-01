import pytest

@pytest.mark.parametrize(['s', 'new_s', 'r'], [({a: a ** 2 for a in range(7)}, {a: a ** 3 for a in range(4)}, {0:0, 1:1, 2:8, 3:27, 4:16, 5:25, 6:36}),
                                               (dict.fromkeys(['a', 'b'], 100), {'a': 400, 'c':250}, {'a': 400, 'b':100, 'c':250})])
def test_update(s, new_s, r):
    s.update(new_s)
    assert s == r
