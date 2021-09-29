# @Time    : 
# @Author  : chen
# 异常就是程序运行时发生错误的信号，程序随即发生终止行为
# 常见的异常的处理方式:
# %% 语法结构1
"""
try:
  被检测的代码块
except 异常类型：
其中：try 中一旦检测到异常，就执行这个位置的逻辑
"""
try:
    f1 = open('test1.txt.txt', encoding='UTF-8')
    g = (line.strip() for line in f1)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopAsyncIteration:
    f1.close()
# 读取test.txt 文件中的文件，当检测到异常，就抛出  StopAsyncIteration，然后关闭文件
#%%语法结构2: 多分支
s1 = 'hello python'
try:
    int(s1)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)
#%%语法结构三:万能的异常
s1 = 'hello Python'
try:
    int(s1)
except Exception as e:
    print(e)
# %%语法结四: 当try的时候没有异常时执行 else，无论是否异常都执行 finally
s1 = 100
try:
    int(s1)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print('try内代码块没有异常则执行我')
finally:
    print('无论异常与否,都会执行该模块,通常是进行清理工作')