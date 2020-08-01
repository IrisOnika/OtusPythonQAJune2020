import pytest

@pytest.mark.parametrize(["s", "l"], [(';lkj;lkjl;kj', 12),
                                        ('', 0)])
def test_len(s, l):
    assert l == len(s)


