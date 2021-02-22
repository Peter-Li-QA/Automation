import pytest
import requests

from common.db_handler import DBHandler
# from common.yaml_handler import yaml_config, user_config
from jsonpath import jsonpath
from middleware.handler import MidHandler


def login(phone, pwd):
    user = {
        "mobile_phone": phone,
        "pwd": pwd
    }
    resp = requests.request(method='POST',
                            url=MidHandler.yaml_config['host'] + '/member/login',
                            headers={"X-Lemonban-Media-Type": "lemonban.v2"},
                            json=user
                            )
    resp_json = resp.json()
    token = jsonpath(resp_json, '$..token')[0]
    token_type = jsonpath(resp_json, '$..token_type')[0]
    id = jsonpath(resp_json, '$..id')[0]
    leave_amount = jsonpath(resp_json, '$..leave_amount')[0]
    token = " ".join([token_type, token])
    return {"id": id,
            "token": token,
            "leave_amount": leave_amount}


@pytest.fixture()
def login_investor():
    """登录。 得到 ID, token, leave_amount
    """
    user = {
        "mobile_phone": MidHandler.user_config['investor_user']['phone'],
        "pwd": MidHandler.user_config['investor_user']['pwd']
    }
    login_data = login(user['mobile_phone'], user['pwd'])
    # YZHandler.investor_user_id = login_data['id']
    # YZHandler.investor_user_token = login_data['token']
    return login_data


@pytest.fixture()
def admin_login():
    """管理员登录"""
    user = {
        "mobile_phone": MidHandler.user_config['admin_user']['phone'],
        "pwd": MidHandler.user_config['admin_user']['pwd']
    }
    return login(user['mobile_phone'], user['pwd'])


@pytest.fixture()
def loan_login():
    """管理员登录"""
    user = {
        "mobile_phone": MidHandler.user_config['loan_user']['phone'],
        "pwd": MidHandler.user_config['loan_user']['pwd']
    }
    return login(user['mobile_phone'], user['pwd'])


@pytest.fixture()
def add_loan(loan_login):
    headers = {"X-Lemonban-Media-Type": "lemonban.v2",
               "Authorization": loan_login["token"]}

    data = {
        "member_id": loan_login['id'],
        "title": "报名 Python 全栈自动化课程",
        "amount": 6300.00,
        "loan_rate": 12.0,
        "loan_term": 12,
        "loan_date_type": 1,
        "bidding_days": 5
    }

    resp = requests.request(method='POST',
                            url=MidHandler.yaml_config['host'] + '/loan/add',
                            headers=headers,
                            json=data)
    resp_json = resp.json()
    loan_id = jsonpath(resp_json, '$..id')[0]
    return loan_id


@pytest.fixture()
def db():
    """管理数据库链接的夹具"""
    db_conn = MidHandler.db_class()
    yield db_conn
    db_conn.close()


if __name__ == '__main__':
    print(login())

# 多值断言 第二版
# ("code",0)
# for key,value in expected.items():
#     tyr:
#         assert  resp.json()[key]==value
#     except AssertionError as e:
#         raise e
# 多值断言 第一版
# assert resp.json()['code']==expected["code"]
# assert resp.json()['msg'] == expected["msg"]

# 第三版 多值断言
#     for key, value in expected.items():
#
#         jsonpath(resp.json(), key)[0] == value
#         try:
#             assert resp.json()[key] == value
#         except AssertionError as e:
#             MidHandler.logger.error(e)
#             MidHandler.logger.info("测试数据:{}".format(json_data))
#         raise e