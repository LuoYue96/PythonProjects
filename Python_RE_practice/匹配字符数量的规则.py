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
res=re.match('[a-zA-Z0-9]{6,11}@163\.com','dasdd41@163.com')
print(res.group())