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
        # early_stopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=50, verbose=2)
        # self.model.fit(trainX, trainY, epochs=100, batch_size=8,validation_data=(testX, testY),callbacks=[early_stopping])
        model_checkpoint_callback = keras.callbacks.ModelCheckpoint(
            filepath=self.filename,
            # save_weights_only=True,
            # monitor='val_acc',
            # mode='max',
            save_best_only=True)
        self.model.fit(trainX, trainY, epochs=50, batch_size=16,validation_data=(testX, testY),callbacks=[model_checkpoint_callback])
        # self.model.save(self.filename)
        return
    def test(self,testX, testY):
        model = keras.models.load_model(self.filename)
        ret = model.predict(testX)
        ret = ret.reshape(-1,10)
        y = testY.reshape(-1,10)
        # print( np.around(ret[0:10], decimals=2))

        a = ret.reshape(-1)
        a.sort()
        a1 = a[a<0.1]
        a = a[a>=0.1]
        print("0.1:",a1.shape[0])
        a2 = a[a<0.2]
        a = a[a>=0.2]
        print("0.2:",a2.shape[0])
        a3 = a[a<0.3]
        a = a[a>=0.3]
        print("0.3:",a3.shape[0])
        a4 = a[a<0.4]
        a = a[a>=0.4]
        print("0.4:",a4.shape[0])
        a5 = a[a<0.5]
        a = a[a>=0.5]
        print("0.5:",a5.shape[0])
        a6 = a[a<0.6]
        a = a[a>=0.6]
        print("0.6:",a6.shape[0])
        a7 = a[a<0.7]
        a = a[a>=0.7]
        print("0.7:",a7.shape[0])
        a8 = a[a<0.8]
        a = a[a>=0.8]
        print("0.8:",a8.shape[0])
        a9 = a[a<0.9]
        a = a[a>=0.9]
        print("0.9:",a9.shape[0])
        

        # p = 0.4
        for i in range(1,10):
            p = 0.1+i*0.01
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
            print("p=",p)
            print("totoal cost:",cost)
            print("totoal come:",come)
            print("totoal profit:",come-cost)
        return

if __name__=='__main__':
    n = 80
    p = Prepare()
    data = Data()
    ai = AI(n,'model.h5')

    # data.getAll()
    # p.prepare(data.data,n,1)
    # ai.train(p.trainX,p.trainY,p.testX,p.testY)
    # ai.test(p.testX,p.testY)

    data.getLatest(1000)
    p.prepare(data.data,n,1)
    ai.test(p.x,p.y)
