import socket
import threading

#处理客户端任务
def handle_client(connect_socket):
    # 5.接收数据
    recv_data = connect_socket.recv(1024)
    print("客户端发来的消息是：", recv_data.decode())
    # 6.发送数据
    connect_socket.send("客户端你好".encode())
    # 7.关闭套接字
    connect_socket.close()

if __name__ == '__main__':

    # 1.创建服务端套接字对象
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #设置端口服用
    tcp_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    # 2.绑定IP地址和端口 bind参数中IP地址可以不写，“”表示默认本机IP
    #tcp_server.bind(("127.0.0.1",8888))
    tcp_server.bind(("",8888))
    # 3.设置监听,128表示服务端等待排队连接的最大数量（消息队列深度）
    tcp_server.listen(128)
    #循环接收多个客户端请求
    while True:
        # 4.等待接受客户端的连接请求,accept阻塞等待，返回一个用以和客户端连接的socket，客户端地址
        connect_socket,ip_port = tcp_server.accept()
        print("客户端地址：",ip_port)
        #使用线程处理客户端请求
        client_thread = threading.Thread(target=handle_client,args=((connect_socket,)))
        client_thread.start()
    tcp_server.close()