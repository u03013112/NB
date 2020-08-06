#coding=utf-8
from PIL import ImageGrab
import pyautogui
import cv2

class Pic:
    def capture(self,filename):
        # self.captureByPIL(filename)
        self.captureByAutogui(filename)
    def captureByPIL(self,filename):
        im = ImageGrab.grab()
        im.save(filename)
    def captureByAutogui(self,filename):
        img = pyautogui.screenshot(region=[0,0,1000,1000]) # x,y,w,h
        img.save(filename)
        # img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
        
if __name__=='__main__':
    p = Pic()
    p.capture("pic.png")
