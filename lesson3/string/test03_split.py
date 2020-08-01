import pytest

@pytest.mark.parametrize(["s", "sp", "r"], [('белый-белый', '-', ['белый', 'белый']),
                                            ('99/11', '/', ['99', '11'])])
def test_split(s, sp, r):
    assert r == s.split(sp)


