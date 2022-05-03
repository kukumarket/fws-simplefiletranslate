import platform
import select
import socket
from datetime import datetime
import os

print("FWS© kuku2012")
print("您好。")
print("您正在运行的软件是 Simple File Translate Server 服务器端")
print("您的系统为:" + platform.system())
print("您的平台为:" + platform.platform())
print("您的设备类型为:" + platform.machine())
print("您的处理器架构为:" + platform.processor())
print("目前固定绑定9680端口.")
print("当前路径：{}".format(os.getcwd()))
print("搜索当前路径下的文件.")
print("Mode         Name  ")
for item in os.listdir():
    if os.path.isdir(item):
        print("--d-         {}".format(item))
    elif os.path.isfile(item):
        print("---f         {}".format(item))
BIND_IP = "127.0.0.1"
#BIND_IP = "10.1.0.4"
BIND_PORT = 9680
CMD_SIZE = 1024
param = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((BIND_IP, BIND_PORT))  # 绑定要监听的端口
server.listen(1)  # 开始监听 表示可以使用五个链接排队
rxset = [server]
txset = []


brun = True
#while brun:  # conn就是客户端链接过来而在服务端为期生成的一个链接实例
    # print('已启动监听.')
    # conn, addr = server.accept()  # 等待链接,多个链接的时候就会出现问题,其实返回了两个值
    # print(conn, addr)
    #
    # while brun:
    #     try:
    #         data = conn.recv(CMD_SIZE)  # 接收数据
    #         str = data.decode()
    #         conn.send(data.upper())
    #         if len(str) != 0:
    #             print('接收到信息:{}字节,内容为{}'.format(len(str),str))
    #
    #
    #         # print('{}'.format(time.strftime("%Y-%m-%d %H:%M:%S")))
    #         # print(datetime.now())
    #
    #         # conn.send(str.encode()) #然后再发送数据
    #         if str == "quit":
    #             print("接收到退出指令！")
    #             str = "{}".format(datetime.now())
    #             print(str)
    #             brun = False
    #             break
    #         else:
    #             continue
    #
    #     except ConnectionResetError as e:
    #         print('关闭了正在占线的链接！')
    #         break
    # conn.close()
while brun:
    print("启动监听:服务器:{} 端口:{}".format(BIND_IP,BIND_PORT))
    client,addr = server.accept()
    print("接收到来自{}的连接".format(addr))
    while brun:
        try:
            data = client.recv(CMD_SIZE)
            print("recev:{}".format(data.decode('utf-8')))
            if data:
                print(data.decode('utf-8'))
                client.send("已接收到指令!返回值(模拟)".encode('utf-8'))
            else:
                print("客户端已经停止发送数据.")
                break
        except ConnectionResetError as e:
            print("客户端已经主动关闭连接.")
    client.close()


server.close()

