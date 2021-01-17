import requests
import urllib3
import json

class APIClient:
    """
    Упрощенный клиент для работы с API
    Инициализируется базовым url на который пойдут запросы
    """

    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        print("POST request to {}".format(url))
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        url = self.base_address + path
        print("GET request to {}".format(url))
        return requests.get(url=url, params=params)

# не будет работать, потому что код мы определяем не у класса, а у объекта класса
    def status(self, path="/", meth="get"):
        url = self.base_address + path
        if meth == "get":
            #'фиксируем' объект
            res = requests.get(url)
            return str(res.status_code)

# метод возвращает текст страницы, полученной при отправке запроса по заданному url'у
    def text_dict(self, path="/"):
        url = self.base_address + path
        print(url)
        http = urllib3.PoolManager()
        resp = http.request('Get', url)
        print(resp.data)
        resp_dict = json.loads(resp.data)
        return resp_dict
