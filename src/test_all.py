import pytest
import requests


class TestOne:

    def test_one(self):
        resp = requests.get(url="https://www.python.org/")
        print(resp.status_code)
        assert resp.status_code == 200
        assert True
