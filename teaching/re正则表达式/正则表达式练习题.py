# @Time    : 
# @Author  : chen
#%%例题1：
import re
def func(ret, key, value):
    ret[key] = value
    return ''
# func函数完成为字典ret增加键值
def func1(x):
    return func(ret, x.group(1), x.group(2))
ret = {}
string = 'apple pear banana meat'
# \s：Matches any whitespace character（匹配空白符）; equivalent to [ \t\n\r\f\v]
print(re.subn(r'(apple|banana)\s(\w+)\s?', func1, string))
print(ret)
#%%
print(re.subn(r'(apple)\s(\w+)?', r'', string))