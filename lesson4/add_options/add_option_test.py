
from lesson4.conftest import api_client
import pytest


@pytest.fixture
def site(request):
    ap = api_client(request)
    return ap

def test_check_url(site, url, code):
    print(site.status)
    assert site.status() == code
#    assert str(site.get().status_code) == code
