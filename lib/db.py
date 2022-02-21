from unittest import result
import pymysql

def get_db_conn():
    conn = pymysql.connect(
    host="10.10.1.173",
    port=3307,
    user="root",
    password="root",
    database="ums_new",
    charset='utf8'
    )
    return conn

def query_db(sql):
    conn =get_db_conn()
    cur = conn.cursor()
    cur.execute(sql)
    result= cur.fetchall()
    cur.close()
    conn.close()
    return result

def check_user(name):
    sql = "select * from user_info where `name`='{}'".format(name)
    result= query_db(sql)
    return True if result else False

    