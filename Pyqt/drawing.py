from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt, QRect
import random

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        self.central = QWidget()
        self.setCentralWidget(self.central)

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        #self.write(qp)
        #self.dots(qp)
        #self.lines(qp)
        #self.rectangle(qp)
        self.circle(qp)
        qp.end()

    def write(self, qp: QPainter):
        qp.setPen(QColor("black"))
        qp.setFont(QFont("Arial", 18))
        text = "Start writing..."
        qp.drawText(self.rect(), Qt.AlignCenter, text)

    def dots(self, qp: QPainter):
        qp.setPen(QColor("blue"))
        for i in range(10000):
            x = random.randint(1, self.width())
            y = random.randint(1, self.height())
            qp.drawPoint(x, y)

    def lines(self, qp: QPainter):
        fonts = [Qt.DashDotDotLine, Qt.DashLine, Qt.SolidLine, Qt.DotLine, Qt.DashDotLine]
        x, y, xx, yy = 100, 100, 450, 100
        for i in fonts:
            pen = QPen(Qt.magenta, random.randint(1, 10),i)
            qp.setPen(pen)
            qp.drawLine(x, y, xx, yy)
            y += 50; yy += 50

    def rectangle(self, qp: QPainter):
        # brush = QBrush(QColor("cyan"), Qt.SolidPattern)
        # qp.setBrush(brush)
        # pen = QPen(QColor("purple"), 4, Qt.SolidLine)
        # qp.setPen(pen)
        # qp.drawRect(50, 20, 250, 80)

        vrast = self.height() // 2
        hrast = self.width() // 5
        for i, patt in enumerate((Qt.Dense1Pattern, Qt.Dense2Pattern, Qt.Dense3Pattern, Qt.Dense4Pattern,
                                  Qt.Dense5Pattern, Qt.Dense6Pattern, Qt.VerPattern, Qt.HorPattern,
                                  Qt.DiagCrossPattern, Qt.BDiagPattern)):
            num_row = i // 5
            num_col = i % 5
            brush = QBrush(QColor("black"), patt)
            qp.setBrush(brush)
            qp.drawRect(num_col * hrast, num_row * vrast, 100, 150)

    def circle(self, qp: QPainter):
        brush = QBrush(QColor("black"), Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawEllipse(200, 150, 200, 100)

def run():
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()