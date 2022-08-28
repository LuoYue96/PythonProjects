import pymysql
#创建连接对象
conn = pymysql.connect(host="192.168.44.128",port=3306,user="root",password="LYmingji123",database="python_test1",charset="utf8")
#获取游标对象
cur = conn.cursor()
#执行sql语句
# #增加一条记录
# sql = "insert into students(name) values('pycharm');"
# cur.execute(sql)
#删除一条
# sql = "delete from students where id = 14;"
# cur.execute(sql)
#更改
sql = "update students set name = 'poix' where id = 12 ;"
cur.execute(sql)
#查询
sql = "select * from students;"
cur.execute(sql)

content = cur.fetchall()
for i in content:
    print(i)

#关闭游标  关闭连接
cur.close()
#提交操作
conn.commit()
conn.close()
