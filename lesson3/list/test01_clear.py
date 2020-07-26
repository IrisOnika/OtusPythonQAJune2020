import pytest

@pytest.mark.parametrize("test_input", [[1, 2, 3], ['a', 'b', 'c'], []])
def test_clear(test_input):
    test_input.clear()
    assert test_input == []


