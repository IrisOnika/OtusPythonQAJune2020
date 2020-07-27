import pytest

@pytest.mark.parametrize("test_input", [({'a', 'b'}, {1, 2}, {'a', 'b', 1, 2}),
                                        ({1, 2, 4}, {3, 4, 5}, {i for i in range(1, 6)})])
def test_update(test_input):
    s: set = test_input[0]
    s.update(test_input[1])
    assert s == test_input[2]


