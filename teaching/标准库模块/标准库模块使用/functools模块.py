# @Time    : 
# @Author  : chen
# functools 是 Python 中很简单但也很重要的模块，主要是一些 Python 高阶函数相关的函数。
"""说到高阶函数，这是函数式编程范式中很重要的一个概念，简单地说， 就是一个可以接受函数作为参数或者以函数作为
返回值的函数，因为 Python 中函数是一类对象， 因此很容易支持这样的函数式特性。"""
# %%
'''函数式编程中有个很重要的概念叫做柯里化（把接受多个参数的函数变换成接受一个单一参数的函数，并且返回接受余下的
参数而且返回结果的新函数的技术），简单地（虽然并不准确）说，就是这样地效果(Python中你可以使用partial函数实现类似的效果)：'''

from functools import partial


def add(x, y):
    return x + y


add_y = partial(add, 3)  # add_y是一个函数
print(add_y(4))

# %% partialmethod是Python3.4中新引入的装饰器，作用类似于partial, 不过仅仅作用于方法。
from functools import partialmethod


class Cell(object):
    def __init__(self):
        self._alive = False

    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)

    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)


c = Cell()
print(c.alive)  # False
print(c.set_alive())
print(c.alive)  # True
# %%
"""functools库中装饰器相关的函数是update_wrapper、wraps，还搭配WAPPER_ASSIGNMENTS和WRAPPER_UPDATES两个常量使用，
作用就是消除Python装饰器的一些负面作用。"""


def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@decorator
def add(x, y):
    return x + y


print(add)
'''可以看到被装饰的函数的名称，也就是函数的__name__属性变成了wrapper，这就是装饰器带来的副作用，实际上add函数整个变成了
decorator(add)，而wraps装饰器能消除这些副作用：'''
# %% wraps函数
from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@decorator
def add(x, y):
    return x + y


print(add)
# 会更正的属性定义在 WRAPPER_ASSIGNMENTS 中：
print()
# %% update_wrapper函数
# wraps其实是update_wrapper的特殊化，实际上wraps(wrapped)相当于partial(update_wrapper, wrapped=wrapped, **kwargs)
# 因此，上面的代码可以用update_wrapper重写如下：
from functools import update_wrapper
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return update_wrapper(wrapper, func)
@decorator
def add(x, y):
    return x + y
print(add)

# %%
import functools
def reverse_numeric(x, y):
    return y - x
sorted([5, 2, 4, 1, 3], key=functools.cmp_to_key(reverse_numeric))
# %%
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        key = cmp_to_key(lambda x, y: int(y) - int(x))
        res = ', '.join(sorted(map(str, nums), key=key))
        return res
'''注意：该函数用于将旧式的比较函数转换为关键字函数。旧式的比较函数：接收两个参数，返回比较的结果。返回值小于零则前者
小于后者，返回值大于零则相反，返回值等于零则两者相等。关键字函数：接收一个参数，返回其对应的可比较对象。
例如 sorted(), min(), max(), heapq.nlargest(), heapq.nsmallest(), itertools.groupby() 都可作为关键字
函数。'''
nums = [-1, -2, 3, 4, 9, 2, 3, 4, 5]
s = Solution()
# a = map(str, nums)
# print(list(a), type(a))  # 列表不去重
print(s.largestNumber(nums))
nums = {1, 2, 3, 4, 9, 2, 3, 4, 5}
# a = map(str, nums)
# print(list(a), type(a))  # 集合会去重
print(s.largestNumber(nums))

# %%
