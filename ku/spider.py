# encoding:utf-8
import requests
import numpy as np
import math
from login import Login
class Data:
    def __init__(self):
        self.cookie = Login().getCookies()
    def get(self,startdate,enddate):
        url = "https://sbmm1.onestalk.com/share/ajax/GetLotteryResults.aspx"
        body = {'gType':'156','startdate':startdate,'enddate':enddate,'search':2}
        headers = {'Cookie':self.cookie}
        try:
            r = requests.post(url,body, headers = headers)
        except requests.exceptions.RequestException as e:
            print(e)
            return
        # print(r.json())
        if r.json().get('status') == 'Msg_Logout':
            print('need login')
            self.cookie = Login().getCookies()
            return
        else:
            print('got',len(r.json()),'data')
        ret = []
        data = r.json()
        for k in range(len(data)-1,-1,-1):
            v = data[str(k)]
            # print(v)
            d = {}
            d['d1'] = int(v['Num1'])
            d['d2'] = int(v['Num2'])
            d['d3'] = int(v['Num3'])
            d['d4'] = int(v['Num4'])
            d['d5'] = int(v['Num5'])
            d['d6'] = int(v['Num6'])
            d['d7'] = int(v['Num7'])
            d['d8'] = int(v['Num8'])
            d['d9'] = int(v['Num9'])
            d['d10'] = int(v['Num10'])
            d['id'] = int(v['Gid'])
            d['date'] = v['Date']
            ret.append(d)
        return ret
    
if __name__=='__main__':
    data = Data()
    ret = data.get('2020-08-18','2020-08-18')
    print(ret)
    