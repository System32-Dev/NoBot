import pyautogui
import random
import string
import time
import webbrowser                                                                      
from PIL import Image

screenWidth, screenHeight = pyautogui.size()

class NoBot():
    def sleep(amm):
        for x in range(0,int(amm)):
            time.sleep(0)

    def type(text):
        chars = string.printable
        for x in range(0,len(text)):
            if random.randint(0,5) == 5:
                pyautogui.press(chars[random.randint(0,len(chars))])
                pyautogui.press('backspace')
                NoBot.sleep(0.3)
                pyautogui.press(text[x])
            else:
                pyautogui.press(text[x])
                NoBot.sleep(0.34)
    
    def press(key):
        pyautogui.press(key)

    def click(side):
        if side.lower() == 'Left':
            pyautogui.leftClick()
        if side.lower() == 'Right':
            pyautogui.rightClick()
    
    def move(x,y,speed,click):
        pyautogui.moveTo(int(x),int(y),int(speed))
        if click is True:
            NoBot.sleep(0.3)
            pyautogui.leftClick()
    
    def centerMouse():
        mouseMidX, mouseMidY = screenWidth/2,screenHeight/2
        pyautogui.moveTo(mouseMidX,mouseMidY,0)

class WebService():
    def web():
        return webbrowser.get()
    """def solveCaptcha(path):
        im = Image.open(path)
        im = im.convert("P")"""
