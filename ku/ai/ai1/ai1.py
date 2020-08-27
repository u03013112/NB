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
            verbose=1,
            monitor='val_accuracy',
            mode='max',
            save_best_only=True)
        self.model.fit(trainX, trainY, epochs=50, batch_size=16,validation_split=0.2,callbacks=[model_checkpoint_callback])
        # self.model.save(self.filename)
        return
    def test(self,testX, testY):
        model = keras.models.load_model(self.filename)
        ret = model.predict(testX)
        ret = ret.reshape(-1,10)
        y = testY.reshape(-1,10)
        
        cost = 0 
        come = 0
        retStr = "count:"+str(y.shape[0]) + "\n"

        for i in range(ret.shape[0]):
            cost += 2
            r0 = np.argmax(ret[i])
            r1 = np.argmax(y[i])
            if r0 == r1:
                come += 9.9*2
        retStr += "totoal cost:" + str(cost) + "\n"
        retStr += "totoal come:" + str(come) + "\n"
        retStr += "totoal profit:" + str(come-cost) + "\n"
        print(retStr)
        return retStr
    def load(self):
        self.model = keras.models.load_model(self.filename)
    def predict(self,data40):
        data = data40.reshape(-1,400)
        ret = self.model.predict(data)
        ret = ret.reshape(-1)
        # print(ret)
        a = []
        for i in range(ret.shape[0]):
            if ret[i] > 0.101:
                a.append(i+1)
        return a

if __name__=='__main__':
    n = 40
    p = Prepare()
    data = Data()
    
    retStr = ''
    for i in range(10):
        retStr += '\n第'+str(i+1)+'名:\n'
        ai = AI(n,'model'+str(i)+'.h5')
        data.getAll()
        p.prepare(data.data,n,i)
        ai.train(p.trainX,p.trainY,p.testX,p.testY)
        retStr += ai.test(p.testX,p.testY) + "\n"

    print(retStr)
    # data.getLatest(200)
    # p.prepare(data.data,n,0)
    # ai.test(p.x,p.y)

    # data.getLatest(40)
    # r = ai.predict(data.data)
    # print(r)
