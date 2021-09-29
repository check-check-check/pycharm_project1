# @Time    : 
# @Author  : chen
"""当在循环体中需要根据某一条件终止循环时，则可以使用break语句实现。如需要计算1～n的连续整数累加时，
当累加和小于等于300时，n的最大值是多少。实现该功能的代码如下。"""
i = 1
sum = 0
while True:
    sum = sum + i
    if sum > 300:
        break # 当sum<300，继续向下执行；当sum>300，中止while循环；
    i+= 1
    print(sum, i-1)
#%% 一个简单的for循环
for i in range(0, 10) :
    print("i的值是: ", i)
    if i == 2 :
        # 执行该语句时将结束循环
        break
#%% 对于带 else 块的 for 循环，如果使用 break 强行中止循环，程序将不会执行 else 块
for i in range(0, 10) :
    print("i的值是: ", i)
    if i == 2 :
        # 执行该语句时将结束循环
        break
    else:
        print('else块: ', i)
#%% 针对嵌套的循环结构来说，Python 的 break 语句只能结束其所在的循环体，而无法结束嵌套所在循环的外层循环
for i in range(0,4) :
    print("此时 i 的值为：",i)
    for j in range(5):
        print("    此时 j 的值为:",j)
        break
    print("跳出内层循环")
# 每次执行内层循环体时，第一次循环就会遇到 break 语句，即做跳出所在循环体的操作，转而执行外层循环体的代码
#%% 如果想达到 break 语句不仅跳出单前所在循环，同时跳出外层循环的目的，可先定义 bool 类型的变量来标志是否需要跳出
# 外层循环，然后在内层循环、外层循环中分别使用两条 break 语句来实现。

exit_flag = False
# 外层循环
for i in range(0, 5):#外层循环
    # 内层循环
    for j in range(0, 3):#内层循环
        print("i的值为: %d, j的值为: %d" % (i, j))
        if j == 1 :
            exit_flag = True
            # 跳出内层循环
            break
    # 如果exit_flag为True，跳出外层循环
    if exit_flag :
        break
#%%
has_power =True
times = 0
while has_power:
    print('大王叫我来巡山')
    times+= 1
    if times>=3:
        print('已经巡逻了3次，不巡逻了')
        has_power = False
    for x in range(1, 4):
        print("while循环内部的for循环："+str(x))
    else:
        print('我是for的else')
else:
    print('我是while的else')
#%%
has_power =True
times = 0
while has_power:
    print('大王叫我来巡山')
    times+= 1
    if times>=3:
        print('已经巡逻了3次，不巡逻了')
        has_power = False
    for x in range(1, 4):
        print("while循环内部的for循环："+str(x))
        if x == 2:
            break
    else:
        print('我是for的else')
else:
    print('我是while的else')