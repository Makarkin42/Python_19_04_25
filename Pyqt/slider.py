from sliderui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
#self.lcdNumber.display

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.horizontalSlider.valueChanged.connect(self.slide)
        self.dlina = 50

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        self.rect(qp)
        qp.end()

    def rect(self, qp: QPainter):
        brush = QBrush(QColor("cyan"), Qt.SolidPattern)
        qp.setBrush(brush)
        pen = QPen(QColor("purple"), 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawRect(2, 2, self.dlina, 100)
        self.update()

    def slide(self):
        self.dlina = int(self.horizontalSlider.value() / 100 * self.width())

def run():
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()