# encoding:utf-8
import math
import numpy as np
from data import Data
from tensorflow import keras
from tensorflow.keras import layers

class AI0:
    def __init__(self,n):
        self.n = n
        self.model0 = self.createModel()
        self.model1 = self.createModel()
        self.model2 = self.createModel()
    def createModel(self):
        n = self.n
        model = keras.Sequential(
            [
                keras.Input(shape=(n*10)),
                keras.layers.Dense(512, activation="relu"),
                keras.layers.Dropout(0.2),
                keras.layers.Dense(512, activation="relu"),
                keras.layers.Dropout(0.2),
                keras.layers.Dense(512, activation="relu"),
                keras.layers.Dropout(0.1),
                keras.layers.Dense(512, activation="relu"),
                keras.layers.Dropout(0.1),
                keras.layers.Dense(512, activation="relu"),
                keras.layers.Dropout(0.1),
                keras.layers.Dense(512, activation="relu"),
                keras.layers.Dropout(0.1),
                keras.layers.Dense(512, activation="relu"),
                keras.layers.Dropout(0.1),
                keras.layers.Dense(512, activation="relu"),
                keras.layers.Dropout(0.1),
                keras.layers.Dense(512, activation="relu"),
                keras.layers.Dropout(0.1),
                keras.layers.Dense(512, activation="relu"),
                keras.layers.Dropout(0.1),
                keras.layers.Dense(10, activation="softmax"),
            ]
        )
        model.compile(loss='categorical_crossentropy',optimizer='RMSprop',metrics=['accuracy'])
        return model
    def prepare(self,filename):
        # 只预测第一名的测试
        print('preparing')
        data = np.load(filename)
        totalCount = data.shape[0]
        trainCount = math.floor(totalCount * 0.75)

        n = self.n
        data = data.reshape(-1)
        trainX = np.array([])
        trainY0 = np.array([])
        trainY1 = np.array([])
        trainY2 = np.array([])
        for i in range(n,trainCount):
            x = data[(i-n)*10:i*10]
            trainX = np.append(trainX,x)

            y0 = np.zeros(10)
            y0[int(data[i*10])-1] = 1
            trainY0 = np.append(trainY0,y0)

            y1 = np.zeros(10)
            y1[int(data[i*10+1])-1] = 1
            trainY1 = np.append(trainY1,y1)

            y2 = np.zeros(10)
            y2[int(data[i*10+2])-1] = 1
            trainY2 = np.append(trainY2,y2)
        
        self.trainX = trainX.reshape(-1,10*n)
        self.trainY0 = trainY0.reshape(-1,10)
        self.trainY1 = trainY1.reshape(-1,10)
        self.trainY2 = trainY2.reshape(-1,10)

        testX = np.array([])
        testY0 = np.array([])
        testY1 = np.array([])
        testY2 = np.array([])
        for i in range(trainCount,totalCount):
            x = data[(i-n)*10:i*10]
            testX = np.append(testX,x)
            
            y0 = np.zeros(10)
            y0[int(data[i*10])-1] = 1
            testY0 = np.append(testY0,y0)

            y1 = np.zeros(10)
            y1[int(data[i*10+1])-1] = 1
            testY1 = np.append(testY1,y1)

            y2 = np.zeros(10)
            y2[int(data[i*10+2])-1] = 1
            testY2 = np.append(testY2,y2)
        
        self.testX = testX.reshape(-1,10*n)
        self.testY0 = testY0.reshape(-1,10)
        self.testY1 = testY1.reshape(-1,10)
        self.testY2 = testY2.reshape(-1,10)
        print('prepared ok')
        
    def train(self):
        early_stopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=50, verbose=2)
        self.model0.fit(self.trainX, self.trainY0, epochs=200, batch_size=16,validation_data=(self.testX, self.testY0),callbacks=[early_stopping])
        self.model0.save('my_model0.h5')
        self.model1.fit(self.trainX, self.trainY1, epochs=200, batch_size=16,validation_data=(self.testX, self.testY1),callbacks=[early_stopping])
        self.model1.save('my_model1.h5')
        self.model2.fit(self.trainX, self.trainY2, epochs=200, batch_size=16,validation_data=(self.testX, self.testY2),callbacks=[early_stopping])
        self.model2.save('my_model2.h5')
        return
    def test(self):
        model = keras.models.load_model('my_model0.h5')
        ret0 = model.predict(self.testX)
        ret0 = ret0.reshape(-1,10)
        y = self.testY0.reshape(-1,10)
        print(ret0[0:10])
        p = 0.11
        cost = 0 
        come = 0
        print("count:",y.shape[0])

        for i in range(ret0.shape[0]):
            r0 = ret0[i].reshape(-1)
            r1 = y[i].reshape(-1)
            for j in range(r0.shape[0]):
                if r0[j] > p:
                    cost = cost + 1
                    if r1[j] == 1:
                        come = come + 9.9
        
        print("totoal cost:",cost)
        print("totoal come:",come)
        print(come-cost)
        return

if __name__=='__main__':
    ai = AI0(40)
    ai.prepare('2020-08.npy')
    # np.save('tx0.npy',ai.trainX)
    # np.save('ty0.npy',ai.trainY)
    # np.save('x0.npy',ai.testX)
    # np.save('y0.npy',ai.testY)
    # tx = np.load('tx0.npy')
    # ty = np.load('ty0.npy')
    # x = np.load('x0.npy')
    # y = np.load('y0.npy')
    # ai.train()
    ai.test()
