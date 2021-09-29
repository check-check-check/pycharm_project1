# @Time    : 
# @Author  : chen
#%%
import sys
def exitfunc():
    print('exit is done!')
sys.exitfunc=exitfunc #设置退出时要自动调用的函数
print('hello world')
sys.exit(1) #退出，后边的语句不再执行（ 但在退出之前会自动调用exitfunc() ）
print('ok')  #该语句不会执行

#%%sys应用案例1
import sys
def exitfunc(value):
    '''clear function'''
    print(value)
    sys.exit(0) #没有去捕获 抛出的SystemExit异常，执行到该语句时退出解释器
print('hello!')
try:
    sys.exit(5)  #抛出的SystemExit异常，被成功捕获
except SystemExit as value:
    exitfunc(value)
print('not out!') #该语句不会执行

#%%sys应用案例1
from sys import argv  # 通过这种导入，直接使用argv
import os

def ping(net, start=80, end=85, n=1, w=3):
    for i in range(start, end + 1):
        ip = net + "." + str(i)
        command = "ping %s -n %d -w %d" % (ip, n, w)
        print(ip, ("通", "不通")[os.system(command)])  # system用1,0表示通与不通，1不通，0通

# 示例输入
if len(argv) not in [2, 4, 6]:
    print("参数输入错误！")
    print("1.py  111.202.98")
    print("1.py  111.202.98 70 80")
    print("1.py  111.202.98 70 80 1 5")

elif len(argv) == 2:
    net = argv[1]
    ping(net)

elif len(argv) == 4:
    net = argv[1]
    ping(net, start=int(argv[2]), end=int(argv[3]))

else:
    net = argv[1]
    ping(net, start=int(argv[2]), end=int(argv[3]), n=int(argv[4]), w=int(argv[5]))

