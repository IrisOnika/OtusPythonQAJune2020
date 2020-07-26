import pytest

@pytest.mark.parametrize("test_input", [([0, 1, 2, 3, 4],[0, 1, 2, 3, 4]), ([8, 9, 0],[8, 9, 0])])
def test_append(test_input):
    l: list = test_input[0]
    print(l)
    l.append('x')
    print(l)
    for i1, i2 in zip(l, test_input[1]):
        i1 == 'x' if i2 is None else i2



