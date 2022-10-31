import sys
import os
import requests


def fetch(url):
    req = requests.get(url)
    res = req.content
    print(res)

url = sys.argv[1]
fetch(url)
