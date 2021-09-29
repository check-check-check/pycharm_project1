# @Time    : 
# @Author  : chen
# %%文件读操作
f = open('yesterday', 'r', encoding="utf-8")  # 打开文件
# 读第一行
first_line = f.readline()
print(first_line)
# 读下一行
print(f.readline())

# 读余下的内容
# f.readlines()读余下所有行，存在一个列表中
# data1=f.readlines()
# for line in data1:
#     print(line.strip())

# 读余下的内容
# print('我是分隔线'.center(50, '-'))
# # 读取剩下的所有内容,存成一个字符串，文件大时不要用
# data = f.read()
# # 打印文件
# print(type(data), data)

# 读第10行到第20行
print('我是分隔线'.center(50, '-'))
# 以下是效率比较低的程序，适用于读取小文件
# for index,value in enumerate(f.readlines()):
#     if index > 9:
#         pass
#         if index < 21:
#             print(value.strip())
#         else :
#             continue

# for index,value in enumerate(f.readlines()):
#     if index > 9 and index < 21:
#         print(value.strip())
#     else :
#         continue

# 对于文件比较大的文件，采用以下写法
count = 0
for i in f:
    count += 1
    if count >= 10 and count <= 20:
        print(i.strip())

    else:
        continue

print('我是分隔线'.center(50, '-'))
# 关闭文件
f.close()

# %%

f = open('yesterday', 'r', encoding="utf-8")
print(f.readline())  # 打开文件
print(f.tell())  # 光标所在位置，值位字符的个数
print(f.seek(0))
print(f.tell())
print(f.encoding)
print(f.name)

# %%
f = open('yesterday1', 'a+', encoding="utf-8")  # 打开文件
f.write('welcome to python!\n')
f.write('欢迎来到python\n')
data = f.read()
print(data)
f.close()

# %%读写‘r+'
"""
w     以写方式打开，
a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+     以读写模式打开
w+     以读写模式打开 (参见 w )
a+     以读写模式打开 (参见 a )
rb     以二进制读模式打开
wb     以二进制写模式打开 (参见 w )
ab     以二进制追加模式打开 (参见 a )
rb+    以二进制读写模式打开 (参见 r+ )
wb+    以二进制读写模式打开 (参见 w+ )
ab+    以二进制读写模式打开 (参见 a+ )"""
"""注意：
1、使用'W'，文件若存在，首先要清空，然后（重新）创建，
2、使用'a'模式 ，把所有要写入文件的数据都追加到文件的末尾，即使你使用了seek（）指向文件的其他地方，如果文件不存在，将自动被
创建。"""


# %%写读’w+'


