import pytest


@pytest.mark.parametrize("test_input", [([1, 4], 5, [1, 4, 'x']), ([0, 1, 2, 3, 4], 2, [0, 1, 'x', 2, 3, 4]), ([8, 9, 0], 0,['x', 8, 9, 0])])
def test_insert(test_input):
    l: list = test_input[0]
    l.insert(test_input[1], 'x')
    for i1, i2 in zip(l, test_input[2]):
        assert i1 == i2