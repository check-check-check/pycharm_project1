# @Time    : 
# @Author  : chen
#%%
# 清空pickler的“备忘”，使用Pickler实例在序列化对象的时候，它会“记住”已经被序列化的对象引用，所以对同一对象多次调用dump(obj)，
# pickler不会“傻呼呼”的去多次序列化。
import pickle
import io
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name + "_" + str(self.age))

aa = Person("Battier", 6)
aa.show()
fle = io.BytesIO()
pick = pickle.Pickler(fle)
pick.dump(aa)
val1 = fle.getvalue()
print(len(val1))

# pick.clear_memo()
pick.dump(aa)
val2 = fle.getvalue()
print(len(val2))
fle.close()
print("=" * 50)
#%%
"""
3.pickle.dumps(obj[, protocol])函数的功能：将obj对象序列化为string形式，而不是存入文件中。
4.pickle.loads(string)函数的功能：从string中读出序列化前的obj对象。"""
import pickle
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def show(self):
        print(self.name + "_" + str(self.age))
aa = Person("JGood", 2)
string = pickle.dumps(aa)
print(string)
#%% 代码示例：
import pickle as p
new_str = "We'd better struggle for the future rather than regret for the past."
new_list = list(map(lambda x: chr(x), range(65, 91)))
new_dict = {1: "a", 2: "b"}

# 使用dump()将数据序列化到文件中
fp = open("pickle.txt", "wb")
p.dump(new_str, fp)
p.dump(new_list, fp)
p.dump(new_dict, fp)
fp.close()
print("=" * 50)

# 使用load()将数据从文件中序列化读出(顺序读取，先存储的先读出)
fp = open("pickle.txt", "rb")
data1 = p.load(fp)
print(data1)
data2 = p.load(fp)
print(data2)
data3 = p.load(fp)
print(data3)
# data4=p.load(fp)
# print (data4)          #data4赋值时会报异常EOFError: Ran out of input
fp.close()
print("=" * 50)

# 使用dumps()将数据转化为只有python语言认识的字符串
p_str = p.dumps(data1)
print(p_str)
print("=" * 50)

# 使用loads()将pickle数据转换为python的数据结构
mes = p.loads(p_str)
print(mes)
print("=" * 50)