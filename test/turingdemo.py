import os

import requests
from requests_toolbelt import MultipartEncoder
import json

url = "http://smartdevice.ai.tuling123.com/speech/chat"

payload = {"parameters": {
    "ak": "b8bfa00d66264e41afc0c91b1850f855",
    "uid": "ac96068d8631ad2323dabd31040ca599",
    "asr": 4,
    "tts": 2,
    "token": "6a919c190dfd43aaa897f9a5da830053",
    "tone": 20,
    "flag": 3
}}

files_path = os.path.dirname(os.path.dirname(__file__))
opus_path = os.path.join(files_path, 'data')
opus_file = os.path.join(opus_path, 'apple.opus')

# files = {'speech': ('apple.opus', open(opus_file, 'rb'), 'application/octet-stream')}

m = MultipartEncoder(
    fields={
        "parameters": json.dumps({
            "ak": "b8bfa00d66264e41afc0c91b1850f855",
            "uid": "ac96068d8631ad2323dabd31040ca599",
            "asr": 4,
            "tts": 2,
            "token": "6a919c190dfd43aaa897f9a5da830053",
            "tone": 20,
            "flag": 3
        }),
        'speech': ('apple.opus', open(opus_file, 'rb'), 'application/octet-stream')
    },
    boundary="----WebKitFormBoundarybtXd96AztrPD9eZT"
)

headers = {
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarybtXd96AztrPD9eZT',
    'Cache-Control': 'no-cache'
}

# response = requests.request("POST", url, headers=headers, data=payload, files=files)
response = requests.request("POST", url=url, headers=headers, data=m)
print(response.text)
print(response.json())