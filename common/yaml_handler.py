"""
读取yaml文件
"""
import yaml
# from config.path import config_path
from config import path
import os



def read_yaml(file_path):
    """通过file_path文件路径读取yaml数据
    得到的是一个字典。
    SafeLoader 解析时更安全
    """
    with open(file_path, encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    return data


def write_yaml(yaml_path, new_data_name='',new_value=''):
    old_value=read_yaml(yaml_path)
    update=old_value
    update[new_data_name]=new_value
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(update, f)

#
# file_list=[]
# def file_name(file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         for file in files:
#             if os.path.splitext(file)[1] == '.yaml':
#                 file_list.append(os.path.join(root, file))
#     return file_list
# print("file_list",file_list)


# print("yaml_path is :", yaml_path)
# print("yaml_config is :", yaml_config)

# 'a\b\c config.yaml==>a\b\c\config.yaml ==>'\'.join['a\b\c','config.yaml']
