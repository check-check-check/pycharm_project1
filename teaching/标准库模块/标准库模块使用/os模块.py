# @Time    : 
# @Author  : chen
# OS模块简单的来说它是一个Python的系统编程的操作模块，可以处理文件和目录这些我们日常手动需要做的操作。
# %%第一个：系统操作
import os
import sys
print(os.sep) #返回路径各部分之间的分隔符
print(os.name) #返回当前操作系统名称('posix', 'nt', 'os2', 'mac', 'ce', 'riscos'),windows为'nt'，linux为'posix'
print(os.getenv('path')) #读取环境变量名称

# os.getcwd():该方法用于获取执行py文件的位置空间，可以理解为当前的执行目录(the current working directory)，完全与py文件所在的位置无关
print(os.getcwd()) #获取当前文件所在路径（目录）,pycharm里面默认的工作目录是你项目的工作目录

print(os.path.basename(__file__)) #获取当前脚本的名字

print(sys.path[0])
print(os.path.abspath(sys.argv[0]))
print(os.path.realpath(sys.argv[0]))

print(os.curdir) #返回的'.'表示当前目录
#%% 获取路径的几种方法，谨慎使用
import os
import sys
path1 = os.getcwd()
print("(1) os.getcwd() path is %s" % path1)
path2 = os.path.abspath('.')
print("(2) os.path.abspath('') path is %s" % path2)
# print("(2) os.path.abspath('') path is %s" % os.path.abspath(''))
path3 = os.path.abspath(os.path.dirname(__file__))
print("(3) os.path.abspath('') path is %s" % path3)
# sys.argv列表第一个元素存储的是当前文件所在的目录
print(sys.argv[0])
path4 = os.path.abspath('')
print("(4) abs path is %s" % path4) #sys.argv[0]表示代码本身文件路径


# %%第二个：目录操作-增删改查
current_dir = os.getcwd()
all_files = os.listdir(current_dir) #返回指定目录下的所有文件和目录名
print(all_files)
print(os.path.exists(current_dir)) #判断文件或目录是否存在
#判断
for i in all_files:
    print(os.path.abspath(i)) #获得绝对路径
    print(os.path.isdir(i)) #判断目录是否存在
    print(os.path.isfile(i))  # 判断文件是否存在
    print(os.path.getsize(i))  # 返回文件大小
print(os.path.basename(current_dir))#返回文件名, 等价于：print(os.path.split(current_dir)[1])
print(os.path.dirname(current_dir)) #返回文件路径，等价于：print(os.path.split(current_dir)[0])

#%%例题1：判断一个路径下的内容是一个文件，还是一个目录
import os
current_dir = os.getcwd()
print(current_dir)
dirs= os.path.dirname(current_dir)
print(dirs)
if os.path.exists(dirs):
    files= os.listdir(dirs)
    # print(files)
    for i in files:
        # 拼接了路径
        fullpath = os.path.join(dirs,i)
        if os.path.isfile(fullpath):
            print(fullpath+'：是一个文件')
        else:
            print(fullpath+'：是一个目录')
#%% 例题2：创建目录，做自动化测试时存放测试报告，目录
import os
current_dir = os.getcwd()
new_dir = current_dir + 'v1'
print(new_dir)
#判断目录是否存在
if not os.path.exists(new_dir):
    os.makedirs(new_dir)
print('%s是否创建成功：%s' % (new_dir, os.path.exists(new_dir)))
#%% 实例3：打印当前目录中包含'os'的文件，已经打印出绝对路径
"""
思路：
第一步：获取当前路径下的文件或者文件夹
第二步：循环文件，判断是否问文件，如果是文件，就判断是否包含'os'字符串，然后打印
"""
import os
current_dir = os.getcwd()
for i in os.listdir(current_dir):
    if os.path.isfile(i):
        if '模块' in i:
            print(i)
#或者
print([i for i in os.listdir(current_dir) if os.path.isfile(i) and '模块' in i])
#%% 实例4：将文件夹下所有图片名称加上'_fc'
import os
import time
def change_name(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path)  # 分割出目录与文件
        lists = file_path[1].split('.')  # 分割出文件与文件扩展名
        file_ext = lists[-1]  # 取出后缀名(列表切片操作)
        img_ext = ['bmp', 'jpeg', 'gif', 'psd', 'png', 'jpg']
        if file_ext in img_ext:

            os.rename(path, file_path[0] + '/' + lists[0] + '_fc.' + file_ext)
            i += 1  # 注意这里的i是一个陷阱
        # 或者
        # img_ext = 'bmp|jpeg|gif|psd|png|jpg'
        # if file_ext in img_ext:
        #    print('ok---'+file_ext)
    elif os.path.isdir(path):
        for x in os.listdir(path):
            change_name(os.path.join(path, x))  # os.path.join()在路径处理上很有用
img_dir = 'D:\\xx\\xx\\images'
img_dir = img_dir.replace('\\', '/')
start = time.time()
i = 0
change_name(img_dir)
c = time.time() - start
print('程序运行耗时:%0.2f' % (c))
print('总共处理了 %s 张图片' % (i))