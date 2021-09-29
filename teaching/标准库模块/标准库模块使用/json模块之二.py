# @Time    : 
# @Author  : chen
# json.dumps方法
# %% obj参数--要序列化的Python对象
# %% skipkeys=False参数
"""
是否跳过要序列化的对象中字典元素的key不是基本类型的数据；
如果为True，则跳过，如果为False，将抛出TypeError异常。"""
import json

emp_info = {'name': 'bob', b'age': 24}  # 包含key为bytes类型的元素
print(json.dumps(emp_info, skipkeys=True))  # skipkeys参数为默认值False
# %%ensure_ascii=True参数
"""是否将要序列化的对象中的字符串中的非ascii字符进行转义。如果该参数为True，
    则将字符串中的非ascii字符转义成unicode字符串，否则，将不会进行转义。"""
message = '我爱Python3'
print(json.dumps(message, ensure_ascii=False))
# %% check_circular=True
"""是否进行容器类型的循环引用检查。如果该参数设置为False，则不进行检查，但是可能会引发OverflowError或更严重的情况。
如果该参数设置为True，则将进行容器类型的循环引用检查，并在发现循环引用时抛出异常。"""
emp_dict = {'id': 1, 'dept': 'sales'}
emp_dict['info'] = emp_dict  # 字典中包含循环引用
print(json.dumps(emp_dict, check_circular=False))  # 默认进行循环引用的检查，将引发ValueError异常
# %% allow_nan=True参数
"""
是否允许序列化超出范围的float类型的值（如float('inf')、float('-inf')、float('nan')）。
如果该参数设置为True，则上面列出的那些值将依次使用JavaScript中等价的值（Infinity、-Infinity、NaN）来进 行替代；
如果该参数设置为False，并且要序列化的对象中出现了那些超出范围的值，则将引发ValueError异常。"""
num_list = [2, 5, float('inf'), float('-inf'), float('nan')]
print(json.dumps(num_list))  # allow_nan的值默认为True，列表中后三个值将被替换为js中等价的值
print(json.dumps(num_list, allow_nan=False))  # allow_nan设置为False，引发ValueError异常
# %%indent=None参数
"""是否在数组元素和对象成员前增加缩进以便使格式更加美观。如果该参数设置为大于等于1的整数，则添加换行符和对应数量的空格表示
缩进，如果设置为0，则表示只添加换行符，如果设置为None，则表示无缩进。"""
response = {'status': 'success', 'code': 200, 'data': ['002', 'json', 5000]}
print(json.dumps(response))  # 默认值None，不缩进
print(json.dumps(response, indent=0))  # 设置为0，则只添加换行
print(json.dumps(response, indent=4))  # 设置为4，添加换行和缩进
# %% separators=None参数
"""设置Json中各项之间、对象的键和值之间的分隔符；该参数必须是一个2元组，元组第一个元素表示Json数据中各项之间的分隔符，
元组的第二个元素表示Json对象的键和值之间的分隔符。默认的分隔符为（’,’, ‘:’）"""
response = {'status': 'success', 'code': 200, 'data': ['002', 'json', 5000]}
print(json.dumps(response))
print(json.dumps(response, separators=(';', '!')))
print(json.dumps(response, indent=4, separators=(';', '!')))
# %% default=None参数
"""指定一个函数，用来将不可进行序列化的Python对象转化为可序列化的Python对象。"""
print(json.dumps(b'hello world', default=list))
print(json.dumps(b'hello world'))
# %% sort_keys=False参数
"""是否要将对象中字典元素按照key进行排序。默认为False，即不进行排序，若指定为True，则会进行排序。"""
emp_info = {'name': 'bob', 'age': 23, 'dept': 'sales', 'gender': 'male'}
print(json.dumps(emp_info, indent=4, sort_keys=True))  # 按照key排序
# %%cls=None参数
"""指定一个定制的JSONEncoder的子类（例如，重写了.default()方法用来序列化附加的类型），指定该参数时请使用cls关键字参数。
如果未指定该参数，则将使用默认的JSONEncoder。"""
import json
class IteratorEncoder(json.encoder.JSONEncoder):
    def default(self, o):
        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable) #序列化成指定类型：列表
        return super().default(self, o) #否则不改变，继承json.encoder.JSONEncoder类，不做改变


def get_nums(n):
    if not isinstance(n, int):
        raise TypeError('Expected int object')
    while n > 0:
        yield n
        n -= 1
p=json.dumps(get_nums(10), indent=4, cls=IteratorEncoder)
print(p, type(p))

