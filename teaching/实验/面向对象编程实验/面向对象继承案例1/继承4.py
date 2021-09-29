# @Time    : 
# @Author  : chen
# 第4关：多重继承
# 本关的编程任务是补全"继承4.py"文件的代码，实现当调用类C的test()时，继承的是类A的test()。
# 当调用类D的check()时，继承的是类B的check()。
# 当调用类E的test()时，继承的是类A的test()
# 具体要求如下：
# 填入定义子类C的代码；
# 填入定义子类D的代码。

class A:
    def test(self):
        print("this is A.test()")
class B:
    def test(self):
        print("this is B.test()")
    def check(self):
        print("this is B.check()")
# 请在下面填入定义类C的代码
########## Begin ##########
class C(A,B):
########## End ##########
    pass
# 请在下面填入定义类D的代码
########## Begin ##########
class D(A,B):
########## End ##########
    def check(self):
        super().check()
        # print("this is D.check()")
# 请在下面填入定义类E的代码
########## Begin ##########
class E(C,D):
########## End ##########
    pass

# 当调用类C的test()时，继承的是类A的test()
obj1 = C()
obj1.test()
# 当调用类D的check()时，继承的是类B的check()
obj2 = D()
obj2.check()
# 当调用类E的test()时，继承的是类A的test()
obj3 = E()
obj3.test()