import tkinter as tk

window = tk.Tk()
window.geometry("720x480")
window.title("Кликер")
window["bg"]="black"

result = 0
price_click = 25
price_auto = 10000
one_click = 1
one_auto = 0

def clicker():
    global result
    result += one_click
    ochki.configure(text=f"{result}")

def one():
    global result
    global one_click
    global price_click
    if result >= price_click:
        result -= price_click
        one_click * 2
        price_click * 2.1
        ochki.configure(text=f"{result}")
        int(price_click.configure(text==f"{price_click}"))
        one_click.configure(text=f"{one_click}")

ochki = tk.Label(window,text=f"{result}",font=("times new roman",20),fg="white",bg="black")
ochki.pack()

button1 = tk.Button(window,text=f"Цена на улучшение клика: {price_click}",font=("times new roman",18),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",command=one)
button1.pack()

button2 = tk.Button(window,text=f"Цена на улучшение авто клика: {price_auto}",font=("times new roman",18),fg="white",bg="black",
activeforeground="yellow",activebackground="grey")
button2.pack()

click_button = tk.Button(window,text="НАЖАТЬ",font=("times new roman",30),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",command=clicker)
click_button.pack()

click_text = tk.Label(window,text=f"Очки за один клик: {one_click}",font=("times new roman",20),fg="white",bg="black")
click_text.pack()

auto_text = tk.Label(window,text=f"Очки за каждую секунду: {one_auto}",font=("times new roman",20),fg="white",bg="black")
auto_text.pack()











#window.mainloop()