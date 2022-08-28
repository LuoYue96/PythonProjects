import pymysql
#创建连接对象
conn = pymysql.connect(host="192.168.44.128",port=3306,user="root",password="LYmingji123",database="python_test1",charset="utf8")
#获取游标对象
cur = conn.cursor()
# #执行sql语句
# para = input("请输入要查询的名字：")
# sql = "select * from students where name = '%s';" % para
# cur.execute(sql)
# for i in cur.fetchall():
#     print(i)
# print(sql)
# cur.close()
# conn.close()
#防止sql注入版本
para = input("请输入要查询的名字：")
sql = "select * from students where name = %s;"
#执行sql
cur.execute(sql,para)
for i in cur.fetchall():
    print(i)
cur.close()
conn.close()