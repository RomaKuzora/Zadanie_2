import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class DrawYellowCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.is_drawing = False
        self.push_btn.clicked.connect(self.result)

    def paintEvent(self, event):
        if self.is_drawing:
            painter = QPainter(self)
            brush = QBrush(QColor(255, 247, 0))
            painter.setBrush(brush)
            for _ in range(3):
                side = random.randint(20, 50)
                x = random.randint(0, 800)
                y = random.randint(0, 600)
                painter.drawEllipse(x - side, y - side, side * 2, side * 2)
                self.is_drawing = False

    def result(self):
        self.is_drawing = True
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawYellowCircle()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
