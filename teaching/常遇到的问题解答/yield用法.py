# @Time    : 
# @Author  : chen
"""首先，如果你还没有对yield有个初步分认识，那么你先把yield看做“return”，这个是直观的，它首先是个return，普通的return
是什么意思，就是在程序中返回某个值，返回之后程序就不再往下运行了。看做return之后再把它看做一个是生成器（generator）的
一部分（带yield的函数才是真正的迭代器），好了，如果你对这些不明白的话，那先把yield看做return,然后直接看下面的程序，你
就会明白yield的全部意思了"""
#%%
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)
g = foo()
print(next(g))
# 1.程序开始执行以后，因为foo函数中有yield关键字，所以foo函数并不会真的执行，而是先得到一个生成器g(相当于一个对象)
# 2.直到调用next方法，foo函数正式开始执行，先执行foo函数中的print方法，然后进入while循环
# 3.程序遇到yield关键字，然后把yield想想成return,return了一个4之后，程序停止，并没有执行赋值给res操作，此时next(g)语句执行
# 完成，所以输出的前两行（第一个是while上面的print的结果,第二个是return出的结果）是执行print(next(g))的结果，
print("*"*20)
print(next(g))
# 4.又开始执行下面的print(next(g)),这个时候和上面那个差不多，不过不同的是，这个时候是从刚才那个next程序停止的地方开始执行的，
# 也就是要执行res的赋值操作，这时候要注意，这个时候赋值操作的右边是没有值的（因为刚才那个是return出去了，并没有给赋值操作的左边
# 传参数），所以这个时候res赋值是None,所以接着下面的输出就是res:None
print("*"*20)
print(next(g))
# 5.程序会继续在while里执行，又一次碰到yield,这个时候同样return出4，然后程序停止，print函数输出的4就是这次return出的4.
"""带yield的函数是一个生成器，而不是一个函数了，这个生成器有一个函数就是next函数，next就相当于“下一步”生成哪个数，这一次的next开始的
地方是接着上一次的next停止的地方执行的，所以调用next的时候，生成器并不会从foo函数的开始执行，只是接着上一步停止的地方开始，然后遇到
yield后，return出要生成的数，此步就结束。"""
#%%
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(g.send(7))
#%% 问题1：上面那个res的值为什么是None，这个变成了7?
"""这是因为，send是发送一个参数给res的，因为上面讲到，return的时候，并没有把4赋值给res，下次执行的时候只好继续执行赋值操作，只好赋值
为None了，而如果用send的话，开始执行的时候，先接着上一次（return 4之后）执行，先把7赋值给了res,然后执行next的作用，遇见下一回的
yield，return出结果后结束。"""
#%% 问题2：为什么用这个生成器，是因为如果用List的话，会占用更大的空间
for n in range(1000):
    a=n
# 这个时候range(1000)就默认生成一个含有1000个数的list了，所以很占内存。
# 这个时候你可以用刚才的yield组合成生成器进行实现，也可以用xrange(1000)这个生成器实现yield组合：
def foo(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num
print(foo(0))
for n in foo(0):
    print(n)
#%%
import collections
def flatten(items, ingore_types=(str, bytes)):
    for x in items:
        # isinstance(x, collections.Iterable) 检查是否有某个元素是可迭代的；
        # 如果有，那么就用yield from将这个可迭代对象作为一种子例程进行递归，它将所有的值都产生出来
        if isinstance(x, collections.Iterable) and not isinstance(x, ingore_types):
            # not isinstance(x, ingore_types)是为了避免将字符串和字节串解释为可迭代对象，进而将他们展开为单独的一个个字符
            yield from flatten(x) #
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)