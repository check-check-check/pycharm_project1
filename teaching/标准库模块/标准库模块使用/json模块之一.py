# @Time    : 
# @Author  : chen
"""JSON(JavaScript Object Notation, JS 对象标记) 是一种轻量级的数据交换格式。JSON的数据格式其实就是python里面的字典
格式，里面可以包含方括号括起来的数组，也就是python里面的列表。"""
# Json模块主要用来进行Python对象的序列化和反序列化。
"""Python对象包括：
所有Python基本数据类型，列表，元组，字典，自己定义的类，等等等等，当然不包括Python的字符串类型，把字符串或者文件鎏中的字符
串转为字符串会报错的"""
#%% Json模块提供了四个方法： dumps、dump、loads、load
"""
一. dumps 和 dump:
 dumps和dump   序列化方法
 dumps只完成了序列化为str，
 dump必须传文件描述符，将序列化的str保存到文件中"""
# dumps可以格式化所有的基本数据类型为字符串
import json
print(json.dumps([]))
print(json.dumps(1))   # 数字
print(json.dumps('1'))   # 字符串
dict1 = {"name":"Tom", "age":23}
print(json.dumps(dict1))     # 字典

#%%
a = {"name":"Tom", "age":23}
with open("test.json", "a", encoding='utf-8') as f:
    # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
    f.write(json.dumps(a, indent=4))
    #json.dump(a,f,indent=4)   # 和上面的效果一样
#%%
"""二. loads 和 load 
loads和load  反序列化方法
       loads 只完成了反序列化，
       load 只接收文件描述符，完成了读取文件和反序列化"""
import json
json.loads('{"name":"Tom", "age":23}')
with open("test.json", "r", encoding='utf-8') as f:
    aa = json.loads(f.read())
    f.seek(0)
    bb = json.load(f)    # 与 json.loads(f.read())
print(aa)
print(bb)
#%%例题1：
s = '{"name": "wade", "age": 54, "gender": "man"}'

# json.loads读取字符串并转为Python对象
print("json.loads将字符串转为Python对象: type(json.loads(s)) = {}".format(type(json.loads(s))))
print("json.loads将字符串转为Python对象: json.loads(s) = {}".format(json.loads(s)))

# json.load读取文件并将文件内容转为Python对象
# 数据文件要s.json的内容 --> {"name": "wade", "age": 54, "gender": "man"}
with open('test.json', 'r') as f:
    s1 = json.load(f)
    print("json.load将文件内容转为Python对象: type(json.load(f)) = {}".format(type(s1)))
    print("json.load将文件内容转为Python对象: json.load(f) = {}".format(s1))
#%%日常工作中最常见的就是把字符串通过json.loads转为字典，其实json的loads方法不仅可以把字符串转为字典，还可以转为任何Python对象。
print('json.loads 将整数类型的字符串转为int类型: type(json.loads("123456"))) --> {}'.format(type(json.loads("123456"))))
print('json.loads 将浮点类型的字符串转为float类型: type(json.loads("123.456")) --> {}'.format(type(json.loads("123.456"))))
print('json.loads 将boolean类型的字符串转为bool类型: type(json.loads("true")) --> {}'.format((type(json.loads("true")))))
print('json.loads 将列表类型的字符串转为列表: type(json.loads(\'["a", "b", "c"]\')) --> {}'.format(type(json.loads('["a", "b", "c"]'))))
print('json.loads 将字典类型的字符串转为字典: type(json.loads(\'{"a": 1, "b": 1.2, "c": true, "d": "ddd"}\')) --> %s' % str(type(json.loads('{"a": 1, "b": 1.2, "c": true, "d": "ddd"}'))))
#%%loads函数的参数--s
"""把一个字符串反序列化为Python对象，这个字符串可以是str类型的，也可以是unicode类型的，如果参数s是以ASCII编码的字符串，那么需要
手动通过参数encoding指定编码方式，不是以ASCII编码的字符串，是不被允许的，你必须把它转为unicode"""

#%%loads函数的参数介绍--object_hook
# object_hook参数是可选的，它会将（loads的)返回结果字典替换为你所指定的类型,这个功能可以用来实现自定义解码器，如JSON-RPC
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def toJSON(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }

    @staticmethod
    def parseJSON(dct):
        if isinstance(dct, dict):
            p = Person(dct["name"], int(dct['age']), dct['gender'])
            return p
        return dct
s = '{"name": "马云", "age": 54, "gender": "man"}'
# 测试json.loads方法的object_hook参数
p = json.loads(s, object_hook=Person.parseJSON)
# print(p)
print("json.loads 是否将字符串转为字典了: --> " + str(isinstance(p, dict)))
print("json.loads 是否将字符串转为Person对象了: --> " + str(isinstance(p, Person)))
#%% object_pairs_hook参数
"""object_pairs_hook参数是可选的，它会将结果以key-value有序列表的形式返回,形式如：[(k1, v1), (k2, v2), (k3, v3)],如果
object_hook和object_pairs_hook同时指定的话优先返回object_pairs_hook"""
s = '{"name": "马云", "age": 54, "gender": "man"}'
# 测试json.loads方法的object_pairs_hook参数
import collections
print("-" * 30 + "> test object_pairs_hook <" + "-" * 30)
p = json.loads(s, object_hook=Person.parseJSON, object_pairs_hook=collections.OrderedDict)
# p = json.loads(s, object_hook=Person.parseJSON, object_pairs_hook=Person.parseJSON)
print("json.loads 测试同时指定object_hook和object_pairs_hook,最终调用哪个参数: --> " + str(type(p)))
print("json.loads 指定object_pairs_hook结果将会返回一个有序列表 --> {}".format(p))
#%% parse_float参数
"""parse_float参数是可选的，它如果被指定的话，在解码json字符串的时候，符合float类型的字符串将被转为你所指定的，比如说你可以指定
为decimal.Decimal"""
# 测试json.loads方法的parse_float参数
import decimal
print("-" * 30 + "> test parse_float <" + "-" * 30)
p = json.loads("123.456", parse_float=decimal.Decimal)
print("json.loads 通过parse_float参数将原本应该转为float类型的字符串转为decimal类型: type(json.loads(\"123.456\", parse_float=decimal.Decimal)) --> " + str(type(p)))
print(p)
#%% parse_int参数
# parse_int参数是可选的，它如果被指定的话，在解码json字符串的时候，符合int类型的字符串将被转为你所指定的，比如说你可以指定为float
# 测试json.loads方法的parse_int参数
print("-" * 30 + "> test parse_int <" + "-" * 30)
p = json.loads("123", parse_int=float)
print("json.loads 通过parse_int参数将原本应该转为int类型的字符串转为float类型: type(json.loads(\"123\", parse_int=float)) --> " + str(type(p)))
print(p,type(p))
#%% parse_constant参数
# parse_constant参数是可选的，它如果被指定的话，在解码json字符串的时候，如果出现以以下字符串:-Infinity，Infinity，NaN那么指定的parse_constant方法将会被调用到
def transform(s):
    """
    此方法作为参数传给json.load(s)方法的parse_constant转译NAN, -Infinity,Infinity
    :param s:
    :return:
    """
    # NaN --> not a number
    if "NaN" == s:
        return "Not a Number"
    # 将负无穷大转为一个非常小的数
    elif "-Infinity" == s:
        return -999999
    # 将正无穷大转为一个非常大的数
    elif "Infinity" == s:
        return 999999
    else:
        return s

# 测试json.loads方法的parse_constant参数
print("-" * 30 + "> test parse_constant <" + "-" * 30)
print("json.loads Infinity: --> " + str(json.loads('Infinity')))
print("json.loads parse_constant convert Infinity: --> " + str(json.loads('Infinity', parse_constant=transform)))

print("json.loads -Infinity: --> " + str(json.loads('-Infinity')))
print("json.loads parse_constant convert -Infinity: --> " + str(json.loads('-Infinity', parse_constant=transform)))

print("json.loads NaN: --> " + str(json.loads('NaN')))
print("json.loads parse_constant convert NaN : --> " + str(json.loads('NaN', parse_constant=transform)))
#%%
print(json.dumps(float('-inf')))
print(json.dumps(float('nan')))
print(json.dumps(float('inf')))
