import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Request:
    def __init__(self, url, method='get', data=None, headers=None):
        self.url = url
        self.method = method
        self.data = data
        self.verify = False
        self.headers = headers
        self.request_result = None
        self.__results = None

    def __pack(func):
        def wrapper(*args, **kwargs):
            args[0].headers = {'Content-Type': 'application/json'} if args[0].headers is None else args[0].headers
            func(*args)
        return wrapper

    @__pack
    def __get(self):
        res = requests.get(self.url, headers=self.headers, verify=False)
        self.__results = res.json()

    @__pack
    def __post(self):
        res = requests.post(self.url, data=self.data, headers=self.headers, verify=False)
        self.__results = res.json()

    @__pack
    def __put(self):
        res = requests.put(self.url, data=self.data, headers=self.headers, verify=False)
        self.__results = res.json()

    @property
    def request_result(self):
        {
            'get': self.__get,
            'post': self.__post,
            'put': self.__put,

        }[self.method]()
        return self.__results

    @request_result.setter
    def request_result(self, value):
        return


