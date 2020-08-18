# encoding:utf-8
import requests
import numpy as np
import math
class Data:
    def get(self,startdate,enddate):
        url = "https://sbmm1.onestalk.com/share/ajax/GetLotteryResults.aspx"
        body = {'gType':'156','startdate':startdate,'enddate':enddate,'search':2}
        headers = {'Cookie':'ASP.NET_SessionId=pbet31czrfg201e31pps2z2v'}
        try:
            r = requests.post(url,body, headers = headers)
        except requests.exceptions.RequestException as e:
            print(e)
            return
        # print(r.json())
        if r.json().get('status') == 'Msg_Logout':
            print('need login')
            return
        else:
            print('got',len(r.json()),'data')
        dataNp = np.array([])
        data = r.json()
        for k in range(len(data)-1,-1,-1):
            v = data[str(k)]
            # print(v)
            v1 = int(v['Num1'])
            v2 = int(v['Num2'])
            v3 = int(v['Num3'])
            v4 = int(v['Num4'])
            v5 = int(v['Num5'])
            v6 = int(v['Num6'])
            v7 = int(v['Num7'])
            v8 = int(v['Num8'])
            v9 = int(v['Num9'])
            v10 = int(v['Num10'])
            dataNp = np.append(dataNp,[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10])
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
    def y(self,y):#对结果进行处理，将一维名次数组，变为二维名次数组
        ret = np.zeros(100).reshape(-1,10)
        for i in range(10):
            ret[i,int(y[i]-1)]=1
        return ret

    def prepare(self):
        print('preparing')
        totalCount = self.data.shape[0]
        trainCount = math.floor(totalCount * 0.75)

        n = 10 #采样数，根据前n组结果，猜这次的结果
        data = self.data.reshape(-1)
        trainX = np.array([])
        trainY = np.array([])
        for i in range(n,trainCount):
            x = data[(i-10)*10:i*10]
            y = self.y(data[i*10:(i+1)*10])
            trainX = np.append(trainX,x)
            trainY = np.append(trainY,y)
        
        self.trainX = trainX.reshape(-1,10*n)
        self.trainY = trainY.reshape(-1,100)

        testX = np.array([])
        testY = np.array([])
        for i in range(trainCount,totalCount):
            x = data[(i-10)*10:i*10]
            y = self.y(data[i*10:(i+1)*10])
            testX = np.append(testX,x)
            testY = np.append(testY,y)
        
        self.testX = testX.reshape(-1,10*n)
        self.testY = testY.reshape(-1,100)
        print('prepared ok')

if __name__=='__main__':
    data = Data()

    data.get('2020-08-18','2020-08-18')
    # data.save('2020-08-3.npy')
    # data.balance()

    # data.get('2020-08-1','2020-08-14')
    # data.save('2020-08.npy')
    # data.balance()

    # a = np.load('2020-08.npy')
    # print(a.shape)
    # b = 499+491+454+502+467+539+443+506+544+460
    # print(b)

    # data.load('2020-08-3.npy')
    # print(data.data[0:3])
    # data.prepare()
    # print(data.trainX[0:3])
    # print(data.trainY[0:3])
    # print(data.testX[0:3])
    # print(data.testY[0:3])

    # y = np.arange(1,11)
    # print(y)
    # np.random.shuffle(y)
    # print(y)
    # print(data.y(y))