import threading

#全局变量
g_num = 0

#对全局变量进行加操作
def sum1():
    for i in range(1000000):
        #声明全局变量
        global g_num
        g_num+=1
    print("sum1:",g_num)
#对全局变量进行加操作
def sum2():
    for i in range(1000000):
        global g_num
        g_num+=1
    print("sum2:",g_num)

if __name__ == '__main__':
    #创建线程
    sum1_thread = threading.Thread(target=sum1)
    sum2_thread = threading.Thread(target=sum2)
    #启动线程
    sum1_thread.start()
    sum2_thread.start()