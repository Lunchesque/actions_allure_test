import pytest
import requests
import allure
import logging


@allure.severity(allure.severity_level.CRITICAL)
class TestOne:

    logger = logging.getLogger()

    @pytest.mark.smoke
    def test_one(self):
        with allure.step("Get python url"):
            resp = requests.get(url="https://www.python.org/")
            self.logger.debug(f"Get status code is {resp.status_code}")
            assert resp.status_code == 201
            

    @pytest.mark.smoke
    def test_two(self):
        resp = requests.get(url="https://www.python.org/")
        self.logger.debug(f"Get status code is {resp.status_code}")
        assert resp.status_code == 200
