"""

"""
# import pymysql
# from pymysql.cursors import DictCursor
#
#
# class DBHandler:
#     def __init__(self,
#                  host='8.129.91.152',
#                  port=3306,
#                  user='future',
#                  password='123456',
#                  # 不要写成utf-8，mysql中 会出错
#                  charset='utf8',
#                  # 指定数据库
#                  database='futureloan',
#                  cursorclass=DictCursor
#                  ):
#         self.connect = pymysql.connect(host=host,
#                                        port=port,
#                                        user=user,
#                                        password=password,
#                                        # 不要写成utf-8，mysql中 会出错
#                                        charset=charset,
#                                        # 指定数据库
#                                        database=database,
#                                        cursorclass=cursorclass
#                                        )
#         # 2.获取游标,转化成字典
#         self.cursor = self.connect.cursor()
#
#     def query(self, sql_query, one=True):
#         """
#         数据库查询
#
#         """
#         # self.connect.commit()
#         # self.cursor.execute(sql_query)
#         # if one:
#         #     return self.cursor.fetchone()
#         # return self.cursor.fetchall()
#         if one:
#             return self.query_one(sql_query)
#         return self.query_all(sql_query)
#         # 关闭
#         cursor.close()
#         self.connect.close()
#
#     def query_one(self, sql_query):
#         self.cursor=self.connect.cursor()
#         self.connect.commit() #查询之前提交事务，重新拍一下照片，拿到最新的数据
#         self.cursor.execute(sql_query)
#         data=self.cursor.fetchone()
#         self.cursor.close()
#         return data
#
#     def query_all(self, sql_query):
#         self.cursor=self.connect.cursor()
#         self.connect.commit() #查询之前提交事务，重新拍一下照片，拿到最新的数据
#         self.cursor.execute(sql_query)
#         data=self.cursor.fetchall()
#         self.cursor.close()
#         return data
#
#     def insert(self, sql_insert):
#         self.cursor.execute('insert sql commond')
#         # 提交
#         self.connect.commit()
#
#     def update(self,sql_update):
#         # 提交
#         self.connect.commit()
#         pass
#
#     def delete(self,sql_delete):
#         # 提交
#         self.connect.commit()
#         pass
#
#     def close(self):
#         # self.cursor.close()
#         self.connect.close()
#
#
# if __name__ == '__main__':
#     db = DBHandler()
#     data = db.query('SELECT * FROM futureloan.member  LIMIT 10;', one=False)
#     print("Data is :", data)
#     db.close()


##########################################
"""

"""
import pymysql
from pymysql.cursors import DictCursor


class DBHandler:
    def __init__(self,
                 host='',
                 port=3306,
                 user='',
                 password='',
                 # 不要写成utf-8，mysql中 会出错
                 charset='utf8',
                 # 指定数据库
                 database='',
                 cursorclass=DictCursor
                 ):
        self.connect = pymysql.connect(host=host,
                                       port=port,
                                       user=user,
                                       password=password,
                                       # 不要写成utf-8，mysql中 会出错
                                       charset=charset,
                                       # 指定数据库
                                       database=database,
                                       cursorclass=cursorclass
                                       )
        # 2.获取游标,转化成字典
        self.cursor = self.connect.cursor()

    def query(self, sql_query, one=True):
        """
        数据库查询

        """
        # self.connect.commit()
        # self.cursor.execute(sql_query)
        # if one:
        #     return self.cursor.fetchone()
        # return self.cursor.fetchall()
        if one:
            return self.query_one(sql_query)
        return self.query_all(sql_query)
        # 关闭
        cursor.close()
        self.connect.close()

    def query_one(self, sql_query):
        self.cursor = self.connect.cursor()
        self.connect.commit()  # 查询之前提交事务，重新拍一下照片，拿到最新的数据
        self.cursor.execute(sql_query)
        result_data = self.cursor.fetchone()
        self.cursor.close()
        return result_data

    def query_all(self, sql_query):
        self.cursor = self.connect.cursor()
        self.connect.commit()  # 查询之前提交事务，重新拍一下照片，拿到最新的数据
        self.cursor.execute(sql_query)
        result_data = self.cursor.fetchall()
        self.cursor.close()
        return result_data

    def insert(self, sql_insert):
        self.cursor.execute('insert sql commond')
        # 提交
        self.connect.commit()

    def update(self, sql_update):
        # 提交
        self.connect.commit()
        pass

    def delete(self, sql_delete):
        # 提交
        self.connect.commit()
        pass

    def close(self):
        # self.cursor.close()
        self.connect.close()


if __name__ == '__main__':
    db = DBHandler(host='8.129.91.152',
                   port=3306,
                   user='future',
                   password='123456',
                   database='futureloan'
                   )
    # data = db.query('SELECT * FROM futureloan.member  LIMIT 10;', one=False)
    data = db.query('SELECT leave_amount FROM futureloan.member  WHERE id =31 LIMIT 10;', one=True)
    # data = db.query('SELECT leave_amount FROM futureloan.member WHERE id=31;', one=True)
    print("Data is :", data)
    db.close()
