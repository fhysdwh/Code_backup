import sqlite3

con = sqlite3.connect('Database/demo1.db')
cur = con.cursor()

sql = 'insert into t_person(name, age) values(?, ?)'

try:
    cur.execute(sql,('李四', 23))
    con.commit()
    print('插入成功')
except Exception as e:
    print(e)
    con.rollback()
    print('插入失败')
finally:
    cur.close()
    con.close()
