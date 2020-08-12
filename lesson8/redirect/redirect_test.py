import pytest
import requests

host = 'http://httpbin.org/'

def getRedirects(host, redirectTimes=1, allowRedirects=True):
    url = host + 'redirect/' + str(redirectTimes)
    response = requests.get(url, allow_redirects=allowRedirects)
    return response

@pytest.mark.parametrize(["h", "r_times", "exp_resp"], [(host, '1', '302')])
def test_redirect(h, r_times, exp_resp):
    resp = getRedirects(h, redirectTimes=r_times)
    assert resp == f'<Response [{exp_resp}]>'