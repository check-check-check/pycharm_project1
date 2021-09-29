# @Time    : 
# @Author  : chen
# sys是system的缩写，用来获取操作系统和编译器的一些配置，设置及操作
# %% sys.argv用来接收从外部传进程序内的参数
import sys
print(sys.argv[0])
# cmd环境下输入：python sys模块.py 1 2 3 4 5 6
# 则输出：['sys模块.py', '1', '2', '3', '4', '5', '6']
print(sys.path)

#%% sys.exit 函数
"""执行至主程序的末尾时,解释器会自动退出. 但是如果需要中途退出程序, 你可以调用sys.exit 函数,
它带有一个可选的整数参数返回给调用它的程序. 这意味着你可以在主程序中捕获对sys.exit 的调用。
（注：0是正常退出，其他为不正常，可抛异常事件供捕获!）"""
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
#%% sys.path path是一个目录列表,供Python从中查找第三方扩展模块。
# 功能：获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到。
import sys
print(sys.path)
# 有时候为了让python能够找到我们自己定义的模块，需要修改sys.path的内容
sys.path.append('test') # 在path的开始位置 插入test
print(sys.path)
import test
#%%sys.modules
'''功能：sys.modules是一个全局字典，该字典是python启动后就加载在内存中。每当程序员导入新的模块，sys.modules将自动
记录该模块。当第二次再导入该模块时，python会直接到字典中查找，从而加快了程序运行的速度。它拥有字典所拥有的一切方法。'''
import sys
print(sys.modules.keys())
print(sys.modules.values())
print(sys.modules["sys"])
#%%sys.platform
# 获取当前执行环境的平台
import sys
sys.platform

#%%sys.builtin_module_names返回一个列表，包含内建模块的名字。如：
import sys
def find_module(module):
    if module in sys.builtin_module_names:
        print(module," => ","__builtin__")
    else:
        print(module,"=> ",__import__(module).__file__)

find_module('os')
find_module('sys')
find_module('zlib')
find_module('string')
#%% 进度条
import sys
import time
# def view_bar(num,total):
#     rate = num / total
#     rate_num = int(rate * 100)
#     #r = '\r %d%%' %(rate_num)
#     r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
#     sys.stdout.write(r)
#     sys.stdout.flush

def view_bar(num):
    rate_num = num
    r = '\r%s>%d%%' % ('▇' * rate_num, rate_num,)
    sys.stdout.write(r) #print(r)每次输出自动换行
    sys.stdout.flush #


if __name__ == '__main__':
    for i in range(0, 101):
        time.sleep(0.1)
        view_bar(i)
#%%
import sys
temp = sys.stdout
sys.stdout = open('test1.txt','w') #通过修改这种映射关系来把我们的打印操作重定向到其它地方
print('hello world')
sys.stdout = temp #恢复默认映射关系
print('nice')

#参考博客：https://blog.csdn.net/he_and/article/details/80675070

#%%
print(sys.getdefaultencoding())  #获取解释器默认编码。
print(sys.getfilesystemencoding())  #获取内存数据存到文件里的默认编码。

