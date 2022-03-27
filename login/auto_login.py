#Подключаемся
import selenium
import getpass
import webbrowser
from selenium import webdriver
import requests

#просим ввести данные
name = input('Введите имя: ')
password = getpass('Введите пароль: ')
#адрес ссылки
url = 'google.com/log'
#создаем браузер
web = webdriver.Firefox()
#подключаемся к странице
web.get(url)
#подключаемся к логину и паролю и вводим его
web_name = web.find_element_by_id('name1')
web_name.send_keys(name)
web_password = web.find_element_by_id('pass')
web_password.send_keys(password)
#нажимаем кнопку логина
button_web = web.find_element_by_id('button1')
button_web.submit()

