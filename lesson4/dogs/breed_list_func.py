from lesson4.conftest import open_read
from lesson4.conftest import api_client_base
import pytest

host = 'https://dog.ceo/api/breeds'
list_all = '/list/all'
random1 = '/image/random'
random1_result = 'https://images.dog.ceo/breeds/'


def dogs_api():
    ap = api_client_base(host)
    return ap

