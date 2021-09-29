# @Time    :
# @Author  : chen
"""
Python全局变量和局部变量：
定义在函数内的为局部变量，在外部访问局部变量会出现未定义的错误
定义在函数外的变量称为全局变量，可以在整个函数范围内访问
当函数中存在与全局变量重名的变量，以函数中的局部变量为准
"""
# globals() 函数会以字典类型返回当前位置的全部全局变量
# locals() 函数会以字典类型返回当前位置的全部局部变量
a = 1234
print(len(globals()))
print(globals()['a'])

# 这个方法一般用于将A函数内的变量添加到全局变量里
globals()['key'] = 'value'
print(globals()['key'])


# %% 实例1-locals()查看局部变量
def add_tcy(a, b):
    z = a + b
    print(z)
    s = locals()
    locals()['z'] = -100  # 修改局部名字空间拷贝变量无影响
    print(z)
    return s['z'], z, s


f = add_tcy(3, 4)  # z并未改变，改变的locals()拷贝的副本 
print(f)
# %% 实例2-globals()查看修改删除全局变量
import os

print('name' in globals())  # False
globals()['name'] = os.getcwd()
print('name' in globals())  # True
del globals()['name']
print('name' in globals())  # False 
# %% 实例3-globals()在命名空间中修改全局变量
x, y = 10, 20
z = x + y
print(z)  # 30
globals()['x'] = -100  # globals()修改变量x的值为-100
z = x + y
print(z)  # -80

# %% 例题：测试全局变量和局部变量
# 显示函数定义： 
lst = [0, 0]


def view_variable(locals, globals, lst=lst):
    '''仅显示变量，去除其他显示'''

    def ChooseVariable(data):
        d = {}
        for key, value in data.items():  # items() 函数以列表返回可遍历的(键, 值) 元组数组。
            if ('__' not in key) and (not isinstance(value, dict)) and ('lst' not in key):
                if 'function' in str(value):
                    value = 'fun'
                d[key] = value
                lst[1] = lst[1] + 1
                lst[0] = (lst[0] + 1) if (lst[1] % 2) == 0 else lst[0]
        return d

    print('{}.1.locals={}'.format(lst[0], ChooseVariable(locals)))
    print('{}.2.globals={}'.format(lst[0], ChooseVariable(globals)))


print(len(locals()), len(globals()))
view_variable(locals(), globals())

# %% 实例1：
g_x0 = 1  # 全局作用域
l = locals()
g = globals()
view_variable(l, g)
# 1.locals={'view_variable': 'fun', 'g_x0': 1}
# 2.globals={'view_variable': 'fun', 'g_x0': 1} 
# %% 实例2：测试全局变量和局部变量---闭包变量测试
g1 = -1000


def test_func():
    V0 = 10  # 作用域为test_func函数
    l = locals()
    g = globals()
    view_variable(l, g)


# 0.1.locals={'V0': 10}
# 0.2.globals={'view_variable': 'fun', 'g1': -1000, 'test_func': 'fun'}

def local_func():
    V0 = 20  # 作用域为本函数
    l = locals()
    g = globals()
    view_variable(l, g)


# 1.1.locals={'V0': 20}
# 1.2.globals={'view_variable': 'fun', 'g1': -1000, 'test_func': 'fun'}
def nonlocal_func():
    nonlocal V0  # 作用域为test_func函数内部
    V0 = 15
    l = locals()
    g = globals()
    view_variable(l, g)


# 2.1.locals={'V0': 15}
# 2.2.globals={'view_variable': 'fun', 'g1': -1000, 'test_func': 'fun'}
def global_func():
    global V0  # 新建global全局变量
    V0 = -1
    l = locals()
    g = globals()
    view_variable(l, g)


# 3.1.locals={}
# 3.2.globals={'view_variable': 'fun', 'g1': -1000, 'test_func': 'fun', 'V0': -1}

local_func()
print("V0=:", V0)  # V0=10
nonlocal_func()
print("V0=:", V0)  # V0=15
global_func()
print("V0=", V0)  # 同名内部优先V0=15
l = locals()
g = globals()
view_variable(l, g)
# 4.1.locals={'V0': 15, 'local_func': 'fun', 'nonlocal_func': 'fun', 'global_func': 'fun'}
# 4.2.globals={'view_variable': 'fun', 'g1': -1000, 'test_func': 'fun', 'V0': -1}

# %%测试调用
test_func()
print(V0)  # V0=-1
l = locals()
g = globals()
view_variable(l, g)
# 5.1.locals={'view_variable': 'fun', 'g1': -1000, 'test_func': 'fun', 'V0': -1}
# 5.2.globals={'view_variable': 'fun', 'g1': -1000, 'test_func': 'fun', 'V0': -1}
