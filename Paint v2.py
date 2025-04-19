import tkinter as tk
from tkinter.colorchooser import askcolor
from math import cos,sin,radians

window = tk.Tk()
window.geometry("850x600")
window.title("Paint v2")
window["bg"]="black"

pole = tk.Canvas(window,width=790,height=600,bg="grey")
pole.grid(row=0,column=0,rowspan=9)

size = 15
shape = "\\\\\\"
color = "red"

shape_dict = {
    "circle":"🔴", "square":"🟥", "\\\\\\":"\\\\\\", "///":"///"}

def draw(event):
    #print(event.__dict__)
    if event.widget.__class__ is not tk.Canvas:
        return
    if shape == "circle":
        pole.create_oval(event.x - size,event.y - size,event.x + size,event.y + size,
                         fill=color,outline=color)
    elif shape == "square":
        pole.create_rectangle(event.x - size, event.y - size, event.x + size, event.y + size,
                         fill=color, outline=color)
    elif shape == "\\\\\\":
        pole.create_line(event.x - size, event.y - size, event.x + size, event.y + size,
                         fill=color)
    elif shape == "///":
        pole.create_line(event.x + size, event.y - size, event.x - size, event.y + size,
                         fill=color)

def eraser(event):
    pole.create_oval(event.x - size,event.y - size,event.x + size,event.y + size,
                         fill=("grey"),outline=("grey"))

def butsize(new):
    global size, shape
    if new == "+" and size < 97.5:
        size += 2.5
        indic.configure(text=size)
    elif new == "-" and size > 0:
        size -= 2.5
        indic.configure(text=size)
    elif new not in ("+","-"):
        shape = new
        indic2.configure(text=shape_dict[shape])

def colorchoose():
    global color
    newcolor = askcolor(title="Выбор цвета")[1]
    if newcolor:
        color = newcolor
        indic.configure(bg=color)
        
button1 = tk.Button(window,text="➕",font=("times new roman",18),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",width=3,command=lambda:butsize("+"))
button1.grid(row=0,column=1)

button1 = tk.Button(window,text="➖",font=("times new roman",18),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",width=3,command=lambda:butsize("-"))
button1.grid(row=1,column=1)

button1 = tk.Button(window,text="🔴",font=("times new roman",18),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",width=3,command=lambda:butsize("circle"))
button1.grid(row=2,column=1)

button1 = tk.Button(window,text="🟥",font=("times new roman",18),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",width=3,command=lambda:butsize("square"))
button1.grid(row=3,column=1)

button1 = tk.Button(window,text="\\\\\\",font=("times new roman",18),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",width=3,command=lambda:butsize("\\\\\\"))
button1.grid(row=4,column=1)

button1 = tk.Button(window,text="///",font=("times new roman",18),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",width=3,command=lambda:butsize("///"))
button1.grid(row=5,column=1)

button1 = tk.Button(window,text="🎨",font=("times new roman",18),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",width=3,command=colorchoose)
button1.grid(row=6,column=1)

indic = tk.Label(window,text=size,font=("times new roman",18),fg="white",bg=color)
indic.grid(row=7,column=1)

indic2 = tk.Label(window,text=shape_dict[shape],font=("times new roman",18),fg="white",bg="black")
indic2.grid(row=8,column=1)

pole.bind_all("<1>",draw)
pole.bind_all("<B1-Motion>",draw)

pole.bind_all("<3>",eraser)
pole.bind_all("<B3-Motion>",eraser)

tk.mainloop()