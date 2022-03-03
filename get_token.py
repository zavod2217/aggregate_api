import config
from lr7 import lite_requests
import json


class Single(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Single, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Token(metaclass=Single):
    connection = None

    def __init__(self, conf):
        self._host = f"{conf['services']['connect']['host']}:{conf['services']['connect']['port']}"
        self._url = conf['services']['auth']['url']
        self._login = conf['services']['auth']['login']
        self._password = conf['services']['auth']['password']
        self._data = _data = json.dumps({
            "username": self._login,
            "password": self._password
        })
        self.token = None

    def get(self):
        if self.token is None:
            res = lite_requests.Request(f'{self._host}{self._url}', 'post', self._data)
            self.token = res.request_result['token']
        return self.token


token = Token(config.data).get()



