import config
from lr7 import lite_requests
import get_token
import json

token = get_token.token
method = config.data['services']['request']['method']
host = config.data['services']['connect']['host']
port = config.data['services']['connect']['port']
url = config.data['services']['request']['url']
headers = {"Authorization": f"Bearer {token}"}

_a = lite_requests.Request(f'{host}:{port}{url}', method, data='[{}]', headers=headers)
print(_a.request_result)

