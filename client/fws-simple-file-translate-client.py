import datetime
import platform
import socket
import time

print("FWS© kuku2012")
print("您好。")
print("您正在运行的软件是 Simple File Translate Server 客户端")
print("您的系统为:"+platform.system())
print("您的平台为:"+platform.platform())
print("您的设备类型为:"+platform.machine())
print("您的处理器架构为:"+platform.processor())

#BIND_IP="20.125.30.16"
BIND_IP="127.0.0.1"
BIND_PORT=9680

print("目前固定绑定{}端口.".format(BIND_PORT))
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
# client.setsockopt(socket.SOL_SOCKET,socket.SO_KEEPALIVE,True)
# client.ioctl(socket.SIO_KEEPALIVE_VALS,(1,60*1000,30*1000))
client.connect((BIND_IP,BIND_PORT)) #建立一个链接，连接到本地的6969端口
# addr = client.accept()
# print '连接地址：', addr

# msg = 'dir:{}'.format(datetime.datetime.now())
# client.send(msg.encode('utf-8'))  # 发送一条信息 python3 只接收byte流
# data = client.recv(1024)
# print(data.decode('utf-8'))
ncount = 0
while True:
    ncount = ncount + 1
    msg = 'dir:{}'.format(datetime.datetime.now())
    client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收byte流
    data = client.recv(1024)
    time.sleep(10)
    if ncount > 5:
        break
client.close()




# client.close() #关闭这个链接