import pytest

@pytest.mark.parametrize(['s', 'r'], [('буковки', False),
                                      ('65465465456', True)])
def test_isdigit(s, r):
    assert s.isdigit() == r


