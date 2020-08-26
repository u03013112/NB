# encoding:utf-8

import pymysql
class DB:
    def connect(self):
        conn = pymysql.connect(
            # host="mysql",
            host="www.u03013112.cn",
            user="root",
            password="!@#sspaas@U0",
            database="ku",
            charset="utf8")
        cursor = conn.cursor()
        self.conn = conn
        self.cursor = cursor
    def disconnected(self):
        self.cursor.close()
        self.conn.close()
        # print("mysql is disconnected")
    def getLatest(self,n):
        ret = []
        self.connect()
        try:
            sql = "SELECT * FROM (SELECT * FROM `car` ORDER BY `id` DESC LIMIT %d) as t ORDER BY `id` ASC" % n
            print(sql)
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                r = {}
                r['gid'] = row[0]
                r['date'] = row[1]
                r['d1'] = row[2]
                r['d2'] = row[3]
                r['d3'] = row[4]
                r['d4'] = row[5]
                r['d5'] = row[6]
                r['d6'] = row[7]
                r['d7'] = row[8]
                r['d8'] = row[9]
                r['d9'] = row[10]
                r['d10'] = row[11]
                ret.append(r)
        except Exception as e:
            print('getLatest失败', e)
        self.disconnected()
        return ret
    def getRange(self,n,m):
        ret = []
        self.connect()
        try:
            sql = "SELECT * FROM `car` ORDER BY `id` ASC LIMIT %d,%d" % (n,m)
            print(sql)
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                r = {}
                r['gid'] = row[0]
                r['date'] = row[1]
                r['d1'] = row[2]
                r['d2'] = row[3]
                r['d3'] = row[4]
                r['d4'] = row[5]
                r['d5'] = row[6]
                r['d6'] = row[7]
                r['d7'] = row[8]
                r['d8'] = row[9]
                r['d9'] = row[10]
                r['d10'] = row[11]
                ret.append(r)
        except Exception as e:
            print('getLatest失败', e)
        self.disconnected()
        return ret
    def getAll(self):
        ret = []
        self.connect()
        try:
            sql = "SELECT * FROM `car` ORDER BY `id` ASC"
            print(sql)
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                r = {}
                r['gid'] = row[0]
                r['date'] = row[1]
                r['d1'] = row[2]
                r['d2'] = row[3]
                r['d3'] = row[4]
                r['d4'] = row[5]
                r['d5'] = row[6]
                r['d6'] = row[7]
                r['d7'] = row[8]
                r['d8'] = row[9]
                r['d9'] = row[10]
                r['d10'] = row[11]
                ret.append(r)
        except Exception as e:
            print('getAll', e)
        self.disconnected()
        return ret
    def createTableP(self):
        # 打开数据库连接
        self.connect()
        sql2 = """CREATE TABLE IF NOT EXISTS car_p (
            `id`  INT UNSIGNED AUTO_INCREMENT,
            `in` INT UNSIGNED,
            `out` INT UNSIGNED,
            `backup` TEXT(1024),
            `done` INT UNSIGNED,
            PRIMARY KEY ( `id` )
            )CHARSET=utf8"""
        try:
            self.cursor.execute(sql2)
        except Exception as e:
            self.conn.rollback() # 事务回滚
            print('事务处理失败', e)
        else:
            self.conn.commit() # 事务提交
            print('事务处理成功', self.cursor.rowcount)# 关闭连接
            self.disconnected()
    def insertP(self,array):
        self.connect()
        try:
            for i in range(len(array)):
                data = array[i]
                sql = "INSERT IGNORE INTO `car_p`(`id` ,`in`,`out`,`backup`,`done`)\
                    VALUES (%d,%d,%d,'%s',%d)" % \
                    (data['id'],data['in'],data['out'],data['backup'],data['done'])
                # print(sql)
                self.cursor.execute(sql)
            self.conn.commit() # 事务提交
            print('事务处理成功', self.cursor.rowcount)# 关闭连接
        except Exception as e:
            self.conn.rollback() # 事务回滚
            print('事务处理失败', e)    
        self.disconnected()
    def getLatestP(self,n):
        ret = []
        self.connect()
        try:
            sql = "SELECT * FROM (SELECT * FROM `car_p` ORDER BY `id` DESC LIMIT %d) as t ORDER BY `id` ASC" % n
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                r = {}
                r['gid'] = row[0]
                r['in'] = row[1]
                r['out'] = row[2]
                r['backup'] = row[3]
                r['done'] = row[4]
                ret.append(r)
        except Exception as e:
            print('getLatest失败', e)
        self.disconnected()
        return ret
    def query(self,sql):
        self.connect()
        results = None
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            self.conn.commit() # 事务提交
            print('事务处理成功', self.cursor.rowcount)
        except Exception as e:
            print('getLatest失败', e)
        
        self.disconnected()
        return results

if __name__=='__main__':
    db = DB()
    print(db.getRange(1000,2000)[0])