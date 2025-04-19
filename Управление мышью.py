import pyautogui as pa
from math import cos,sin,radians
import time
time.sleep(5)
position = pa.position()
print(position)

#pa.moveTo(500,0,duration=2)
#pa.moveRel(600,500,duration=2)
#pa.moveTo(962,16,duration=2)
#pa.moveTo(143,270,duration=2)
#pa.click(clicks=2)

pa.dragRel(300,0,duration=1)
pa.dragRel(0,300,duration=1)
pa.dragRel(-300,0,duration=1)
pa.dragRel(0,-300,duration=1)
pa.dragRel(45,-45,duration=1)
pa.dragRel(300,0,duration=1)
pa.dragRel(0,300,duration=1)
pa.dragRel(-300,0,duration=1)
pa.dragRel(0,-300,duration=1)
pa.dragRel(300,0,duration=1)
pa.dragRel(-45,45,duration=1)
pa.dragRel(0,300,duration=1)
pa.dragRel(45,-45,duration=1)
pa.dragRel(-300,0,duration=1)
pa.dragRel(-45,45,duration=1)

X,Y = pa.position()
#for i in range(46):
    #pa.dragTo(x=X+cos(radians(i*8))*150,y=Y+sin(radians(i*8))*150)