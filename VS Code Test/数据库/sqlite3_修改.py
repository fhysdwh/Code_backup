import sqlite3

con = sqlite3.connect('Database/demo1.db')
cur = con.cursor()

sql = 'update t_person set name=? where id=?'

try:
     cur.execute(sql,('张三', 1))
     con.commit()
     print('修改成功！')
except Exception as e:
    print(e)
    con.rollback()
    print('修改失败！')
finally:
    cur.close()
    con.close()
