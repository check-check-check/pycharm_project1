# @Time    : 
# @Author  : chen
# Python里面的hashlib模块提供了很多加密的算法，这里介绍一下hashlib的简单使用事例，用hashlib的md5算法加密数据
#%% 1. md5()加密算法

import hashlib
hash = hashlib.md5() #创建了一个md5算法的对象(md5不能反解)，即造出hash工厂
hash.update(bytes('123456',encoding='utf-8')) #运送原材料喽，要对哪个字符串进行加密，就放这里
print(hash.hexdigest()) #产出hash值,拿到加密字符串
"""我们可以看到生成结果是一个32位（5f4dcc3b5aa765d61d8327deb882cf99）的16进制字符串，生成结果是固定的128 bit字节
（需要注意的是加密是固定的，就是关系是一一对应的，是存在缺陷的，可以被对撞出来，特别是一些使用123456类作为密码的用户）"""
#%% 2. sha1()加密算法
hash2=hashlib.sha1()#sha1算法，hashlib很多加密算法
hash2.update(bytes('123456',encoding='utf-8'))
print(hash2.hexdigest())
# sha1()加密算法的结果是160 bit字节，通常用一个40位的16进制字符串表示。