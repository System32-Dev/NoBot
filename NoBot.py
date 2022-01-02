import pyautogui
import random
import string
import time
import webbrowser

screenWidth, screenHeight = pyautogui.size()

class NoBot():
    def sleep(amm):
        for x in range(0,int(amm)):
            time.sleep(0)

    def typeText(text):
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

    def move(x,y,speed,click):
        if click is True:
            pyautogui.moveTo(x,y,speed)
            NoBot.sleep(0.3)
            pyautogui.leftClick()
        else:
            pyautogui.moveTo(x,y,speed)
    def web():
        return webbrowser.get()
print("Thank, you for using NoBot")