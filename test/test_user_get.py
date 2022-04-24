#
import requests
from lib.base_case import BaseCase
#from lib.assertions import Assertions
#
class TestUserGet(BaseCase):
    def test_get_users(self):
        response = requests.get("https://playground.learnqa.ru/api/user/2")

        print(response.content)