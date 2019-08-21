import json
import os

_pwd = os.path.dirname(__file__).split("trello-python-api-test")[0]


class Utils:
    def __init__(self):
        with open(_pwd + "trello-python-api-test\\data\\config\\config.json") as json_file:
            self.config_data = json.load(json_file)

    def get_config_data(self):
        return self.config_data

    def get_test_data(self, test_data_name):
        with open(_pwd + "trello-python-api-test\\data\\test_data\\" + test_data_name + ".json") as json_file:
            return json.load(json_file)
