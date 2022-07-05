import multiprocessing
import time
import os
def coding(num):
    print("coding进程的pid：%d"%os.getpid())
    print("coding父进程的pid：%d"%os.getppid())
    for i in range(num):
        print('coding....')
        time.sleep(0.2)
def muscing(count):
    print("muscing进程的pid：%d"%os.getpid())
    print("muscing父进程的pid：%d"%os.getppid())
    for i in range(count):
        print('muscing....')
        time.sleep(0.2)
codepro = multiprocessing.Process(target=coding,args=(3,))
muscpro = multiprocessing.Process(target=muscing,kwargs={"count":4})

if __name__ == '__main__':
    print("主进程的pid：%d" % os.getpid())
    codepro.start()
    muscpro.start()
