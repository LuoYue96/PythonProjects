import threading
import time

#工作函数
def work():
    for i in range(5):
        print("working...")
        time.sleep(0.3)
    print("子线程执行结束")

if __name__ == '__main__':
    #创建子线程
    #方式1：参数方式设置守护主线程
    work_thread = threading.Thread(target=work,daemon=True)
    work_thread.start()
    time.sleep(1)
    print("主线程运行结束")
