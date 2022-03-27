#импортирую запрос
import requests
#создаю ссылку
url = 'google.com/login'
#создаю фунцию авто заполнения 
def req_log(username, password):
    data = {
        "username": username,
        "password": password
    }
    r = requests.get(url,data = data)
#вызываю фунцию со значением 
req_log('Devs','12')