# -*- coding:utf-8 -*-  
import keyboard  #监听键盘
import pyautogui as pag    #监听鼠标
from PIL import  ImageGrab   #截图、读取图片、保存图片

keyboard.wait('a')
x1, y1 = pag.position()
keyboard.wait('a')
x2, y2 = pag.position()
print(x1,y1,x2,y2)