from random import choice
import requests

https_list=[
]

http_list=[
]


def get_proxies():
    """
    请求代理
    使用方法：response = requests.get(url, headers=headers, proxies=proxy.get_proxies())
    """

    proxies ={
        "http": 'http://'+choice(http_list),
        "https": 'https://'+choice(https_list),
    }
    return proxies
