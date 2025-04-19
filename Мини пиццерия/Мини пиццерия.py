import tkinter as tk
import time
import random
from math import cos, sin, radians
from PIL import ImageTk, Image

WIDTH = 800
HEIGHT = 600
window = tk.Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("Мини пиццерия")
window.iconbitmap('pizza.ico')
window["bg"] = "black"
window.wm_resizable(False, False)

pole = tk.Canvas(window, width=WIDTH, height=HEIGHT - 135, bg="grey")
pole.grid(row=0, column=0, columnspan=4)

X = 300
Y = 250


class Pizza:
    sizes = {"Маленькая": 80, "Средняя": 100, "Большая": 120}

    def __init__(self):
        self.x = X
        self.y = Y
        self.speed = 0
        self.size = random.choice(tuple(self.sizes))
        self.radius = self.sizes[self.size]
        self.testo = [pole.create_oval(self.x - self.radius, self.y - self.radius,
                                       self.x + self.radius, self.y + self.radius, fill="wheat1",
                                       outline="burlywood1", width=4)]

    def move(self):
        for i in self.testo:
            pole.move(i, self.speed, 0)


pizza = Pizza()


class Order:
    ingr = {"Маленькая": ["Сыр", "Пепперони", "Грибы", "Колбаски", "Курица"],
            "Средняя": ["Сыр x2", "Пепперони x2", "Грибы x2", "Колбаски x2", "Курица x2"],
            "Большая": ["Сыр x2", "Пепперони x2", "Грибы x2", "Колбаски x2", "Курица x2"]}

    def __init__(self, size):
        self.minus = random.randint(0, 4)
        print(self.minus)
        self.order = ["Соус"]
        for i in range(self.minus):
            self.order.append(random.choice(self.ingr[size]))
        pole.itemconfig(lable, text="\n".join(self.order))


pole.create_rectangle(2, 2, 170, 150, fill="white")
lable = pole.create_text(85, 75, text="", font=("times new roman", 20), fill="black")

orderi = Order(pizza.size)

def sause():
    if pizza.speed == 0:
        radius = pizza.radius * 0.9
        pizza.testo.append(pole.create_oval(X - radius, Y - radius,
                                            X + radius, Y + radius, fill="tomato",
                                            outline="tomato"))


def pepperoni():
    if len(pizza.testo) > 1 and pizza.speed == 0:
        for i in range(18):
            radius = pizza.radius * 0.9
            angle = random.randint(0, 90)
            sx = int(cos(radians(angle)) * radius)
            sy = int(sin(radians(angle)) * radius)
            x = X + random.randint(-sx, sx)
            y = Y + random.randint(-sy, sy)
            radius = 12
            pizza.testo.append(pole.create_oval(x - radius, y - radius,
                                                x + radius, y + radius, fill="crimson",
                                                outline="red"))

def cheese():
    if len(pizza.testo) > 1 and pizza.speed == 0:
        for i in range(100):
            radius = pizza.radius * 0.9
            angle = random.randint(0, 90)
            sx = int(cos(radians(angle)) * radius)
            sy = int(sin(radians(angle)) * radius)
            x = X + random.randint(-sx, sx)
            y = Y + random.randint(-sy, sy)
            r = 1.5
            pizza.testo.append(pole.create_rectangle(x - r, y - r * 3,
                                                     x + r, y + r * 3, fill="goldenrod1", outline="goldenrod3"))


def sausage():
    if len(pizza.testo) > 1 and pizza.speed == 0:
        for i in range(32):
            radius = pizza.radius * 0.9
            angle = random.randint(0, 90)
            sx = int(cos(radians(angle)) * radius)
            sy = int(sin(radians(angle)) * radius)
            x = X + random.randint(-sx, sx)
            y = Y + random.randint(-sy, sy)
            radius = 6
            pizza.testo.append(pole.create_oval(x - radius, y - radius,
                                                x + radius, y + radius, fill="firebrick3",
                                                outline="firebrick4"))


def chiko():
    if len(pizza.testo) > 1 and pizza.speed == 0:
        for i in range(18):
            radius = pizza.radius * 0.9
            angle = random.randint(0, 90)
            sx = int(cos(radians(angle)) * radius)
            sy = int(sin(radians(angle)) * radius)
            x = X + random.randint(-sx, sx)
            y = Y + random.randint(-sy, sy)
            radius = 11
            pizza.testo.append(pole.create_oval(x, y - radius,
                                                x + radius, y + radius, fill="lightgoldenrod2",
                                                outline="lightgoldenrod4"))


def shrooms():
    if len(pizza.testo) > 1 and pizza.speed == 0:
        for i in range(28):
            radius = pizza.radius * 0.9
            angle = random.randint(0, 90)
            sx = int(cos(radians(angle)) * radius)
            sy = int(sin(radians(angle)) * radius)
            x = X + random.randint(-sx, sx)
            y = Y + random.randint(-sy, sy)
            radius = 4
            pizza.testo.append(pole.create_rectangle(x - radius, y - radius * 1.5,
                                                     x + radius, y + radius * 1.5, fill="sienna4",
                                                     outline="gray24"))


def go():
    if len(pizza.testo) > 1:
        pizza.speed = 5
        pole.lift(furn)


button1 = tk.Button(window, text="Соус", font=("times new roman", 25), fg="white", bg="black",
                    activeforeground="yellow", activebackground="grey", width=12, command=sause)
button1.grid(row=1, column=0)

button2 = tk.Button(window, text="Сыр", font=("times new roman", 25), fg="white", bg="black",
                    activeforeground="yellow", activebackground="grey", width=12, command=cheese)
button2.grid(row=1, column=1)

button3 = tk.Button(window, text="Пепперони", font=("times new roman", 25), fg="white", bg="black",
                    activeforeground="yellow", activebackground="grey", width=12, command=pepperoni)
button3.grid(row=1, column=2)

button4 = tk.Button(window, text="Курица", font=("times new roman", 25), fg="white", bg="black",
                    activeforeground="yellow", activebackground="grey", width=12, command=chiko)
button4.grid(row=2, column=0)

button5 = tk.Button(window, text="Грибы", font=("times new roman", 25), fg="white", bg="black",
                    activeforeground="yellow", activebackground="grey", width=12, command=shrooms)
button5.grid(row=2, column=1)

button6 = tk.Button(window, text="Колбаски", font=("times new roman", 25), fg="white", bg="black",
                    activeforeground="yellow", activebackground="grey", width=12, command=sausage)
button6.grid(row=2, column=2)

button7 = tk.Button(window, text="В\nПЕЧЬ!", font=("times new roman", 21), fg="white", bg="black",
                    activeforeground="yellow", activebackground="grey", height=3, width=7, command=go)
button7.grid(row=1, column=3, rowspan=2)

furnace = Image.open("furn.png")
furnace = furnace.resize((500, 500))
furnace = ImageTk.PhotoImage(furnace)

furn = pole.create_image(700, 225, anchor="center", image=furnace)
pole.lift(furn)

while True:
    window.update()
    window.update_idletasks()
    time.sleep(1 / 20)
    pizza.move()
    x = pole.coords(pizza.testo[0])[0]
    if x >= 600:
        for i in pizza.testo:
            pole.delete(i)
        pizza.__init__()
        orderi.__init__(pizza.size)
