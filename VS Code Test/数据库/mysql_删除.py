import pymysql


con = pymysql.connect(host = 'localhost', user = 'root', password = 'nimabi518', database = 'python_test', port = 3306)
print(con)
cur = con.cursor()

sql = 'delete from gudong where id=%s'

try:
    cur.execute(sql,(2))
    con.commit()
    print('删除成功！')
except Exception as e:
    print(e)
    con.rollback()
    print('删除失败！')
finally:
    cur.close()
    con.close()