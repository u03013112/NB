# encoding:utf-8
import time
from page1 import Page1
from page2 import Page2

while (True):
    
    p1 = Page1()
    if p1.check() == True:
        p1.intoKU()
        if p1.intoCheck() == True:
            p1.intoGame()
            p2 = Page2()
            if p2.check() == True:
                p2.intoGame()
            else:
                pyautogui.hotkey('command','w')

    time.sleep(10)