#Телепортация на землю
import json

#Враг определен
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
#загружаем цель
text = json.loads(json_text)
#наводим на первую цель
a = (text['messages'])
#наводим на вторую цель
b = (a[1])
#наводим на третию цель ---- >> Огонь
print(b['message'])



