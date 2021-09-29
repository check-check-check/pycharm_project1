# @Time    : 
# @Author  : chen

import queue
"""主要作用：
解耦，使程序实现松耦合（一个模块修改不会影响其他模块）; 提高效率"""
"""队列与列表的关系
队列中数据只有一份，取出就没有了，区别于列表，列表数据取出只是复制了一份"""
#%% 分类
# 1.FIFO (先入先出): queue.Queue(maxsize=0) # If maxsize is <= 0, the queue size is infinite
import queue
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())
print(q.get())
#%%LIFO (后入先出): queue.LifoQueue
import queue
q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())
print(q.get())
#%% PriorityQueue (数据可设置优先级): queue.PriorityQueue #同优先级的按照 ASCII 排序
import queue
q = queue.PriorityQueue()
q.put((2, '2'))
q.put((1, '1'))
q.put((3, '3'))
q.put((1, 'a'))

print(q.get())
print(q.get())
print(q.get())
print(q.get())

#%% 例题
from queue import Queue, LifoQueue, PriorityQueue
# 先进先出队列
q = Queue(maxsize=5)
# 后进先出队列
lq = LifoQueue(maxsize=6)
# 优先级队列
pq = PriorityQueue(maxsize=5)

for i in range(5):
    q.put(i)
    lq.put(i)
    pq.put(i)

print("先进先出队列：%s;是否为空：%s；多大,%s;是否满,%s" % (q.queue, q.empty(), q.qsize(), q.full()))
print("后进先出队列：%s;是否为空：%s;多大,%s;是否满,%s" % (lq.queue, lq.empty(), lq.qsize(), lq.full()))
print("优先级队列：%s;是否为空：%s,多大,%s;是否满,%s" % (pq.queue, pq.empty(), pq.qsize(), pq.full()))
print(q.get(), lq.get(), pq.get())
print("先进先出队列：%s;是否为空：%s；多大,%s;是否满,%s" % (q.queue, q.empty(), q.qsize(), q.full()))
print("后进先出队列：%s;是否为空：%s;多大,%s;是否满,%s" % (lq.queue, lq.empty(), lq.qsize(), lq.full()))
print("优先级队列：%s;是否为空：%s,多大,%s;是否满,%s" % (pq.queue, pq.empty(), pq.qsize(), pq.full()))

#%% 还有一种队列是双边队列，示例代码如下：
from queue import deque # 其实是：from collections import deque
dq=deque(['a','b'])
dq.append('c')
print('dq:',dq)
print('dq.pop():',dq.pop())
print('dq:',dq)
print('dq.popleft():', dq.popleft())
print('dq:',dq)
dq.appendleft('d')
print('dq:', dq)
print(len(dq))

#%%多线程和queue
import threading
import queue
q = queue.Queue(5)  # 长度，队列中最多存放5个数据

def put():
    for i in range(20):
        q.put(i)
        print("数字%d存入队列成功" % i)
    q.join()  # 阻塞进程，直到所有任务完成，取多少次数据task_done多少次才行，否则最后的ok无法打印
    print('ok')


def get():
    for i in range(20):
        value = q.get()
        print("数字%d重队列中取出" % value)
        q.task_done()  # 必须每取走一个数据，发一个信号给join
    # q.task_done()   #放在这没用，因为join实际上是一个计数器，put了多少个数据，
    # 计数器就是多少，每task_done一次，计数器减1，直到为0才继续执行


t1 = threading.Thread(target=put, args=())
t1.start()
t2 = threading.Thread(target=get, args=())
t2.start()
