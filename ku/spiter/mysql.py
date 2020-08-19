# encoding:utf-8

import pymysql
class DB:
    def connect(self):
        conn = pymysql.connect(
            host="mysql",
            user="root",
            password="!@#sspaas@U0",
            database="ku",
            charset="utf8")
        cursor = conn.cursor()
        self.conn = conn
        self.cursor = cursor
    def createDBAndTable(self):
        # 打开数据库连接
        self.connect()
        sql1 = """CREATE Database IF NOT EXISTS ku Character Set UTF8"""
        sql2 = """CREATE TABLE IF NOT EXISTS car (
            `id`  INT UNSIGNED AUTO_INCREMENT,
            `date` CHAR(200),
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
    def insert(self,array):
        self.connect()
        try:
            for i in range(len(array)):
                data = array[i]
                sql = "INSERT IGNORE INTO `car`(`id` ,`date`,`d1` ,`d2` ,`d3` ,`d4` ,`d5` ,`d6` ,`d7` ,`d8` ,`d9` ,`d10`)\
                    VALUES (%d,\'%s\',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)" % \
                    (data['id'],data['date'],data['d1'],data['d2'],data['d3'],data['d4'],data['d5'],data['d6'],data['d7'],data['d8'],data['d9'],data['d10'])
                # print(sql)
                self.cursor.execute(sql)
            self.conn.commit() # 事务提交
            print('事务处理成功', self.cursor.rowcount)# 关闭连接
        except Exception as e:
            self.conn.rollback() # 事务回滚
            print('事务处理失败', e)    
        self.disconnected()

from spider import Spider
if __name__=='__main__':
    db = DB()
    db.createDBAndTable()

    s = Spider()
    ret = s.get('2020-08-19','2020-08-19')
    print(ret[0:3])
    db.insert(ret[0:3])     




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