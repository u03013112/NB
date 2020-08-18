# encoding:utf-8

import pymysql
class DB:
    def __init__(self):
        # 打开数据库连接
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="!@#sspaas@U0",
            database="ku",
            charset="utf8")
        
        cursor = conn.cursor()

        sql = """CREATE Database IF NOT EXISTS ku Character Set UTF8"""
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS car (
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
        cursor.execute(sql)
        self.conn = conn
        print("mysql is connected")
    def exit(self):
        self.conn.close()
        print("mysql is disconnected")

if __name__=='__main__':
    db = DB()
    db.exit()  