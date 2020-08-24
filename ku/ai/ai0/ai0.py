# encoding:utf-8
import math
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import sys
sys.path.append("..")
from common.prepare import Prepare
from common.data import Data

class AI:
    def __init__(self,n,filename):
        self.n = n
        self.filename = filename
        self.model = self.createModel()        
    def createModel(self):
        n = self.n
        model = keras.Sequential(
            [
                keras.Input(shape=(n*10)),
                keras.layers.Dense(512, activation="relu"),
                keras.layers.Dropout(0.3),
                keras.layers.Dense(512, activation="relu"),
                keras.layers.Dropout(0.3),
                keras.layers.Dense(512, activation="relu"),
                keras.layers.Dropout(0.3),
                keras.layers.Dense(10, activation="softmax"),
            ]
        )
        model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])
        return model    
    def train(self,trainX,trainY,testX,testY):
        early_stopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=50, verbose=2)
        # self.model.fit(trainX, trainY, epochs=100, batch_size=8,validation_data=(testX, testY),callbacks=[early_stopping])
        self.model.fit(trainX, trainY, epochs=50, batch_size=16,validation_data=(testX, testY))
        self.model.save(self.filename)
        return
    def test(self,testX, testY):
        model = keras.models.load_model(self.filename)
        ret = model.predict(testX)
        ret = ret.reshape(-1,10)
        y = testY.reshape(-1,10)
        print( np.around(ret[0:10], decimals=2))
        p = 0.4
        cost = 0 
        come = 0
        print("count:",y.shape[0])

        for i in range(ret.shape[0]):
            r0 = ret[i].reshape(-1)
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
    n = 40
    p = Prepare()
    data = Data()
    # data.getAll()
    data.getLatest(1000)
    p.prepare(data.data,n,0)

    ai = AI(n,'model.h5')
    # ai.train(p.trainX,p.trainY,p.testX,p.testY)
    # ai.test(p.testX,p.testY)
    ai.test(p.x,p.y)
