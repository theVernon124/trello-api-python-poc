import requests
import pytest

from commands.Utils import Utils
from commands.TestSteps import TestSteps


class TestLogin(object):
    utils = None
    steps = None
    config_data = None
    login_data = None

    @classmethod
    def setup_class(cls):
        cls.utils = Utils()
        cls.steps = TestSteps()
        cls.config_data = cls.utils.get_config_data()
        cls.login_data = cls.utils.get_test_data("login")

    @pytest.mark.smoke
    def test_valid_login(self):
        s = requests.Session()
        dsc = s.get(self.config_data["url_home"]).cookies["dsc"]
        req = self.steps.perform_auth(self.login_data["input_data"]["login_method"],
                                      self.login_data["input_data"]["email"], self.login_data["input_data"]["password"])
        code = req.json()["code"]
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "authentication": code,
            "dsc": dsc
        }
        req = s.post(self.config_data["url_session"], headers=headers, data=data)
        assert req.status_code == 204

    @pytest.mark.negative
    def test_invalid_auth_method(self):
        s = requests.Session()
        self.steps.perform_auth()
        data = {
            "method": self.login_data["input_data"]["invalid_login_method"],
            "factors[user]": self.login_data["input_data"]["email"],
            "factors[password]": self.login_data["input_data"]["password"]
        }
        req = s.post()
