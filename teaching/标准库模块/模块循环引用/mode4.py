# @Time    : 
# @Author  : chen
# 文件名：mode6.py
from mode5 import run
def test():
    pass
if __name__ == '__main__':
    run()
'''执行该模块需要调用mode5模块，但是mode5又调用该模块，从而形成循环调用'''
# 解决方案参照：https://blog.csdn.net/weixin_33755557/article/details/92112800