def decor(func):
    print("Начало")
    def wrapper():
        print("Начало декоратора")
        func()
        print("Конец декоратора")
    return wrapper

@decor
def main():
    print("Всё работает!!!")

def sandwich(func):
    def wrapper(*args):
        print("<==========>")
        func(*args)
        print("<==========>")
    return wrapper

@sandwich
def nap(spis):
    for i in spis:
        print(" "*(6-len(i)//2)+i)
spis = ["Сыр", "Колбаса", "Помидор", "Соус"]
#main()
nap(spis)