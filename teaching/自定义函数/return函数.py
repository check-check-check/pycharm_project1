# @Time    : 
# @Author  : chen
# @Time    :
# @Author  : chen
'''函数可以不用return，如果没有return返回值，函数返回的值为None
函数可以返回数字，字符串，列表，元组，字典，集合
如果返回多个值，则返回的值将以元组返回'''


# return语句代表函数执行结束，函数不执行return语句后的操作
def test():
    print("Before the return")
    return 0
    print("After the return")


print(test())
