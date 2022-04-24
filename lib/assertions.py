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

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
             respons_as_dict = response.json()
        except json.JSONDecodeError:
             assert False,f"Respons it not Json Format"
        assert name in respons_as_dict,f"Respons no key"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False,f"response it not json format"

        assert name in response_as_dict,f"Respons it not json Key" 

    @staticmethod  
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"No status Code"            


