"""日志处理的封装"""

# 导入信息放在模块最上面
import logging
import os
from config import path
import time


def get_logger(name='Root',
               logger_level='DEBUG',
               stream_handler_level='DEBUG',
               file=None,
               file_handler_level='DEBUG',
               fmt_str='Time:%(asctime)s-日志等级：%(levelname)s-收集器名称:%(name)s-日志:%(message)s-%(filename)s-%(lineno)s-'
               ):
    # logger 封装
    # 1.获取日志收集器logger
    logger_obj = logging.getLogger(name)  # 收集器名字
    logger_obj.setLevel(logger_level)
    fmt = logging.Formatter(fmt_str)

    # 日志处理器：
    handler = logging.StreamHandler()
    handler.setLevel(stream_handler_level)
    logger_obj.addHandler(handler)
    handler.setFormatter(fmt)

    # 文件处理器
    if file:
        file_handler = logging.FileHandler(file, encoding="utf8")
        file_handler.setLevel(file_handler_level)
        logger_obj.addHandler(file_handler)
        file_handler.setFormatter(fmt)

    return logger_obj


time_now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))

if __name__ == '__main__':
    folder_name = os.path.dirname(os.path.dirname(__file__))
    folder_base_name = os.path.basename(folder_name)
    logger_file = os.path.join(path.logs_path, folder_base_name+'_' + time_now + '.log')
    logger = get_logger(file=logger_file)
    logger.debug('debug message')
