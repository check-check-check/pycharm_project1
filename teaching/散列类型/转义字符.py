# @Time    :
# @Author  : chen
# str = '\n张\n\n\n三   '
# print(str)
# strip_str=str.strip()
# print(strip_str)
# \r是将光标移到一行的开始,所以\r之后的内容会覆盖掉上次打印的内容
print("你好!\r我是Python!")
# "\n"换行,打印结果分列在两行
print('i love you \ni love you too')
# "\t"制表符,打印结果中间隔了一个制表符
print('i love you \ti love you too')
# r:字符串前加字母"r"表示后面字符串中不进行转义
print(r'i love you \ni love you too')
# \\:可以看到打印结果中间隔了一个反斜杠
print('i love you \\i love you too')
# \b退格符,将光标前移,覆盖
print('abcde\b\bfg')

#%%正斜杠和反斜杠
path = r"C:\Windows\temp\readme.txt"
path1 = r"c:\windows\temp\readme.txt"
path2 = "c:\\windows\\temp\\readme.txt"
path3 = "c:/windows/temp/readme.txt"
'''
path："\"为字符串中的特殊字符，加上r后变为原始字符串，则不会对字符串中的"\t"、"\r" 进行字符串转义
path1：大小写不影响windows定位到文件
path2：用一个"\"取消第二个"\"的特殊转义作用，即为"\\"
path3：用正斜杠做目录分隔符也可以转到对应目录，并且在python中path3的方式也省去了反斜杠\转义的烦恼
'''
#%% \t认识
print('1\t2')
print(12345)

s = '\t'
s_uf8 = s.encode(encoding='utf-8')
print(s_uf8, len(s_uf8))
print(s, s, s, len(s))
s_gbk = s.encode(encoding='GBK')
print(s_gbk, len(s_gbk))