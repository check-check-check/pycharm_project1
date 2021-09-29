# @Time    : 
# @Author  : chen
#%%串行：join函数，等待该进程执行完，再继续向下执行
import threading
import time

def run(n):
    print("task ",n )
    time.sleep(2)
    print("task done",n)

start_time = time.time()

for i in range(50):
    t = threading.Thread(target=run,args=("t-%s" %i ,))
    t.start()
    t.join()

print("----------all threads has finished...")
print("cost:",time.time() - start_time)
