import requests
import json

def get_jwt_token():
    url = 'http://api-sku-aggregator.com:8000/users/login/'
    credentials = { "email": "farooqseedat@gmail.com", "password": "123456fs" }
    response = requests.post(url=url, data=credentials)
    return json.loads(response.content)

def get_access_token(refresh):
    if not refresh:
        return {}
    response = requests.post(
            url='http://api-sku-aggregator.com:8000/users/token-refresh/',
            data={"refresh":refresh}
        ).content
    json_serialized_response = json.loads(response)
    return json_serialized_response.get("access")
