import sys
#标记-清除机制
import  psutil
import os
import gc
# a=[]
# #获取变量a被引用的次数，a在被创建时一次，在本次查询时又被引用一次共两次（本次查询结束会自动释放引用，即实际只有一次）
# print(sys.getrefcount(a))
# #可证明geterfcount在执行结束后自动释放了
# print(sys.getrefcount(a))   #显示2次
# b=a
# c=b
# d=c
# e=d
# f=e
# print(sys.getrefcount(a))   #显示7次
# list1=[]
# list2=[]
# list1.append(list2)
# list2.append(list1)
# def showmemory(tag):
#     pid=os.getpid()
#     processor=psutil.Process(pid)
#     info=processor.memory_full_info()
#     memory=info.uss/1024/1024
#     print('{} memory used: {}'.format(tag,memory))
# def func():
#     showmemory('初始化')
#     a=[i for i in range(10000000)]
#     b=[i for i in range(10000000)]
#     a.append(b)
#     b.append(a)
#     showmemory('创建列表对象a b 之后')
#     print(sys.getrefcount(a))
#     print(sys.getrefcount(b))
#     # del a       #手动删除变量a  发现依然无法释放内存
#     # del b       #手动删除变量a  发现依然无法释放内存
#     pass
# func()
# gc.collect()   #手动调用gc进行垃圾回收
# showmemory('运行结束之后')
import gc
print(gc.get_threshold())
