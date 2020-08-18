# encoding:utf-8
import math
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

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
    def train(self,trainX,trainY,testX,testY):
        early_stopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=50, verbose=2)
        self.model.fit(trainX, trainY, epochs=100, batch_size=8,validation_data=(testX, testY),callbacks=[early_stopping])
        self.model.save(self.filename)
        return
    def test(self,testX, testY):
        model = keras.models.load_model(self.filename)
        ret = model.predict(testX)
        ret = ret.reshape(-1,10)
        y = testY.reshape(-1,10)
        print(ret[0:10])
        p = 0.11
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
    ai = AI(40)
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
