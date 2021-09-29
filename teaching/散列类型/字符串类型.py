# @Time    : 
# @Author  : chen
# %%
str = '你好，世界！Hello World!'
print(str[1])

print(len(str))  # 字符串长度
print(str.index('H'))  # 第一次出现'H'字符的位置
print(str.index('世界'))
print(str.index(' '))  # 空格的位置
print(str.upper())  # 转换成大写字母
print(str.lower())  # 转换成小写字母
print(str.capitalize())  # 第一个字母变成大写,其他字母变小写
print(str.find('H', 0, -1))  #
print(str.center(40, '*'))
print(str.count('!', 0))  #
print(str.endswith('!', 0, len(str)+1)) #以什么结尾，判断结果是否为真或者假
print(str.startswith('你')) #以什么开头，判断结果是否为真或者假
print(str.swapcase()) #字符串大小写翻转

print(str.isalnum()) #是否字母数字组成
str1='  ALi Lang  '
print(str1.casefold())  #将字符串中的所有大写字母转换为小写字母
print(str1.lstrip()) #去除左边空格、tab键、换行符
print(str1.rstrip()) #去除右边空格、tab键、换行符
#%% strip()会去除给定字符串的指定字符，指定字符可以是一个或多个，去除从左右分别进行，没有则忽略
s = '   ===Python==='
print(s.strip(' ')) #去空格，左侧空格被去除，右侧无空格，忽略
# print(s.strip(' =')) #去空格和=
# print(s.strip(' =n'))#去空格，=和n
# print(s.strip('= ')) #类似case2，去空格和=，可以看到指定chars次序不影响结果
# print(s.strip('n')) #尝试直接去除n，无效，亦不报错
print(s.strip('P'))
#%%replace函数
s='hello python,hello world,hello c++,hello java!'
print(s.replace('hello', ''))
print(s) #python中string是不可变的
print(s.replace('hello', '你好', 2))
print(s.replace('hhh','haha')) #要替换的'wahaha'子串不存在，直接返回原字符串
#%% split(seq,maxsplit)函数 可以通过指定的字符串对字符串进行分割，分割之后返回的是一个列表
string='1;2;3;4;5;6;7;8;9'
#seq 指定的分割字符  maxsplit 最大的分割次数 不指定默认全部分割
rs=string.split(';')
print(rs)

#%% str.join（iterable）函数:可以使用str字符串中的字符来连接join()中的list、字符串和字典
s = 'abcd efg'
print(' '.join(s))
s1 = ['h', 'e', 'llo']
print(''.join(s1))

s2 ={'h': 1, 'e': 2, 'llo': 3}
print(''.join(s2.keys()))
# print(''.join(s2.values()))

#%%
a = "i,am,a,boy,in,china"
print(a.find('china'))
print (a.find('i',a.find('china')))
print (a.rfind('i'))

