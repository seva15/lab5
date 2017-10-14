import BaseClient
import requests


class GetUserID(BaseClient.BaseClient):
    def __init__(self, username):
        self.username = username
    method = "users.get"
    http_method = "?user_ids="

    def get_data(self):
        response = requests.get(self.generate_url()).json()
        return response["response"][0]["uid"]


