# import socket
# """
# 通过socket内置方法创建套接字对象
# 套接字需要两个参数
#     1.ip协议类型
#         ipv4
#         ipv6
#     2.套接字类型
#         tcp
#         udp
# """
# udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# '''
# 指定发送的地址，端口信息
# ip：网络地址
# port：应用程序
# '''
# dest_address=('',8080)
# '''
# 发送的信息
# '''
# send_message = input('请输入要发送的内容')
# '''
# 通过socket对象将信息发送出去
# '''
# udp_socket.sendto(send_message.encode('utf-8'),dest_address)
# '''
# 发送完成要关闭socket
# '''
# udp_socket.close()
s = "3+5"
print(eval(s))