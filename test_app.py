import json

class TestAPICase():
    def test_welcome(self, api):
      res = api.get('/')
      assert res.status == '200'
      assert res.json['message'] == 'Welcome to our API!'
