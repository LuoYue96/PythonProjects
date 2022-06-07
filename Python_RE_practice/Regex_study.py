#通过Python中的re模块的使用最终掌握正则表达式的常用匹配规则
import re
strdata='Python is the best language in the world'
'''
match 只能匹配以xxx开头的字符串，第一个参数是正则，第二个参数是要匹配的对象
re.match(pattern,string,flags=0)
pattern---匹配的正则表达式；string---要匹配的字符串；flags---标志位。如是否区分大小写，多行匹配等
flag可选标志位：
    re.I---使匹配对大小写不敏感；re.L---做本地化识别（locale-aware）匹配；re.M---多行匹配，影响^和$；
    re.U---根据Unicode解析字符，影响\w \W \b \B;re.X---该标志通过给予你更灵活的格式以便你将正则表达式写的更易于理解
    如果同时使用多个标志位，用|分隔，如 re.i|re.L
'''
#res=re.match('Python is the best',strdata,re.I|re.M)
res = re.match('(.*) is (.*?) .*',strdata)
if res:
    print('match success')
    '''
    我们可以使用group（num）或者groups（）匹配对象函数来获取匹配表达式
    group（num=0）---匹配的整个表达式的字符串，group（）可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
    groups（）---返回一个包含所有小组字符串的元组，从1到所含的小组号
    '''
    print(res.groups())
    #print(res)
    print(res.group(1))
    print(res.group(2))

else:
    print('match fail')
    #匹配失败时，res为none
    print(res)