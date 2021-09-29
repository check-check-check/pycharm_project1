# @Time    : 
# @Author  : chen
# -*- coding: utf-8 -*-
#在Python3以后，字符串和bytes类型彻底分开了。字符串是以字符为单位进行处理的，bytes类型是以字节为单位处理的。
# """
# bytes对象只负责以二进制字节序列的形式记录所需记录的对象，至于该对象到底表示什么（比如到底是什么字符）则由相应
# 的编码格式解码所决定。Python3中，bytes通常用于网络数据传输、二进制图片和文件的保存等等。可以通过调用bytes()
# 生成bytes实例，其值形式为 b'xxxxx'，其中 'xxxxx' 为一至多个转义的十六进制字符串（单个 x 的形式为：\x12，其
# 中\x为小写的十六进制转义字符，12为二位十六进制数）组成的序列，每个十六进制数代表一个字节（八位二进制数，取值范
# 围0-255），对于同一个字符串如果采用不同的编码方式生成bytes对象，就会形成不同的值.
# """
# 以下为实例
b = b''         # 创建一个空的bytes
print(b)
b = bytes()     # 创建一个空的bytes
print(b)
b = b'hello'    #  直接指定这个hello是bytes类型
print(b)
b = bytes('hello',encoding='GBK')  #利用内置bytes方法，将字符串转换为指定编码的bytes
print(b)
b = 'hello'.encode('GBK')   # 利用字符串的encode方法编码成bytes，默认为utf-8类型
print(b)
b = b'hello'.decode('GBK') #将bytes对象解码成字符串，默认使用utf-8进行解码。
print(b)
#%%
b1 = b'123'
b2 = b'abc'
print(b1 + b2)