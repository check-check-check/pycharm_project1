# @Time    : 
# @Author  : chen
import socket
import os
import time

server = socket.socket()
server.bind(('localhost', 6969))
server.listen()
while True:
    # 等待连接
    conn, addr = server.accept()
    print('new conn:', addr)
    while True:
        print('等待新指令.....')
        data = conn.recv(1024)
        if not data:
            print('客户端已断开！')
            break  # 输入为空，跳出该循环，跳到外围循环；输入不为空，向下执行
        print('执行指令：', data)
        re_cmd = os.popen(data.decode()).read()  # 接受字符串，执行结果也是字符串
        print("before send: ", len(re_cmd), re_cmd)
        if len(re_cmd) == 0:
            re_cmd = "cmd has no output..."

        conn.send(str(len(re_cmd.encode())).encode("utf-8"))  # 首先发大小给客户端
        time.sleep(0.5)
        conn.send(re_cmd.encode("utf-8"))
        print("send done")
server.close()
