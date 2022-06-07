'''编写一个简单的模拟mysql登录，用来熟悉argparse模块'''
import argparse

#创建一个解释器
parse=argparse.ArgumentParser(prog='系统登录',usage='%(prog)s [options] usage',
                              description='系统自定义命令行文件',epilog='my-epilog')

#添加位置参数
parse.add_argument('LoginType',type=str,help='需要登录的系统类型')

#添加可选参数
parse.add_argument('-u',dest='user',help='用户名')
parse.add_argument('-p',dest='password',help='密码')

result=parse.parse_args() #解析参数

if result.user == 'root' and result.password == '12345':
    print('success')
else:
    print('fail')