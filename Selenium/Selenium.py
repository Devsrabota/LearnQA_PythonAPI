#подключаем Селениум 
import webbrowser
from selenium import webdriver

#создаем браузер
browser = webdriver.Firefox()
#подключаем стартовую странницу 
browser.get('https://google.com')
#делаем скрин шот 
browser.save_screenshot("12.png")
#перезагрузка страницы
browser.refresh()
#закрываю страницу
browser.quit()

