import requests

from commands.Utils import Utils


class TestSteps():
    def __init__(self):
        self.config_data = Utils().get_config_data()

    def perform_auth(self, method, user, password):
        s = requests.Session()
        data = {
            "method": method,
            "factors[user]": user,
            "factors[password]": password
        }
        return s.post(self.config_data["url_authentication"], data=data)

    def create_board(self, name, key, token):
        s = requests.Session()
        data = {
            "name": name,
            "key": key,
            "token": token
        }
        return s.post(self.config_data["url_boards"], data=data)

    def delete_board(self, board_id):
        url = self.config_data["url_boards"] + '/' + board_id
        params = {
            "key": self.config_data["key"],
            "token": self.config_data["token"]
        }
        requests.delete(url, params=params)

    def create_list(self, name, board_id, key, token):
        s = requests.Session()
        data = {
            "name": name,
            "idBoard": board_id,
            "key": key,
            "token": token
        }
        return s.post(self.config_data["url_lists"], data)