from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,QTabWidget
from PyQt5.QtGui import QPalette, QColor

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.setupUI4()

    def setupUI1(self):
        layout = QVBoxLayout()
        self.central.setLayout(layout)
        for color in ("black", "purple", "green", ""):
            layout.addWidget(Color(color))

    def setupUI2(self):
        layout = QVBoxLayout()
        self.central.setLayout(layout)
        for color in ("black", "purple", "green"):
            layout.addWidget(Color(color))
        layout2 = QHBoxLayout()
        layout.addLayout(layout2)
        for color in ("black", "purple", "green"):
            layout2.addWidget(Color(color))
        for color in ("black", "purple", "green"):
            layout.addWidget(Color(color))

    def setupUI3(self):
        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.central.setLayout(layout)

        layout.addWidget(Color("purple"), 0, 1)
        layout.addWidget(Color("green"), 1, 0)
        layout.addWidget(Color("black"), 0, 3)

    def setupUI4(self):
        widget = QTabWidget(self)
        self.setCentralWidget(widget)
        for color in ("black", "purple", "green"):
            widget.addTab(Color(color), color)

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