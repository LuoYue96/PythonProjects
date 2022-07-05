#python命令行参数

# import sys
# '''命令行参数1 sys.argv'''
# #argv返回命令行参数是一个列表，第一个元素就是执行的py文件名。sys.argv支持切片
# print('参数个数为：',len(sys.argv),'个参数')
# print('参数列表：',sys.argv)
#argv只提供了简单的命令行参数获取方式，并没有提供命令行提示，无法做到像linux命令一样可以给用户提供help帮助。

'''命令行参数2 argparse模块
argparse模块可以轻松的编写用户友好的命令行界面，该程序定义了它需要的参数，argparse并将找出如何解析这些参数，argparse还会
自动生成帮助和用法消息，并在用户给出的程序无效参数时发生错误
参数：
prog:文件名，默认为sys.argv[0]，用来在help信息中描述程序的名称
usage:描述程序用途的字符串
description：help信息前显示的信息
epilog：help信息之后显示的信息
parent：由ArgumentParser对象组成的列表，他们的arguments选项会被包含到新ArgumentParser对象中。（类似继承）
formatter_class:help信息输出的格式，为了美观
prefix_chars:参数前缀，默认为’-‘（最好不要修改）
fromfileprefixchars:前缀字符，放在文件名之前
add_help:是否增加-h/-help选项(默认为True)，一般help信息是必须的，设为False时，help信息里面不再显示-h、-help信息
argument_default:-(default:None）设置一个全局的选项的缺省值，一般每个选项单独设置，基本没用
'''
import argparse
#创建一个解释器对象
parse=argparse.ArgumentParser(prog='我的第一个脚本程序',usage='%(prog)s [options] usage',
                              description='my-编写自定义命令行的文件',epilog='my-epilog')
#添加位置参数【必选参数】
parse.add_argument('name',type=str,help='你的名字')
parse.add_argument('age',type=str,help='你的性别')

#添加可选参数
parse.add_argument('-s','--sex',default='男',choices=['男','女'],type=str,help='你的性别')
'''
add_argument的参数：
    metaver：帮助信息中显示的参数名称
    const：保存一个常量
    default：默认值
    type：参数类型，默认为str
    choices：设置参数值的范围，如果choices中的类型不是字符串，记得指定type
    dest：参数名
'''

#parse.print_help()

#开始解析参数
result=parse.parse_args()
#print(result)
print('start')