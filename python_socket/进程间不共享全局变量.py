import multiprocessing
import time
#全局变量
my_list=[]

#写入数据
def write_data():
    for i in range(3):
        my_list.append(i)
        print("my_list add:",i)
    print("write_data",my_list)

#读取数据
def read_data():
    print("read_data:",my_list)

if __name__ == "__main__" :
    write_process = multiprocessing.Process(target=write_data)
    read_process = multiprocessing.Process(target=read_data)
    write_process.start()
    time.sleep(1)
    #先写后读，发现全局变量在读进程中仍为空，证明进程间不共享全局变量
    read_process.start()
'''
创建子进程实际上是对主进程资源的拷贝，也可以说子进程是主进程的副本，进程间操作的资源均是进程内部对全局的拷贝
操作的并非是同一变量，故进程间不共享全局变量    
    '''