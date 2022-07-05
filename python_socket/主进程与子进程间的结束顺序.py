'''
主进程与子进程的结束顺序
'''
import multiprocessing
import time

#工作函数
# def work():
#     for i in range(10):
#         print("子进程工作中。。。")
#         time.sleep(0.2)
#
# if __name__ == '__main__':
#     work_pro = multiprocessing.Process(target=work)
#     work_pro.start()
#     time.sleep(1)
    #发现，子进程work是与后面代码同步执行，输出完“主进程执行完毕”后，work依然在执行



'''通过如下方法，可以提前结束子进程，确保在主进程执行完成后再执行'''
def work():
    for i in range(10):
        print("子进程工作中。。。")
        time.sleep(0.2)
if __name__ == '__main__':
    work_pro = multiprocessing.Process(target=work)
    #方式1：设置守护进程
    #work_pro.daemon = True
    work_pro.start()
    time.sleep(1)
    #方式2：手动结束子进程
    work_pro.terminate()
    print('主进程执行完毕')