from lesson4.pivo.breweries_func import *
import re
import cerberus

@pytest.mark.parametrize('number', ['/1', '/777'])
def test_check_breeds_list(number):
    ap = brewer_api()
    res = ap.text_dict(path=number)
    print(res)
    schema = open_read('pivo/schema_pivo.json')
    v = cerberus.Validator()
    assert v.validate(res, schema)



