import tkinter as tk
from tkinter.colorchooser import askcolor

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Вход")
        self["bg"]="grey25"
        self.color = "grey35"
        self.name = ""
        namee = tk.Label(self, text="Введите имя", font=("arial", 15), fg="white", bg="black")
        namee.pack()

        self.entry = tk.Entry(self, font=("arial", 15), justify="center", bg="grey60")
        self.entry.pack()

        col = tk.Label(self, text="Выберите цвет", font=("arial", 15), fg="white", bg="black")
        col.pack()

        self.indic = tk.Button(self, text="Цвет", font=("arial", 15), fg="white", bg=self.color,
                          activeforeground="grey30", activebackground="grey", command=self.colchange)
        self.indic.pack()

        self.button = tk.Button(self, text="Войти ", font=("arial", 15), fg="white", bg="grey35",
                           activeforeground="grey30", activebackground="grey", command=self.nick)
        self.button.pack()

        tk.mainloop()

    def colchange(self):
        newcolor = askcolor(title="Выбор цвета")[1]
        if newcolor:
            self.color = newcolor
            self.indic.configure(bg=self.color)

    def nick(self):
        self.name = self.entry.get()
        if self.name:
            self.destroy()
