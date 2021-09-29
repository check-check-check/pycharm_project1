# @Time    : 
# @Author  : chen
class DataTest:
    def __init__(self, id, address):
        self.id = id
        self.address = address
        self.d = {self.id: 1,
                  self.address: "192.168.1.1"
                  }

    def __getitem__(self, key):
        return "hello"

data = DataTest(1, "192.168.2.11")
print(data[2])

#%%
class Tag:
    def __init__(self, id):
        self.id = id

    def __getitem__(self, item):
        print('这个方法被调用')
        return self.id


a = Tag('This is id')
print(a, a.id)
print(a[0])