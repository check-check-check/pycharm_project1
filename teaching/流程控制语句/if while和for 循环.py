# @Time    : 
# @Author  : chen
#%% if 、while和for 循环
"""
1.if：语句的判断条件可以用>（大于）、<(小于)、==（等于）、>=（大于等于）、<=（小于等于）来表示其关系。
如果条件成立，执行条件后的代码块内容，不成立，直接跳过代码块；
代码只执行一次；
2.while：用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。判断条件可以
是任何表达式，任何非零、或非空（null）的值均为true。
在给定的判断条件为 true 时执行循环体，否则退出循环体。
3.for：for循环可以遍历任何序列的项目，如一个列表或者一个字符串；
"""
# %% if、while、for的区别
# 假设:需要用代码实现一个判断：输入一个水果的名字，假设水果是属于一个列表中的数据，则输出：Good！
# 使用if、While、for可以达到同样的效果：
# if语句实现判断：
fruit = ['banana', 'apple', 'orange']
if 'apple' in fruit:
    print('Good！')
# while语句实现判断：
fruit = ['banana', 'apple', 'orange']
while 'apple' in fruit:
    print('Good！')
    break
# for语句实现:
fruit = ['banana', 'apple', 'orange']
for i in fruit:
    if i == 'apple':
        print('Good！')

#%% break语句

# 1.假设while语句没有break：
while 'apple' in ['banana', 'apple', 'orange']:
    print ('Good!')
# while的运行结果则会出现无限循环，如果不强制停止，则程序无法停止耗用大量内存。

# 2.假设for语句假设无break，可以看到for循环是遍历列表中所有的数据项，遍历结束后就停止执行了。
fruit = ['banana', 'apple', 'orange']
for i in fruit:
    if i == 'apple':
        print('Good！')
