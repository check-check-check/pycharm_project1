# @Time    : 
# @Author  : chen
# 第3关 从标准类派生
class ChangeAbs(int):
    def __new__(cls, val):
        # 填入使用super()内建函数去捕获对应父类以调用它的__new__()方法来计算输入数值的绝对值的代码
        # 求一个数的绝对值的函数为abs()
        # 返回最后的结果
        ########## Begin ##########
        return super(ChangeAbs, cls).__new__(cls, abs(val))
        ########## End ##########


obj1 = ChangeAbs(-2)
print(obj1)


class SortedKeyDict(dict):
    def keys(self):
        # 填入使用super()内建函数去捕获对应父类使输入字典自动排序的代码
        # 返回最后的结果
        ########## Begin ##########
        # return sorted(super(SortedKeyDict,self).keys())
        return sorted(super(SortedKeyDict, self).keys())
        ########## End ##########
obj2 = ChangeAbs(-2)
print(obj2)