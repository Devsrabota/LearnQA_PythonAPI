#
import requests
#
url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'
#
a = {'method': 'get'}
b = {'method': 'head'}
c = {'method': 'post'}
d = {'method': 'put'}
e = {'method': 'delete'}
#
spi = [a,b,c,d,e]
#
respons_a = requests.get(url, params = a)
respons_b = requests.head(url, data = b)
respons_c = requests.post(url, data = c)
respons_d = requests.put(url, data = d)
respons_e = requests.delete(url, data = e)
#
spi_1 = [respons_a,respons_b,respons_c,respons_d,respons_e]

for spi in spi_1:
    
    print(spi.headers)