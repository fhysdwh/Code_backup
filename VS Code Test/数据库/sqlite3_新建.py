import sqlite3


con = sqlite3.connect('Database/demo1.db')
cur = con.cursor()
sql = """create table t_person(
    id INTEGER primary key autoincrement,
    name VARCHAR not null,
    age INTEGER
    )"""
try:
    cur.execute(sql)
    print('创建表成功！')
except Exception as e:
    print(e)
    print('创建表失败！')
finally:
    cur.close()
    con.close()


