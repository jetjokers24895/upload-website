import json
import re
from pprint import pprint

import requests

from var import env, path

import upload_api as api


def write_file(text):
    with open("text.txt", "w+") as w:
        w.write(text)

try:
    s = requests.Session()

    r0 = s.get(env.base_url)
    _reg = re.search(r'<meta name="csrf-token" content="(.*)">', r0.text)
    assert _reg != None
    _token = _reg.groups()[0]

    data = {
        "email": "admin@admin.com",
        "password": "password",
        "_token": _token,
        "redirect": "/"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    r1 = s.post(env.login,  data=data)

    #upload
    
    

except Exception as e:
    print("######EXCEPTION#####")
    print(e)
