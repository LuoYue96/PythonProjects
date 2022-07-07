import threading
import time

#获取线程信息的函数
def get_info():
    time.sleep(1)
    current_thread = threading.current_thread()
    print(current_thread)

if __name__ == '__main__':
    #创建子线程
    for i  in range(10):
        sub_thread = threading.Thread(target=get_info)
        sub_thread.start()
