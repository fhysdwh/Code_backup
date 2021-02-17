import pymysql


con = pymysql.connect(host = 'localhost', user = 'root', password = 'nimabi518', database = 'python_test', port = 3306)
print(con)
cur = con.cursor()

sql = 'update gudong set age=%s where id=%s'

try:
    cur.execute(sql,(30, 1))
    con.commit()
    print('修改成功！')
except Exception as e:
    print(e)
    con.rollback()
    print('修改失败！')
finally:
    cur.close()
    con.close()