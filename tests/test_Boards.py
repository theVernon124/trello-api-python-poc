import requests

from commands.Utils import Utils
from commands.TestSteps import TestSteps


class TestBoards(object):
    utils = None
    steps = None
    config_data = None
    board_data = None
    board_id = None

    @classmethod
    def setup_class(cls):
        cls.utils = Utils()
        cls.steps = TestSteps()
        cls.config_data = cls.utils.get_config_data()
        cls.board_data = cls.utils.get_test_data("boards")

    @classmethod
    def teardown_class(cls):
        cls.steps.delete_board(cls.board_id)

    def test_valid_create_board(self):
        req = self.steps.create_board(self.board_data["input_data"]["board_name"], self.config_data["key"],
                                      self.config_data["token"])
        res = req.json()
        self.__class__.board_id = res["id"]
        assert req.status_code == 200
        assert res["name"] == self.board_data["input_data"]["board_name"]
