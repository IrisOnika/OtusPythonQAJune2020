from lesson4.conftest import open_read
from lesson4.conftest import api_client_base
from lesson4.dogs.breed_list_func import *
import re

# with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'breеd_list.json'), 'r') as breeds:
#     breeds_all = breeds.read()
#     breeds_list = loads(breeds_all)


# @pytest.mark.parametrize("input1, input2 ", [(1, 1)])
def test_check_breeds_list():
    ap = dogs_api()
    res = ap.text_dict(path=list_all)
    breed_list_dict = res.get("message")
    # breed_list = list(breed_list_dict.keys())
    breeds_list = open_read('dogs/breеd_list.json')
    assert breed_list_dict == breeds_list

def test_by_breed_random():
    ap = dogs_api()
    res = ap.text_dict(path=random1)
    rand1 = res.get("message")
    # Проверяем, что в message одна строка в виде "https://images.dog.ceo/breeds/{название_породы}/{номер_картинки}.jpg"
    assert re.match(r"^" + random1_result + r"\w+/\w+.jpg$", rand1)








# @pytest.mark.parametrize(["h", "r_times", "exp_resp", "allow_redir"], [(host, '2', '302', True)])
# @pytest.Function
# def test_redirect(host, r_times, exp_resp, allow_redir):
# def test_redirect(host):








url = host + 'breeds/list/all'
# http = urllib3.PoolManager()
#
# resp = http.request('Get', url)
# # print(resp.data)
# # print(type(resp.data))
#
# resp_dict = json.loads(resp.data)
# # print(resp_dict)
# # print(type(resp_dict))
# print(resp_dict.get('status'))



# response = requests.get(url)


# headers = response.headers
# t = response.data
# with open('data.json', 'w', encoding='utf-8') as fh: #открываем файл на запись
#     fh.write(json.dumps(t, ensure_ascii=False)) #преобразовываем словарь data в unicode-строку и записываем в файл
# with open('data.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
#     data = json.load(fh)

# print(f'Происходит: "{response}"')
# print(headers)
# print(type(data))
# print(t.keys())

    # print(f'Ожидается: "<Response [{exp_resp}]">')
    # print(range(int(r_times)))
    # print(list(range(int(r_times))))
    #
    # for i in list(range(int(r_times))):
    #     assert str(response) == f'<Response [{exp_resp}]>'