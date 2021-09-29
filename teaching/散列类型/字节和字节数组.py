# @Time    : 
# @Author  : chen
# 参考博客：https://blog.csdn.net/qq_40498551/article/details/88948569
"""
bytes 与bytearray都是Python3才引入的两个类型。
bytes 表示字节序列，是一个不可变的数据类型。
bytearray 表示字节数组，是一个可变的数据类型。
定义这两种类型的数据，在内存中开辟的空间都得是连续的。
"""
#%% bytes 类型
# bytes:定义空字节，空字节前面有个 b 来区分。
print(bytes())
# bytes(int):
print(bytes(5)) #直接定义字节的个数，就是创造了几个空字节，但是每个字节里面是空的
#注意：这是ASCII 0 ，不是阿拉伯数字0，阿拉伯数字0是十进制48，十六进制30.
# bytes(iteratable)
"""创造可迭代对象的元素个数相等的字节，然后把每个元素填充进去。
注意，必须是整型int 的可迭代对象。"""
print(bytes(range(8)))
print(bytes([1,2,3]))
print(bytes([97, 98]))  #按16进制的ACCII码返回
print(bytes([0x61, 0x62]))#0x是16进制标识
#%% bytes(byte) or bytes(‘string’,encode) :等价于string.encode()
s1='中国人'
print(s1.encode())#默认'utf8'编码
print(bytes(s1,'utf-8'))
print(bytes(bytes(s1,'utf-8')))
print(b'ab', b'\x61\x62')

#%% bytearray 类型
print(bytearray())  # 空bytearray
print(bytearray(5))  # 指定字节的bytearray，被0填充
print(bytearray(range(5)))  # --> bytearray [0,255]的int组成的可迭代对象
print(bytearray('abc', 'utf8'))  # -> bytearray #近似string.encode()，不过返回可变对象
# bytearray(bytes_or_buffer)  # 从一个字节序列或者buffer复制出一个新的可变的bytearray对象

#%% bytearray操作
print(bytearray(b'abcdef').replace(b'f',b'k'))
print(bytearray(b'abc').find(b'b'))
#print(bytearray.fromhex(string)),string必须是2个字符的16进制的形式，'6162 6a 6b'，空格将被忽略
print(bytearray.fromhex('6162 09 6a 6b00'))
