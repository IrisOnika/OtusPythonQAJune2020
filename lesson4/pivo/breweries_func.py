from lesson4.conftest import open_read
from lesson4.conftest import api_client_base
import pytest

host = 'https://api.openbrewerydb.org/breweries'
host1 = 'https://api.openbrewerydb.org/breweries?'
search_query = '/search?query='

def brewer_api(path=host):
    ap = api_client_base(path)
    return ap

