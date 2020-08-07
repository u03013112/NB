#coding=utf-8
from PIL import ImageGrab,Image
import pyautogui
import base64
from io import BytesIO

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
    def pil2base64(self,image):
        imgBytesIO = BytesIO()
        image.save(imgBytesIO, format='JPEG')
        byte_data = imgBytesIO.getvalue()
        base64_str = base64.b64encode(byte_data)
        return base64_str

if __name__=='__main__':
    # p = Pic()
    # p.capture("pic.png")
    im = pyautogui.screenshot()
    region = im.crop((50,0,1000,22))
    region = region.convert('RGB')
    print(region)
    pic = Pic()
    print(pic.pil2base64(region))
