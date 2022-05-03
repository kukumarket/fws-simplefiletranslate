import platform
import socket
from datetime import datetime

print("FWS© kuku2012")
print("您好。")
print("您正在运行的软件是 Simple File Translate Server 服务器端")
print("您的系统为:" + platform.system())
print("您的平台为:" + platform.platform())
print("您的设备类型为:" + platform.machine())
print("您的处理器架构为:" + platform.processor())
print("目前固定绑定9680端口.")
BIND_IP = "20.125.30.16"
BIND_PORT = 9680

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((BIND_IP, BIND_PORT))  # 绑定要监听的端口
server.listen(5)  # 开始监听 表示可以使用五个链接排队
brun = True
while brun:  # conn就是客户端链接过来而在服务端为期生成的一个链接实例
    print('已启动监听.')
    conn, addr = server.accept()  # 等待链接,多个链接的时候就会出现问题,其实返回了两个值
    print(conn, addr)

    while brun:
        try:
            data = conn.recv(1024)  # 接收数据
            print("接收到{}字节".format(len(data)))
            str = data.decode()
            print('接收到信息:', str)
            conn.send('接收到{}'.format(str).encode())

            # print('{}'.format(time.strftime("%Y-%m-%d %H:%M:%S")))
            # print(datetime.now())

            # conn.send(str.encode()) #然后再发送数据
            if str == "quit":
                print("接收到退出指令！")
                str = "{}".format(datetime.now())
                print(str)
                brun = False

        except ConnectionResetError as e:
            print('关闭了正在占线的链接！')
            break
    conn.close()
