from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)

        self.butt = QPushButton("TAP ME", self)
        #self.butt.setText("TAP")
        self.butt.move(250, 100)

        self.labl = QLabel("Введите логин", self)
        self.labl.move(260, 160)

        self.log = QLineEdit(self)
        self.log.move(250, 190)

        self.lablee = QLabel("Введите пароль", self)
        self.lablee.move(258, 220)

        self.loggg = QLineEdit(self)
        self.loggg.move(250, 250)

        self.but = QPushButton("ВОЙТИ", self)
        self.but.move(250, 290)
        self.but.clicked.connect(self.enter)

        self.result = QLabel("", self)
        self.result.move(255, 50)

        self.name = "pyqt"
        self.passw = "piton"

    def enter(self):
        print("Вход")
        login = self.log.text()
        password = self.loggg.text()
        print(login, password)
        if login == self.name and password == self.passw:
            self.close()
        else:
            self.result.setText("Ваши данные неверны!")
            self.result.adjustSize()

def run():
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()