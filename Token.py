#Погружаемся 
import requests
import time
#иследую затопленый фрегат
url = 'https://playground.learnqa.ru/ajax/api/longtime_job'
#ключ со мной
param_token = 'token'
#ключ подошел
respons = requests.get(url,param_token)
#проверяю ответ если в сундуке наша надпись
print('Первый запрос  ' + respons.text)
for status in respons.text:
     if {'status': 'Job is ready'}:
         #я нашел эту рукопись ура!!!
         print('Второй запрос  ' + 'status: Job is ready')
         break
     else:
         time.sleep(3)
