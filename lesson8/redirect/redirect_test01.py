import pytest
import requests

host = 'http://httpbin.org/'


@pytest.mark.parametrize(["h", "r_times", "exp_resp", "allow_redir"], [(host, '2', '302', True)])
def test_redirect(h, r_times, exp_resp, allow_redir):
    url = host + 'redirect/' + str(r_times)
    response = requests.get(url, allow_redirects=allow_redir)
    print(f'Происходит: "{response}"')

    print(f'Ожидается: "<Response [{exp_resp}]">')
    print(range(int(r_times)))
    print(list(range(int(r_times))))

    for i in list(range(int(r_times))):
        assert str(response) == f'<Response [{exp_resp}]>'