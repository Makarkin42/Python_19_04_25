from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont, QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QRect
import random, copy

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 600)
        self.setWindowTitle("2048")
        self.logofont = QFont("Times New Roman", 72)
        self.textfont = QFont("Arial", 16)
        self.numfont = QFont("SimSun", 48)
        self.margin = 10
        self.colors = {0: (204, 192, 179), 2: (238, 228, 218), 4: (237, 224, 200), 8: (242, 177, 121),
                       16: (245, 149, 99), 32: (246, 124, 95), 64: (246, 94, 59), 128: (237, 207, 114),
                       256: (237, 207, 114), 512: (237, 207, 114), 1024: (237, 207, 114), 2048: (237, 207, 114)}
        self.score = 0
        self.init_game()

    def init_game(self):
        self.desk_size = 4
        self.desk = [[0 for i in range(self.desk_size)]for a in range(self.desk_size)]

        start_plit = 0
        while start_plit < 2:
            row = random.randint(0, self.desk_size - 1)
            column = random.randint(0, self.desk_size - 1)
            if self.desk[row][column] == 0:
                nums = [2, 4, 8]
                self.desk[row][column] = random.choice(nums)
                start_plit += 1
        print(self.desk)

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        self.draw_logo(qp)
        self.draw_desk(qp)
        self.draw_score(qp)
        qp.end()

    def draw_score(self, qp: QPainter):
        qp.setPen(QColor("black"))
        qp.setFont(QFont("SimSun", 36))
        qp.drawText(self.margin, self.height() - 90, self.width() - self.margin,
                    90, Qt.AlignLeft, f"points: {str(self.score)}")

    def draw_logo(self, qp: QPainter):
        text = ""
        qp.setPen(QColor("Purple"))
        if self.check_lose():
            qp.setFont(QFont("Times New Roman", 28))
            text = "You lose!\nPress space to restart"
        else:
            qp.setFont(self.logofont)
            text = "2048"
        qp.drawText(0, 0, self.width(), 100,  Qt.AlignCenter, text)

    def draw_desk(self, qp: QPainter):
        qp.setBrush(QColor("darkblue"))
        size = self.width() - self.margin * 2
        qp.drawRect(self.margin, 100, size, size)

        size_cell = (self.width() - self.margin * (2 + self.desk_size + 1)) // self.desk_size
        for row in range(self.desk_size):
            for col in range(self.desk_size):
                num = self.desk[row][col]
                color = self.colors[num]
                qp.setBrush(QColor(*color))
                xcell = self.margin * 2 + (size_cell + self.margin) * col
                ycell = 100 + self.margin + (size_cell + self.margin) * row
                qp.drawRect(xcell, ycell, size_cell, size_cell)
                if num != 0:
                    qp.setPen(QColor("black"))
                    if num >= 128 and num < 1024:
                        qp.setFont(QFont("SimSun", 40))
                    elif num >= 1024:
                        qp.setFont(QFont("SimSun", 28))
                    else:
                        qp.setFont(self.numfont)
                    qp.drawText(xcell, ycell, size_cell, size_cell, Qt.AlignCenter, str(num))

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_A:
            self.move(dir = "left")
        elif key == Qt.Key_D:
            self.move(dir = "right")
        elif key == Qt.Key_W:
            self.move(dir = "up")
        elif key == Qt.Key_S:
            self.move(dir = "down")
        if self.check_lose():
            if key == Qt.Key_Space:
                self.init_game()
                self.score = 0
                self.update()

    def move(self, dir):
        moved = False
        if dir == "left":
            moved = self.xmove(isleft=True)
        elif dir == "right":
            moved = self.xmove(isleft=False)
        elif dir == "up":
            moved = self.ymove(isup=True)
        elif dir == "down":
            moved = self.ymove(isup=False)
        if not moved:
            return
        self.new_plit()
        if self.check_lose():
            pass
        self.update()

    def new_plit(self):
        free_plit = []
        for row in range(self.desk_size):
            for col in range(self.desk_size):
                if self.desk[row][col] == 0:
                    free_plit.append((row, col))
        if free_plit:
            roww, column = random.choice(free_plit)
            nums = [2, 4, 8]
            self.desk[roww][column] = random.choice(nums)
            return True

    def merge(self, row):
        pair = False
        new_row = []
        for i in range(len(row)):
            if pair:
                self.score += int(row[i]*2)
                new_row.append(row[i]*2)
                pair = False
            else:
                if i + 1 < len(row) and row[i] == row[i + 1]:
                    pair = True
                else:
                    new_row.append(row[i])
        return new_row

    def check_lose(self):
        old_desk = copy.deepcopy(self.desk)
        old_score = self.score
        losed = False
        if not self.xmove(isleft=True) and not self.xmove(isleft=False):
            if not self.ymove(isup=True) and not self.ymove(isup=False):
                losed = True
        self.score = old_score
        if losed:
            return losed
        else:
            self.desk = old_desk

    def xmove(self, isleft):
        old_desk = copy.deepcopy(self.desk)
        for row in range(self.desk_size):
            new_nums = []
            for col in range(self.desk_size):
                if self.desk[row][col] != 0:
                    new_nums.append(self.desk[row][col])
            if len(new_nums) >= 2:
                new_nums = self.merge(new_nums)
            for i in range(self.desk_size - len(new_nums)):
                if isleft:
                    new_nums.append(0)
                else:
                    new_nums.insert(0, 0)
            for col in range(self.desk_size):
                self.desk[row][col] = new_nums[col]
        return old_desk != self.desk

    def ymove(self, isup):
        old_desk = copy.deepcopy(self.desk)
        for col in range(self.desk_size):
            new_nums = []
            for row in range(self.desk_size):
                if self.desk[row][col] != 0:
                    new_nums.append(self.desk[row][col])
            if len(new_nums) >= 2:
                new_nums = self.merge(new_nums)
            for i in range(self.desk_size - len(new_nums)):
                if isup:
                    new_nums.append(0)
                else:
                    new_nums.insert(0, 0)
            for row in range(self.desk_size):
                self.desk[row][col] = new_nums[row]
        return old_desk != self.desk

def run():
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()