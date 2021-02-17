import pymysql


con = pymysql.connect(host = 'localhost', user = 'root', password = 'nimabi518', database = 'python_test', port = 3306)
print(con)
cur = con.cursor()

sql = 'select * from gudong'

try:
   
    cur.execute(sql)
    data_one = cur.fetchone()
    print(data_one)
    data_all = cur.fetchall()
    print(len(data_all))
    for data in data_all:
        print(data[1])
    print('查询成功！')
except Exception as e:
    print(e)
    print('查询失败！')
finally:
    cur.close()
    con.close()