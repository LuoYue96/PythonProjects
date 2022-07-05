# def Sum(*args):
#     result=0
#     for iterm in args:
#         result+=iterm
#     return result
# result = Sum(1,2,3,4,5,6,7)
# print("sum =%d"%result)
#
# def Newlist(*args):
#     nwli =[]
#     for i in range(1,len(args),2):
#         nwli.append(i)
#     print(nwli)
# Newlist(0,1,2,3,4,5,6,7)
#
# def Newdict(**kwargs):
#     newdict={}
#     for i,j in kwargs.items():
#         if len(j)>2:
#             j=j[:2]
#         newdict[i]=j
#     return newdict
# newdict=Newdict(name='ABdd',age=[1,2,3,5,4])
# print(newdict)
# pro = '123456'
# def Test():
#     global pro
#     print('pro:{}'.format(pro))
#     pro+='d'
#     print(pro)
# Test()
# print(pro)
#万物皆对象，实参传递的是对象的引用
#函数的传参，对于可变类型传参，修改函数内部标量，外部参数也会跟着改变；不可变类型参数在函数内部修改则不会影响外部参数
#可变实参可修改外部参数
# a = 'dsadasd'
# li = ['1','2']
# def Test(parms):
#     parms.append('s')
#     print(parms)
#     print(type(parms))
# Test(li)
# print(li)
#不可变类型参数不可修改外部参数
# a = 2
# def test(b):
#     b+=1
#     print(b)
# test(a)
# print(a)
'''
匿名函数
语法：lambda 参数1，参数2。。。：表达式
特点：使用lambda关键字创建函数；匿名函数冒号后面的表达式有且只有一个，
匿名函数自带return，return表达式的计算结果
缺点：lambda只能是单个表达式，不是一个代码块，设计本意是为了满足简答函数的场景，仅能封装简单逻辑
'''
#通过变量调用匿名函数
# M = lambda x,y:x+y
# print(M(2,3))
# T = lambda x,y:x if x>y else y
# print(T(0,9))
# #等价
# H = (lambda x,y:x if x>y else y )(0,9)
# print(H)
'''递归函数
规则：必须有一个结束条件，否则递归无法结束会一直递归下去，直到达到递归最大深度
优点：逻辑简单、定义简单
缺点：容易导致栈溢出，内存资源紧张，甚至内存泄漏
'''
#求阶乘
#普通方法做
# def jiechengP(args):
#     result = 1
#     for i in range(1,args+1):
#         result*=i
#     return result
# print('5的阶乘：{}'.format(jiechengP(5)))
#
# #递归函数
# def jiechengDigui(args):
#     if args == 1 :
#         return 1
#     else:
#         return args*jiechengP(args-1)
# print('5的阶乘：{}'.format(jiechengDigui(5)))
#递归案例，模拟实现 树形结构的遍历
# import os
# def findfile(filepath):
#     listRs = os.listdir(filepath)   #得到该路径下的所有文件和文件夹
#     for fileitem in listRs:
#         fullpath = os.path.join(filepath,fileitem)  #获取完整的文件路径
#         if os.path.isdir(fullpath):             #判断当前是否为文件夹
#             findfile(fullpath)                  #如果是文件夹，则继续递归
#         else:
#             print(fileitem)
#     else:
#         return
#调用搜索文件夹对象
#findfile("F:\PycharmProjects\pythonProject")
"""python内置函数"""
#数学运算
#abs()取绝对值
# print(abs(-10))
# #round(num1,num2)取近似值，非严谨的四舍五入，要根据实际的python版本
# #num1为要计算的数字，num2为保留的小数位数
# print(round(3.22))
# print(round(4.4232,1))
# #pow(a,b)计算a的b次方
# print(pow(3,3))
# print(divmod(3,2))
# #max()求最大值，min()求最小值
# print(max([1,3,2,423,4423]))
# #sum()求和，可以对系列进行求和计算
# print(sum([3,23,4],3))
#eval 可以执行表达式和函数
# a,b,c = 1,2,3
# print("动态执行的函数:{}".format(eval('a*b+c-323+a*b')))
# def TestFun():
#     print('我执行了吗?')
#     pass
# eval('TestFun()')
# print(divmod(10,2))
#转换函数
# print(ord('a'))
#print(bool([1,2,3,0]),all([]))

#序列操作sorted（）对所有可迭代的对象进行排序操作
#sort是应用在list上的方法，sort是在原对象上进行修改，sorted是返回一个新的列表，不修改原本的
#sorted（object,reverse=False(升序default）/True(降序））
# li = [2,3,1,4,65,7]
# tu = (2,3,54,532,5,0)
# #li.sort() #sort是list的内置方法，直接修改原list
# print(li)
# li_new = sorted(li,reverse=False)  #sorted()返回一个新的列表，不会修改原始对象；False升序
# li_jiang = sorted(li,reverse=True)
# print(li_new)
# print(li_jiang)
# newtu = sorted(tu,reverse=False)
# print(type(newtu),newtu)
#reverse() 用于反向输出列表的元素

#zip()：就是用来打包多个可迭代对象，返回元组列表，如果对象间长度不一样，按照最短的进行压缩
# s1 = ['a','b','c']
# s2 = ['1','2','3']
# s3 = ['d','l']
# #print(list(zip(s1)))   #压缩一个数据
# print(list(zip(s1,s2)))     #压缩两个数据
# print(list(zip(s1,s2,s3)))
#用zip做个简单的库管记录
# def printBookInfo():
#     books=[] #存储所有的图书信息
#     id=input('请输入编号（用空格隔开）：').split()
#     name=input('请输入书名（用空格隔开）：').split()
#     position=input('请输入位置（用空格隔开）：').split()
#     bookinfo=zip(id,name,position)  #打包处理
#     for bookinfoitem in bookinfo:
#         dictbook={'编号':bookinfoitem[0],'书名':bookinfoitem[1],'位置':bookinfoitem[2]}
#         books.append(dictbook)
#     for i in books:
#         print(i)
# printBookInfo()

#enumerate  对可迭代对象进行处理，分离出元素和下标，下标可自定义更改为任意数字为起始值
# list = ['a','v','c','r']
# for index,item in enumerate(list):
#     print(index,item)
# dicts = {'vvsd':1,'dsada':22,'fdsfx':33}
# for i in dicts.items():
#     print(i[1])

"""集合，set 不支持索引和切片，是一个无序的且不重复的容器，类似字典，都是{}，但是只有key没有value"""
# set1 = {21,232,43,5}
# print(type(set1))
# #添加add
# set1.add('python')
# print(set1)
# #清空 clear
# #set1.clear()
# #取差集.例如：a.difference(b), 取在a中且不在b中的元素 == a-b
# set2 = {21,32,43,555}
# #print(set1.difference(set2),set1-set2)
# #取交集 intersection  == &
# print(set1.intersection(set2),set1&set2)
# #取并集，union   == |
# print(set1.union(set2),set1 | set2)
# #移除数据，pop
# re = set1.pop()
# print(re,set1)
# #指定移除的元素 discard
# set1.discard(43)
# print(set1)
# #update 两个集合
# set1.update(set2)
# print(set1)
# a = 'dsada'
# print(a.ljust(10,'0'))
# print(sum(range(1,11)))
print(int(0x101))