import requests

from commands.Utils import Utils
from commands.TestSteps import TestSteps


class TestLists(object):
    utils = None
    steps = None
    config_data = None
    list_data = None
    board_id = None

    @classmethod
    def setup_class(cls):
        cls.utils = Utils()
        cls.steps = TestSteps()
        cls.config_data = cls.utils.get_config_data()
        cls.list_data = cls.utils.get_test_data("lists")
        cls.board_id = cls.steps.create_board(cls.list_data["input_data"]["board_name"], cls.config_data["key"],
                                              cls.config_data["token"]).json()["id"]

    @classmethod
    def teardown_class(cls):
        cls.steps.delete_board(cls.board_id)

    def test_valid_create_list(self):
        req = self.steps.create_list(self.list_data["input_data"]["list_name"], self.board_id, self.config_data["key"],
                                     self.config_data["token"])
        res = req.json()
        assert req.status_code == 200
        assert res["name"] == self.list_data["input_data"]["list_name"]
        assert res["idBoard"] == self.board_id
