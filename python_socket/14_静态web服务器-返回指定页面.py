import socket

if __name__ == '__main__':
    # 1.编写一个TCP服务端程序；
    #创建serversocket
    web_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    web_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    #绑定服务地址
    web_server_socket.bind(("",8080))
    #开启监听
    web_server_socket.listen(128)

    while True:
        # 与客户端连接通信
        client_socket, client_addr = web_server_socket.accept()
        # 2.获取浏览器发送的HTTP请求数据；
        client_request = client_socket.recv(1024).decode()
        request_data = client_request.split(" ")
        print(request_data)
        request_path = request_data[1]
        #检查请求的资源路径是否填写，如果没有指定，则默认为index.html
        if request_path == "/":
            request_path = "/index.html"
        #print(client_request.decode())
        #检查请求的资源是否存在，如果不存在就采用异常捕获，返回404
        try:
            # 3.读取固定页面数据，把页面数据组装成HTTP响应报文数据发送给浏览器；
            with open("." + request_path, "rb") as f:
                file_data = f.read()
        except Exception as e:
            # 响应行
            response_line = "HTTP/1.1 404 Not found\r\n"
            # 响应头
            response_header = "Server:PythonWeb"
            # 响应体
            response_body = "404 Not found sorry"
            # 响应内容
            response_data = (response_line + response_header + "\r\n" + response_body).encode()
            client_socket.send(response_data)
        #如果存在就正常进行
        else:
            #响应行
            response_line = "HTTP/1.1 200 ok\r\n"
            #响应头
            response_header = "Server:PythonWeb"
            #响应体
            response_body = file_data
            #响应内容
            response_data = (response_line + response_header + "\r\n").encode() + response_body
            client_socket.send(response_data)
        finally:
            print(response_data.decode())
            # 4.HTTP响应报文数据发送完成成后，关闭客户端socket
            client_socket.close()