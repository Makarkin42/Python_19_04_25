import pyautogui as pa

pa.alert(text="Добро пожаловать!",title="От Сайта",button="Войти на сайт")
while True:
    answer = pa.confirm(text="Вы зарегистрированы на сайте?",title="От сайта",buttons=["Войти в аккаунт","Регистрация"])
    print(answer)
    if answer == "Регистрация":
        login = pa.prompt(text="Введите логин",title="От сайта")
        password = pa.password(text="Введите пароль",title="От сайта",mask="#")
        print(login,password)
        with open("Пароли.txt", "r+") as file:
            dann = eval(file.read())
            dann[login] = password
            file.seek(0)
            file.write(str(dann))
    elif answer == "Войти в аккаунт":
        login = pa.prompt(text="Введите логин", title="От сайта")
        password = pa.password(text="Введите пароль", title="От сайта", mask="#")
        with open("Пароли.txt","r+") as file:
            dann = eval(file.read())
            if login in dann and password == dann[login]:
                pa.alert("Успешный вход!")
                print(login, password)
                break
    else:
        break