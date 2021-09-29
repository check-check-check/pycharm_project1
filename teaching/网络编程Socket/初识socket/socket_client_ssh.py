# @Time    : 
# @Author  : chen
import socket

client = socket.socket()
client.connect(('localhost', 6969))

while True:
    cmd = input('输入数据:').strip()
    if len(cmd) == 0:
        continue  # 输入为空，进入下次循环，不往下执行；输入不为空，向下执行
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024)  # 接受命令结果的长度
    print("命令结果大小:", cmd_res_size)
    received_size = 0
    received_data = b''
    # 防止粘包：循环接收 ，直到全部接收信息
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data)  # 每次收到的有可能小于1024，所以必须用len判断
        # print(data.decode())
        received_data += data
    else:
        print("cmd res receive done...", received_size)
        print(received_data.decode())
client.close()
