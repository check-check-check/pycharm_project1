# @Time    : 
# @Author  : chen
# @Time    :
# @Author  : chen
# 关于Python中re模块使用
import re
'''
re模块对正则表达式的使用步骤一般有三步:
    1、re.compile(正则表达式) 将正则表达式字符串编译为Pattern实例
    2、用pattern实例去处理文本并获得匹配结果（比如一个Match实例）
    3、然后用Match实例去获得信息
'''
"""
当我们在Python中使用正则表达式时，re模块内部会干两件事情：
1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
2.用编译后的正则表达式去匹配字符串;"""
"""
那么如果一个正则表达式要重复使用几千次，出于效率的考虑，我们是不是应该先把这个正则先预编译好，接下来重复使用时就不再需要
编译这个步骤了，直接匹配，提高我们的效率"""
#%% 这里先介绍几个常用的Pattern对象常用的方法：
pattern = re.compile(r'dsa')
print(pattern) # 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
mat = pattern.match('dsafwew2223')
mat2 = pattern.match('jjfdsafee')
mat3 = pattern.match('jjfdsafeedsa1', 9,)
res = mat.group()

# 1、注意这里的match(str,pos,endpos)这里pos和endpos代表匹配字符串的开头和结尾，默认是0和len(str)
"""匹配到的Match对象，我们将使用其具有的group()方法取出匹配结果。re.match方法从头开始匹配，匹配不到就返回None
pattern.match和re.match的区别是pattern.match可以指定匹配的起始位置"""
print(mat)
print(mat2)
print(mat3)
print(res)

#%% 2、search(str,pos,endpos)是查找整个字符串匹配找到的第一个，无需从头开始匹配
ser = pattern.search('erweadsafdsae')
print(ser)
print(ser.group())

#%% 3、findall(str,pos,endpos)这个方法是返回所有的子串并返回一个list
pattern2 = re.compile(r'\d+') #数字或者数字串
lst = pattern2.findall("abc111def222rst333xyz")
print(lst)

#%% 4、finditer(str,pos,endpos)找到所有匹配的子串，并返回由这些匹配结果（match object）组成的迭代器。
pattern3 = re.compile(r'\d+')
p = pattern3.finditer('abc111def222rst333xyz')
print(p)  # <callable_iterator object at 0x0000000002C5E780>是迭代器
for i in p:
    print(i.group())

# 通过match或search函数，生成 re.Match object实例，对实例进行以下group()/groups()/start()/end()/span()操作，获取信息                                # 获取相关信息
#%% 关于match object有几个常用的方法：
# 1、match.group（）：返回 match object 中的字符串。
# 在正则表达式中用于获取分段截获的字符串
# m.group() == m.group(0) == 所有匹配的字符，与括号无关
"""\w匹配单个数字、字符、汉字或者下划线"""
pattern4 = re.compile(r"(\w+) (\w+)")
m = pattern4.match("KobeBryant _, _ L")


print(m)
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.group(1, 2))

#%% 2、match.groups()： 返回由所有分组匹配到的字符串组成的 tuple。
# m.groups() == (m.group(1), m.group(2) ...)
m2 = re.match(r"(\d+)\.(\d+)", "24.1632")
print(m2.groups())

#%% 3、match.start()：没有参数时，返回匹配到的字符串的起始位置。指定参数（整数）时，返回该分组匹配到的字符串的起始位置。
print(m.start())# 默认是1
print(m.start(2))

#%% 4、match.end()：返回结束位置
print(m.end())
print(m.end(1))

#%% 5、match.span([group])：返回一个二元 tuple 表示匹配到的字符串的范围，即 (start, end)。
print(m.span())
print(m.span(2))

#%% 上面所说到的一些都是对象的函数，然而还有一些模块可以直接调用的函数
#   1、compile（）:上面介绍过了
#   2、match()
print(re.match('\w+', 'hehakhe_hdsfas').group())
#   3、search（）
# 对比match函数和search函数可发现：
# 1.match()函数只检测re是不是在string的开始位置匹配或者指定开始的位置（match函数pos参数），也就是说match()只有在0位置
# 匹配成功的话才有返回， 如果不是开始位置匹配成功的话，match()就返回none, 不能和span()、group()搭配使用，否则会报错；
# 2.search()会扫描整个string查找匹配；search()可以不从0位置开始匹配，这就是和match()的区别

print(re.match(r"(\w+) (\w+)", " Kobe Bryant, Lakers"))
print(re.match(r"(\w+) (\w+)", "Kobe Bryant, Lakers").groups())

print(re.search(r"(\w+) (\w+)", " Kobe Bryant, Lakers").groups())
print(re.search(r"(\w+) (\w+)", "Kobe Bryant, Lakers").groups())
#   4、findall()
print(re.findall('\d+', 'hafu3uhaher432'))
#   5、finditer()
k = re.finditer('\d+', 'hfasui23ihw54552i')
for i in k:
    print(i.group())

#%%
'''
    关于re.compile() 函数：它还接受可选的第二个参数，用以设置匹配模式。
    可选的匹配模式有：
    re.IGNORECASE：忽略大小写，同 re.I。
    re.MULTILINE：多行模式，改变^和$的行为，同 re.M。
    re.DOTALL：点任意匹配模式，让'.'可以匹配包括'\n'在内的任意字符，同 re.S。
    re.LOCALE：使预定字符类 \w \W \b \B \s \S 取决于当前区域设定， 同 re.L。
    re.ASCII：使 \w \W \b \B \s \S 只匹配 ASCII 字符，而不是 Unicode 字符，同 re.A。
    re.VERBOSE：详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。
    主要是为了让正则表达式更易读，同re.X。例如，以下两个正则表达式是等价的：
    (这个选项忽略规则表达式中的空白和注释，并允许使用 ’#’ 来引导一个注释。这样可以让你把规则写得更美观些。)
    a = re.compile(r"""\d +  # the integral part
                       \.    # the decimal point
                       \d *  # some fractional digits""", re.X)
    b = re.compile(r"\d+\.\d*")
'''
#%% re模块除了能搜索匹配字符串以外还可以修改字符串
# 1、split（）:一种是用re模块直接调用，一种是pattern对象调用
pattern = re.compile(r"[A-Z]+")
g = pattern.split("abcDefgHijkLmnoPqrs")
print(g)  # ['abc', 'efg', 'ijk', 'mno', 'qrs']
print(re.split(r"[A-Z]+", "abcDefgHijkLmnoPqrs"))

#%%  ['abc', 'efg', 'ijk', 'mno', 'qrs']
# 2、sub()和subn():与上面一样，一种是用re模块直接调用，一种是pattern对象调用
# sub和subn的区别在于subn返回的是一个二元tuple(返回值，替换次数)
# pattern.sub(repl, string, count=0)：count代表替换次数
# 用 repl 替换 string 中每一个匹配的子串，返回替换后的字符串。若找不到匹配，则返回原字符串。
def fun(m):
    return m.group().upper()

pattern = re.compile(r"liKE", re.I) #re.IGNORECASE：忽略大小写，同 re.I
s1 = pattern.sub(r"love", "I like you, do you like me?")
s2 = pattern.sub(fun, "I like you, do you like me?") # 我的理解是把匹配到的内容经fun函数处理后返回到所在位置
# repl参数官方解释（help(re.sub)）：
# If it is a callable, it's passed the Match object and must return a replacement string to be used
# 由此可见，fun函数的输入必须是：Match object类型；ruturn返回的被替换成的内容


s3 = pattern.subn(r"love", "I like you, do you like me?")
s4 = pattern.subn(fun, "I like you, do you like me?", 1)
print(s1)
print(s2)
print(s3)
print(s4)

# re.sub(pattern, repl, string, count=0, flags=0)：flags代表匹配模式
# subn(pattern, repl, string, count=0, flags=0)
print(re.sub(r'liKE', r"love", "I like you, do you like me?", 1, re.I))
print(re.subn(r'likE', r'love', 'I like you, do you like me?', 3, re.I))
