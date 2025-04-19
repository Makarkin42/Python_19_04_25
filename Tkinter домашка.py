import tkinter as tk

window = tk.Tk()
window.geometry("720x480")
window.title("Вопрос на миллион")
window["bg"]="black"

def wrong():
    question.configure(text="Иди учи историю!")
    button1.destroy()
    button3.destroy()
    button4.destroy()
    #button2.destroy()

def right():
    question.configure(text="А ты знаешь историю!")
    window.after(3000,window.destroy)
question = tk.Label(window,text="Год крещения Руси?",font=("times new roman",20),fg="white",bg="black")
question.pack()

button1 = tk.Button(window,text="В 856 году",font=("times new roman",18),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",command=wrong)
button1.pack()

button2 = tk.Button(window,text="В 980 году",font=("times new roman",18),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",command=right)
button2.pack()

button3 = tk.Button(window,text="В 1251 году",font=("times new roman",18),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",command=wrong)
button3.pack()

button4 = tk.Button(window,text="В 1064 году",font=("times new roman",18),fg="white",bg="black",
activeforeground="yellow",activebackground="grey",command=wrong)
button4.pack()













tk.mainloop()