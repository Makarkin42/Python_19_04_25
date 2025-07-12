from pizzaui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
count = 0

class Window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionplus.triggered.connect(self.plus)
        self.actionminus.triggered.connect(self.minus)
        self.num = 0

    def plus(self):
        print(1)
        self.num += 1
        print(2)
        self.label.setText(str(self.num))
        print(3)

    def minus(self):
        self.num -= 1
        self.label.setText(str(self.num))


def run():
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()