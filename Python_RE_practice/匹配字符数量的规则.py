import re
# * 匹配前一个字符出现0次或无限次，即可有可无
#res=re.match('[A-Z]y[A-Z]*','Myasdsa')
# res=re.match('[A-Z]y[a-z]*','MyasdsaASDSADAS')
# print(res.group())
#+ 匹配前一个字符出现1次或无限次,至少1次
#检查变量名是否符合要求，即以字母或者下划线开头
# res=re.match('[a-zA-Z_][\w]+','_nadas312dsame')
# print(res.group())
#? 匹配前一个字符出现0次或1次,即可选匹配
# res=re.match('[a-zA-Z]+[\d]?','ahh2sd')
# print(res.group())
#{min,max} 匹配前一个字符出现至少出现min次，最可max次，min或max可省略
#{m} 匹配前一个字符出现m次，精确匹配
# res=re.match('[a-zA-Z]{3,60}','asdsadzxd')
# print(res.group())
# res=re.match('[a-zA-Z]{4}','asdsadzxd')
# print(res.group())
# res=re.match('[a-zA-Z]{,2}','asdsadzxd')
# print(res.group())
# res=re.match('[a-zA-Z]{3,}','asdsadzxd')
# print(res.group())
#小练习，匹配邮箱
#在匹配‘.com’时，需要注意转义
# res=re.match('[a-zA-Z0-9]{6,11}@163\.com','dasdd41@163.com')
# print(res.group())
# print(re.match(r'C:\\a.txt','C:\\a.txt').group())
#print(r'C:\a.tct')
# ^ 匹配字符串开头
# result='Python is the best language'
# res = re.match('^P[\w,\s]*',result)
# if res:
#     print(res.group())
#$ 匹配字符串末尾
#以匹配邮箱为例
# mailaddress='lkda123@sina.com'
# res = re.match('[\w]{4,9}@[\w]{2,4}\.com$',mailaddress)
# if res:
#     print(res.group())
# | 竖线，匹配左右任意一个表达式 实际上是 或的关系
# data = 'dsdasd123'
# print(re.match('dsdasc|dsdasd123',data).group())
# (ab)分组匹配，每个括号为一组
#匹配电话号码
#   ^有两种含义，一种是代表开头   另一种是取反，否定
# res=re.match('([0-9]*)-([\d]*)','0316-8395903')
# res=re.match('([^-]*)-([\d]*)','aaa-8395903')
# print(res.groups())
# print(res.group(0))
# print(res.group(1))
# print(res.group(2))
#\num 的使用，引用分组num匹配到的字符串
# htmltag='<html><h1>TestData</h1></html>'
# res=re.match(r'<(.+)><(.+)>(.+)</\2></\1>',htmltag)
# print(res.group(1))
# print(res.group(2))
# print(res.group(3))
# print(res.group())
#引用分组 取别名
# data='<div><h1>www.baidu.com</h1></div>'
# res2=re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>.+</(?P=name2)></(?P=name1)>',data)
# print(res2.group())
#compile re模块中的编译方法，可以把一个字符串编译成字节码
#优点，在使用正则表达式进行match的操作时，python会将字符串转为正则表达式对象：
#而如果使用compile则只需要完成一次转换即可，以后再匹配同规则时无需重复转换
# reobj=re.compile('\d{3}')
# rs=reobj.match('12345678')
# print(rs.group())
# #等价于直接使用match编写正则规则
# print(re.match('\d{3}','1234567').group())
# data='123 456 123 753 12314wowww'
# res=re.search('123',data)
# print(res.span())
# print(res.group())
# print(res)
# findall
# text='中华有为，华为，华华'
# reobj=re.compile('华.')
# print(reobj.findall(text))
# re.sub
# re.subn
# data='Python 是最好的语言Python'
# pattren='[a-zA-Z]+'
# print(re.sub(pattren,'Java',data,count=0))
# #subn 会返回一个包含两个元素的元组，第一个元素是修改后的字符串，第二个元素是替换的次数
# print(re.subn(pattren,'Java',data,count=0))
data='百度，阿里，腾讯，华为'
print(re.split(',',data))