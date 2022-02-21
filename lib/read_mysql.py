
import pymysql

conn = pymysql.connect(
    host="10.10.1.173",
    port=3307,
    user="root",
    password="root",
    database="ums_new",
    charset='utf8'
)

cur = conn.cursor()

cur.execute("select * from user_info where `name`='1'")
result = cur.fetchall()
print(result)
cur.close()
conn.close()

