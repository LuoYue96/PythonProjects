import socket

if __name__ == '__main__':
    # 1.编写一个TCP服务端程序；
    #创建serversocket
    web_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定服务地址
    web_server_socket.bind(("",8080))
    #开启监听
    web_server_socket.listen(128)

    while True:
        # 与客户端连接通信
        client_socket, client_addr = web_server_socket.accept()
        # 2.获取浏览器发送的HTTP请求数据；
        client_request = client_socket.recv(1024)
        print(client_request.decode())
        # 3.读取固定页面数据，把页面数据组装成HTTP响应报文数据发送给浏览器；
        with open("./index.html","rb") as f :
            file_data = f.read()
        #响应行
        response_line = "HTTP/1.1 200 ok\r\n"
        #响应头
        response_header = "Server:PythonWeb"
        #响应体
        response_body = file_data
        #响应内容
        response_data = (response_line + response_header + "\r\n").encode() + response_body

        client_socket.send(response_data)
        # 4.HTTP响应报文数据发送完成成后，关闭客户端socket
        client_socket.close()
    web_server_socket.close()