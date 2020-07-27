import pytest

@pytest.mark.parametrize("test_input", [({i for i in range(0, 11, 3)}, 4, {i for i in range(0, 11, 3)}),
                                        (set('миллион'), 'н', {'и', 'л', 'м', 'о'}),
                                        ({i ** 2 for i in range (8)}, 25, {0, 1, 4, 9, 16, 36, 49})])
def test_discard(test_input):
    s: set = test_input[0]
    s.discard(test_input[1])
    assert s == test_input[2]


