from PyQt5.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)


def run():
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()

#pyuic5 -x Pyqt/form.ui -o Pyqt/formui.py