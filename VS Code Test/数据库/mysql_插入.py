import pymysql


con = pymysql.connect(host = 'localhost', user = 'root', password = 'nimabi518', database = 'python_test', port = 3306)
print(con)
cur = con.cursor()

sql = 'insert into gudong(name, age, score) values(%s, %s, %s)'

try:
    #插入单条数据
    #cur.execute(sql,('张三', 18, 99))
    #插入多条数据
    cur.executemany(sql, [('小张', 23, 98.5), ('小李', 24, 80.0), ('小王', 22, 61)])
    con.commit()
    print('插入成功！')
except Exception as e:
    print(e)
    con.rollback()
    print('插入失败！')
finally:
    cur.close()
    con.close()