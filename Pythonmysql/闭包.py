# 闭包的构成条件：
# 1.在函数嵌套(函数里面再定义函数)的前提下；
# def fun_outer(num1):
#     # 2.内部函数使用了外部函数的变量(还包括外部函数的参数)；
#     def fun_inner(num2):
#         num = num1 + num2
#         print("num:",num)
#     # 3.外部函数返回了内部函数。
#     return fun_inner
# #创建闭包实例
# f = fun_outer(10)
# #执行闭包
# f(1)
# f(2)
#通过调用f = fun_outer(10)创建闭包，实际上f()等价于内部函数fun_inner(),即调用闭包函数就相当于调用内部函数。

#闭包案例：实现两个人物对话，关键字，人名、说话内容
#定义外部函数，圈定人物
# def human(name):
#     #定义内部函数，功能说话
#     def say_info(info):
#         print(name,":",info)
#     #返回闭包函数
#     return say_info
# p1 = human('bob')
# p1('hi,are you ok?')
# p2 = human('jenny')
# p2("yes,not bad!")

#闭包案例-通过闭包函数修改外部变量
#外部函数
def outer(num1):
    #内部函数
    def inner(num2):
        #通过nonlocal声明num1.等同于global
        nonlocal num1
        num1 = num2 +6
        print(num1)
    return inner
    #print(num1)
    #inner(10)
    #print(num1)
example = outer(10)
example(20)
example(23)