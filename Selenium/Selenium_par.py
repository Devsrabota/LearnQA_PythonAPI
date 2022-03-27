#подключаем время
from sqlite3 import Time
import time
#подключаем Селениум
import webbrowser
from selenium import webdriver


#Ссылка на сайт
sait = 'https://www.capitalman.company/'
#создаем браузер
browser = webdriver.Firefox()
#подключаем стартовую странницу 
browser.get(sait)
#ждем 3 сек
time.sleep(3)
#Создаем ссылку на элемент кнопка
xpach = '/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/section/div[2]/div/div[2]/div/div[5]/h2/span/span/span/span/a'
#кликаем на кнопку 
browser.find_element_by_xpath(xpach).click()

