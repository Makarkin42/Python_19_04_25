import tkinter as tk

window = tk.Tk()
window.geometry("600x400")
window.title("окко")
window["bg"]="black"

clicks = 0

def action():
    #word.destroy()
    word.configure(text="Давно не виделись!")
    button.configure(command=clicker)
def action2():
    word.configure(text="Я ухожу")
    window.after(3000,window.destroy)

def clicker():
    global clicks
    clicks += 1
    word.configure(text=clicks)

word = tk.Label(window,text="Приветствую!",font=("arial",15),fg="white",bg="black")
word.pack()
button = tk.Button(window,text="Поприветствовать",font=("arial",15),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",command=action)
button.pack()
button2 = tk.Button(window,text="Отстань",font=("arial",15),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",command=action2)
button2.pack()

























tk.mainloop()