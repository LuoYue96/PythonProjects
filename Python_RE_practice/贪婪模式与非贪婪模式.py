#贪婪模式：在满足条件的情况下尽可能多的去匹配数据
import re

# rs=re.match('\d{4,12}','111223341424')
# print(rs.group())
#
# rs=re.match('a.*d','a4442d42zxd')
# print(rs.group())
#
# #非贪婪模式：在满足条件的情况下尽可能少的去匹配数据
# rs=re.match('\d{4,12}?','111223341424')
# print(rs.group())
'''
当^遇到[]，表示取反
data='aAdsad'
reobj=re.compile('(^a.)')
print(reobj.match(data).group())
'''
'''验证密码是否符合   以字母开头，只包含数字、字母、下划线，长度为8-10
data=input('input your password: ')
Verify_pw=re.compile('^[a-zA-Z]\w{7,9}$')
if Verify_pw.match(data):
    print('pass')
    print(Verify_pw.match(data).group())
else:
    print('fail')
'''
'''验证用户名。长度为6-18位的英文字母组成
data=input('input your username: ')
Verify_un=re.compile('[a-zA-Z]{6,18}')
if Verify_un.match(data):
    print('pass')
    print(Verify_un.match(data).group())
else:
    print('fail')
'''
'''邮箱验证126，163，6-18个字符，可以使用字母、数字、下划线，需要以字母开头
data=input('input your email: ')
Verify_mail=re.compile('^[a-zA-Z]\w{5,17}@(126|163)\.com$')
if Verify_mail.match(data):
    print('pass')
    print(Verify_mail.match(data).group())
else:
    print('fail')
'''
'''匹配手机号  包含 移动联动电信  11位，需要注意前三位
data=input('input your number: ')
Verify_mail=re.compile('^1[3458][0-9]\d{8}?$')
if Verify_mail.match(data):
    print('pass')
    print(Verify_mail.match(data).group())
else:
    print('fail')
'''
'''将文本中的s替换为S。
data='dsfxcfed sadASDdsff'
res=re.sub('s','S',data,count=0)
print(res)
'''
'''  '<span>受大环境的</span><span>受大苏打</span><span>而感到反感</span>' 将span标签的内容全部匹配出来   '''
data='<span>受大环境的</span><span>受大苏打</span><span>而感到反感</span>'

res=re.findall(r'<span>(.*?)</span>',data)
print(res)