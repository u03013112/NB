# encoding:utf-8
import requests
import numpy as np
class Data:
    def get(self,startdate,enddate):
        url = "https://sbmm1.onestalk.com/share/ajax/GetLotteryResults.aspx"
        body = {'gType':'156','startdate':startdate,'enddate':enddate,'search':2}
        headers = {'Cookie':'ASP.NET_SessionId=koekpx2gj5kkdhzsxzalfhsp; visid_incap_2284640=IfCJbI6xQHa2lRU7ibA55RKtNl8AAAAAQUIPAAAAAABsU5jO6qjbsCNtX0bmYqAo; incap_ses_797_2284640=2haLTO1ALUZM14GjWYMPCxKtNl8AAAAAItrzbM9D5hlkm9Cija34Mw==; visid_incap_2029550=4OfWmEuvQgeZFKL9bWl5ihStNl8AAAAAQUIPAAAAAAC5lloctlyDFr+epFIUIMn3; incap_ses_797_2029550=+x3cKodsZTEm2oGjWYMPCxStNl8AAAAAKvrHgsvZcVNNd8HLikd+vA=='}
        try:
            r = requests.post(url,body, headers = headers)
        except requests.exceptions.RequestException as e:
            print(e)
            return
        # print(r.json())
        dataNp = np.array([])
        data = r.json()
        for k in range(len(data)-1,-1,-1):
            v = data[str(k)]
            # print(v)
            v1 = v['Num1']
            v2 = v['Num2']
            v3 = v['Num3']
            v4 = v['Num4']
            v5 = v['Num5']
            v6 = v['Num6']
            v7 = v['Num7']
            v8 = v['Num8']
            v9 = v['Num9']
            v10 = v['Num10']
            dataNp = np.append(dataNp,[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10])
        dataNp = dataNp.reshape(-1,10)
        self.data = dataNp
    def save(self,filename):
        np.save(filename,self.data)
    def load(self,filename):
        self.data = np.load(filename)
    def show(self):
        print(self.data)      
    def balance(self):
        # 查看是否足够平均
        a = self.data
        for i in range(10):
            ret = np.zeros(10)
            for j in range(a.shape[0]):
                # print(int(a[j][i]))
                ret[int(a[j][i])-1] = ret[int(a[j][i])-1] + 1
            print(i,":",ret)


if __name__=='__main__':
    data = Data()

    # data.get('2020-07-1','2020-07-31')
    # data.save('2020-07.npy')
    # data.balance()

    # data.get('2020-08-1','2020-08-14')
    # data.save('2020-08.npy')
    # data.balance()

    a = np.load('2020-08.npy')
    print(a.shape)
    b = 499+491+454+502+467+539+443+506+544+460
    print(b)
