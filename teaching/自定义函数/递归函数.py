# @Time    : 
# @Author  : chen
'''递归函数:在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。'''
'''
递归函数特性：
1.必须有一个明确的结束条件；
2.每次进入更深一层递归时，问题规模相比上次递归都应有所减少
3.相邻两次重复之间有紧密的联系，前一次要为后一次做准备（通常前一次的输出就作为后一次的输入）。
4.递归效率不高，递归层次过多会导致栈溢出.
（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，
每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出）
'''


# %% 计算1到100之间相加之和；通过循环和递归两种方式实现

# 循环方式
def sum_cycle(n):
    sum = 0
    for i in range(1, 101):
        sum = sum + i
    return sum


# 递归方式
def sum_recu(n):
    if n > 0:
        return n + sum_recu(n - 1)
    else:
        return 0


print(sum_cycle(100))
print(sum_recu(100))


# 把上面的递归求和函数的参数改成10000就导致栈溢出！
# print(sum_cycle(10000))
# print(sum_recu(10000))

# %%对于一般递归
def normal_recursion(n):
    if n <= 1:
        return 1
    else:
        return n + normal_recursion(n - 1)


print(normal_recursion(5))

'''
编译器会执行：
5 + normal_recursion(4)
5 + 4 + normal_recursion(3)
5 + 4 + 3 + normal_recursion(2)
5 + 4 + 3 + 2 + normal_recursion(1)
5 + 4 + 3 + 3
5 + 4 + 6
5 + 10
15
'''
# 此处编译器会分配递归栈来保存中间结果
# 每一级递归都需要调用函数, 会创建新的栈,随着递归深度的增加, 创建的栈越来越多, 造成爆栈:boom
# %% 尾递归
'''尾递归：尾递归基于函数的尾调用, 每一级调用直接返回函数的返回值更新调用栈,而不用创建新的调用栈,
类似迭代的实现, 时间和空间上均优化了一般递归!'''
'''尾递归相对传统递归，其是一种特例。在尾递归中，先执行某部分的计算，然后开始调用递归，所以你可以得到当前的计算结果，
而这个结果也将作为参数传入下一次递归。这也就是说函数调用出现在调用者函数的尾部，因为是尾部，所以其有一个优越于传统
递归之处在于无需去保存任何局部变量，从内存消耗上，实现节约特性。'''

def tail_recursion(n, total=0):
    if n == 0:
        return total
    else:
        return tail_recursion(n - 1, total + n)
print(tail_recursion(5,0))

'''
此时，编译器做的工作：
tail_recursion(5,0)
tail_recursion(4,5)
tail_recursion(3,9)
tail_recursion(2,12)
tail_recursion(1,14)
tail_recursion(0,15)
15
你可以看到当前时刻的计算值作为第二个参数传入下一个递归，使得系统不再需要保留之前计算结果。
尾递归的优势就显而易见了。
'''
#%%
print(normal_recursion(998))
print(tail_recursion(998,0))
'''但是python本身不支持尾递归（没有对尾递归做优化），而且对递归的次数有限制，当递归深度超过1000时（不同的Python版本可能有所不同），会抛出异常：
分别执行:recursion(998),tail_recursion(998,0)
输出：
498501
498501
没有问题，当调用:recursion(999),tail_recursion(999,0)时，
输出：RuntimeError: maximum recursion depth exceeded
因为递归次数超出了1000'''
#%% 修改最大的递归层数
import sys
sys.setrecursionlimit(8000) #修改最大的递归层数
print(normal_recursion(2986))

