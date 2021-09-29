# @Time    : 
# @Author  : chen
#我们先自定义一个模块 名为mode1.py;
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
