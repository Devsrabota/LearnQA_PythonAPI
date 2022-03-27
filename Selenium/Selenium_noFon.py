#подключаем Селениум
import webbrowser
from selenium import webdriver
#отключаем в браузере видимость Селениума
option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled',False)
#отключаем всплывающие элементы
option.set_preference('dom.webnotifications.enabled',False)


#Ссылка на сайт
sait = 'https://www.capitalman.company/'
#создаем браузер и передаем ему параметры отключения видимости
browser = webdriver.Firefox(options=option)
#подключаем стартовую странницу 
browser.get(sait)
#Создаем ссылку на элемент кнопка
xpach = '/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/section/div[2]/div/div[2]/div/div[5]/h2/span/span/span/span/a'
#кликаем на кнопку 
browser.find_element_by_xpath(xpach).click()

