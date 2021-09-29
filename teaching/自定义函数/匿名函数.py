# @Time    : 
# @Author  : chen
# lambda函数的语法只包含一个语句，如下：lambda arg1,arg2,.....argn:expression
"""
# 关键字lambda表示匿名函数，
# 冒号:之前的a,b,c表示它们是这个函数的参数。
# 匿名函数不需要return来返回值，表达式本身结果就是返回值。
"""
# %% 带参数匿名函数
fun1 = lambda x: x ** 3  # 一个参数
fun2 = lambda x, y, z: x + y + z  # 多个参数
fun3 = lambda x, y=3: x * y  # 允许参数存在默认值
# 匿名函数调用，和一般的函数调用一样
print(fun1(1))
print(fun2(1, 2, 3))
print(fun3(1, 2))

# 直接后面传递实参
print((lambda x, y: x if x > y else y)(101, 102))

# 例题1
a = lambda x="Boo", y="Too", z="Zoo": x + y + z
print(a(y='rrr'))

# %% 无参匿名函数:
t = lambda: True  # 分号前无任何参数
print(t())


# 等价于下面的def定义的函数
def t():
    return True


print(t())

# %% 例题2
s = "this is\na\ttest1.txt"  # 建此字符串按照正常情形输出
print(s.split())  # split函数默认分割:空格，换行符，TAB
print(' '.join(s.split()))  # 用join函数转一个列表为字符串

# 等价于:
fun = lambda x: ' '.join(x.split())
print(fun(s))

# %% 例题3
a = lambda *z: z  # *z返回的是一个元组
print(a())
a = lambda **z: z  # *z返回的是一个字典
print(a())
# %%例题4
# lambda返回的值，结合map,filter,reduce使用
print(list(filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6])))
print([x for x in [1, 2, 3, 4, 5, 6] if x % 3 == 0])

# %%例题5
# lambda嵌套到普通函数中,lambda函数本身做为return的值
def increment(n):
    return lambda x: x + n
print(increment(5)(2))
# %%例题6
# 和列表联合使用
L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]
for f in L:
    print(f(2))
# 或者，这样调用：
print(L[0](2))
# %%例题7
# 和字典结合使用:
dic = { 'A': lambda: 2*2,
        'B': lambda: 2*4,
        'C': lambda: 2*8}
print(dic['B']())
# %%例题7:和map及list联合使用
