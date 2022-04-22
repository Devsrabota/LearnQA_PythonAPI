#
import requests
from lib.base_case import BaseCase
#from lib.assertions import Assertions
#
class TestUserRegister(BaseCase):
      def test_create_user_with_existing_email(self):
          str1 = 'vinkotov'
          str2 = '@'
          str3 = 'examle.com'
          email_all = str1 + str2 + str3
          data = {
               'password': '123',
               'username':'learnqa',
               'firstName': 'learnqa',
               'lastName': 'learnqa',
               'email': email_all
          }
          response = requests.post("https://playground.learnqa.ru/api/user/",data = data)

          print(response.status_code)
          print(response.content)

          email_st = len(email_all)
          if email_st == 1:
               assert True, f"error '{email_all}' 1 simvol"
          elif email_st == 255:
               assert True, f"error '{email_all}' 255 simvol"

               assert response.status_code == 400, f"Status Code bad"

               assert str2 != '', f"error '{email_all}' not @"
               assert str1 != '', f"error not name@'{str3}'"
               assert str3 != '', f"error not '{str1}'@host"
               
               
