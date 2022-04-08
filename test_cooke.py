import requests
#
class TestExample1:
    def test_cooke(self):
        url = 'https://playground.learnqa.ru/api/homework_cookie'
        respons = requests.get(url)
        print(respons.cookies)
        assert "auth_sid" in respons.cookies, f"No cookeis '{respons.cookies}"
        