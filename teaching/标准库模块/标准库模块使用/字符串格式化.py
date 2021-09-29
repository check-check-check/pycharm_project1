# @Time    : 
# @Author  : chen
# 参考博客：https://www.cnblogs.com/panwenbin-logs/p/10813950.html
"""Python的字符串格式化有两种方式: 百分号方式、format方式。百分号的方式相对来说比较老，
而format方式则是比较先进的方式，企图替换古老的方式，目前两者并存。"""
# %% %格式
tpl = "i am %s" % "alex"
print(tpl)
tpl = "i am %s age %d" % ("alex", 18)
print(tpl)
tpl = "i am %(name)s age %(age)d" % {"name": "alex", "age": 18}
print(tpl)
tpl = "percent %.2f" % 99.97623
print(tpl)
tpl = "i am %(pp).2f" % {"pp": 123.425556, }
print(tpl)
tpl = "i am %.2f%%" % (123.425556)
print(tpl)


# %%format格式
tpl = "i am {}, age {}, {}".format("seven", 18, 'alex')
print(tpl)
tpl = "i am {}, age {}, {}".format(*["seven", 18, 'alex'])
print(tpl)
tpl = "i am {0}, age {1}, really {0}".format("seven", 18)
print(tpl)
tpl = "i am {0}, age {1}, really {0}".format(*["seven", 18])
print(tpl)
tpl = "i am {name}, age {age}, really {name}".format(name="seven", age=18)
print(tpl)
tpl = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18})
print(tpl)
tpl = "i am {1[0]}, age {1[1]}, really {1[2]}".format([1, 2, 3], [11, 22, 33])
print(tpl)
tpl = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 88888.1)
print(tpl)
tpl = "i am {:s}, age {:d}".format(*["seven", 18])
print(tpl)
tpl = "i am {name:s}, age {age:d}".format(name="seven", age=18)
print(tpl)
tpl = "i am {name:s}, age {age:d}".format(**{"name": "seven", "age": 18})
print(tpl)
tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
print(tpl)
tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
print(tpl)
tpl = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
print(tpl)
tpl = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)
print(tpl)