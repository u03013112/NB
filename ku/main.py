# encoding:utf-8

import numpy as np
from prepare import Prepare
from ai import AI

if __name__=='__main__':
    n = 40
    p = Prepare()
    data = np.load('../2020-08.npy')
    p.prepare(data,n,3)

    ai = AI(n,'./models/model_40_3.h5')
    ai.train(p.trainX,p.trainY,p.testX,p.testY)
    ai.test(p.testX,p.testY)
