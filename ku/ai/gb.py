# encoding:utf-8
import time

from common.mysql import DB
from common.data import Data
from ai0.ai0 import AI as AI0

class GB:
    def __init__(self):
        db = DB()
        db.createTableP()
    def done(self):
        db = DB()
        d = db.getLatestP(100)
        for j in range(len(d)):
            dp = d[j]
            if dp['done'] == 0:
                sql = "SELECT * FROM `car` WHERE `id`=%d" % dp['gid']
                print(sql)
                ret = db.query(sql)
                if len(ret) != 1:
                    print('len(ret)!=1',len(ret))
                    return
                print(ret)
                out = 0
                backup = dp['backup']
                backupA1 = backup.split(',')
                for i in range(len(backupA1)):
                    backupA2 = backupA1[i].split('-')
                    if len(backupA2) == 2:
                        mingci = int(backupA2[0])
                        num = int(backupA2[1])
                        print(mingci,num)
                        if num == ret[0][1+mingci]:
                            out = out + 20
                print(out)
                sql = "UPDATE `car_p` SET `done`=1,`out`=%d WHERE `id`=%d" % (out,dp['gid'])
                print(sql)
                ret = db.query(sql)
    def getLatestGID(self):
        db = DB()
        d = db.getLatest(1)
        if len(d) > 0:
            gid = d[0]['gid']
            return gid
        return 0
    def getLatestGIDP(self):
        db = DB()
        d = db.getLatestP(1)
        if len(d) > 0:
            gid = d[0]['gid']
            return gid
        return 0
    def checkNeedBeDone(self):
        db = DB()
        d = db.getLatestP(1)
        if len(d) > 0:
            if d[0]['done'] == 0:
                return True
        return False
    def checkNeedPredict(self):
        gid0 = self.getLatestGID()
        gid1 = self.getLatestGIDP()
        if gid0 >= gid1:
            print('来新题目了')
            return True
        print('不需要计算',gid0,gid1)
        return False
    def predict(self):
        array = []

        data = {}
        r = self.predict0()
        backup = ''
        inCount = 0
        for i in range(len(r)):
            backup = backup + "1-"+str(r[i])+","
            inCount = inCount + 2
        data['id'] = self.getLatestGID()+1
        data['in'] = inCount
        data['backup'] = backup
        data['out'] = 0
        data['done'] = 0

        array.append(data)

        db = DB()
        db.insertP(array)
    def predict0(self):
        n = 40
        ai = AI0(n,'ai0/model.h5')
        ai.load()
        data = Data()
        data.getLatest(n)
        x = data.data
        r = ai.predict(x)
        return r

if __name__=='__main__':
    gb = GB()
    while (True):
        time.sleep(30)
        if gb.checkNeedPredict():
            gb.predict()
        gb.done()