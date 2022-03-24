from urllib import response
# Импортируем запрос
import requests
# Создаем запрос 
response = requests.get("https://playground.learnqa.ru/api/get_text")
# Выводим ответ
print(response.text)