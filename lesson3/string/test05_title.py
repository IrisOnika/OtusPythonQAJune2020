import pytest

@pytest.mark.parametrize(["s", "r"], [("фамилия имя отчество", "Фамилия Имя Отчество"),
                                      ("ЗАВТРА БУДЕТ. ЛУЧШЕ", "Завтра Будет. Лучше")])
def test_title(s, r):
    assert s.title() == r


