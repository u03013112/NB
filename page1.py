# encoding:utf-8
import pyautogui
from pic import Pic

p1url = "ku.ku5168.com/?open=true"

class Page1:
    def __init__(self):
        self.pic = Pic("page1.jpg")
    def check(self):
        if self.checkURL() == False:
            return False
        if self.checkLogin() == False:
            return False
        return True
    def checkURL(self):
        urlBox = (175,65,1540,95)
        ret = self.pic.parse(urlBox)
        if ret != p1url :
            print('ret:',ret)
            return False
        print("URL check ok!")
        return True
    def checkLogin(self):
        box = (1393,111,1461,137)
        ret = self.pic.parse(box)
        if ret != "登录" :
            # print('ret:',ret)
            print("login check ok!")
            return True
        else :
            # 手动登录
            print("请手动登录后重试")
            return False
        return True
    def intoKU(self):
        x = 720
        y = 175
        pyautogui.moveTo(x=x, y=y,duration=0.5, tween=pyautogui.linear)
        pyautogui.click()
        # 多点击一次是可能由于焦点不对
        pyautogui.click()
    def intoCheck(self):
        # 暂时不判断，需要重新截图
        box = (784,643,953,685)
        str = "进入游戏"
        return True
    def intoGame(self):
        x = 800
        y = 666
        pyautogui.moveTo(x=x, y=y,duration=1, tween=pyautogui.linear)
        pyautogui.click()

if __name__=='__main__':
    p1 = Page1()
    if p1.check() == True:
        p1.intoKU()
        if p1.intoCheck() == True:
            p1.intoGame()
