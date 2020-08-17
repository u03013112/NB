# encoding:utf-8

import numpy as np
from data import Data
from tensorflow import keras
from tensorflow.keras import layers

class AI:
    def __init__(self,n):
        model = keras.Sequential(
            [
                keras.Input(shape=(100)),
                keras.layers.Dense(n*10, activation="relu"),
                # keras.layers.Dropout(0.3),
                keras.layers.Dense(256, activation="relu"),
                # keras.layers.Dropout(0.3),
                keras.layers.Dense(100, activation="sigmoid"),
            ]
        )
        model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])
        # model.summary()
        self.model = model
        
    def train(self,x,y):
        print(x[0:3])
        print(y[0:3])
        self.model.fit(x, y, epochs=5, batch_size=32)
        return
    def test(self,x,y):
        loss_and_metrics = self.model.evaluate(x, y, batch_size=128)
        print(loss_and_metrics)
        return

if __name__=='__main__':
    data = Data()
    data.load('2020-08-3.npy')
    data.prepare()

    ai = AI(10)
    ai.train(data.trainX,data.trainY)
    ai.test(data.testX,data.testY)
