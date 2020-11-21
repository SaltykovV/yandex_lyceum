import random
import sys

from PyQt5.QtCore import QRect, QPoint, QSize
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui import Ui_MainWindow

COORDS = (200, 200)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.repaint)

        self.do_paint = False

    def draw_circle(self, p: QPainter):
        p.setBrush(QColor(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))
        size = int(random.choice(range(30, 150, 2)) * 0.5)
        p.drawEllipse(COORDS[0] - size * 0.5, COORDS[1] - size * 0.5, size, size)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
            self.do_paint = False

    def repaint(self):
        self.do_paint = True
        super(MainWindow, self).repaint()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
