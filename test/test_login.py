import requests
import pytest
from middleware.handler import MidHandler

# 准备数据
data = MidHandler.excel.read('login')
# zyb_payload = {
#     'parameters': '{"ak":"b8bfa00d66264e41afc0c91b1850f855","uid":"fd1d4665ee2d6f81897848734a0e6b62","token":"","asr":3,"tts":2,"tone":20}',
#     'speech': '{"type":2}'
# }
# tl_payload = {'parameters': '{"ak":"b8bfa00d66264e41afc0c91b1850f855","uid":"fd1d4665ee2d6f81897848734a0e6b62",'
#                             '"token":"","flag":0,"type":2,"extra":{"bookId": 250,"cameraId": 3333423,"innerUrlFlag": '
#                             '1,"debug": 0,"typeFlag": 1} '
#               }


# headers = {"Content-Type": "multipart/form-data", "token": ""}

@pytest.mark.parametrize('info', data)
def test_login(info):
    resp = requests.request(url=MidHandler.yaml_config['host'],
                            method=info['method'],
                            files=eval(info['headers']),
                            data=eval(info['parameters'])
                            )

    # print("json is :", resp.text)
    # try:
    #     assert resp.json()['msg'] == info['expected']
    # except AssertionError as e:
    #     MidHandler.logger.error(e)
    #     MidHandler.logger.info("测试数据:{}".format(request_data))
    #     raise e
    # print("json is :", resp.json())
    return resp.json()


# print(test_login(payload))
# a = test_login(tl_payload)
# print('______________________tl_payload is______________________ : ', a)
# b = test_login()
# print('______________________payload is_________________________ : ', b)
