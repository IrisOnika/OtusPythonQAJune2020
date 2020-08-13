import pytest
from json import loads
from lesson4.api_client import APIClient
import os.path


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)

def api_client_base(path):
    return APIClient(base_address=path)

# def open_read(file_name):
#     with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name), 'r') as breeds:
#         res = breeds.read()
#         res_list = loads(res)
#         return res_list

def open_read(file_name):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name), 'r') as breeds:
        res = breeds.read()
        res_list = loads(res)
        return res_list





    #возможные варианты API в рамках данного ДЗ
# https://dog.ceo/dog-api/
# https://www.openbrewerydb.org/
# https://jsonplaceholder.typicode.com/
# https://dog.ceo/dog-api/



def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )
    parser.addoption(
        "--status_code",
        default="200",
        help="This is default status code"
    )
    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="method to execute"
    )

@pytest.fixture
def url(request):
    return request.config.getoption("--url")






