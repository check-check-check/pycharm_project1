# @Time    : 
# @Author  : chen
import random
def roll(sides=6):
    """
    投掷一次骰子并返回点数。
    sides：骰子有多少面，默认为6。"""

    '*** 在这里补充你的代码 ***'
    '*** 随机产生1-6之间的整数 ***'
    '*** 提示，查阅random的randint函数的文档 ***'
    num_rolled = random.randint(1, sides)
    return num_rolled


def main():
    sides = 6
    stop = False
    '*** 在这里补充你的代码 ***'
    '*** 修改while循环的条件，使用stop变量控制循环的结束 ***'
    while not stop:
        user_in = input('试试手气？ 回车=掷骰子， Q=退出')
        '*** 在这里补充你的代码 ***'
        '*** 修改if的条件，根据用户的选择做决定 ***'
        '*** 注意，用户输入Q，无论大小写都可以退出 ***'
        if user_in.lower() == 'q': #转换字符串中所有大写字符为小写
            stop = True
        else:
            num_rolled = None
            '*** 在这里补充你的代码 ***'
            '*** 调用roll函数来掷骰子 ***'
            num_rolled = roll(sides)
            print('你掷出了 %d 点' % num_rolled)
    print('欢迎下次再来')

"""
__name__ == “__main__” 作为启动py文件的main函数入口
一个项目中必然会包含多个模块文件，每个模块文件在自己写完代码之后会做一些简单的测试用于检测bug 或者 
对自己的函数调用写一个简单的示例，而恰到好处的是：__name__ == “__main__”  既不会影响你的测试代码，
也不会影响别人调用你的接口函数。
"""
#参考博客 https://blog.csdn.net/zhanshen112/article/details/90551493
if __name__ == '__main__':
    main()
