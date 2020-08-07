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
        im1 = pyautogui.screenshot()
        im1.save(filename)


if __name__=='__main__':
    p = Pic()
    p.capture("pic.png")
