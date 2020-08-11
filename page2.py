# encoding:utf-8
import time
import pyautogui
from pic import Pic

p2url = "/Home/Game"
dt = 1
class Page2:
    def __init__(self):
        # time.sleep(10)
        # self.pic = Pic("page2.jpg")
        pass
    def check(self):
        # if self.checkURL() == False:
        #     return False
        while (True):
            self.pic = Pic("page2.jpg")
            if self.flashCheck() == False:
                self.flashAllow()
                time.sleep(dt)
                continue
            if self.authCheck() == False:
                return False
            time.sleep(0.1)                
            if self.intoCheck() == False:
                time.sleep(dt)
                continue
            else:
                break
        return True
    def checkURL(self):
        urlBox = (175,65,1540,95)
        ret = self.pic.parse(urlBox)
        l = len(p2url)
        ret = ret[-1*l:]
        if ret != p2url :
            print('p2 checkURL ret:',ret)
            return False
        print("URL check ok!")
        return True
    def flashCheck(self):
        box = (857,554,1069,573)
        ret = self.pic.parse(box)
        str = "点击即可启用 Adobe Flash Player"
        if ret == str :
            print('p2 flashCheck ret:',ret)
            return False
        print('p2 flashCheck ret2:',ret)
        print('flash check ok')
        return True
    def flashAllow(self):
        x = 900
        y = 560
        pyautogui.moveTo(x=x, y=y,duration=0.5, tween=pyautogui.linear)
        pyautogui.click()
        
        x = 400
        y = 220
        pyautogui.moveTo(x=x, y=y,duration=0.5, tween=pyautogui.linear)
        pyautogui.click()
        return
    def authCheck(self):
        box = (938,499,1273,542)
        ret = self.pic.parse(box)
        print(ret)
        str = "验证失败,请重新登入!"
        if ret == str :
            print('p2 authCheck ret:',ret)
            return False
        print('auth check ok')
        return True
    def intoCheck(self):
        box = (696,510,771,535)
        str = "进入游戏"
        ret = self.pic.parse(box)
        if ret != str :
            print('intoCheck ret:',ret)
            return False
        return True
    def intoGame(self):
        x = 700
        y = 520
        pyautogui.moveTo(x=x, y=y,duration=1, tween=pyautogui.linear)
        pyautogui.click()

if __name__=='__main__':
    p2 = Page2()
    p2.authCheck()
