# import json

# class TestAPICase():
#     def test_welcome(self, api):
#       res = api.get('/')
#       assert res.status == '200'
#       assert res.json['message'] == 'Welcome to our API!'
import os
import tempfile

import pytest

from app import app


@pytest.fixture
def client():
    app.config.update({'TESTING': True})

    with app.test_client() as client:
        yield client

def test_welcome_page(client):

    res = client.get('/')
    assert b'Welcome to our API!' in res.data
    assert res.status =='200 OK'
    assert res.json['message'] == 'Welcome to our API!'

def test_get_users(client):

    res = client.get('/users')
    assert res.status == '200 OK'
    assert res.json[0] == {'email': 'something@example.com', 'id': 1, 'name': 'Stefan'}
    assert len(res.json) == 3

def test_get_user_by_id(client):
        res = client.get('/users/2')
        assert res.status == '200 OK'
        assert res.json['name'] == 'Cami'
