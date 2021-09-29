# @Time    : 
# @Author  : chen
#%% 1.替代内层for循环
# 如果生成器函数需要产出另一个生成器生成的值，传统的解决方法是使用嵌套的for循环：
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i
s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))
#%% chain 生成器函数把操作依次交给接收到的各个可迭代对象处理。
# Python3.3之后引入了新语法：
def chain(*iterables):
    for i in iterables:
        yield from i
print(list(chain(s, t)))
"""yield from 完全代替了内层的 for 循环。
yield from x 表达式对 x 对象所做的第一件事是，调用 iter(x)，从中获取迭代器。因
此，x 可以是任何可迭代的对象。在这个示例中使用 yield from代码读起来更顺畅，不过感觉更像是语法糖。"""
#%%例子1：我们有一个嵌套型的序列，想将它扁平化处理为一列单独的值。
from collections import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x
items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)
"""
1.collections.Iterable是一个抽象基类，我们用isinstance(x, Iterable)检查某个元素是否是可迭代的.如果是的话,那么就用yield from
  将这个可迭代对象作为一种子例程进行递归。最终返回结果就是一个没有嵌套的单值序列了。
2.代码中额外的参数ignore types和检测语句isinstance(x, ignore types)用来将字符串和字节排除在可迭代对象外，防止将它们再展开
  成单个的字符。
3.如果这里不用yield from的话，那么就需要另外一个for来嵌套，并不是一种优雅的操作"""
#%% 例子2：利用一个Node类来表示树结构
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)
# __iter__代表一个Pyton的迭代协议，返回一个迭代器对象,就能迭代了;depth_frist返回一个生成器