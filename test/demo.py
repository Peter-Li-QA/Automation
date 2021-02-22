import requests
import pytest
from middleware.handler import MidHandler

# 准备数据
data = MidHandler.update_tests_data()
# payload={'Content-Type': 'multipart/form-data;charset=UTF-8',
# 'parameters': '{"ak":"b8bfa00d66264e41afc0c91b1850f855","uid":"fd1d4665ee2d6f81897848734a0e6b62","token":"","asr":3,"tts":2,"tone":20}',
# 'speech': '{"type":4}'}

# tl_payload = {'parameters': '{"ak":"b8bfa00d66264e41afc0c91b1850f855","uid":"fd1d4665ee2d6f81897848734a0e6b62",'
#                             '"token":"","flag":0,"type":2,"extra":{"bookId": 250,"cameraId": 3333423,"innerUrlFlag": '
#                             '1,"debug": 0,"typeFlag": 1} '
#               }


@pytest.mark.parametrize('info', data)
def test_login(info):
    token = "79650f37b8f04f82b12d961fa469f8ab"

    actual_method='POST'
    actual_file=eval(info['file'])
    actual_data=eval(info['parameters'])
    resp = requests.request(url=MidHandler.yaml_config['host'],
                            method=actual_method,
                            files=actual_file,
                            data=actual_data
                            )

    # print("json is :", resp.text)
    # try:
    #     assert resp.json()['msg'] == info['expected']
    # except AssertionError as e:
    #     MidHandler.logger.error(e)
    #     MidHandler.logger.info("测试数据:{}".format(request_data))
    #     raise e
    print("\n  json responds is :", resp.json())
    # new_token=resp.json()['token']
    # # print("\n  token         is :", token)
    # new_paras=eval(actual_data['parameters'])['token']
    # x=eval(actual_data['parameters'])
    # x['token']=new_token
    # new_data=x
    # MidHandler.excel.write('login',new_data,2,6)

    return resp.json()


# print(test_login(payload))
# a = test_login(data[0])
# print('\n______________________tl_payload   is______________________ : \n', a)
# print('\n______________________return token is______________________ : \n', a['token'])
# b = test_login()
# print('______________________payload is_________________________ : ', b)
