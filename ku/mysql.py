# encoding:utf-8

import pymysql
class DB:
    def connect(self):
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="!@#sspaas@U0",
            database="ku",
            charset="utf8")
        cursor = conn.cursor()
        self.conn = conn
        self.cursor = cursor
    def init(self):
        # 打开数据库连接
        self.connect()
        sql1 = """CREATE Database IF NOT EXISTS ku Character Set UTF8"""
        sql2 = """CREATE TABLE IF NOT EXISTS car (
            `id`  INT UNSIGNED AUTO_INCREMENT,
            `date` DATE,
            `d1` INT UNSIGNED,
            `d2` INT UNSIGNED,
            `d3` INT UNSIGNED,
            `d4` INT UNSIGNED,
            `d5` INT UNSIGNED,
            `d6` INT UNSIGNED,
            `d7` INT UNSIGNED,
            `d8` INT UNSIGNED,
            `d9` INT UNSIGNED,
            `d10` INT UNSIGNED,
            PRIMARY KEY ( `id` )
            )CHARSET=utf8"""
        try:
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
        except Exception as e:
            self.conn.rollback() # 事务回滚
            print('事务处理失败', e)
        else:
            self.conn.commit() # 事务提交
            print('事务处理成功', self.cursor.rowcount)# 关闭连接
            self.disconnected()
    def disconnected(self):
        self.cursor.close()
        self.conn.close()
        print("mysql is disconnected")

if __name__=='__main__':
    db = DB()
    db.init()
     




#     try:
#     cursor.execute(sql_1)
#     cursor.execute(sql_2)
#     cursor.execute(sql_3)
# except Exception as e:
#     connect.rollback() # 事务回滚
#     print('事务处理失败', e)
# else:
#     connect.commit() # 事务提交
#     print('事务处理成功', cursor.rowcount)# 关闭连接
#     cursor.close()
#     connect.close()