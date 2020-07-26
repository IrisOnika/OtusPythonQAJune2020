import pytest

skip = 'skip'

# def if_you_need_an_error_message(error_type, arg1, arg2):
#     if error_type == 'no element in list':
#         return f'В списке {arg1} нет элемента {arg2}'
#
#     else:
#         pass


def skip_list_index_args(l: list, x, start, end):
    try:
        if end == skip:
            if start == skip:
                ind = l.index(x)
            else:
                ind = l.index(x, start)
        else:
            ind = l.index(x, start, end)
    except ValueError:
        ind = f'В списке {l} нет элемента {x}'
    return ind

@pytest.mark.parametrize("test_input", [([1, 1, 4, 12, 3, 4], 1, 0, skip, skip), ([1, 1, 4, 12, 3, 4], 4, 5, 3, skip),  ([1, 1, 4, 12, 3, 4], 4, 5, 2, 4), ([1, 1, 4, 12, 3, 4], 7, 'exception', skip, skip)])
def test_index(test_input):
    l: list = test_input[0]
    i = skip_list_index_args(l, test_input[1], test_input[3], test_input[4])
    i == f'В списке {l} нет элемента {test_input[1]}' if test_input[2] =='exception' else test_input[2]
