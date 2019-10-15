"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : 10/7/2019
    Remark      : zmz
"""
from pyquery import PyQuery as pq
import requests

if __name__ == '__main__':
    with open('zmz.html', encoding='utf-8') as f:
        html = f.read()
    obj = pq(
        # url='http://got001.com/resource.html?code=d8gbn3',
        html
    )
    print(obj('#tab-g0-MP4'))

