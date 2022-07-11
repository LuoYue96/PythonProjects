import threading
import time

my_list = []

def write(num):
    for i in range(num):
        my_list.append(i)
        print("add: %d"%i)

def read():
    print("read:",my_list)

if __name__ == '__main__':
    write_thread = threading.Thread(target=write,args=(3,))
    read_thread = threading.Thread(target=read)
    write_thread.start()
    time.sleep(1)
    read_thread.start()