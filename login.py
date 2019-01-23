import os
import json
import re
from pprint import pprint

import requests

from var import env, test

import upload_api as api




def write_file(text):
    with open("text.txt", "w+") as w:
        w.write(text)

def prepare_to_post(path, _token, category_id):
    try:
        list_files = api.get_files(path)
        zip_file = api.get_zip_file(list_files)
        os.remove(zip_file)
        
    except AssertionError as e:
        print(e)
    finally:
        #create zip _files
        api.create_zip_file(file)
        #make_data_to_post
        multi_files= make_files_to_post(path)
        #make data 
        data_to_post = api.make_data(path, _token, category_id)
        #post
        return multi_files, data_to_post

def make_files_to_post(path):
    #make pic to post
    _pic = api.make_pic_to_post(path)
    #make zip to post
    _zip = api.make_zip_to_post(path)
    return [_pic, _zip]


def make_files_to_post_v2(path):
    #make pic to post
    _pic = api.make_pic_to_post_v2(path)
    #make zip to post
    _zip = api.make_zip_to_post_v2(path)
    return {**_pic, **_zip}

# try:
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
path = test.path_dir
# print(path)
list_files = api.get_files(path)
# print(list_files)
for file in list_files:
    # prepare_to_post(file, _token, 2)
    multi_files, data_to_post = prepare_to_post(file, _token, 2)
    # print(multi_files)
    # pprint(data_to_post)
    # r = s.post(env.upload, data = data_to_post, files = multi_files)
    r = requests.post("https://httpbin.org/post", files =multi_files)
    print(r.status_code)
    pprint(r.headers)
    pprint(r.text)

# except Exception as e:
#     print("######EXCEPTION#####")
#     print(e)
