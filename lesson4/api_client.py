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

    def status(self, path="/", meth="get"):
        if meth == "get":
            return self.get(path).status_code


    def text_dict(self, path="/"):
        url = self.base_address + path
        print(url)
        http = urllib3.PoolManager()
        resp = http.request('Get', url)
        print(resp.data)
        resp_dict = json.loads(resp.data)
        return resp_dict
