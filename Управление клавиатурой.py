import pyautogui as pa
import time
time.sleep(1.5)

pa.write("print('Hello world')",interval=0.1)
pa.press("enter")
with pa.hold("shift"):
    pa.write("hello")

time.sleep(1)
pa.hotkey("shift","f10")
