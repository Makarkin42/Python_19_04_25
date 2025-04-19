import turtle

window = turtle.Screen()
window.setup(width=1000,height=800)
window.title("ракушка")
window.bgcolor("black")
t1 = turtle.Turtle()
t1.color("white")
#t1.left(90)
#t1.forward(150)
#t1.begin_fill()
#t1.circle(120,steps=80)
#t1.end_fill()
'''colores = ["orange","pink","purple","grey"]
t1.speed(25)
for i in range(80):
    t1.color(colores[i%4])
    t1.circle(i*1.5)
    t1.right(240)'''

colors = ["white","grey"]
t1.speed(15)
t1.hideturtle()
for i in range(120):
    t1.color(colors[i%2])
    t1.circle(i*1.3)
    t1.right(5)




turtle.mainloop()