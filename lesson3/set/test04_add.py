import pytest

@pytest.mark.parametrize("test_input", [({i for i in range(0, 11, 3)}, 4, {0, 3, 4, 6, 9}),
                                        (set('миллион'), 'ы', {'и', 'л', 'м', 'о', 'ы', 'н'}),
                                        ({i ** 2 for i in range (8)}, 25, {i ** 2 for i in range (8)})])
def test_add(test_input):
    s: set = test_input[0]
    s.add(test_input[1])
    assert s == test_input[2]


