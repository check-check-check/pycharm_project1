# @Time    : 
# @Author  : chen
#%% 调用子目录下的模块，形如以下结构:mode3模块调用mode1或mode3
'''
different_catalogues
 ├─ mydir1
 │  ├─ mode1.py
 │  └─ mode2.py
 ├─ mode3.py
'''
# import mydir1.mode2
# import mydir1.mode1
import  mydir1 #导入包的本质是执行该包下的__init__.py文件

