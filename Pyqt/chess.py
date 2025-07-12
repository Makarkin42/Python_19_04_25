from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QPalette, QColor

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.setup1()

    def setup1(self):
        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.central.setLayout(layout)
        for i in range(8):
            for a in range(8):
                color = "black" if (i + a)%2 == 0 else "white"
                layout.addWidget(Color(color), i, a)


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
def run():
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()
