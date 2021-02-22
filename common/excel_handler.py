"""
excel 操作
"""
import os

import openpyxl

from config.path import data_path


class ExcelHandler():
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self, sheet_name):
        """
        读取数据
        打开文件
        """
        work_book = openpyxl.open(self.file_path)
        print("work_book is :", work_book)
        work_sheet = work_book[sheet_name]
        # print(work_sheet.values)
        data = list(work_sheet.values)  # 转化生成器对象为list
        header = data[0]
        # print("header is :", header)
        # 获取所有数据
        # 初始化列表
        all_data = []
        for row in data[1:]:
            row_dict = dict(zip(header, row))  # 用zip 把连个列表组合成元组列表
            # print("row_dict is :", row_dict)
            all_data.append(row_dict)
        return all_data  # all_data #data[1:]

    def write(self, sheet_name, data, row, column):
        """写入excel数据"""
        work_book = openpyxl.load_workbook(self.file_path)
        work_sheet = work_book[sheet_name]
        work_sheet.cell(row=row, column=column).value = data
        # 通过workbook保存和关闭
        work_book.save(self.file_path)
        work_book.close()


if __name__ == '__main__':
    xls_file = os.path.join(data_path, 'cases.xlsx')
    xls = ExcelHandler(xls_file)  # 初始化一个对象实例
    excel_data = xls.read(('register'))
    print('excel data is :', excel_data)
