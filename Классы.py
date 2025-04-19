class Sharik:
    def __init__(self,color = "pink",size = "medium"):
        self.color = color
        self.size = size
    def boom(self):
        print("BOOM!")
        self.size = "Взорван"

bal1 = Sharik("yellow","small")
bal2 = Sharik(size = "big")
print(bal1.color,bal1.size)
print(bal2.color,bal2.size)
bal1.boom()
print(bal1.color,bal1.size)

trip = {13: ("Гостиный двор", "ГДК", "Магазин Гипер", "Галерея"),
        25: ("Парк Победы", "Улица Ленина", "Главная площадь", "Речное депо")}
class Bus:
    def __init__(self,nomer):
        self.nomer = nomer
        self.marshrut =trip[nomer]

    def stop(self,i):
        print(f"Автобус номер {self.nomer} прибыл на остановку {self.marshrut[i]}")

bus13 = Bus(nomer = 25)
for i in range(4):
    bus13.stop(i=i)
'''class Animal:
    color = "brown" 
    size = "big"

zoo = []

for i in range(150):
    zoo.append(Animal())
print(zoo)'''