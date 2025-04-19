import tkinter as tk
import time
from playsound import playsound
VIDTH = 850
HEIGHT = 600
window = tk.Tk()
window.geometry(f"{VIDTH}x{HEIGHT}")
window.title("Paint v2")
window["bg"]="black"

pole = tk.Canvas(window,width=VIDTH,height=HEIGHT,bg="grey")
pole.grid(row=0,column=0)

class Ball:
    def __init__(self,x1 = 50, y1 = 20, x2 = 75, y2 = 45, vx = 9,vy = 6):
        self.figure = pole.create_oval(x1,y1,x2,y2,fill="red",outline="black")
        self.xspeed = vx
        self.yspeed = vy
    def walk(self):
        pole.move(self.figure,self.xspeed,self.yspeed)
        x1, y1, x2, y2 = pole.coords(self.figure)
        if x2 >= VIDTH or x1 <= 0:
            self.xspeed =- self.xspeed
        if y2 >= HEIGHT:
            record()
            del ball[ball.index(self)]
            if not ball:
                pole.create_text(425,300, text="Ты проиграл", font=("arial",100))
                rocket.score = 0
                pole.itemconfig(scorre, text=f"Счет {rocket.score}\nРекорд {record()}")
        elif y1 <= 0:
            self.yspeed = - self.yspeed
        xr1, yr1, xr2, yr2 = pole.coords(rocket.figure)
        if y2 >= yr1 and y1 <= yr2 and x1 <= xr2 and x2 >= xr1 and self.yspeed > 0:
            self.yspeed =- self.yspeed - 0.75
            boost = 0.6 if self.xspeed > 0 else - 0.6
            self.xspeed += boost
            rocket.score += 1
            #playsound("pong.wav",block=False)
            pole.itemconfig(scorre,text=f"Счет {rocket.score}\nРекорд {record()}")
            if rocket.score %10 == 0:
                ball.append(Ball(x1,y1,x2,y2,-self.xspeed,-6))


def record():
    with open("рекорды.txt","r+") as file:
        number = file.read()
        if rocket.score > int(number):
            file.seek(0)
            file.write(str(rocket.score))
            return rocket.score
        else:
            return int(number)

def restart(event):
    if not ball:
        pole.delete("all")
        rocket.__init__()
        global scorre
        scorre = pole.create_text(830, 15, text=f"Счет {rocket.score}\nРекорд {record()}", anchor="ne", font=("arial", 30),
                                  fill="black")
        ball.append(Ball())

class Rocket:
    def __init__(self):
        self.figure = pole.create_rectangle(350,525,500,540,fill="green",outline="green")
        self.speed = 0
        self.score = 0
    def motion(self,event):
        pole.moveto(self.figure, event.x - 75, 525)

rocket = Rocket()
ball = [Ball()]

scorre = pole.create_text(830,15,text = f"Счет {rocket.score}\nРекорд {record()}", anchor="ne", font = ("arial",30), fill = "black")
pole.bind_all("<Motion>",rocket.motion)
pole.bind_all("<space>",restart)
while True:
    window.update()
    window.update_idletasks()
    time.sleep(1/30)
    for i in ball:
        i.walk()

