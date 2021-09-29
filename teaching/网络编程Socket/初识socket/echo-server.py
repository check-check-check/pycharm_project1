# @Time    : 
# @Author  : chen
import socket

HOST = '127.0.0.1'  # 标准的回环地址 (localhost)
PORT = 65432        # 监听的端口 (非系统级的端口: 大于 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) # 元组的形式
    s.listen()
    conn, addr = s.accept() #我们通过调用 accept() 方法拥有了一个新的 socket 对象
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            # 1024 是缓冲区数据大小限制最大值参数 bufsize，并不是说 recv() 方法只返回 1024个字节的内容
            if not data:
                break
            conn.sendall(data)