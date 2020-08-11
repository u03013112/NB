#coding=utf-8
from PIL import ImageGrab,Image
import pyautogui
import base64
from io import BytesIO
from ocr import OCR

class Pic:
    def __init__(self,filename):
        im = pyautogui.screenshot().convert('RGB')
        im.save(filename)
        self.filename = filename
        self.im = im
        self.ocr = OCR('dmrLU83szTXVUd5SEQKNQbtu','K0N6gTZwaaPeI4nN8Ij2ZEaI5tt1aEuE')

    def parse(self,box):
        region = self.im.crop(box)
        b64 = self.pil2base64(region)
        return self.ocr.parseBase64(b64)

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
    print(region)
    region = region.convert('RGB')
    print(region)
    pic = Pic()
    # print(pic.pil2base64(region))
