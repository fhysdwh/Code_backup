import sqlite3

con = sqlite3.connect('Database/demo1.db')
cur = con.cursor()

sql = 'select * from t_person'

try:
    cur.execute(sql)
    #单条查询
    # data = cur.fetchone()
    #查询多条，返回一个由元组组成的序列
    data_all = cur.fetchall()
    print(len(data_all))

    for data in data_all:
        print(data)
    
    print('查询结束！')
except Exception as e:
    print(e)
    print('查询失败')
finally:
    cur.close()
    con.close()
