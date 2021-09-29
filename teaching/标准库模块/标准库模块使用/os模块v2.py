# @Time    : 
# @Author  : chen
#os模块
import os
import time
class OS_dir(): #在Python2中这个object一定要写,但是在Python3中可写可不写(默认就继承了object)
    def __init__(self):
        self.path = os.getcwd() #当前路径
        self.time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time())) #当前日期

    #创建文件夹
    def mkdir(self, name):
        file = self.path + '\\' + name + self.time
        if not os.path.exists(file):
            os.mkdir(file)
            print(file, '创建成功！')
        else:
            print(file, '目录已存在')

    #重命名文件夹
    def rename(self, old_name, new_name):
        old_file = self.path + '\\' + old_name + self.time
        new_file = self.path + '\\' + new_name + self.time
        try:
            if not os.path.exists(old_file):
                print(old_file, '搜索不到该目录！')
            else:
                os.rename(old_file, new_file)
                print(new_file, '目录重命名成功！')
        except FileExistsError as e:
            print('请修改！重命名目录名称已存在！', e)

    #删除文件夹
    def rmdir(self, name):
        file = self.path + '\\' + name + self.time
        if not os.path.exists(file):
            print(file, '搜索不到该目录！')
        else:
            os.rmdir(file)
            print(file, '该文件夹已删除！')

if __name__=='__main__':
    #执行
     o = OS_dir() #实例化一个类
     o.mkdir('新建')
     time.sleep(2)
     o.rename('新建', '重命名')
     time.sleep(2)
     # o.rmdir('重命名')

