# 该脚本用来测试生成uid

import sys
from Crypto.Cipher import AES
import Crypto

apikey = sys.argv[1]
secret = sys.argv[2]
deviceId = sys.argv[3]

'''
apikey = 'b8bfa00d66264e41afc0c91b1850f855'
secret = '09h928747iO6bJ7S'
deviceId = 'ai10000000000001'
'''
apikey = 'b8bfa00d66264e41afc0c91b1850f855'
secret = '09h928747iO6bJ7S'
deviceId = 'ai10000000000001'


# 通过deviceId获取uid
def get_uid(in_apikey, in_secret, in_deviceId):
    apikey = in_apikey
    secret = in_secret
    text = in_deviceId
    IV = apikey[0:16]
    cipher = AES.new(bytes(secret, encoding='utf-8'), AES.MODE_CBC, IV=bytes(IV, encoding='utf-8'))
    data = cipher.encrypt(bytes(text, encoding='utf-8'))
    uid = data.hex()
    return uid


uid = get_uid(apikey, secret, deviceId)
print(uid)
