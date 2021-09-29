# @Time    : 
# @Author  : chen
import hashlib
import time
# 对当前时间戳进行加密
def create_md():
    m = hashlib.md5()
    m.update(bytes(str(time.time()),encoding='utf-8'))
    return m.hexdigest()
