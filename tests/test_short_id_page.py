import re
from uuid import uuid4

import pytest


@pytest.fixture()
def unique_url():
    random_uuid = uuid4()
    return f"https://{random_uuid}"


@pytest.fixture()
def created_short_id(test_client, unique_url):
    data = {
        "url": unique_url
    }
    response = test_client.post('/', data=data, follow_redirects=True)
    # I'm lazy to install BeautifulSoap :)
    regex_pattern = re.compile(rb'<a href="(.*)" target', flags=re.MULTILINE)
    short_id = regex_pattern.search(response.data).group(1)

    return short_id.decode("utf-8")


def test_views_amount_counter(test_client, unique_url, created_short_id):
    for _ in range(15):
        test_client.get(f'/{created_short_id}')

    data = {"url": unique_url}
    response = test_client.post('/', data=data, follow_redirects=True)
    assert b'Views amount: 15' in response.data


def test_invalid_short_link(test_client):
    response = test_client.get('/invalid', follow_redirects=True)
    assert response.status_code == 200
    assert b'Invalid URL' in response.data
