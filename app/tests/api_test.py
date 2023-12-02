import pytest

from copy import deepcopy
from fastapi.testclient import TestClient

from app.tests.api_testdata import testdata


access_token: str = ''


@pytest.mark.parametrize('test_description', testdata)
def test_endpoint(
        test_description,
        client: TestClient,
):
    global access_token

    print(f'\n'
          f' {test_description["test"]}')

    kw = deepcopy(test_description['request'])
    kw['url'] = test_description['endpoint_url']

    if test_description['auth']:
        kw['headers']['Authorization'] = f'Bearer {access_token}'

    if test_description['method'] == 'GET':
        response = client.get(**kw)
    elif test_description['method'] == 'POST':
        response = client.post(**kw)
    else:
        pytest.fail('incorrect description of the test')

    if test_description['save_token']:
        access_token = response.json().get('access_token', None)
        assert access_token

    if test_description['response_status_code']:
        assert response.status_code == test_description['response_status_code']

    if test_description['response_json']:
        assert response.json() == test_description['response_json']
