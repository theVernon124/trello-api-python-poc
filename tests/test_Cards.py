import requests

from commands.Utils import Utils
from commands.TestSteps import TestSteps


class TestCards(object):
    utils = None
    steps = None
    config_data = None
    card_data = None
    board_id = None
    list_id = None

    @classmethod
    def setup_class(cls):
        cls.utils = Utils()
        cls.steps = TestSteps()
        cls.config_data = cls.utils.get_config_data()
        cls.card_data = cls.utils.get_test_data("cards")
        cls.board_id = cls.steps.create_board(cls.card_data["input_data"]["board_name"], cls.config_data["key"],
                                          cls.config_data["token"]).json()["id"]
        cls.list_id = cls.steps.create_list(cls.card_data["input_data"]["list_name"], cls.board_id,
                                            cls.config_data["key"], cls.config_data["token"]).json()["id"]

    @classmethod
    def teardown_class(cls):
        cls.steps.delete_board(cls.board_id)

    def test_valid_create_card(self):
        s = requests.Session()
        data = {
            "idList": self.list_id,
            "name": self.card_data["input_data"]["card_name"],
            "key": self.config_data["key"],
            "token": self.config_data["token"]
        }
        req = s.post(self.config_data["url_cards"], data)
        res = req.json()
        assert req.status_code == 200
        assert res["idList"] == self.list_id
        assert res["name"] == self.card_data["input_data"]["card_name"]

