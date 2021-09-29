# @Time    : 
# @Author  : chen
# %% help：返回对象的帮助信息
print(help(str))
print(help(str.split))
# %% dir：返回对象或者当前作用域内的属性列表
import math
print(dir(math))
# %% id：返回对象的唯一标识符
a = 'some text'
print(id(a))
# %% hash：获取对象的哈希值
print(hash('good good study'))
# %% type：返回对象的类型，或者根据传入的参数创建一个新的类型
print(type(1))  # 返回对象的类型
# %% len：返回对象的长度
print(len('abcd'))  # 字符串
print(len(bytes('abcd', 'utf-8')))  # 字节数组
print(len((1, 2, 3, 4)))  # 元组
print(len([1, 2, 3, 4]))  # 列表
print(len(range(1, 5)))  # range对象
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4}))  # 字典
print(len({'a', 'b', 'c', 'd'}))  # 集合
print(len(frozenset('abcd')))  # 不可变集合
# %% ascii：返回对象的可打印表字符串表现方式
print(ascii(1), type(ascii(1)))
print(ascii('&'))
print(ascii(9000000))
print(ascii('中文'))  # 非ascii字符
# %% format：格式化显示值
# 格式：format(value[, format_spec])
# 字符串可以提供的参数 's' None
# format(format('some string','o'))
# 1. 如果参数format_spec未提供，则和调用str(value)效果相同，转换成字符串格式化。
print(format(3.1415936), type(format(3.1415936)))
# 2. 对于不同的类型，参数format_spec可提供的值都不一样
# 字符串可以提供的参数 's' None
print(format('some string', 's'))  # 's'代表字符串类型
# 3. 整形数值可以提供的参数有 'b' 'c' 'd' 'o' 'x' 'X' 'n' None
print(format(3, 'b'))  # 转换成二进制
print(format(97, 'c'))  # 转换unicode成字符
print(format(11, 'd'))  # 转换成10进制
print(format(11, 'o'))  # 转换成8进制
print(format(11, 'x'))  # 转换成16进制 小写字母表示
print(format(11, 'X'))  # 转换成16进制 大写字母表示
print(format(11, 'n'))  # 和d一样
print(format(11))  # 默认和d一样

# 4. 浮点数可以提供的参数有 'e' 'E' 'f' 'F' 'g' 'G' 'n' '%' None
print(format(314159267, 'e'))  # 科学计数法，默认保留6位小数
print(format(314159267, '0.2e'))  # 科学计数法，指定保留2位小数
print(format(314159267, '0.2E'))  # 科学计数法，指定保留2位小数，采用大写E表示
print(format(314159267, 'f'))  # 小数点计数法，默认保留6位小数
print(format(3.14159267000, 'f'))  # 小数点计数法，默认保留6位小数
print(format(3.14159267000, '0.8f'))  # 小数点计数法，指定保留8位小数
print(format(3.14159267000, '0.10f'))  # 小数点计数法，指定保留10位小数
print(format(3.14e+1000000, 'F'))  # 小数点计数法，无穷大转换成大小字母


# %% vars：返回当前作用域内的局部变量和其值组成的字典，或者返回对象的属性列表
# 作用于类实例
class My():
    def __init__(self, name):
        self.name = name

    def test(self):
        print(self.name)

# vars(My)#返回一个字典对象，他的功能其实和  My.__dict__  很像
a = My('chen')
for key, value in vars(a).items():
    print(key, ':', value)

