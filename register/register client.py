from PyQt5.QtWidgets import QApplication, QMainWindow
from registerui import Ui_MainWindow
import socket

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.enter)
        self.lineEdit_3.setText("10.10.88.238:12516")
        self.ip = ""
        self.port = ""

    def checkvect(self, mess):
        first = None
        for index, lett in enumerate(mess):
            if lett == "<":
                first = index
            if lett == ">" and first is not None:
                second = index
                result = mess[first + 1: second]
                return result

    def check_log(self):
        log = self.lineEdit.text()
        if len(log.strip()) >= 3:
            return True
        return False

    def check_pass(self):
        password = self.lineEdit_2.text()
        for i in password:
            if i.lower() not in "1234567890_qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапрлджэячсмитьбюо":
                return False
        if len(password.strip()) >= 6:
            return True
        return False

    def ip_port(self):
        try:
            self.ip, self.port = self.lineEdit_3.text().split(":")
            if 1 <= int(self.port) <= 65535:
                print(self.ip, self.port)
                for i in self.ip.split("."):
                    if not (1 <= int(i) <= 255):
                        return False
                if len(self.ip.split(".")) != 4:
                    return False
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def enter(self):
        if self.check_log() and self.check_pass() and self.ip_port():
            print("true")
            login = self.lineEdit.text()
            password = self.lineEdit_2.text()
            master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            master.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            master.connect((self.ip, int(self.port)))
            master.send(f"{login},{password}".encode())
            mess = master.recv(1024).decode()
            mess = self.checkvect(mess)
            if mess == "1":
                self.close()
            elif mess == "-1":
                self.label_2.setText("Неверно введен пароль!")
                self.label.setText("Введите логин...")
            elif mess == "0":
                self.label.setText("Такой логин не зарегестрирован!")
                self.label_2.setText("Введите пароль...")
        else:
            print("False")
            #testlogin88 ne1234


def run():
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()