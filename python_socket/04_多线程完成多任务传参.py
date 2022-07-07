# Author：LuoYue
import threading
import time

#任务1：code
def coding(num):
    for i in range(num):
        print('coding ... ')
        time.sleep(0.2)
#任务2：music
def music(count):
    for i in range(count):
        print("music...")
        time.sleep(0.2)

if __name__ == '__main__':
    #创建子进程-code
    code_thread = threading.Thread(target=coding,args=(3,))
    #创建子进程-music
    music_thread = threading.Thread(target=music,args=(5,))
    #启动子进程
    code_thread.start()
    music_thread.start()