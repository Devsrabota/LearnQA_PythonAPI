from requests import Response
import json
#
class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected value, error_massage):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"respons in json format , respons Text '{response.text}'"

        assert name in response_as_dict, f"Respons no key '{name}'"
        assert response_as_dict[name] == expected_value, error_massage

