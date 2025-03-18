import pyautogui
import time,random

while True:
    x = random.randint(600,700)
    y = random.randint(500,600)
    pyautogui.moveTo(x,y,5)
    time.sleep(5)