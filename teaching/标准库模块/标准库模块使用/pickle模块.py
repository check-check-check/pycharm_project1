
# @Time    :
# @Author  : chen
# pickle提供了一个简单的持久化功能。可以将对象以文件的形式存放在磁盘上
"""说明：pickle模块只能在python中使用，python中几乎所有的数据类型（列表，字典，集合，类等）都可以用pickle来序列化，
pickle序列化后的数据，可读性差，人一般无法识别"""
# https://blog.csdn.net/chunmi6974/article/details/78392230
import pickle

"""
1.pickle.dump(obj, file[, protocol])序列化对象，并将结果数据流写入到文件对象中。参数protocol是序列化模式，默认值为0(待确认)，
表示以文本的形式序列化。protocol的值还可以是1或2，表示以二进制的形式序列化。
file必须以二进制可写模式打开，即“wb”
2.pickle.load(file)反序列化对象。将文件中的数据解析为一个Python对象。其中要注意的是，在load(file)的时候，要让python能够找到
类的定义，否则会报错;
file必须以二进制可读模式打开，即“rb” 
"""

import pickle
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def show(self):
        print(self.name + "_" + str(self.age))

aa = Person("JGood", 2)
aa.show()
f = open('G:\\p', 'wb')
pickle.dump(aa, f, 0)
# f.write(pickle.dumps(aa))
f.close()
# del Person #如果不注释掉del Person的话，那么会报错：意思就是当前模块找不到类的定义了
f = open('G:\\p.txt', 'rb')
bb = pickle.load(f)
f.close()
bb.show()
print("=" * 50)
