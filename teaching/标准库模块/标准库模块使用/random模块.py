# @Time    : 
# @Author  : chen
# random库是使用随机数的Python标准库
"""random库包含两类函数，常用的共8个:
--基本随机函数： seed(), random()
--扩展随机函数：randint(), getrandbits(), uniform(), randrange(), choice(), shuffle()"""
import random
#%% random.seed函数：可以在调用其他随机模块函数之前调用此函数：生成同样的结果
# 参考博客：https://blog.csdn.net/weixin_43901998/article/details/101602411
random.seed(10) #产生种子0对应的序列
print(random.random())
random.seed(10)
print(random.random())
#%% random.random函数:用于生成一个0到1的随机浮点数: 0 <= n < 1.0
print(random.random())

#%% random.randrange(m,n[,k])
# 随机选取0到100间的3的倍数：
print(random.randrange(0, 101, 3))
#%%random.getrandbits(k)
print(random.getrandbits(3))
#2位二进制：00（0），01（1），10（2），11（3）
#%% random.randint函数:用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
print(random.randint(12,20))#生成的随机数n:12<=n<=20
print(random.randint(20,20))#结果永远是20
# print(random.randint(20,10))#该语句是错误的。下限必须小于上限。
#%% random.uniform函数:用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。
print(random.uniform(10,20))
print(random.uniform(20,10))
#%% random.randrange函数，从指定范围内，按指定基数递增的集合中获取一个随机数
print(random.randrange(10, 100, 2))#结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。
print(random.randrange(10, 100, 2))#在结果上与 random.choice(range(10, 100, 2) 等效。

#%% random.choice函数：从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。
# 这里要说明一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence。
print(random.choice("学习Python"))
print(random.choice(["JGood","is","a","handsome","boy"]))
print(random.choice(("Tuple","List","Dict")))

#%% random.shuffle函数: 用于将一个列表中的元素打乱
p=["Python","is","powerful","simple","andsoon..."]
random.shuffle(p)
print(p)
#%% random.sample函数：从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
list=[1,2,3,4,5,6,7,8,9,10]
slice=random.sample(list,5)#从list中随机获取5个元素，作为一个片断返回
print(slice)
print(list)#原有序列并没有改变。