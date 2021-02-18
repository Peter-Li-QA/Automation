"""日志处理的封装"""

# 导入信息放在模块最上面
import logging
import os
from config import path
import time




def get_logger(name='Pet日志收集器',
               logger_level='WARNING',
               strem_handeler_level='DEBUG',
               file=None,
               file_handler_level='INFO',
               fmt_str='\nTime:%(asctime)s---日志等级：%(levelname)s---收集器名称:%(name)s---日志:%(message)s---%(filename)s---%(lineno)s---'
               ):
    # logger 封装
    # 1.获取日志收集器logger
    logger = logging.getLogger(name)  # 收集器名字"python36"
    logger.setLevel(logger_level)

    # Time:%(asctime)s---日志等级：%(levelname)s---收集器名称:%(name)s---日志:%(message)s---%(filename)s---%(lineno)s---
    fmt = logging.Formatter(fmt_str)

    # 日志处理器：
    handler = logging.StreamHandler()
    handler.setLevel(strem_handeler_level)
    logger.addHandler(handler)
    handler.setFormatter(fmt)

    # 文件处理器
    if file:
        file_handler = logging.FileHandler(file, encoding="utf8")
        file_handler.setLevel(file_handler_level)
        logger.addHandler(file_handler)
        file_handler.setFormatter(fmt)
    return logger
    # 5.设置格式
    # # 6.处理器添加到收集器上
    # logger.addHandler(handler)
    # logger.addHandler(file_handler)
    #
    # # 作页
    # # 封装成函数，自定义传参，返回值需要返回logger变量，因为下面调用会用到logger.info
    # # 封装成类，没必要，但是可以方便养成类封装和类调用的概念
    # # 可以用logging 继承方式

    return logger


time_now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
# date=logging.Formatter(datetime.time)
folder_name = os.path.dirname(os.path.dirname(__file__))
# print("Basename of folder_name is :",os.path.basename(folder_name))
folder_base_name = os.path.basename(folder_name)
log_path = path.logs_path
log_name = '{}/{}_{}.log'.format(log_path, folder_base_name, time_now)

# print("folder_name is :",folder_name)
# print("dirname is :",path.logs_path)
# log_file=os.path.join(path.logs_path,'{}_log.log'.format(folder_name))
# log_file = os.path.join(path.logs_path, log_name)
#
# # 收集器
# logger = get_logger(file=log_file)  # 初始化，得到logger 对象

# logger=get_logger()

if __name__ == "__main__":
    logger = get_logger()  # 没提供file 名称不会生成日志
    # logger=get_logger(file="python36.log")

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning  message')
    logger.error('error message')
    logger.critical('critical message')
