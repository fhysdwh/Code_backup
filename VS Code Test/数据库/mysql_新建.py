import pymysql


con = pymysql.connect(host = 'localhost', user = 'root', password = 'nimabi518', database = 'python_test', port = 3306)
print(con)
cur = con.cursor()

sql = """
    create table gudong(
        id int primary key auto_increment,
        name varchar(30) not null,
        age int(2),
        score float(3,1)
    )
"""
try:
    cur.execute(sql)
    print('创建表成功！')
except Exception as e:
    print(e)
    print('创建表失败！')
finally:
    cur.close()
    con.close()


