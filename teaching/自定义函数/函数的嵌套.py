# @Time    : 
# @Author  : chen
# 函数的嵌套调用是在"函数调用中再调用其他函数"。也就是说:函数嵌套允许在一个函数中调用另外一个函数
# %%案例1
name = "flower"


def change_name():
    name = "fish"  # 局部变量的作用域只在函数内部

    def change_name2():
        name = "tree"
        print("第3层打印", name)

    change_name2()  # 调用内层函数
    print("第2层打印", name)


change_name()
print("最外层打印", name)
# %%案例2  二分查找：从一列表中找到其中某一位置。
# 定义一个无序列表
date = [21, 33, 22, 10, 9, 24, 8, 34, 53, 8, 23, 43, 1, 3, 10]
# 排序
date.sort()
print(int(len(date) / 2))


def binary_search(datesets, find_num):
    if len(datesets) > 0:
        find_nums = int(len(datesets) / 2)
        print(datesets[find_nums])
        if datesets[find_nums] == find_num:
            print("Find num:", datesets[find_nums])
        elif datesets[find_nums] > find_num:
            print("\033[31;1mgoing to left side \033[0m:", datesets[find_nums], datesets[:find_nums + 1], find_num)
            binary_search(datesets[0:find_nums], find_num)
        else:
            print("\033[32;1mgoing to right  side \033[0m:", datesets[find_nums], datesets[find_nums:], find_num)
            binary_search(datesets[find_nums + 1:], find_num)
    else:
        print("Cannot fine the num", find_num)


# 如无法理解.请执行后进行分解.
binary_search(date, 24)

# %%三元运算情况1
a = 1
b = 2
if a < b:
    c = b
else:
    c = a
print(c)
# 这样写代码非常繁琐，所以在遇到if else非常简单的时候，可以用到三元运算
a = 1
b = 2
c = b if a < b else a
print(c)
# %%三元运算情况2
# 多条语句以英文逗号隔开：每条语句都会执行，程序返回多条语句的返回值组成的元组。
a = 1
b = 2
st = print("crazyit"), 'a大于b' if a > b else "a不大于b"
print(st, type(st))
# %%三元运算情况3
# 多条语句以英文分号隔开：每条语句都会执行，程序只返回第一条语句的返回值。
a = 1
b = 2
st = print("crazyit"); x = 20 if a > b else "a不大于b"
print(st)
print(x)

# %%三元运算情况4
# 三目运算符支持嵌套，通过嵌套三元运算符，可以执行更复杂的判断。
c = 5
d = 5
# 下面将输出c等于d
print("c大于d") if c > d else (print("c小于d") if c < d else print("c等于d"))