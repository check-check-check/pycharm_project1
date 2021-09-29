# @Time    :
# @Author  : chen
import sys
def exitfunc(value):
    print(value)
    sys.exit(0)

print("hello")
try:
    sys.exit(1)
except SystemExit as value:
    exitfunc(value)
print("come?")
#%% 路径寻找
import os
path1 = os.path.dirname('__file__')
print(path1) #获取当前运行脚本的绝对路径
# print(os.path.realpath('__file__'))