import os
import re
import json
import requests
from faker import Faker
from pymysql.cursors import DictCursor
from common.yaml_handler import read_yaml
from common.logger_handler import get_logger, time_now
from common.excel_handler import ExcelHandler
from common.db_handler import DBHandler
from config import path


# class MidDBHanlder(DBHandler):
#     def __init__(self,
#                  host=user_config['db']['host'],
#                  port=user_config['db']['port'],
#                  user=user_config['db']['user'],
#                  password=user_config['db']['password'],
#                  # 不要写成utf-8
#                  charset=user_config['db']['charset'],
#                  # 指定数据库
#                  database=user_config['db']['database'],
#                  cursorclass=DictCursor
#                  ):
#         super.__init__(host=host,
#                        port=port,
#                        user=user,
#                        password=password,
#                        charset=charset,
#                        database=database,
#                        cursorclass=cursorclass)

class MidDBHandler(DBHandler):
    def __init__(self):
        yaml_path = os.path.join(path.config_path, 'config.yaml')
        yaml_config = read_yaml(yaml_path)
        user_path = os.path.join(path.config_path, 'security.yaml')
        user_config = read_yaml(user_path)

        super().__init__(host=user_config['db']['host'],
                         port=user_config['db']['port'],
                         user=user_config['db']['user'],
                         password=user_config['db']['password'],
                         # 不要写成utf-8
                         charset=user_config['db']['charset'],
                         # 指定数据库
                         database=user_config['db']['database'],
                         cursorclass=DictCursor)


class MidHandler():
    """任务：中间层。 common 和 调用层。
    使用项目的配置数据，填充common模块
    """
    # 替换数据
    # 新手机号码
    new_phone = ''
    investor_user_id = ''
    investor_user_token = ''
    admin_user_id = ''
    admin_user_token = ''
    loan_user_id = ''
    loan_user_token = ''

    # yaml 读取
    yaml_path = os.path.join(path.config_path, 'config.yaml')
    yaml_config = read_yaml(yaml_path)

    user_path = os.path.join(path.config_path, 'security.yaml')
    user_config = read_yaml(user_path)

    # logger
    logger_file = os.path.join(path.logs_path, yaml_config['logger']['file'] + '_' + time_now + '.log')
    logger = get_logger(name=yaml_config['logger']['name'],
                        file=logger_file)
    folder_name = os.path.dirname(os.path.dirname(__file__))
    folder_base_name = os.path.basename(folder_name)
    log_path = path.logs_path
    log_name = '{}/{}_{}.log'.format(log_path, folder_base_name, time_now)

    # excel对象
    excel_file = os.path.join(path.data_path, 'cases.xlsx')
    excel = ExcelHandler(excel_file)

    # 辅助函数
    # help_funcs = helper

    # 数据库
    db_class = MidDBHandler

    # 需要动态替换#...# 的数据
    investor_phone = user_config['investor_user']['phone']
    investor_pwd = user_config['investor_user']['pwd']
    loan_phone = user_config['loan_user']['phone']
    loan_pwd = user_config['loan_user']['pwd']
    admin_phone = user_config['admin_user']['phone']
    admin_pwd = user_config['admin_user']['pwd']

    # 类方法，前面用cls，代表类本身
    @classmethod
    def replace_data(cls, my_string, pattern='#(.*?)#'):
        """数据动态替换"""
        # pattern = '#(.*?)#'
        results = re.finditer(pattern=pattern, string=my_string)
        for result in results:
            # old= '#investor_phone#'
            old = result.group()
            # key = 'investor_phone'
            key = result.group(1)

            if old == "#new_phone#":
                new = MidHandler.generate_new_phone()

            else:
                new = str(getattr(cls, key, ''))
            my_string = my_string.replace(old, new)
        return my_string

    @classmethod
    def get_token(cls):
        data = MidHandler.excel.read('login')
        url = "http://smartdevice.ai.tuling123.com/speech/chat"
        content_type = eval(data[0]['paras'])['Content-Type']
        ak = MidHandler.user_config['ak']
        uid = MidHandler.user_config['uid']
        parameter = json.dumps({"ak": ak, "uid": uid, "token": "", "asr": 4, "tts": 3, "tone": 20})
        payload = {'Content-Type': content_type,
                   'parameters': parameter}
        files = [
            ('speech', ('apple.opus', open('E:/Hannto/Automation/Github/Chameleon/Audio/apple.opus', 'rb'),
                        'application/octet-stream'))
        ]
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        return response.json()['token']

    @classmethod
    def update_tests_data(cls):
        data = MidHandler.excel.read('login')
        case_range = len(data)
        index_num: int
        new_token = MidHandler.get_token()
        for index_num in range(case_range):
            new_parameters = eval(eval(data[index_num]['paras'])['parameters'])
            new_parameters["ak"] = MidHandler.user_config['ak']
            new_parameters["uid"] = MidHandler.user_config['uid']
            new_parameters["token"] = new_token
            new_paras = {"parameters": json.dumps(new_parameters)}
            str_new_paras = json.dumps(new_paras)
            data[index_num]['paras'] = str_new_paras

        return data

    @classmethod
    def generate_new_phone(cls):
        """自动生成手机号"""
        fk = Faker(locale='zh_CN')
        while True:
            phone = fk.phone_number()
            db = MidDBHandler()
            phone_in_db = db.query('SELECT * FROM member WHERE mobile_phone = {}'.format(phone))
            db.close()
            if not phone_in_db:
                cls.new_phone = phone
                return phone

    # db = DBHandler(host='8.129.91.152',
    #              port=3306,
    #              user='future',
    #              password='123456',
    #              # 不要写成utf-8
    #              charset='utf8',
    #              # 指定数据库
    #              database='futureloan',
    #              cursorclass=DictCursor)


# def generate_new_phone():
#     """自动生成手机号"""
#     fk = Faker(locale='zh_CN')
#     while True:
#         phone = fk.phone_number()
#         db = MidDBHandler()
#         phone_in_db = db.query('SELECT * FROM member WHERE mobile_phone = {}'.format(phone))
#         db.close()
#         if not phone_in_db:
#             return phone


db = MidDBHandler()

if __name__ == '__main__':
    # strings = '{"mobile_phone": "#investor_phone#", "pwd": "#investor_pwd#", "mobile_phone": "#loan_phone#", "pwd": "#loan_pwd#", "mobile_phone": "#admin_phone#", "pwd": "#admin_pwd#"}'
    # a = MidHandler.replace_data(strings)
    a = MidHandler.update_tests_data()
    print('data is : ', a)
