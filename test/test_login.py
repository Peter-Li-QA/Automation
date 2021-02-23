import requests
import pytest
from middleware.handler import MidHandler

# 准备数据
data = MidHandler.update_tests_data()


@pytest.mark.parametrize('info', data)
def test_login(info):
    actual_method = info['method']
    actual_file = eval(info['file'])
    actual_data = eval(info['paras'])
    resp = requests.request(url=MidHandler.yaml_config['turing']['url'],
                            method=actual_method,
                            files=actual_file,
                            data=actual_data,
                            )

    print("\n  json responds is :", resp.text, "\n")
    return resp.json()
