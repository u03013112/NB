# encoding:utf-8
import sys
sys.path.append("..")
from common.prepare import Prepare
from common.data import Data

from ai1 import AI

class Go:
    def __init__(self):
        self.n = 40
        pass
    def go(self):
        p = Prepare()
        data = Data()
        ret = []
        data.getLatest(self.n)
        for i in range(10):
            ai = AI(self.n,'model'+str(i)+'.h5')
            a = ai.predict(data.data)
            ret.append(a)
        return ret

if __name__=='__main__':
    go = Go()
    print(go.go())