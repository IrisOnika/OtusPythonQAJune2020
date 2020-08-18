from lesson4.pivo.breweries_func import *
import re
import cerberus

@pytest.mark.parametrize('number', ['/1', '/777'])
def test_check_breeds_schema(number):
    ap = brewer_api()
    res = ap.text_dict(path=number)
    print(res)
    schema = open_read('pivo/schema_pivo.json')
    v = cerberus.Validator()
    assert v.validate(res, schema)

@pytest.mark.parametrize(('page_num', 'count'),
                         [
                             # кейсы для номера вызываемой страницы
                             ('0', 20),
                             ('1', 20),
                             ('401', 20),
                             # для текущего состояния базы (текущего кол-ва пивоварен)
                             ('402', 12),
                             ('403', 0)
                            ])
def test_check_breeds_page_num(page_num, count):
    ap = brewer_api()
    res = ap.text_dict(path=f'?page={page_num}')
    res_count = 0
    for item in res:
        res_count += 1
    assert res_count == count

@pytest.mark.parametrize(('per_page', 'count'), [('0', 0),
                                      ('1', 1),
                                      ('50', 50),
                                      ('51', 50)])
def test_check_breeds_per_page(per_page, count):
    ap = brewer_api()
    res = ap.text_dict(path=f'?per_page={per_page}')
    res_count = 0
    for item in res:
        res_count += 1
    assert res_count == count

@pytest.mark.parametrize('search', ['California', 'Russia', 'khjkhjkh'])
def test_check_breeds_per_page(search):
    ap = brewer_api()
    res = ap.text_dict(path=f'{search_query}{search}')
    print(f'res={res}')
    for item in res:
        print(item.get("id"))
        count=0
        for i in list(item.keys()):
            if str(item.get(i)).find(search) > -1:
                print(i)
                count += 1
        if res != []:
            assert count > 0
        else:
            assert count == 0






