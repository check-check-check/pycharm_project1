# @Time    : 
# @Author  : chen
#函数无返回值的情况
import  time #导入time库

def logger():

    time_format = '%Y-%m-%d %x' # 年-月-日 时分秒
    time_current = time.strftime(time_format) #调用time库下的strftime函数将本地时间转化成字符串格式的时间
    with open('a.txt','a+') as f: #文档操作，抽取句柄，设置成a+模式：可读写文件【可读；可写；可追加】
        f.write('%s end action\n' %time_current)

def test1():
    print('in the test1')
    logger()
def test2():
    print('in the test2')
    logger()

def test3():
    print('in the test3')
    logger()

test1()
test2()
test3()