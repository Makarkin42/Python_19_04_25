from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from Asciiui import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.horizontalScrollBar.valueChanged.connect(self.scroller)
        self.horizontalScrollBar_2.valueChanged.connect(self.scroller)

    def scroller(self):
        self.label_2.setText(f"Размер шрифта\n(в пикселях):\n{self.horizontalScrollBar.value()}")
        self.label_3.setText(f"Глубина\nцвета:\n{self.horizontalScrollBar_2.value()}")
        self.update()


def run():
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()