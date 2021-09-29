# @Time    : 
# @Author  : chen
# 你想让你的对象可以向和str、list、tuple一样通过下标访问元素吗？在Python就可以做到，只需要重写__getitem__方法
# 一般如果想使用索引访问元素时，就可以在类中定义这个方法（__getitem__(self, key) ）
#%% 案例1
"""
求数列1, 3, 5, 7, ········的第n项
"""
class ProblemA(object):
    def __getitem__(self, n):
        return n * 2 - 1

solu = ProblemA()
answer = solu[100] #对象[下标值]，进行这样的调用时，就会马上调用这个魔法方法__getitem__
print(answer)
#%% 案例2
class DataBase:
    def __init__(self, id, address):
        '''初始化方法'''
        self.id = id
        self.address = address
        self.d = {self.id: id,
                  self.address: address,
                  }
    def __getitem__(self, key):
        return self.d.get(key, "default")
data = DataBase(1, "192.168.2.11")
print(data[data.id], data[data.address],data['anyone'])

#%% 案例3
class DataBase:
    def __init__(self, id, address):
        '''初始化方法'''
        self.id = id
        self.address = address

    def __getitem__(self, key):
        return self.__dict__.get(key, "default")

data = DataBase(1, "192.168.2.11")
print(data["anyone"])
print(data["id"], data["address"])

#%%案例4
class STgetitem:
    def __init__(self, text):
        self.text = text

    def __getitem__(self, index):
        result = self.text[index].upper()
        return result


p = STgetitem("python")
print(p[0])
print("------------------------")
for char in p:
    print(char)