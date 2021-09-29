# @Time    : 
# @Author  : chen
str = '中国人'
print(str)
str_utf8 = str.encode('utf-8')
print(str_utf8)

str_gbk = str.encode('GBK')
print(str_gbk)


print(len(str))
print(len(str_utf8))
print(len(str_gbk))