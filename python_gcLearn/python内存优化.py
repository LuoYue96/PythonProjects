#python内部有小整数池[-5,256] 和大整数池

#通过创建同一对象
a=1
b=1
print(id(a),id(b))
#删除，变量a，b
del a,b
#再次创建c，同样指向1，发现内存地址依然和之前一样，证明1的内存地址固定，属于小整数池
c=1
print(id(c))
#代码编写要符合Python Pep8规范