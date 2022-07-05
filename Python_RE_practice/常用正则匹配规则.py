import re
#.点的使用，匹配规则是除了换行符之外的字符
# names='李明','张亮','李广','李志','王政'
# #匹配规则
# pattern='李.'
# for name in names:
#     res=re.match(pattern,name)
#     if res:
#         print(res.group())
#[]中括号的使用，匹配中括号内的任意一个字符:[abc]--匹配abc中任意一个，[a-z]--匹配a到z这26个字母
# list=['abc','a23ads','vs23s']
# for item in list:
#     res=re.match('[a-z]',item)
#     if res:
#         print(res.group())
#\d 匹配一个数字 0-9
# data='213adsad'
# print(re.match('\d',data).group())
# #\D匹配一个非数字的字符
# data2='dsa231'
# print(re.match('\D',data2))
#\s匹配一个空白字符或者tab键
#\S匹配一个非空白字符
#\w匹配一个单词字符，a-z A-Z 0-9,汉字
# data='打赏dsads121'
# print(re.match('\w',data).group())
#\W匹配非单词字符
# data='@!@#$dasd'
# print(re.match('\W',data).group())