#Поехали на море
import requests
#Конечная точка моря
api = 'https://playground.learnqa.ru/api/long_redirect'
#посмотрели какая погода на море
respons = requests.get(api)
#погода нормальная или нет
print(respons)
#спросили у друга как он туда ехал
doroga = respons.history
#он говрит дорога хорошая или плохая
print(doroga)
#узнали у яндекса путь
for a in doroga:
    print(a.url)