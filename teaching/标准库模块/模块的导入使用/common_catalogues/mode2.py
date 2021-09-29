# @Time    : 
# @Author  : chen
#我们先自定义一个模块 名为mode2.py;
#那么我们现在对其进行约束一下，要求只能使用fun3()和func2()功能；
#我们在mod模块开头加入一下
__all__ = ['func3','func2','name']
print("hello world")
name = "zjk"
def func1():
    print("zjk1")

def func2():
    print("zjk2")
    func1()

def func3():
    print("zjk3")
    func2()
