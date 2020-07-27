import pytest

@pytest.mark.parametrize("test_input", [({'a', 'b'}, {1, 2}, set()),
                                        ({1, 2, 4}, {3, 4, 5}, {4})])
def test_intersection(test_input):
    s = test_input[0]&test_input[1]
    assert s == test_input[2]


