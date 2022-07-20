import socket
import threading
import sys

class HTTPwebServer():
    def __init__(self,port):
        self.port = port
        # 1.编写一个TCP服务端程序；
        # 创建serversocket
        self.web_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.web_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定服务地址
        self.web_server_socket.bind(("", self.port))
        # 开启监听
        self.web_server_socket.listen(128)

    def client_handle(self,client_socket):
        # 2.获取浏览器发送的HTTP请求数据；
        self.client_request = client_socket.recv(1024).decode()
        request_data = self.client_request.split(" ")
        print(request_data)
        # 判断浏览器是否返回一个空字节内容（当浏览器关闭时会返回一个空内容）
        if len(request_data) == 1:
            client_socket.close()
            return
        # 获取请求资源路径
        request_path = request_data[1]
        # 检查请求的资源路径是否填写，如果没有指定，则默认为index.html
        if request_path == "/":
            request_path = "/index.html"
        # print(client_request.decode())
        # 检查请求的资源是否存在，如果不存在就采用异常捕获，返回404
        try:
            # 3.读取固定页面数据，把页面数据组装成HTTP响应报文数据发送给浏览器；
            with open("." + request_path, "rb") as f:
                file_data = f.read()
        except Exception as e:
            # 响应行
            response_line = "HTTP/1.1 404 Not found\r\n"
            # 响应头
            response_header = "Server:PythonWeb\r\n"
            # 响应体
            response_body = "404 Not found sorry\r\n"
            # 响应内容
            response_data = (response_line + response_header + "\r\n" + response_body).encode()
            client_socket.send(response_data)
        # 如果存在就正常进行
        else:
            # 响应行
            response_line = "HTTP/1.1 200 ok\r\n"
            # 响应头
            response_header = "Server:PythonWeb\r\n"
            # 响应体
            response_body = file_data
            # 响应内容
            response_data = (response_line + response_header + "\r\n").encode() + response_body
            client_socket.send(response_data)
        finally:
            # 4.HTTP响应报文数据发送完成成后，关闭客户端socket
            client_socket.close()
    def start(self):
        while True:
            # 与客户端连接通信
            client_socket, client_addr = self.web_server_socket.accept()
            client_handle_thread = threading.Thread(target=self.client_handle, args=(client_socket,))
            client_handle_thread.start()

if __name__ == '__main__':
    #获取命令行参数，并判断给定的端口号格式是否正确
    if len(sys.argv) == 2 :
        if sys.argv[1].isdigit():
            port = int(sys.argv[1])
            #print("web服务器端口号为："+port)
        else:
            print("您输入的端口号格式不正确，请输入整型")
            exit()
    else:
        exit()
    #创建web服务器对象
    my_web_server = HTTPwebServer(port)
    #启动web服务器
    my_web_server.start()

