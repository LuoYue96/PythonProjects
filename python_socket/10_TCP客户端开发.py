import socket
import time


if __name__ == '__main__':

    #1.创建客户端socket    AF_INET表示IPv4  SOCK_STREAM表示TCP协议
    tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2.与服务器建立连接
    tcp_client.connect(("127.0.0.1",8888))
    #3.发送数据
    time.sleep(3)
    tcp_client.send('nihao'.encode(encoding='utf-8'))

    #4.接收数据
    recv_data = tcp_client.recv(1024)

    print(recv_data.decode())
    #5.关闭socket
    tcp_client.close()
