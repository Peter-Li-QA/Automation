"""帮助模块"""
# import random


from faker import Faker
from common.db_handler import DBHandler




    # fk.phone_number #随机生成人名fk.name;随机生成地址fk.address()
    # if not phone_in_db():
    #     return  phone


# def generate_new_phone_2():
#     """自动生成手机号码"""
#     phone='1'+random.choice(['3','4','5','6'])
#     for i in range (9):
#         num=random.randint(0,9) #每次生成0~9 数值拼接
#         phone+=str(num)

if __name__ == '__main__':
    print(generate_new_phone())
