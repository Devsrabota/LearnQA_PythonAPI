#
from requests import Response
#
class BaseCase:
    def get_cookie(self,response: Response,cookie_name):
        assert cookie_name in response.cookies, f"No cookie respons'{cookie_name}'"
        return response.cookies[cookie_name]
    def get_header(self,response: Response,headers_name):
        assert headers_name in response.headers, f"No cookie respons'{headers_name}'"
        return response.cookies[headers_name]    
    def get_json_value(self,response: Response,name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:    
             assert False, f"Json not format'{name}'"
        assert name in response_as_dict, f"Response Json no key '{name}'"     
        return response_as_dict[name] 
