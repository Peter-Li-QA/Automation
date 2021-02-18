import requests

url = "http://smartdevice.ai.tuling123.com/speech/chat"

payload={'Content-Type': 'multipart/form-data',
'parameters': '{"ak":"b8bfa00d66264e41afc0c91b1850f855","uid":"fd1d4665ee2d6f81897848734a0e6b62","token":"","asr":3,"tts":2,"tone":20}'}
files=[

]
headers = {
  'Content-Type': 'multipart/form-data'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
