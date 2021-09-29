# @Time    : 
# @Author  : chen
'''全局变量和局部变量的区别在于作用域，全局变量在整个py文件中声明，全局范围内可以使用；
局部变量是在某个函数内部声明的，只能在函数内部使用，如果超出使用范围（函数外部），则会报错。'''
School = "xcxy college"
Names = ["Li", "Wang", "Xu"]
Names_tuple = (1, 2, 3, 4)
A = 100
# %% 在函数内部，如果局部变量与全局变量变量名一样，则优先调用局部变量。

def func():
    A = 250
    print(A)
print(A)  # 打印全部变量
func()  # 局部变量
print(A)

#%%如果想在函数内部改变全局变量，需要在前面加上global关键字，在执行函数之后，全局变量值也会改变。
def func():
    global A
    A = 200
    print(A)

print(A)    # 打印全局变量
func()      # 局部变量
print(A)   # 改变后的全局变量


# %%如果全局变量是列表类型，可以通过list的列表方法去对列表进行修改，并且可以不用global来声明。
Names = ["Li", "Wang", "Xu"]
def change_name():
    Names[0] = "chen"
    print("inside func：\n", Names)


print(Names)
change_name()
print(Names)

# %%
def change_name(name):
    global School
    School = "大数据学院"
    print("before change：", name, School)
    name = "wang"  # 这个函数就是这个变量的作用域
    age = 23
    print("after change:", name)


print("school:", School)  #函数执行前
name = "zhao"
change_name(name)
print("school:", School)  #函数执行后
print(name)
# print("age:", age) #局部变量只能通过函数去访问


