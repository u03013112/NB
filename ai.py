# encoding:utf-8

import numpy as np
from data import Data
from tensorflow import keras
from tensorflow.keras import layers

class AI:
    def __init__(self,n):
        model = keras.Sequential(
            [
                keras.Input(shape=(n*10)),
                keras.layers.Dense(256, activation="relu"),
                keras.layers.Dense(256, activation="relu"),
                keras.layers.Dense(256, activation="relu"),
                # keras.layers.Dropout(0.3),
                keras.layers.Dense(100, activation="sigmoid"),
            ]
        )
        model.compile(loss='categorical_crossentropy',optimizer='sgd')
        # model.summary()
        self.model = model
        
    def train(self,x,y):
        # print(x[0:3])
        # print(y[0:3])
        self.model.fit(x, y, epochs=200, batch_size=16)
        self.model.save('my_model.h5')
        return
    def test(self,x,y):
        model = keras.models.load_model('my_model.h5')
        # print(x.shape)
        ret = model.predict(x)
        ret = np.around(ret, decimals=2)
        ret = ret.reshape(-1,10,10)
        print(ret[0])
        print(y[0].reshape(-1,10))

        print(ret[1])
        print(y[1].reshape(-1,10))

        print(ret[2])
        print(y[2].reshape(-1,10))

        
        return

if __name__=='__main__':
    # data = Data()
    # data.load('2020-08.npy')
    # data.prepare()

    # np.save('tx.npy', data.trainX)
    # np.save('ty.npy', data.trainY)

    # np.save('x.npy', data.testX)
    # np.save('y.npy', data.testY)

    x = np.load('x.npy')
    y = np.load('y.npy')
    ai = AI(10)
    # ai.train(x,y)
    ai.test(x,y)
