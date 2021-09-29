# @Time    : 
# @Author  : chen
# 自动补全代码提示前符号类别：
# p：parameter 参数
# m：method 方法
# c：class 类
# v：variable 变量
# f：function 函数
import socket

# 第一步：创建socker实例
server = socket.socket()
# socket.AF_INET IPv4(默认),
# socket.SOCK_STREAM流式socket , for TCP(默认),
# 0:(默认)与特定的地址家族相关的协议,如果是 0 ，则系统就会根据地址格式和套接类别,自动选择一个合适的协议
print(server)
# 第二步：绑定ip和端口，在AF_INET下，以元组（host,port）的形式表示地址
server.bind(('localhost', 8899))
# 第三步：开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。
server.listen(3)
print('listening:.......正在监听！')

while True:
    # 接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
    # 第四步:接收TCP 客户的连接（阻塞式）等待连接的到来
    conn, addr = server.accept()
    # print(conn, addr)
    # conn就是从客户端链接过来为其生成的一个链接实例
    print('有客户端连接上了服务端！')
    count = 0
    while True:
        # 第五步：接收客户端发来的数据
        client_data = conn.recv(1024)
        print("收到的客户端数据client_data:", client_data.decode())
        if not client_data:
            print("client has lost:.....")
            break
        server_data = b' from the server_data'
        conn.send(server_data)
        print("服务端数据发送成功！")
        count += 1
        if count > 2:
            break
server.close()
