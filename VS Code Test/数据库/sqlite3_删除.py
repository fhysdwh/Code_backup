import sqlite3

con = sqlite3.connect('Database/demo1.db')
cur = con.cursor()

sql = 'delete from t_person where id=?'

try:
     cur.execute(sql,(1, ))
     con.commit()
     print('删除成功！')
except Exception as e:
    print(e)
    con.rollback()
    print('删除失败！')
finally:
    cur.close()
    con.close()
