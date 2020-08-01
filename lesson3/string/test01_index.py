import pytest

skip = 'skip'

week = 'понедельник вторник среда четверг пятница суббота воскресенье'
weeks = 'понедельник вторник среда четверг пятница понедельник вторник'

def index_substr(s, sub, st, e):
     try:
         if st == skip:
             if e == skip:
                 return s.index(sub)
             else:
                 return s.index(sub, end = e)
         else:
             if e == skip:
                 return s.index(sub, start=st)
             else:
                 return s.index(sub, start=st, end=e)
     except ValueError:
         return f'в строке {s} нет подстроки {sub}'



@pytest.mark.parametrize(["s", "sub", "st", "e", "ind"], [(weeks, 'понедельник', skip, skip, 0),
                                                          (week, 'вторник', skip, 49, 11),
                                                          (weeks, 'понедельник', 10, skip, 50),
                                                          (week, 'четверг', 10, 50, 26),
                                                          (weeks, 'суббота', skip, skip, 'no index')])
def test_index(s, sub, st, e, ind):
    index_substr(s, sub, st, e) == f'в строке {s} нет подстроки {sub}' if ind == 'no index' else ind

#
