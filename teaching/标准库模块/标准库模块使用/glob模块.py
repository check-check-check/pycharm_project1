# @Time    : 
# @Author  : chen
# glob是python自己带的一个文件操作相关模块，用它可以查找符合自己目的的文件，类似于Windows下的文件搜索
"""
查找文件只用到三个匹配符：”*”, “?”, “[]“。
”*”匹配0个或多个字符；”?”匹配单个字符；”[]“匹配指定范围内的字符，如：[0-9]匹配数字。
"""
# (1).glob.glob返回所有匹配的文件路径列表。它只有一个参数pathname，定义了文件路径匹配规则，这里可以是绝对路径，
# 也可以是相对路径。 下面是使用glob.glob的例子：
import glob
# 获取指定目录下的所有图片
print(glob.glob(r"G:\资料备份\资料备份\积分申报\*.jpg"))#(绝对路径）


print(glob.glob(r'./*.py')) # 获取本级目录的所有.py文件

print(glob.glob("../*")) #上一级所有目录
print(glob.glob("./*.*")) #本级所有文件
print(glob.glob("C:/*")) #C盘所有目录
print(glob.glob("C:/*[PB][RO]*")) #C盘所有包含pr、po、br或者bo的的目录，不区分大小写

print(glob.glob("C:/*P?O*")) #C盘所有包含P_o的目录

print(glob.glob("E:\*\*.txt")) # C盘两级目录所有的txt
#%% glob.iglob()函数
"""glob.iglob()函数获取一个可遍历对象，使用它可以逐个获取匹配的文件路径名。与glob.glob()的区别
是：glob.glob()可同时获取所有的匹配路径，而glob.iglob()一次只能获取一个匹配路径"""
iter1 = glob.iglob("E:\*\*.txt")
print(iter1)
for i in iter1:
    print(i)


