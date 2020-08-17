# encoding:utf-8
import requests
import numpy as np
import math
class Data:
    def get(self,startdate,enddate):
        url = "https://sbmm1.onestalk.com/share/ajax/GetLotteryResults.aspx"
        body = {'gType':'156','startdate':startdate,'enddate':enddate,'search':2}
        headers = {'Cookie':'visid_incap_2029550=hGd+MMXbTomBPGG11gpesHmjK18AAAAAQUIPAAAAAAA0hAYgF7M8V0mjOx7y2ejd; visid_incap_2284640=yRswnQSjS4OZ8Yeg4wxkg3mjK18AAAAAQUIPAAAAAACtDu70GgPVGFAYFmlTkrQ5; ASP.NET_SessionId=dbzec4o5g5gzcg1atmrvneau; visid_incap_1291906=wLPQllFMSuuOu1dW4zRTh6F0Ml8AAAAAQUIPAAAAAAAzgGRD0qwOcjuqZw9P0mRI; visid_incap_2029546=5qVkmx5USPGElFdyDncBR6V0Ml8AAAAAQUIPAAAAAAC0cfFzfJJ/4ERCTCpI2XCC; visid_incap_2061726=YOD3c0usRsGqa6q1j6/rC6V0Ml8AAAAAQUIPAAAAAAAC+RmEtUCq1Vcqyfqy+L1T; incap_ses_628_2029546=IOmtFFPYJArC1PgrwRq3CG2PM18AAAAAcn1MHcsa96iyeO8AKUCDLQ==; incap_ses_628_2061726=c33RFzsJ7AqT1/grwRq3CG2PM18AAAAAYvVPV+/o4wMglJxxsWyAQg==; visid_incap_2155316=5jyWu9ceRf2wW7n88MGWJiIRNl8AAAAAQUIPAAAAAAAPx+iVg8ln6eed0W2fWMAg; incap_ses_628_2155316=U5qDaQqv8gJXQ2o6wRq3CCIRNl8AAAAAj/nVgdY2qJITcu8/CS/x1w==; incap_ses_1222_1291906=zdZbL3++/k/qixTalmr1EAVgNl8AAAAA51C4QQDiF0A9djVYPZpwUQ==; incap_ses_628_2284640=sQ9QP0tlDTEI8ac8wRq3CAtgNl8AAAAAQe+yBqy+2lwIlgrK565eSg==; incap_ses_628_2029550=MIYrNHeyCU5R86c8wRq3CA1gNl8AAAAATzQ6vk2VQc0BSH4gSOrT0A==; visid_incap_2130188=aQtH+9NIRLGfkMHX3nCH1sFgNl8AAAAAQUIPAAAAAADM1VJxXNODl+AQW+fyjXgW; incap_ses_628_2130188=0IdHEUhrr0xnCKk8wRq3CMFgNl8AAAAA/3G4xsRgdZtr7aMsAsVP6A==; visid_incap_2029537=dxa86zT1T9uprtU6BFtvkssqOl8AAAAAQUIPAAAAAAAElNlZ9/jJOGDiZMFgAdQ3; incap_ses_1205_2029537=pYflFdOyUFMB4UjuLQW5EMsqOl8AAAAA5NZde0OajFhmreppSAwMOw==; visid_incap_2155285=9dtmo9ZLTP++I7J8Rxp2ac0qOl8AAAAAQUIPAAAAAAC4GdSngJGB3AiY3gE8D7sy; incap_ses_1205_2155285=bcx2OKaHIl9v40juLQW5EM0qOl8AAAAAMYbJGG+pNWRi52wF1URgGA=='}
        try:
            r = requests.post(url,body, headers = headers)
        except requests.exceptions.RequestException as e:
            print(e)
            return
        # print(r.json())
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

    # data.get('2020-08-3','2020-08-3')
    # data.save('2020-08-3.npy')
    # data.balance()

    # data.get('2020-08-1','2020-08-14')
    # data.save('2020-08.npy')
    # data.balance()

    # a = np.load('2020-08.npy')
    # print(a.shape)
    # b = 499+491+454+502+467+539+443+506+544+460
    # print(b)

    data.load('2020-08-3.npy')
    # print(data.data[0:3])
    data.prepare()
    print(data.trainX[0:3])
    print(data.trainY[0:3])
    # print(data.testX[0:3])
    # print(data.testY[0:3])

    # y = np.arange(1,11)
    # print(y)
    # np.random.shuffle(y)
    # print(y)
    # print(data.y(y))