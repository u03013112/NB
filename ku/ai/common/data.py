# encoding:utf-8
import requests
import numpy as np
import math
from common.mysql import DB
class Data:
    def getAll(self):
        db = DB()
        data = db.getAll()
        # data = db.getLatest(10)
        dataNp = np.array([])
        for v in data:
            dataNp = np.append(dataNp,[v['d1'],v['d2'],v['d3'],v['d4'],v['d5'],v['d6'],v['d7'],v['d8'],v['d9'],v['d10']])
        dataNp = dataNp.reshape(-1,10)
        self.data = dataNp
    def save(self,filename):
        np.save(filename,self.data)
    def load(self,filename):
        print('loading',filename)
        self.data = np.load(filename)
        print('load ok',filename)
    def show(self):
        print(self.data)      
    def balance(self):
        # 查看是否足够平均
        a = self.data
        for i in range(10):
            ret = np.zeros(10)
            for j in range(a.shape[0]):
                # print(int(a[j][i]))
                ret[int(a[j][i])-1] = ret[int(a[j][i])-1] + 1
            print(i,":",ret)
    
if __name__=='__main__':
    data = Data()
    data.getAll()
    # print(data.data)
    data.balance()