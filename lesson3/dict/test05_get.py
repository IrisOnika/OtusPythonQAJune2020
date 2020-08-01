import pytest

skip = 'skip'

def dict_get(s, k, d):
    if d == skip:
        v = s.get(k)
    else:
        v = s.get(k, d)
    return v

@pytest.mark.parametrize(['s', 'k', 'd', 'r'], [({a: a ** 2 for a in range(7)}, 4, 7, 16),
                                                ({a: a ** 2 for a in range(7)}, 7, 7, 7),
                                                (dict.fromkeys(['a', 'b'], 100), 'c', skip, None)])
def test_get(s, k, d, r):
    v = dict_get(s, k, d)
    assert v == r