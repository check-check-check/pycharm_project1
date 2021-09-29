# @Time    : 
# @Author  : chen
# unittest是python内置的单元测试框架，具备编写用例、组织用例、执行用例、输出报告等自动化框架的条件。
"""
单元测试框架的优点：
一般来说不用单元测试框架也能编写单元测试，因为单元测试本身就是通过一段代码去验证另一段代码，所以不用单元测试框架
也能编写单元测试。只是使用框架时会有更多的优点
1、提供用例组织与执行：
    当测试用例达到成百上千条时，就产生了扩展性与维护性等问题，此时就需要考虑用例的规范与组织问题了。单元测试框架
便能很好的解决这个问题

2、提供丰富的比较方法：    
    不论是功能测试还是单元测试，在用例完成之后都需要将实际结果与预期结果进行比较(断言)，从而断定用例是否执行通过。
单元测试框架一般会提供丰富的断言方法。例如：相等\不相等，包含\不包含，True\False的断言方法等

3、提供丰富的日志：
    当测试用例执行失败时能抛出清晰的失败原因，当所有用例执行完成之后能提供丰富的执行结果。例如，总执行时间、失败
用例数、成功用例数等
"""
#%% 例1：下面为一段需要测试的代码
class Count():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def Add(self, c):
        sum = self.x + self.y + c
        return sum

    def Subtract(self):
        subtract = self.x - self.y
        return subtract

    def Product(self):
        product = self.x * self.y
        return product

    def Division(self):
        division = self.x / self.y
        return division

if __name__ == "__main__":
    count = Count(6, 3)
    print(count.Add(2))
    print(count.Subtract())
    print(count.Product())
    print(count.Division())
# %% 例1_1：不使用框架编写的单元测试
# 使用非Unittest框架进行单元测试

# from Module.Unittest_Module.Add_count import Count
# 调用其他模块中的函数：from 模块路径.模块名.类名 import 函数名
from Module.Unittest_Module import Add_count
# 调用其他模块中的函数：from 模块路径.模块名 import 类名
class Test_Add_Count():
    def test_add(self):
        try:
            count = Add_count.Count(2, 3)
            # count = Count(2, 3)
            Add = count.Add(2)  # 不管怎么调用，调用方法时都是实例名.方法名()
            # assert (Count.Add == 7), "Integer addition result error"
            # assert (Add_count.Count.Add == 7), "Integer addition result error"
            assert (Add == 7), "Integer addition result error"
        except AssertionError as Error_msg:
            print(Error_msg)
        else:print("Test pass")
test_case = Test_Add_Count()
test_case.test_add()