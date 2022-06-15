#贪婪模式：在满足条件的情况下尽可能多的去匹配数据
import re

rs=re.match('\d{4,12}','111223341424')
print(rs.group())

rs=re.match('a.*d','a4442d42zxd')
print(rs.group())

#非贪婪模式：在满足条件的情况下尽可能少的去匹配数据
rs=re.match('\d{4,12}?','111223341424')
print(rs.group())

rs=re.match('a.*d?','a4442d42zxd')
print(rs.group())