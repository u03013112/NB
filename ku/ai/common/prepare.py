# encoding:utf-8
import requests
import numpy as np
import math
class Prepare:
    # data numpy格式的全部数据（-1,10），n为模型所需训练数据组数（每组一套结果，10个数），d为预测位置0~9
    def prepare(self,data,n,d):
        print('preparing')
        totalCount = data.shape[0]
        # 只训练80%的数据，并不用fit的时候抽样，这样可以更好的测试结果
        trainCount = math.floor(totalCount * 0.8)

        data = data.reshape(-1)
        xArray = np.array([])
        yArray = np.array([])
        for i in range(n,totalCount):
            x = data[(i-n)*10:i*10]
            y = np.zeros(10)
            yIndex = int(data[i*10+d]-1)
            y[yIndex] = 1
            xArray = np.append(xArray,x)
            yArray = np.append(yArray,y)
        
        xArray = xArray.reshape(-1,10*n)
        yArray = yArray.reshape(-1,10)

        self.trainX = xArray[0:trainCount]
        self.trainY = yArray[0:trainCount]
        self.testX = xArray[trainCount:]
        self.testY = yArray[trainCount:]
        self.x = xArray
        self.y = yArray
        print('prepared ok')

if __name__=='__main__':
    p = Prepare()
    data = np.load('../2020-08-3.npy')
    print(data[0:11])
    p.prepare(data,10,0)
    print(p.trainX[0])
    print(p.trainY[0])