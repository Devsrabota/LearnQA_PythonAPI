import requests
#
class Test_header:
    def header_test(self):

        url = 'https://playground.learnqa.ru/api/homework_header'

        respons = requests.post(url)
        print(respons.headers)
        assert "Server" in respons.headers, f"No headers '{respons.headers}"