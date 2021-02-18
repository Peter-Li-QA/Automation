"""路径"""
import os

#怎么求reports 的目录

# 动态获取路径
config_path=os.path.dirname(os.path.abspath(__file__))
#
# print(os.path.abspath(__file__))
# print("config_path is :",config_path)


#获取项目根目录
root_path=os.path.dirname(config_path)
# print("root_path is :",root_path)


# reports 路径
report_path=os.path.join(root_path,'reports')
if not os.path.exists(report_path):
    os.mkdir(report_path)
# print("report_path is :",report_path)


# log 路径
logs_path=os.path.join(root_path,'logs')
if not os.path.exists(logs_path):
    os.mkdir(logs_path)
# print("log_path is :",logs_path)

# data 路径
data_path=os.path.join(root_path,'data')

# config 路径
config_path=os.path.join(root_path,'config')

# tests 路径
tests_path=os.path.join(root_path,'tests')