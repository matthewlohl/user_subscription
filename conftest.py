import pytest
import app
from app import users

@pytest.fixture
def test_users_data():
  return {
    'id': 1,
    'name': 'Stefan',
    'email': 'something@example.com'
  }

@pytest.fixture()
def users_test_list():
  return [
    {'id': 1, 'name':'Stefan', 'email':'something@example.com'},
    {'id':2, 'name':'Camila', 'email':'something1@example.com'},
    {'id':3, 'name':'Matt', 'email':'something2@example.com'}
]
  # monkeypatch.setattr(users, 'users', test_users)
  # api = app.app.test_client()
  # return api
