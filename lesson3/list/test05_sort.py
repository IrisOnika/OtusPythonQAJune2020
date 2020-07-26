import pytest

skip = 'skip'

address = ['Симферопольская, 18',
           'Мичурина, 39',
           'Ленина, 54',
           'Зелёновская, 26'
           ]
# expected data
address_sort_by_number =['Симферопольская, 18',
                         'Зелёновская, 26',
                         'Мичурина, 39',
                         'Ленина, 54'
                         ]
address_sort_by_street =['Зелёновская, 26',
                         'Ленина, 54',
                         'Мичурина, 39',
                         'Симферопольская, 18'
                         ]
address_sort_by_street_desc = ['Симферопольская, 18',
                               'Мичурина, 39',
                               'Ленина, 54',
                               'Зелёновская, 26'
                               ]

def sort_by_building_number(item):
    return item[item.index(',') + 2]


def sort_args(l:list, k=None, r=False):
    if k == skip:
        l.sort()
        return l
    elif k == 'reverse':
        l.sort(reverse=True)
        return l
    else:
        l.sort(key = k, reverse = r)
        return l

@pytest.mark.parametrize("test_input", [(address, sort_by_building_number, address_sort_by_number),
                                        (address, skip, address_sort_by_street),
                                        (address, 'reverse', address_sort_by_street_desc)])
def test_sort(test_input):
    l: list = test_input[0]
    lsorted = sort_args(l, test_input[1])
    assert lsorted ==  test_input[2]


