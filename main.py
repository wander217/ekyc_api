'''
NOTE:
in order to send request, first change config of $no_proxy adding localhost
'''

# %%
import random as rd
import requests
from glob import glob
import time
import json
import datetime
import os
import json
import shutil
from tqdm import tqdm
import os
import shutil

# ts = datetime.datetime.now().timestamp()

proxies = {'https': 'http://10.22.10.44:7783'}


# url = "http://localhost:8181/api/v2.1/ppr/card/segment"

def get_traceid():
    id = rd.randint(10000, 99999)
    id = "T" + str(id)

    return id


def get_requestid():
    id = rd.randint(100000000, 999999999)
    id = "R" + str(id)

    return id


api_version = 'v2.1'  # 'v1.0'
trigram = 'ppr'
url_form = 'http://localhost:8381/api/{api_version}/{trigram}/card/segment'
# url_form = 'http://localhost:7783/api/{api_version}/{trigram}/face/quality'
# url_form = 'http://localhost:7793/api/{api_version}/{trigram}/faceInfo'
# url_form = 'http://localhost:7783/api/{api_version}/{trigram}/face/quality'


url = url_form.format(api_version=api_version, trigram=trigram)


# url = 'http://localhost:8084/admin/status'


def post_image(image):
    trace_id = get_traceid()
    request_id = get_requestid()
    timestamp = str(int(time.time()))
    # print(trace_id, request_id, timestamp)
    data = {'clientId': 'vscode', 'traceId': trace_id, 'requestId': request_id,
            'unparsed_arguments': {}}  # , 'timestamp': timestamp}

    files = {'request': {'image': image, 'image_url': "empty", 'type': "empty"}}
    data.update(files)
    response = requests.post(url, json=data)
    # print(request_id)
    # response = requests.get(url)
    # print(response)
    # print(response.status_code, response.text)
    return response


if __name__ == '__main__':
    for img_path in tqdm(glob("/data/namth/data/CCCD/*")):
        if os.path.isfile(img_path):
            post_image(img_path)