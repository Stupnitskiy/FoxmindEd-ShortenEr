import json

import pytest


def test_get_index_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200

    # Index page should not return view amount info without redirect
    assert b"Views amount:" not in response.data


def test_post_index_page_without_body(test_client):
    response = test_client.post('/', follow_redirects=True)
    assert response.status_code == 200

    # If there is no POST in the body, server will redirect us to the index page with flashed error
    assert b"The URL is required!" in response.data


def test_post_index_page_with_correct_url(test_client):
    data = {
        'url': 'https://google.com'
    }
    response = test_client.post('/', data=data, follow_redirects=True)
    assert response.status_code == 200
    # We should receive a link with a number of redirects
    assert b"Views amount:" in response.data
