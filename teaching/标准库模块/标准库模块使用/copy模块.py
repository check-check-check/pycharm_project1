# @Time    : 
# @Author  : chen
"""Python中的赋值语句不复制对象，它们在目标和对象之间建立索引。对于可变项目或可变项目的集合，有时需要一个副本，
以便可以更改一个副本而不更改其他副本。该模块提供通用的浅层和深层copy操作。"""
#%%浅copy
"""为什么有赋值还要copy呢？当有一个需求是要把一个数据放到我的程序里进行修改操作，但是还要保持原始数据不变。这个时候
就需要我们的copy登场了
先提一个需求，我的程序需要对一个数据进行修改，但是我又要保持这个数据和修改之前保持一致。那我们怎么操作呢？"""
import copy
a = ['111', '222']  # 我们不对变量a进行修改，因为要保持数据和修改之前一致
b = a
b[0] = '333'
print(a, b)

# copy就是起到了这个作用
a = ['111', '222']
b = copy.copy(a)
b[0] = '333'
print(a, b)
#%% 从上面的例子可以看出引用和copy的区别，但是这还不够，看下面的例子
a = ['111', '222', ['333', '444']]
b = copy.copy(a)
b[2][0] = '555'
print(a, b)
# ['111', '222', ['555', '444']] ['111', '222', ['555', '444']]
# 我们的目的又达不到了，如何是好
#%% 深copy
# 手动deep copy
a = ['111', '222', ['333', '444']]
# 递归copy
def deep_copy(copy_list):
    b = list()
    for i in copy_list:
        if isinstance(i, list):
            i = deep_copy(i)
        b.append(i)
    return b
b = deepp_copy(a)
b[2][0] = '555'
print(a, b)
a = ['111', '222', ['333', '444']]
b = copy.deepcopy(a)
b[2][0] = '555'
print(a, b)
"""从这个例子里可以看出来浅copy和深copy的区别：
浅copy：复制父对象，子对象仍然使用引用的方式。深copy：复制了对象和对象的所有子对象。"""
#%%
"""浅copy和深copy的区别只与复合对象有关(对象包含其他对象，如列表或类实例)
浅copy构造了一个新的复合对象，然后(尽可能地)将原始对象的引用插入。
深copy构造了一个新的复合对象，然后递归地将原始对象的副本插入。
那么问题来了：递归的将原始对象的副本插入，如果这个列表的深度是无限的会怎么样？"""
a = ['111', '222', ['333', '444', ['555', '666']]]
a.append(a)
def deep_copy(copy_list):
    b = list()
    for i in copy_list:
        if isinstance(i, list):
            if i is copy_list:
                pass
            else:
                i = deep_copy(i)
        if i is copy_list:
            b.append(b)
        else:
            b.append(i)
    return b
""""deep_cope函数根据copy_list重构列表b"""
c = deep_copy(a)
c[2][2][0] = '777'
print(a)
print(c)
