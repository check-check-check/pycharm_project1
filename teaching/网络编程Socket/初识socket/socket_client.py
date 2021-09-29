# @Time    : 
# @Author  : chen

import socket
socket_client = socket.socket()
socket_client.connect(('localhost', 8899))
print('conneting:......successing！')
while True:
    msg = input(':').strip()
    # if len(msg):break
    client_data = socket_client.send(msg.encode())
    print("客户端发送数据成功！")
    server_data = socket_client.recv(1024)
    print("客户端接收数据server_data:", server_data.decode())
# socket_client.close()


