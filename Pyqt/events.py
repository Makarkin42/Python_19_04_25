from PyQt5.QtWidgets import QApplication, QMainWindow
from eventsui import Ui_MainWindow

class Window(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.butt1.clicked.connect(self.click)
        self.butt2.clicked.connect(self.click)
        self.butt2.pressed.connect(self.press)
        self.textEdit.textChanged.connect(self.checktext)

    def click(self):
        button = self.sender()
        print("cliCK", button.objectName())

    def press(self):
        button = self.sender()
        print("Pressed", button.objectName())

    def checktext(self):
        text:str = self.sender().toPlainText()
        text_count = len(text.split())
        if text_count <= 3:
            self.sender().setStyleSheet("color: red")
        else:
            self.sender().setStyleSheet("color: rgb(0,0,0)")

def run():
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()