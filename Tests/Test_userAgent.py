import pytest
import requests
#
class Agent:
    User_Agent = [
        ("device"),
        ("browser"),
        ("platform")
    ]
    @pytest.mark.parametrize('condition',User_Agent)
    def User_Agent_url(self,User_Agent):
        url = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
        respons = requests.get(url,User_Agent)
        assert  respons == "Unknown", f"No '{User_Agent}' in '{url}'"
