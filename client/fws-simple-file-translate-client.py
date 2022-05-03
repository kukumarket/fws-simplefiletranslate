import datetime
import platform
import socket
print("FWS© kuku2012")
print("您好。")
print("您正在运行的软件是 Simple File Translate Server 客户端")
print("您的系统为:"+platform.system())
print("您的平台为:"+platform.platform())
print("您的设备类型为:"+platform.machine())
print("您的处理器架构为:"+platform.processor())
print("目前固定绑定9680端口.")
BIND_IP="20.125.30.16"
BIND_PORT=9680
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
client.connect((BIND_IP,BIND_PORT)) #建立一个链接，连接到本地的6969端口
# addr = client.accept()
# print '连接地址：', addr

msg = 'dir'
client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收byte流
data = client.recv(1024) #接收一个信息，并指定接收的大小 为1024字节
print('recv:',data.decode()) #输出我接收的信息
client.close() #关闭这个链接