from lesson4.conftest import open_read
from lesson4.conftest import api_client_base
import pytest

host = 'https://dog.ceo/api/breeds'
host1 = 'https://dog.ceo/api/breed'
list_all = '/list/all'
random1 = '/image/random'
random1_result = 'https://images.dog.ceo/breeds/'


def dogs_api(path=host):
    ap = api_client_base(path )
    return ap

