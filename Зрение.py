import pyautogui as pa
import time

def scr():
    time.sleep(3)
    pos1 = pa.position()
    print(pos1)
    time.sleep(3)
    pos2 = pa.position()
    print(pos2)
    size = pos2.x - pos1.x, pos2.y - pos1.y
    pa.screenshot("scr.png",region=pos1 + size)

def search():
    button = pa.locateOnScreen("scr.png")
    x, y = pa.center(button)
    pa.moveTo(x, y,duration=1)
    pa.click(clicks=100,interval=0.09)

#scr()
time.sleep(3)
search()