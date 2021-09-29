# @Time    : 
# @Author  : chen
# 参考博客：https://blog.csdn.net/xjtuse123/article/details/92406862
# %%调用上级目录下的文件，形如以下结构:mode6想要调用mode4和mode1
'''
different_catalogues
 │——mydir1
 │  ├─ mode1.py
 │  │_ mode2.py
 │  │_ __init__.py
 │
 │——mydir2
 │  │_ mode5.py
 │  │_ mode6.py
 │
 │——mode3.py
 │——mode4.py

 '''
# 做法如下：
import sys
sys.path.append(r'G:\project\python-workplace\teaching\标准库模块\模块的导入使用\different_catalogues')

import mydir1.mode1 # 导入mode1模块的同时，执行了mydir1包下面的__init__()函数
import mode4
#%% 优化做法
import os
import sys

print(__file__)#获取当前程序路径，注意：这里打印出来的路径为相对路径
#动态获取绝对路径
print(os.path.abspath(__file__)) #这才是当前程序绝对路径
print(os.path.dirname(os.path.abspath(__file__))) #当前程序上一级目录，其中dirname返回目录名，不要文件名
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#当前程序上上一级目录

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #当前程序上上一级目录，这里为different_catalogues
sys.path.append(BASE_DIR) #添加环境变量
#%%
import mydir1.mode1 # 导入mode1模块的同时，执行了mydir1包下面的__init__()函数
import mode4
